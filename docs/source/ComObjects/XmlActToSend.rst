XmlActToSend
============

Документ на отправку *Акт о выполнении работ* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83282>`_.
Является производным объектом от :doc:`DocumentToSend <DocumentToSend>`

.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificate``

:Comment:
  **Строка, чтение/запись** - комментарий к документу

:CustomDocumentId:
  **Строка, чтение/запись** - внешний идентификатор документа

:Content:
  :doc:`AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>` **, чтение** - содержимое документа
