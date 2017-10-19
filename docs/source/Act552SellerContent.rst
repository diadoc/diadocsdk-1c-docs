Act552SellerContent
===================

Объект предназначен для работы с содержанием документов типа "Акт в
формате 552-го приказа ФНС"

Свойства
--------

- **Seller** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - исполнитель (продавец услуг)

- **Buyer** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - заказчик (покупатель услуг)

- **Signers** (коллекция :doc:`ValueCollection <ValueCollection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты

- **Grounds** (коллекция :doc:`ValueCollection <ValueCollection>` объектов :doc:`GroundInfo <GroundInfo>`, чтение) - основания

- **Currency** (строка, чтение/запись) - валюта (код)

- **CurrencyRate** (строка, чтение/запись) - курс валюты

- **Works** (коллекция :doc:`ValueCollection <ValueCollection>` объектов :doc:`Act552WorkDescription <Act552WorkDescription>`) - описание выполненных работ

- **DocumentDate** (дата, чтение/запись) - дата составления документа о передаче товара

- **DocumentNumber** (строка, чтение/запись) - номер документа о передаче товара

- **RevisionDate** (дата, чтение/запись) - дата исправления документа

- **RevisionNumber** (строка, чтение/запись) - номер исправления документа

- **DocumentCreator** (строка, чтение/запись) - составитель файла информации продавца

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла

- **OperationType** (строка, чтение/запись) - вид операции

- **OperationTitle** (строка, чтение/запись) - заголовок содержания операции

- **GovernmentContractInfo** (строка, чтение/запись) - идентификатор государственного контракта

- **AdditionalInfo** (строка, чтение/запись) - информационное поле документа

- **DocumentName** (строка, чтение/запись) - наименование первичного документа, определенное организацией

- **TransferInfo** (объект :doc:`Act552TransferInfo <Act552TransferInfo>`) - содержание факта хозяйственной жизни - сведения о передаче результатов работ (о предъявлении оказанных услуг)

Методы
------

-  :doc:`AddSigner <AddSigner-(Act552SellerContent)>` - 

-  :doc:`AddGround <AddGround-(Act552SelerContent)>` - 

-  :doc:`AddWork <AddWork-(Act552SellerContent)>` - 

.. toctree::
   :name: Auto
   :hidden:

    AddSigner <AddSigner-(Act552SellerContent)>
    AddGround <AddGround-(Act552SelerContent)>
    AddWork <AddWork-(Act552SellerContent)>
    Act552WorkDescription <Act552WorkDescription>
    Act552TransferInfo <Act552TransferInfo>