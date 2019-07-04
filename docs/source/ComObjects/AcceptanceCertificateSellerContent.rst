AcceptanceCertificateSellerContent
==================================

Объект предназначен для работы с содержанием формализованного документа "Акт о выполнении работ" в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83259>`_ .
Является производным объектом от :doc:`BaseContent <BaseContent>`.

.. rubric:: Свойства

:Type:
  **строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificateContent``

:Date:
  **дата, чтение/запись** - дата акта

:Number:
  **строка, чтение/запись** - номер акта

:Title:
  **строка, чтение/запись** - заголовок акта

:SignatureDate:
  **дата, чтение/запись** - дата подписи акта исполнителем

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
  **строка, чтение/запись** - дополнительные сведения


.. rubric:: Методы

.. function:: ﻿AcceptanceCertificateSellerContent.AddItem()

  Добавляет :doc:`новый элемент <AcceptanceCertificateItem>` в коллекцию *Items* и возвращает его
