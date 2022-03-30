TovTorgSellerContent
====================

Cодержание документа *ТОРГ-12* в формате приказа `ММВ-7-10/551@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265102>`_.
Является производным объектом от :doc:`BaseContent`


.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``TovTorg``

:Seller:
    :doc:`ExtendedOrganizationInfo` **, чтение** - продавец

:Buyer:
    :doc:`ExtendedOrganizationInfo` **, чтение** - покупатель

:Shipper:
    :doc:`ExtendedOrganizationInfo` **, чтение** - грузоотправитель

:Consignee:
    :doc:`ExtendedOrganizationInfo` **, чтение** - грузополучатель

:Carrier:
    :doc:`ExtendedOrganizationInfo` **, чтение** - перевозчик

:Signers:
    :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - подписанты

:Grounds:
    :doc:`Коллекция <Collection>` **объектов** :doc:`GroundInfo` **, чтение** - основания

:Currency:
    **Строка, чтение/запись** - код валюты

:CurrencyRate:
    **Строка, чтение/запись** - курс валюты

:DocumentDate:
    **Дата, чтение/запись** - дата составления документа о передаче товара

:DocumentNumber:
    **Строка, чтение/запись** - номер документа о передаче товара

:RevisionDate:
    **Дата, чтение/запись** - дата исправления документа о передаче товара

:RevisionNumber:
    **Строка, чтение/запись** - номер исправления документа о передаче товара

:TransferInfo:
    :doc:`TovTorgTransferInfo` **, чтение** - сведения о факте передачи (об отпуске груза)

:DocumentCreator:
    **Строка, чтение/запись** - составитель файла информации продавца

:DocumentCreatorBase:
    **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла

:OperationType:
    **Строка, чтение/запись** - вид операции

:GovernmentContractInfo:
    **Строка, чтение/запись** - идентификатор государственного контракта

:Table:
    :doc:`TovTorgTable` **, чтение** - сведения об ассортименте, количестве, стоимости и другой информации о товарных позициях

:AdditionalInfoId:
    :doc:`AdditionalInfoId` **, чтение** - информационное поле документа

:DocumentName:
    **Строка, чтение/запись** - наименование первичного документа, определенное организацией


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddSigner() <TovTorgSellerContent.AddSigner>`
        * :meth:`AddGround() <TovTorgSellerContent.AddGround>`


.. method:: TovTorgSellerContent.AddSigner()

    Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его


.. method:: TovTorgSellerContent.AddGround()

    Добавляет :doc:`новый элемент <GroundInfo>` в коллекцию *Grounds* и возвращает его