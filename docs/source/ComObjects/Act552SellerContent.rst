Act552SellerContent
===================

Содержаним титула продавца *Акта о выполнении работ* в формате приказа `ММВ-7-10/552@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265283>`_ .
Является производным объектом от :doc:`BaseContent <BaseContent>`.

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificate552``

:Seller:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - исполнитель (продавец услуг)

:Buyer:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - заказчик (покупатель услуг)

:Signers:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner <ExtendedSigner>` **, чтение** - подписанты

:Grounds:
  :doc:`Коллекция <Collection>` **объектов** :doc:`GroundInfo <GroundInfo>` **, чтение** - основания

:Currency:
  **Строка, чтение/запись** - код валюты

:CurrencyRate:
  **Строка, чтение/запись** - курс валюты

:Works:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Act552WorkDescription <Act552WorkDescription>` **, чтение** - описание выполненных работ

:DocumentDate:
  **Дата, чтение/запись** - дата составления документа о передаче товара

:DocumentNumber:
  **Строка, чтение/запись** - номер документа о передаче товара

:RevisionDate:
  **Дата, чтение/запись** - дата исправления документа

:RevisionNumber:
  **Строка, чтение/запись** - номер исправления документа

:DocumentCreator:
  **Строка, чтение/запись** - составитель файла информации продавца

:DocumentCreatorBase:
  **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла

:OperationType:
  **Строка, чтение/запись** - вид операции

:OperationTitle:
  **Строка, чтение/запись** - заголовок содержания операции

:GovernmentContractInfo:
  **Строка, чтение/запись** - идентификатор государственного контракта

:AdditionalInfo:
  :doc:`AdditionalInfoId <AdditionalInfoId>` **, чтение** - информационное поле документа

:DocumentName:
  **Строка, чтение/запись** - наименование первичного документа, определенное организацией

:TransferInfo:
  :doc:`Act552TransferInfo <Act552TransferInfo>` **, чтение** - содержание факта хозяйственной жизни - сведения о передаче результатов работ (о предъявлении оказанных услуг)


.. rubric:: Методы

+----------------------------------+----------------------------------+--------------------------------+
| |Act552SellerContent-AddSigner|_ | |Act552SellerContent-AddGround|_ | |Act552SellerContent-AddWork|_ |
+----------------------------------+----------------------------------+--------------------------------+

.. |Act552SellerContent-AddSigner| replace:: AddSigner()
.. |Act552SellerContent-AddGround| replace:: AddGround()
.. |Act552SellerContent-AddWork| replace:: AddWork()


.. _Act552SellerContent-AddSigner:
.. method:: Act552SellerContent.AddSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его


.. _Act552SellerContent-AddGround:
.. method:: Act552SellerContent.AddGround()

  Добавляет :doc:`новый элемент <GroundInfo>` в коллекцию *Grounds* и возвращает его


.. _Act552SellerContent-AddWork:
.. method:: Act552SellerContent.AddWork()

  Добавляет :doc:`новый элемент <Act552WorkDescription>` в коллекцию *Works* и возвращает его
