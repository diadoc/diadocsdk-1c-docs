Act552SellerContent
===================

Объект предназначен для работы с содержанием формализованного документа "Акт о выполнении работ" в формате приказа `ММВ-7-10/552@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265283>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства
--------

- **Type** (строка, чтение) - тип документа (возвращает строку "XmlAcceptanceCertificate552")

- **Seller** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - исполнитель (продавец услуг)

- **Buyer** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - заказчик (покупатель услуг)

- **Signers** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты

- **Grounds** (:doc:`коллекция <Collection>` объектов :doc:`GroundInfo <GroundInfo>`, чтение) - основания

- **Currency** (строка, чтение/запись) - код валюты

- **CurrencyRate** (строка, чтение/запись) - курс валюты

- **Works** ( :doc:`коллекция <Collection>` объектов :doc:`Act552WorkDescription <Act552WorkDescription>`) - описание выполненных работ

- **DocumentDate** (дата, чтение/запись) - дата составления документа о передаче товара

- **DocumentNumber** (строка, чтение/запись) - номер документа о передаче товара

- **RevisionDate** (дата, чтение/запись) - дата исправления документа

- **RevisionNumber** (строка, чтение/запись) - номер исправления документа

- **DocumentCreator** (строка, чтение/запись) - составитель файла информации продавца

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла

- **OperationType** (строка, чтение/запись) - вид операции

- **OperationTitle** (строка, чтение/запись) - заголовок содержания операции

- **GovernmentContractInfo** (строка, чтение/запись) - идентификатор государственного контракта

- **AdditionalInfo** (:doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа

- **DocumentName** (строка, чтение/запись) - наименование первичного документа, определенное организацией

- **TransferInfo** (:doc:`Act552TransferInfo <Act552TransferInfo>`, чтение) - содержание факта хозяйственной жизни - сведения о передаче результатов работ (о предъявлении оказанных услуг)


Методы
------


-  :doc:`AddSigner <AddSigner-(Act552SellerContent)>` - добавляет новый элемент в коллекцию подписантов

-  :doc:`AddGround <AddGround-(Act552SellerContent)>` - добавляет основание в список оснований

-  :doc:`AddWork <AddWork-(Act552SellerContent)>` - добавляет элемент в коллекцию описаний выполненных работ


.. toctree::
   :name: Auto
   :hidden:

    AddSigner <AddSigner-(Act552SellerContent)>
    AddGround <AddGround-(Act552SellerContent)>
    AddWork <AddWork-(Act552SellerContent)>
    Act552WorkDescription <Act552WorkDescription>
    Act552TransferInfo <Act552TransferInfo>