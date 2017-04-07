InvoiceCorrectionTable
======================

Сведения таблицы корректировочного счета-фактуры

Свойства объекта
----------------


- **Items** (коллекция :doc:`Collection <Collection>` объектов :doc:`ExtendedInvoiceCorrectionItem <ExtendedInvoiceCorrectionItem>`, чтение) - информация о товарах

- **TotalsInc** (объект :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - суммы к увеличению

- **TotalsDec** (объект :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - суммы к уменьшению

Методы объекта
--------------

- :doc:`AddItem <AddItem-(InvoiceCorrectionTable)>` - добавляет элемент информации о товарах

.. toctree::
   :name: Auto
   :hidden:

   ExtendedInvoiceCorrectionItem <ExtendedInvoiceCorrectionItem>
   AddItem <AddItem-(InvoiceCorrectionTable)>
