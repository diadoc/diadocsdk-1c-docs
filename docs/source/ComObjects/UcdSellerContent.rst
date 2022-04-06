UcdSellerContent
================

Содержание документа *Универсальный корректировочный документ* в формате приказа `ММВ-7-15/189@ <https://normativ.kontur.ru/document?moduleId=1&documentId=273231>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``UniversalCorrectionDocument``

:Function:
    **Строка, чтение/запись** - функция документа

    =============== ========
    Значение        Описание
    =============== ========
    Invoice         КСЧФ
    Basic           ДИС
    InvoiceAndBasic КСЧФДИС
    =============== ========

:Name:
    **Строка, чтение/запись** - наименование первичного документа, определенное организацией

:Date:
    **Дата, чтение/запись** - дата УКД

:Number:
    **Строка, чтение/запись** - номер УКД

:Invoices:
    :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceForCorrectionInfo` **, чтение** - счет-фактура (первичный документ), к которому составлен УКД

:Seller:
    :doc:`ExtendedOrganizationInfo` **, чтение** - данные продавца. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для продавца должен быть указан адрес

:Buyer:
    :doc:`ExtendedOrganizationInfo` **, чтение** - данные покупателя. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для покупателя должен быть указан адрес

:Signers:
    :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - подписанты документа. Для документа должен быть указан по крайней мере один подписант.

:EventContent:
    :doc:`EventContent` **, чтение** - содержание события

:InvoiceCorrectionTable:
    :doc:`InvoiceCorrectionTable` **, чтение** - сведения таблицы корректировочного счета-фактуры

:Currency:
    **Строка, чтение/запись** - код валюты по Общероссийскому классификатору валют

:CurrencyRate:
    **Строка, чтение/запись** - курс валюты

:RevisionDate:
    **Дата, чтение/запись** - дата исправления

:RevisionNumber:
    **Строка, чтение/запись** - номер исправления

:AdditionalInfoId:
    :doc:`AdditionalInfoId` **, чтение** - информационное поле документа

:Creator:
    **Строка, чтение/запись** - составитель файла обмена счета-фактуры (информации продавца)

:CreatorBase:
    **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

:GovernmentContractInfo:
    **Строка, чтение/запись** - идентификатор государственного контракта


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddSigner() <UcdSellerContent.AddSigner>`
        * :meth:`AddInvoice() <UcdSellerContent.AddInvoice>`


.. method:: UcdSellerContent.AddSigner()

    Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию **Signers** и возвращает его


.. method:: UcdSellerContent.AddInvoice()

    Добавляет :doc:`новый элемент <InvoiceForCorrectionInfo>` в коллекцию **Invoices** и возвращает его