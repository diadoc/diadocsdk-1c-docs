InvoiceCorrectionTable
======================

Сведения таблицы корректировочного счета-фактуры

Свойства объекта
----------------


- **Items** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedInvoiceCorrectionItem <ExtendedInvoiceCorrectionItem>`, чтение) - информация о товарах

- **TotalsInc** (:doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - суммы к увеличению

- **TotalsDec** (:doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - суммы к уменьшению

Методы объекта
--------------

- :doc:`AddItem <AddItem-(InvoiceCorrectionTable)>` - добавляет элемент информации о товарах
