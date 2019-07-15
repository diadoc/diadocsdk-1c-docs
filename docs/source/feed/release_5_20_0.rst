Релиз 5.20.0
============

.. feed-entry::
   :date: 2017-12-25

- добавлена поддержка работы с "документом любого типа":
    
    - поддержка типа документа "Document" для методов AddDocumentFromFile и AddDocumentFromFileRaw объекта PackageSendTask

    - метод GetDocumentTypes - возвращает описание типов документов, доступных в ящике

- Исправлены ошибки:
    - исключение при присвоении значения "5.02" свойству InvoiceContent.InvoiceVersion
    - если сертификат не содержит ИНН, исключение при попытке чтения PersonalCertificate.INN


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_