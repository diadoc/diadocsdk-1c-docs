TovTorgSellerContent
======================

Объект предназначен для работы с содержанием формализованного документа "ТОРГ-12" в формате приказа `ММВ-7-10/551@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265102>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа (возвращает строку "TovTorg")

- **Seller** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - продавец

- **Buyer** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - покупатель

- **Shipper** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - грузоотправитель

- **Consignee** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - грузополучатель

- **Carrier** (:doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>`, чтение) - перевозчик

- **Signers** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты

- **Grounds** (:doc:`коллекция <Collection>` объектов :doc:`GroundInfo <GroundInfo>`, чтение) - основания

- **Currency** (строка, чтение/запись) - валюта (код)

- **CurrencyRate** (строка, чтение/запись) - курс валюты

- **DocumentDate** (дата, чтение/запись) - дата составления документа о передаче товара

- **DocumentNumber** (строка, чтение/запись) - номер документа о передаче товара

- **RevisionDate** (дата, чтени/запись) - дата исправления документа о передаче товара

- **RevisionNumber** (строка, чтение/запись) - номер исправления документа о передаче товара

- **TransferInfo** (:doc:`TovTorgTransferInfo <TovTorgTransferInfo>`, чтение) - сведения о факте передачи (об отпуске груза)

- **DocumentCreator** (строка, чтение/запись) - составитель файла информации продавца

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла

- **OperationType** (строка, чтение/запись) - вид операции

- **GovernmentContractInfo** (строка, чтение/запись) - идентификатор государственного контракта

- **Table** (:doc:`TovTorgTable <TovTorgTable>`, чтение) - сведения об ассортименте, количестве, стоимости и другой информации о товарных позициях

- **AdditionalInfoId** (:doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа

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