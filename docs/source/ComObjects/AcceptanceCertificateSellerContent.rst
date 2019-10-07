AcceptanceCertificateSellerContent
==================================

Содержание титула продавца *Акта о выполнении работ* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83259>`_ .
Является производным объектом от :doc:`BaseContent <BaseContent>`.

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`

.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificateContent``

:Date:
  **Дата, чтение/запись** - дата акта

:Number:
  **Строка, чтение/запись** - номер акта

:Title:
  **Строка, чтение/запись** - заголовок акта

:SignatureDate:
  **Дата, чтение/запись** - дата подписи акта исполнителем

:Seller:
  :doc:`OrganizationInfo <OrganizationInfo>` **, чтение** - исполнитель (организация, выполнившая работы либо оказавшая услуги)

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`AcceptanceCertificateItem <AcceptanceCertificateItem>` **, чтение** - табличная часть акта выполненных работ

:Official:
  :doc:`Official <Official>` **, чтение** - лицо, подписывающее со стороны исполнителя

:Attorney:
  :doc:`Attorney <Attorney>` **, чтение** - сведения о доверенности подписывающего со стороны исполнителя

:Signer:
  :doc:`Signer <Signer>` **, чтение** - подписант

:AdditionalInfo:
  **Строка, чтение/запись** - дополнительные сведения


.. rubric:: Методы

+-----------------------------------------------+
| |AcceptanceCertificateSellerContent-AddItem|_ |
+-----------------------------------------------+

.. |AcceptanceCertificateSellerContent-AddItem| replace:: AddItem()

.. _AcceptanceCertificateSellerContent-AddItem:
.. method:: AcceptanceCertificateSellerContent.AddItem()

  Добавляет :doc:`новый элемент <AcceptanceCertificateItem>` в коллекцию *Items* и возвращает его
