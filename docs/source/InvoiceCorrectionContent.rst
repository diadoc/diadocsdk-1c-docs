InvoiceCorrectionContent
========================

Объект предназначен для работы с содержанием документов
"корректировочный счет-фактура" и "исправление корректировочного
счета-фактуры" и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------


- **InvoiceVersion** (строка, чтение/запись) - версия формата корректировочного счета-фактуры. Может принимать значения "5.01", "5.02"

- **OriginalInvoices** (:doc:`коллекция <Collection>` объектов :doc:`OriginalInvoice <OriginalInvoice>`, чтение) - данные об счет-фактурах, на основании которых был выставлен корректировочный счет-фактура

- **InvoiceCorrectionDate** (дата, чтение/запись) - дата КСФ

- **InvoiceCorrectionNumber** (строка, чтение/запись, длина не более 256 символов) - номер КСФ

- **InvoiceCorrectionRevisionDate** (дата, чтение/запись) - дата исправления КСФ

- **InvoiceCorrectionRevisionNumber** (строка, чтение/запись, длина не более 3 символов) - номер исправления КСФ

- **Currency** (строка, чтение/запись, обязательно для заполнения. Числовая строка длиной 3 символа. Код должен содержаться в общероссийском классификаторе валют.) - код валюты

- **Seller** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения) - данные продавца

- **Buyer** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения) - данные покупателя

- **Signer** (объект :doc:`Signer <Signer>`, чтение, обязательно для заполнения) - данные подписанта документа

- **Type** (строка, чтение) - тип документа (возвращает строку "InvoiceCorrectionContent")

- **Items** (:doc:`коллекция <Collection>` объектов :doc:`InvoiceCorrectionItem <InvoiceCorrectionItem>`, чтение, обязательно для заполнения) - табличная часть корректировочного счета-фактуры

- **TotalsInc** (объект :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - итоговая сумма к увеличению

- **TotalsDec** (объект :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - итоговая сумма к уменьшению

- **StructedAdditionalInfos** (:doc:`коллекция <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`, чтение/запись) - дополнительные сведения


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(InvoiceCorrectionContent)>` - добавляет строку в табличную часть корректировочного счета-фактуры

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo-(InvoiceCorrectionContent)>` - добавляет строку дополнительных сведений

-  :doc:`AddOriginalInvoice <AddOriginalInvoice>` - добавляет строку c данными о счет-фактуре, на основании которого был выставлен корректировочный счет-фактура



.. toctree::
   :name: Auto
   :hidden:

   AddItem-(InvoiceCorrectionContent) <AddItem-(InvoiceCorrectionContent)>
   InvoiceCorrectionItem <InvoiceCorrectionItem>
   InvoiceTotalsDiff <InvoiceTotalsDiff> 
   InvoiceItemFields <InvoiceItemFields>
   AmountsDiff <AmountsDiff>  
   AddStructedAdditionalInfo <AddStructedAdditionalInfo-(InvoiceCorrectionContent)>
   OriginalInvoice <OriginalInvoice>
   AddOriginalInvoice <AddOriginalInvoice>
