UcdToSend
=========

Документ на отправку *Универсальный корректировочный документ* в формате приказа `ММВ-7-15/189@ <https://normativ.kontur.ru/document?moduleId=1&documentId=273231>`_.
Является производным объектом от :doc:`DocumentToSend`

.. deprecated:: 5.27.0
  Используйте :doc:`CustomDocumentToSend`

.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``UniversalCorrectionDocument``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`UcdSellerContent` **, чтение** - содержимое документа
