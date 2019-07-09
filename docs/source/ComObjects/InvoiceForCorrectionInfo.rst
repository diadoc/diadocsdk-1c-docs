InvoiceForCorrectionInfo
========================

`Сведения о cчете-фактуре, к которому составлен корректировочный счет-фактура <https://normativ.kontur.ru/document?moduleId=1&documentId=273231&rangeId=230596>`_

.. rubric:: Свойства

:InvoiceDate:
  **Дата, чтение/запись** - дата счета-фактуры

:InvoiceNumber:
  **Строка, чтение/запись** - номер счета-фактуры

:InvoiceRevisions:
  :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceRevisionInfo <InvoiceRevisionInfo>` **, чтение** - список исправлений



.. rubric:: Методы

+------------------------------------------------+
| |InvoiceForCorrectionInfo-AddInvoiceRevision|_ |
+------------------------------------------------+

.. |InvoiceForCorrectionInfo-AddInvoiceRevision| replace:: AddInvoiceRevision()



.. _InvoiceForCorrectionInfo-AddInvoiceRevision:
.. method:: InvoiceForCorrectionInfo.AddInvoiceRevision()

  Добавляет :doc:`новый элемент <InvoiceRevisionInfo>` в коллекцию *InvoiceRevisions* и возвращает его
