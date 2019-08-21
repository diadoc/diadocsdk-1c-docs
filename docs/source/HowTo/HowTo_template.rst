Как работать с шаблонами
========================

Шаблон - документ, отправленный без подписи. Шаблоны полезны, если необходимо до отправки показать документ контрагенту. Из шаблона можно создать обычный :doc:`документ <../ComObjects/Document>`


Как отправить шаблон документа
------------------------------

Для отправки шаблона документа необходимо:
    * находиться в контексте :doc:`организации <../ComObjects/Organization>`
    * вызвать метод :meth:`Organization.CreateTemplateSendTask`
    * заполнить :doc:`полученный объект <../ComObjects/TemplateSendTask>`
    * вызвать метод :meth:`TemplateSendTask.Send`

Можно отправлять как однотитульные документы, так и двухтитульные документы - для этого у :doc:`отправляемого шаблона <../ComObjects/TemplateToSend>` есть методы :meth:`TemplateToSend.LoadSellerTitleFromFile` и :meth:`TemplateToSend.LoadBuyerTitleFromFile`

Сами титулы при этом компонента не готовит - подготовкой контента пользователь занимается самостоятельно.


.. note:: Документы, доступные в ящике организации без дополнительных настроек не поддерживают отправку второго титула в виде шаблона. В примере используем УПД СчфДоп для того чтобы не вводить новые понятия

.. code-block:: c#

    Функция ОтправитьШаблонУПДСЧФДОП(BoxId_ОтправителяШаблона,
                                     BoxId_ПолучателяШаблона,
                                     BoxId_ОтправителяДокумента,
                                     BoxId_ПолучателяДокумента,
                                     ПутьДоФайлаТитулаПродавца,
                                     ПутьДоФайлаТитулаПокупателя)

        Отправитель = dd_Connection.GetOrganizationById(BoxId_ОтправителяШаблона);

        TemplateSendTask = Organization.CreateTemplateSendTask();
        TemplateSendTask.ToBoxId          = BoxId_ПолучателяШаблона;
        TemplateSendTask.MessageFromBoxId = BoxId_ОтправителяДокумента;
        TemplateSendTask.MessageToBoxId   = BoxId_ПолучателяДокумента;

        TemplateToSend = dd_TemplateSendTask.AddTemplate("UniversalTransferDocument");
        TemplateToSend.Function = "InvoiceAndBasic";
        TemplateToSend.LoadSellerTitleFromFile(ПутьДоФайлаТитулаПродавца);
        TemplateToSend.LoadBuyerTitleFromFile(ПутьДоФайлаТитулаПокупателя);

        Возврат TemplateSendTask.Send();

    КонецФункции


Как получить документы, созданные из отправленного шаблона
----------------------------------------------------------


После отправки шаблона, вернётся объект :doc:`Template <../ComObjects/Template>`, который содержит идентификатор шаблона. Зная этот идентификатор, можно запросить шаблон повторно, и если из шаблона был создан документ, то в соответствующей коллекции будет указаны ID таких документов. Далее можно вызвать метод :meth:`Organization.GetDocumentById`:

.. code-block:: c#

    // SentTemplate - объект ранее отправленного шаблона
    Функция ПолучитьШаблонныеДокументы(SentTemplate)

        TemplateId = SentTemplate.TemplateId;

        RefreshedTemplate = Organization.GetTemplate(TemplateId);
        FirstTemplateSellerTitle = RefreshedTemplate.Entities.GetItem(0);
        ИдентификаторыДокументовСозданныхИзШаблона = FirstTemplateSellerTitle.CreatedDocumentIds;

        // Идентификаторы можно использовать в методе GetDocumentById
        Возврат ИдентификаторыДокументовСозданныхИзШаблона;

    КонецФункции


.. seealso:: :doc:`HowTo_get_documents`
