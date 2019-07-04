InvoiceContent
==============

Объект предназначен для работы с содержанием формализованного документа "Счет-фактура" и "Исправление счета-фактуры" в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------


- **Type** (строка, чтение) - тип документа (возвращает значение "InvoiceContent")

- **InvoiceVersion** (строка, чтение/запись) - версия формата счета-фактуры. Может принимать значения "5.01", "5.02"

- **Date** (дата, чтение/запись) - дата счета-фактуры

- **Number** (строка, чтение/запись) - номер счета-фактуры

- **InvoiceRevisionDate** (дата, чтение/запись) - дата исправленния счета-фактуры

- **InvoiceRevisionNumber** (строка, чтение/запись) - номер исправления счета-фактуры

- **Currency** (строка, чтение/запись) - код валюты

- **Seller** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - данные продавца

- **Buyer** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - данные покупателя

- **Shipper** (:doc:`ShipperOr ConsigneeInfo <ShipperOrConsigneeInfo>`, чтение) - данные грузоотправителя

- **Consignee** (:doc:`ShipperOr ConsigneeInfo <ShipperOrConsigneeInfo>`, чтение) - данные грузополучателя

- **Signer** (:doc:`Signer <Signer>`, чтение) - данные подписанта документа

- **Totals** (:doc:`InvoiceTotals <Totals-InvoiceTotals>`, чтение) - общие итоги по документу

- **Type** (строка, чтение) - тип документа (возвращает строку "InvoiceContent")

- **Items** (:doc:`коллекция <Collection>` объектов :doc:`InvoiceItem <InvoiceItem>`, чтение) - табличная часть счета-фактуры

- **Payment Documents** (:doc:`коллекция <Collection>` объектов :doc:`PaymentDocument <PaymentDocument>`, чтение) - список платежно-расчетных документов

- **StructedAdditionalInfos** (:doc:`коллекция <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`, чтение) - дополнительные сведения


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(InvoiceContent)>` - добавляет строку в табличную часть счета-фактуры

-  :doc:`AddPaymentDocument <AddPaymentDocument-(InvoiceContent)>` - добавляет сведения о платежно-расчетном документе

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo>` - добавляет строку дополнительных сведений
