InvoiceRevisionToSend
=====================

Документ на отправку *Исправление  счета-фактуры* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567>`_.
Является производным объектом от :doc:`DocumentToSend <DocumentToSend>`

.. versionadded:: 5.5.0


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``InvoiceRevision``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`InvoiceContent <InvoiceContent>` **, чтение** - содержимое документа
