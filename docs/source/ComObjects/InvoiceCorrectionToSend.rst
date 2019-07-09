InvoiceCorrectionToSend
=======================

Документ на отправку *Корректировочный счет-фактура* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=83296>`_.
Является производным объектом от :doc:`DocumentToSend <DocumentToSend>`

.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``InvoiceCorrection``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>` **, чтение** - содержимое документа
