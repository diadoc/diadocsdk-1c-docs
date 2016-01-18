InvoiceContent
==============

Объект предназначен для работы с содержанием документов «счет-фактура» и
«исправление счет-фактуры» и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------


- **InvoiceVersion** (строка, чтение/запись, --- ) - версия формата счет-фактуры. Может принимать значения "5.01", "5.02"

- **Date** (дата, чтение/запись, обязательно для заполнения ) - дата счет-фактуры

- **Number** (строка, чтение/запись, обязательно для заполнения, длина не более 256 символов ) - номер счет-фактуры

- **InvoiceRevision Date** (дата, чтение/запись, --- ) - дата исправленния счет-фактуры (обязательно при формировании InvoiceRevision)

- **InvoiceRevision Number** (строка, чтение/запись, длина не более 3 символов ) - номер исправления счет-фактуры (обязательно при формировании InvoiceRevision)

- **Currency** (строка, чтение/запись, обязательно для заполнения. Числовая строка длиной 3 символа. Код должен содержаться в общероссийском классификаторе валют. ) - код валюты

- **Seller** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения ) - данные продавца

- **Buyer** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения ) - данные покупателя

- **Shipper** (объект :doc:`ShipperOr ConsigneeInfo <ShipperOrConsigneeInfo>`, чтение, --- ) - данные грузоотправителя

- **Consignee** (объект :doc:`ShipperOr ConsigneeInfo <ShipperOrConsigneeInfo>`, чтение, --- ) - данные грузополучателя

- **Signer** (объект :doc:`Signer <Signer>`, чтение, обязательно для заполнения ) - данные подписанта документа

- **Totals** (:doc:`InvoiceTotals <Totals-InvoiceTotals>`, чтение, --- ) - общие итоги по документу

- **Type** (строка, чтение, --- ) - тип документа (возвращает строку "InvoiceContent")

- **Items** (:doc:`Коллекция <Collection>` объектов :doc:`InvoiceItem <InvoiceItem-(Invoice)>`, чтение, обязательно для заполнения ) - табличная часть счет-фактуры

- **Payment Documents** (:doc:`Коллекция <Collection>` объектов :doc:`PaymentDocument <PaymentDocument>`, чтение, -- ) - список платежно-расчетных документов

- **StructedAdditionalInfos** (:doc:`Коллекция <Collection>` объектов :doc:`AdditionalInfoItem <AdditionalInfoItem>` , чтение/запись, --- ) - дополнительные сведения


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(InvoiceContent)>` - добавляет строку в табличную часть счет-фактуры

-  :doc:`AddPaymentDocument <AddPaymentDocument-(InvoiceContent)>` - добавляет сведения о платежно-расчетном документе

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo>` - добавляет строку дополнительных сведений



.. toctree::
   :name: Auto
   :hidden:

   AddItem-(InvoiceContent) <AddItem-(InvoiceContent)>
   AddPaymentDocument-(InvoiceContent) <AddPaymentDocument-(InvoiceContent)>
   InvoiceItem-(Invoice) <InvoiceItem-(Invoice)>
   PaymentDocument <PaymentDocument>
   InvoiceTotals <Totals-InvoiceTotals>
   addStructedAdditionalInfo <addStructedAdditionalInfo>
   AdditionalInfoItem <AdditionalInfoItem>
