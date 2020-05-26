InvoiceToSend
=============

Документ на отправку *Счет-фактура* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567>`_.
Является производным объектом от :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
  Используйте :doc:`CustomDocumentToSend`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``Invoice``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`InvoiceContent` **, чтение** - содержимое документа
