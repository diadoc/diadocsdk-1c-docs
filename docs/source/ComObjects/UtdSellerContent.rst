UtdSellerContent
================

Содержанием формализованного документа *Универсальный передаточный документ* в формате приказа `ММВ-7-15/155@ <https://normativ.kontur.ru/document?moduleId=1&documentId=271958>`_.
Является производным объектом от :doc:`BaseContent <BaseContent>`

.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``UniversalTransferDocument``

:Function:
  **Строка, чтение/запись** - функция документа. |UtdSellerContent-Function|_

:Name:
  **Строка, чтение/запись** - наименование первичного документа, определенное организацией

:Date:
  **Дата, чтение/запись** - дата УПД

:Number:
  **Строка, чтение/запись** - номер УПД

:Seller:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - данные продавца

:Buyer:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - данные покупателя

:Shipper:
  :doc:`Shipper <Shipper>` **, чтение** - данные грузоотправителя

:Consignee:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - данные грузополучателя

:InvoiceTable:
  :doc:`InvoiceTable <InvoiceTable>` **, чтение** - сведения табличной части счета-фактуры

:Currency:
  **Строка, чтение/запись** - код валюты по Общероссийскому классификатору валют

:CurrencyRate:
  **Строка, чтение/запись** - курс валюты

:RevisionDate:
  **Дата, чтение/запись** - дата исправления счета-фактуры

:RevisionNumber:
  **Строка, чтение/запись** - номер исправления счета-фактуры

:AdditionalInfoId:
  :doc:`AdditionalInfoId <AdditionalInfoId>` **, чтение** - информационное поле документа

:TransferInfo:
  :doc:`TransferInfo <TransferInfo>` **, чтение** - сведения о передаче (сдаче) товара/услуги

:Creator:
  **Строка, чтение/запись** - составитель файла обмена счета-фактуры (информации продавца)

:CreatorBase:
  **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

:GovernmentContractInfo:
  **Строка, чтение/запись** - идентификатор государственного контракта

:Signers:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner <ExtendedSigner>` **, чтение** - подписанты документа

:PaymentDocuments:
  :doc:`Коллекция <Collection>` **объектов** :doc:`PaymentDocument <PaymentDocument>` **, чтение** - платежно-расчетные документы


.. rubric:: Методы

+-------------------------------+----------------------------------------+
| |UtdSellerContent-AddSigner|_ | |UtdSellerContent-AddPaymentDocument|_ |
+-------------------------------+----------------------------------------+

.. |UtdSellerContent-AddSigner| replace:: AddSigner()
.. |UtdSellerContent-AddPaymentDocument| replace:: AddPaymentDocument()



.. _UtdSellerContent-AddSigner:
.. method:: UtdSellerContent.AddSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его



.. _UtdSellerContent-AddPaymentDocument:
.. method:: UtdSellerContent.AddPaymentDocument()

  Добавляет :doc:`новый элемент <PaymentDocument>` в коллекцию *PaymentDocuments* и возвращает его



.. rubric:: Дополнительная информация

.. |UtdSellerContent-Function| replace:: Возможные значения
.. _UtdSellerContent-Function:

=================== ========
Значение *Function* Описание
=================== ========
Invoice             СЧФ
Basic               ДОП
InvoiceAndBasic     СЧФДОП
=================== ========
