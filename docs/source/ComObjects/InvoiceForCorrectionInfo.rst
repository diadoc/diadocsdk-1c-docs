InvoiceForCorrectionInfo
========================

Сведения о cчете-фактуре (первичном документе), к которому составлен корректировочный счет-фактура

Свойства объекта
----------------


- **InvoiceDate** (дата, чтение/запись) - дата счета-фактуры

- **InvoiceNumber** (строка, чтение/запись) - номер счета-фактуры

- **InvoiceRevisions** (коллекция :doc:`Collection<Collection>` объектов :doc:`InvoiceRevisionInfo <InvoiceRevisionInfo>`) - с учетом исправления

Методы объекта
--------------


-  :doc:`AddInvoiceRevision <AddInvoiceRevision-(InvoiceForCorrectionInfo)>` - добавляет строку "с учетом исправления"


.. toctree::
   :name: Auto
   :hidden:

   InvoiceRevisionInfo <InvoiceRevisionInfo>
   AddInvoiceRevision <AddInvoiceRevision-(InvoiceForCorrectionInfo)>
