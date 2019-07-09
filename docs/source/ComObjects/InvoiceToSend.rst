InvoiceToSend
=============

Документ на отправку *Счет-фактура* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567>`_.
Является производным объектом от :doc:`DocumentToSend <DocumentToSend>`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``Invoice``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`InvoiceContent <InvoiceContent>` **, чтение** - содержимое документа
