ExtendedInvoiceCorrectionItem
=============================

Сведения о товаре (работе, услуге) универсального корректировочного документа

Свойства объекта
----------------


- **Product** (строка, чтение/запись, обязательно для заполнения. Длина строка не более 1000 символов) - наименование товара

- **OriginalValues** (:doc:`InvoiceItemFields <InvoiceItemFields>`, чтение, обязательно для заполнения) - значения до корректировки

- **CorrectedValues** (:doc:`InvoiceItemFields <InvoiceItemFields>`, чтение, обязательно для заполнения) - значения после корректировки

- **AmountsInc** (:doc:`AmountsDiff <AmountsDiff>`, чтение) - суммы к увеличению

- **AmountsDec** (:doc:`AmountsDiff <AmountsDiff>`, чтение) - суммы к уменьшению

- **ItemAccountDebit** (строка, чтение/запись) - корреспондирующие счета: дебет

- **ItemAccountCredit** (строка, чтение/запись) - корреспондирующие счета: кредит

- **StructedAdditionalInfos** (:doc:`коллекция <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`, чтение/запись) - дополнительные сведения


Методы объекта
--------------

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo-(ExtendedInvoiceCorrectionItem)>` - добавляет строку дополнительных сведений


.. toctree::
   :name: Auto
   :hidden:

   AddStructedAdditionalInfo <AddStructedAdditionalInfo-(ExtendedInvoiceCorrectionItem)>