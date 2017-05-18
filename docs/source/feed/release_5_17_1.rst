Релиз 5.17.1
============

.. feed-entry::
   :date: 2017-05-18

- Поддержка документов старых типов с упд-контентом(UtdInvoice, UtdAcceptanceCertificate, UtdTorg12) в :doc:`AddDocumentFromFileRaw <AddDocumentFromFileRaw>` и :doc:`CreateSendTaskFromFileRaw <CreateSendTaskFromFileRaw>`
- Поддержка шифрования InvoiceCorrection и InvoiceCorrectionRevision

Исправлены ошибки:

- генерация корректных метаданных для шифрованных документов
- корректное получение титула покупателя для шифрованных документов - методы GetBuyerContent

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_