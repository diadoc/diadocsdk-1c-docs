TovTorgSellerContent
======================

Объект предназначен для работы с содержанием документов типа "ТОРГ-12 в
формате 551-го приказа ФНС" (титул продавца) и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------


- **Seller** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - продавец

- **Buyer** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - покупатель

- **Shipper** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - грузоотправитель

- **Consignee** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - грузополучатель

- **Carrier** (объект :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - перевозчик

- **Signers** (коллекция :doc:`Collection <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты

- **Grounds** (коллекция :doc:`Collection <Collection>` объектов :doc:`GroundInfo <GroundInfo>`, чтение) - основания

- **Currency** (строка, чтение/запись) - валюта (код)

- **CurrencyRate** (строка, чтение/запись) - курс валюты

- **DocumentDate** (дата, чтение/запись) - дата составления документа о передаче товара

- **DocumentNumber** (строка, чтение/запись) - номер документа о передаче товара

- **RevisionDate** () - дата исправления документа о передаче товара

- **RevisionNumber** (строка, чтение/запись) - номер исправления документа о передаче товара

- **TransferInfo** (объект :doc:`TovTorgTransferInfo <TovTorgTransferInfo>`, чтение) - сведения о факте передачи (об отпуске груза)

- **DocumentCreator** (строка, чтение/запись) - составитель файла информации продавца

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла

- **OperationType** (строка, чтение/запись) - вид операции

- **GovernmentContractInfo** (строка, чтение/запись) - идентификатор государственного контракта

- **Table** (объект :doc:`TovTorgTable <TovTorgTable>`, чтение) - сведения об ассортименте, количестве, стоимости и другой информации о товарных позициях

- **AdditionalInfoId** (объект :doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа

- **DocumentName** (строка, чтение/запись) - наименование первичного документа, определенное организацией


Методы объекта
--------------


-  :doc:`AddSigner <AddSigner-(TovTorgSellerContent)>` - добавляет новый элемент в список подписантов

-  :doc:`AddGround <AddGround-(TovTorgSellerContent)>` - добавляет основание в список оснований


.. toctree::
   :name: Auto
   :hidden:

   AddSigner <AddSigner-(TovTorgSellerContent)>
   AddGround <AddGround-(TovTorgSellerContent)>
   TovTorgTable <TovTorgTable>
   TovTorgTransferInfo <TovTorgTransferInfo>
   GroundInfo <GroundInfo>

 

