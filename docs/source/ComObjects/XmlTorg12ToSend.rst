XmlTorg12ToSend
===============

Документ на отправку *ТОРГ-12* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83283>`_.
Является производным объектом от :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
  Используйте :doc:`CustomDocumentToSend`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlTorg12``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`Torg12SellerContent` **, чтение** - содержимое документа
