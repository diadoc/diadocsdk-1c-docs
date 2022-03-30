UtdSellerContent
================

Содержанием формализованного документа *Универсальный передаточный документ* в формате приказа `ММВ-7-15/155@ <https://normativ.kontur.ru/document?moduleId=1&documentId=271958>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``UniversalTransferDocument``

:Function:
    **Строка, чтение/запись** - функция документа

    =================== ========
    Значение *Function* Описание
    =================== ========
    Invoice             СЧФ
    Basic               ДОП
    InvoiceAndBasic     СЧФДОП
    =================== ========

:Name:
    **Строка, чтение/запись** - наименование первичного документа, определенное организацией

:Date:
    **Дата, чтение/запись** - дата УПД

:Number:
    **Строка, чтение/запись** - номер УПД

:Seller:
    :doc:`ExtendedOrganizationInfo` **, чтение** - данные продавца

:Buyer:
    :doc:`ExtendedOrganizationInfo` **, чтение** - данные покупателя

:Shipper:
    :doc:`Shipper` **, чтение** - данные грузоотправителя

:Consignee:
    :doc:`ExtendedOrganizationInfo` **, чтение** - данные грузополучателя

:InvoiceTable:
    :doc:`InvoiceTable` **, чтение** - сведения табличной части счета-фактуры

:Currency:
    **Строка, чтение/запись** - код валюты по Общероссийскому классификатору валют

:CurrencyRate:
    **Строка, чтение/запись** - курс валюты

:RevisionDate:
    **Дата, чтение/запись** - дата исправления счета-фактуры

:RevisionNumber:
    **Строка, чтение/запись** - номер исправления счета-фактуры

:AdditionalInfoId:
    :doc:`AdditionalInfoId` **, чтение** - информационное поле документа

:TransferInfo:
    :doc:`TransferInfo` **, чтение** - сведения о передаче (сдаче) товара/услуги

:Creator:
    **Строка, чтение/запись** - составитель файла обмена счета-фактуры (информации продавца)

:CreatorBase:
    **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

:GovernmentContractInfo:
    **Строка, чтение/запись** - идентификатор государственного контракта

:Signers:
    :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - подписанты документа

:PaymentDocuments:
    :doc:`Коллекция <Collection>` **объектов** :doc:`PaymentDocument` **, чтение** - платежно-расчетные документы


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddSigner() <UtdSellerContent.AddSigner>`
        * :meth:`AddPaymentDocument() <UtdSellerContent.AddPaymentDocument>`


.. method:: UtdSellerContent.AddSigner()

    Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его


.. method:: UtdSellerContent.AddPaymentDocument()

    Добавляет :doc:`новый элемент <PaymentDocument>` в коллекцию *PaymentDocuments* и возвращает его