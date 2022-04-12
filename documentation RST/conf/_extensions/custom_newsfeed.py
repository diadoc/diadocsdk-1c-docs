#
# Copyright (c) 2013, Prometheus Research, LLC
#


from __future__ import unicode_literals
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx import addnodes
from sphinx.util import docname_join
import sys, os.path, datetime, collections
from pprint import pprint


RSSFeed = collections.namedtuple('RSSFeed', ['title', 'link', 'description', 'date', 'items'])
RSSItem = collections.namedtuple('RSSItem', ['title', 'link', 'description', 'date'])

class FeedDirective(Directive):

    has_content = True
    option_spec = {
            'rss': directives.unchanged,
            'title': directives.unchanged,
            'link': directives.unchanged,
            'description': directives.unchanged,
    }

    def run(self):
        env = self.state.document.settings.env
        output = []
        entries = []
        includefiles = []
        for entry in self.content:
            if not entry:
                continue
            docname = docname_join(env.docname, entry)
            if docname not in env.found_docs:
                output.append(self.state.document.reporter.warning(
                    'feed contains a reference to nonexisting '
                    'document %r' % docname, line=self.lineno))
                env.note_reread()
            else:
                entries.append((None, docname))
                includefiles.append(docname)
        subnode = addnodes.toctree()
        subnode['parent'] = env.docname
        subnode['entries'] = entries
        subnode['includefiles'] = includefiles
        subnode['maxdepth'] = 1
        subnode['glob'] = False
        subnode['hidden'] = True
        subnode['numbered'] = False
        subnode['titlesonly'] = False
        wrappernode = nodes.compound(classes=['toctree-wrapper'])
        wrappernode.append(subnode)
        output.append(wrappernode)
        subnode = feeds()
        subnode['entries'] = includefiles
        subnode['rss'] = self.options.get('rss')
        subnode['title'] = self.options.get('title', '')
        subnode['link'] = self.options.get('link', '')
        subnode['description'] = self.options.get('description', '')
        output.append(subnode)
        return output


class FeedEntryDirective(Directive):
    option_spec = {
            'author': directives.unchanged,
            'date': directives.unchanged_required,
    }

    def run(self):
        author = self.options.get('author')
        date = self.options.get('date')
        for format in ["%Y-%m-%d"]:
            try:
                date = datetime.datetime.strptime(date, format)
            except ValueError:
                pass
            else:
                break
        else:
            return [doc.reporter.error("invalid date `%s`" % date,
                                       lineno=self.lineno)]
        meta_node = entrymeta(classes=['feed-meta'])
        meta_node += nodes.Text('Выпущено')
        if author:
            meta_node += nodes.Text(' by ')
            author_node = nodes.emphasis(classes=['feed-author'])
            author_node += nodes.Text(author)
            meta_node += author_node
        if date:
            meta_node += nodes.Text(' ')
            date_node = nodes.emphasis(classes=['feed-date'])
            date_node += nodes.Text(date.date())
            meta_node += date_node
        meta_node['author'] = author
        meta_node['date'] = date
        return [meta_node]


class feeds(nodes.General, nodes.Element):
    pass

class entrymeta(nodes.paragraph):
    pass


def print_info(obj):
    print('=' * 50)
    print('Type: ', type(obj))
    if (not isinstance(obj, str)):
        pprint(obj.__dict__)
    pprint(obj)


def process_feed(sphinx_app, sphinx_doc, source_filename):
    #print_info(sphinx_app)
    # sphinx_app.outdir - корень папки, куда будет сложена скомпиленная дока
    # sphinx_app - то же, что app в setup(app)

    sphinx_builder = sphinx_app.builder
    out_format, environment = sphinx_builder.format, sphinx_builder.env
    rss_date = datetime.datetime.utcnow()
    print_info(environment)


    for feed in sphinx_doc.traverse(feeds):
        # print_info(releases)

        rss_items = []
        replacement = []

        rss_filename, rss_title, rss_link, rss_description = feed['rss'], feed['title'], feed['link'], feed['description']

        # print_info(rss_filename)    # 'index.rss'
        # print_info(rss_title)       # 'Новости AddIn Diadoc API'
        # print_info(rss_link)        # ''
        # print_info(rss_description) # ''

        for release_filename in feed['entries']:
            release_info = environment.get_doctree(release_filename)
            # print_info(release_info)
            for meta in release_info.traverse(entrymeta):
                # print_info(meta)
                #section_node = nodes.section()
                title = environment.titles[release_filename]
                for release_info_node in release_info:
                    if isinstance(release_info_node, nodes.section):
                        #print_info(release_info_node)
                        #section_node['ids'] = release_section['ids']
                        title_node = nodes.title()
                        ref_node = nodes.reference(classes=['feed-ref'])
                        ref_node['internal'] = True
                        ref_node['refdocname'] = release_filename
                        ref_node['refuri'] = sphinx_builder.get_relative_uri(source_filename, release_filename)
                        refs = release_info_node['ids']
                        if (len(refs) > 0) :
                            ref_node['refuri'] += '#' + refs[0]
                        ref_node += title[0]
                        title_node += ref_node
                        release_info_node += title_node
                        rss_item_title = "%s" % title[0]
                        rss_item_link = rss_link + sphinx_builder.get_target_uri(release_filename)
                        #environment.resolve_references(section_node, source_filename, sphinx_builder)
                        #replacement.append(section_node)
                        environment.resolve_references(release_info_node, release_filename, sphinx_builder)
                        if out_format == 'html':
                            # print_info(release_section)
                            rss_item_description = sphinx_builder.render_partial(release_info_node)['body']
                            rss_item_date = meta['date']
                            rss_item = RSSItem(rss_item_title, rss_item_link, rss_item_description, rss_item_date)
                            rss_items.append(rss_item)
        feed.replace_self(replacement)
        if out_format == 'html' and rss_filename:
            rss_path = os.path.join(sphinx_builder.outdir, rss_filename)
            with open(rss_path, 'wb') as rss_xml:
                rss_feed = RSSFeed(rss_title, rss_link, rss_description, rss_date, rss_items)
                write_rss(rss_feed, rss_xml)


def format_text(text):
    return '<![CDATA[{}]]>'.format(text) if text else ''


def format_date(date):
    return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (
            ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")[date.weekday()],
            date.day,
            ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[date.month-1],
                                date.year, date.hour, date.minute, date.second)


def get_rss_xml_prolog(rss_feed):
    return '<?xml version="1.0" encoding="utf-8"?>\n' \
           '<rss version="2.0">\n' \
           '  <channel>\n' \
           '    <title>{title}</title>\n' \
           '    <link>{link}</link>\n' \
           '    <description>{desc}</description>\n' \
           '    <lastBuildDate>{date}</lastBuildDate>\n' \
           ''.format(title=rss_feed.title,
                     link=rss_feed.link,
                     desc=format_text(rss_feed.description),
                     date=rss_feed.date)

def get_rss_xml_item(item):
    return '    <item>\n' \
           '      <title>{title}</title>\n' \
           '      <link>{link}</link>\n' \
           '      <description>{desc}</description>\n' \
           '      <guid isPermaLink="true">{guid}</guid>\n' \
           '      <pubDate>{date}</pubDate>\n' \
           '    </item>\n' \
           ''.format(title=format_text(item.title),
                     link=item.link,
                     desc=format_text(item.description),
                     guid=item.link,
                     date=item.date)

def ret_rss_xml_epilog():
    return '  </channel>\n' \
           '</rss>\n'


def write_rss(rss_feed, stream):
    rss_prolog = get_rss_xml_prolog(rss_feed)
    rss_items = (get_rss_xml_item(item) for item in rss_feed.items)
    rss_epilog = ret_rss_xml_epilog()

    stream.write(''.join((rss_prolog, *rss_items, rss_epilog)).encode())


def setup(app):
    app.add_directive('feed', FeedDirective)
    app.add_directive('feed-entry', FeedEntryDirective)
    app.add_node(feeds)
    app.connect('doctree-resolved', process_feed)
