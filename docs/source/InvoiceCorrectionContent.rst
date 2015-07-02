InvoiceCorrectionContent
========================

Объект предназначен для работы с содержанием документов
«корректировочный счет-фактура» и «исправление корректировочного
счета-фактуры».

Свойства объекта
----------------


- **InvoiceVersion** (строка, чтение/запись, --- ) - версия формата корректировочного счет-фактуры. Может принимать значения "5.01", "5.02"

- **Date** (дата, чтение/запись, обязательно для заполнения ) - дата счет-фактуры

- **Number** (строка, чтение/запись, обязательно для заполнения, длина не более 256 символов ) - номер счет-фактуры

- **InvoiceRevision Date** (дата, чтение/запись, --- ) - дата исправленния счет-фактуры (заполняется, если КСФ/ИКСФ формируется на исправленный СФ)

- **InvoiceRevision Number** (строка, чтение/запись, длина не более 3 символов ) - номер исправления счет-фактуры (заполняется, если КСФ/ИКСФ формируется на исправленный СФ)

- **InvoiceCorrection Date** (дата, чтение/запись, --- ) - дата КСФ

- **InvoiceCorrection Number** (строка, чтение/запись, длина не более 256 символов ) - номер КСФ

- **InvoiceCorrection RevisionDate** (дата, чтение/запись, --- ) - дата исправления КСФ

- **InvoiceCorrection RevisionNumber** (строка, чтение/запись, длина не более 3 символов ) - номер исправления КСФ

- **Currency** (строка, чтение/запись, обязательно для заполнения. Числовая строка длиной 3 символа. Код должен содержаться в общероссийском классификаторе валют. ) - код валюты

- **Seller** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения ) - данные продавца

- **Buyer** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения ) - данные покупателя

- **Signer** (объект :doc:`Signer <Signer>`, чтение, обязательно для заполнения ) - данные подписанта документа

- **Type** (строка, чтение, --- ) - тип документа

- **Items** (:doc:`InvoiceCorrectionItem <InvoiceCorrectionItem>`, чтение, обязательно для заполнения ) - табличная часть корректировочного счет-фактуры

- **TotalsInc** (объект :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение, --- ) - итоговая сумма к увеличению

- **TotalsDesc** (объект :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение, --- ) - итоговая сумма к уменьшению

- **AdditionalInfo** (строка, чтение/запись, --- ) - дополнительные сведения


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(InvoiceCorrectionContent)>` - добавляет строку в табличную часть корректировочного счет-фактуры


.. toctree::
   :name: Auto
   :hidden:

   AddItem-(InvoiceCorrectionContent) <AddItem-(InvoiceCorrectionContent)>
   InvoiceCorrectionItem <InvoiceCorrectionItem>
   InvoiceTotalsDiff <InvoiceTotalsDiff> 
   InvoiceItemFields <InvoiceItemFields>
   AmountsDiff <AmountsDiff>  
