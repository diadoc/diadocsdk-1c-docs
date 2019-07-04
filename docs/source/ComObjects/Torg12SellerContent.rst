Torg12SellerContent
===================

Объект предназначен для работы с содержанием формализованного документа "ТОРГ-12" в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------


- **Type** (строка, чтение) - тип документа (возвращает строку "XmlTorg12Content")

- **Date** (дата, чтение/запись) - дата документа

- **Number** (строка, чтение/запись) - номер документа

- **WaybillDate** (дата, чтение/запись) - дата транспортной накладной

- **WaybillNumber** (строка, чтение/запись) - номер транспортной накладной

- **OperationCode** (строка, чтение/запись) - код вида операции

- **GroundName** (строка, чтение/запись) - наименование документа-основания

- **GroundDate** (дата, чтение/запись) - дата документа-основания

- **GroundNumber** (строка, чтение/запись) - номер документа-основания

- **Seller** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - данные продавца

- **Buyer** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - данные покупателя

- **Shipper** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - данные грузоотправителя

- **ShipperDepartment** (строка, чтение/запись) - структурное подразделение грузоотправителя

- **ShipperOkdp** (строка, чтение/запись) - код основного вида деятельности по ОКДП грузоотправителя

- **Consignee** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - данные грузополучателя

- **Items** (:doc:`коллекция <Collection>` объектов :doc:`Torg12Item <Torg12Item>`, чтение) - табличная часть Торг-12

- **Totals** (:doc:`Torg12Totals <Torg12Totals>`, чтение) - итоги по накладной

- **Commons** (:doc:`Torg12Commons <Torg12Commons>`, чтение) - общие сведения по накладной

- **AttachmentSheetsQuantity** (число, чтение/запись) - приложение, количество листов

- **SupplyAllowedBy** (:doc:`Official <Official>`, чтение) - отпуск груза разрешил

- **ChiefAccountant** (:doc:`Official <Official>`, чтение) - главный бухгалтер

- **SupplyPerformedBy** (:doc:`Official <Official>`, чтение) - отпуск груза произвел

- **SupplyDate** (дата, чтение/запись) - дата отпуска груза

- **Signer** (:doc:`Signer <Signer>`, чтение) - подписант

- **AdditionalInfo** (строка, чтение/запись) - дополнительные сведения


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(Torg12SellerContent)>` - добавляет строку в табличную часть Торг-12

-  :doc:`SaveExternalCodes <SaveExternalCodes>` - сохраняет на сервере Диадока список внешних идентификаторов товаров накладной


.. toctree::
   :name: Auto
   :hidden:

   AddItem-(Torg12SellerContent) <AddItem-(Torg12SellerContent)>
   SaveExternalCodes <SaveExternalCodes>
   Torg12Item <Torg12Item>
   Torg12Totals <Torg12Totals>
   Torg12Commons <Torg12Commons>
