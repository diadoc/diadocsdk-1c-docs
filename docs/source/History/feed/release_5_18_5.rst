Релиз 5.18.5
============

.. feed-entry::
   :date: 2017-08-14

Исправлены ошибки:

    - невозможно задать и получить информацию о подписанте для УКД с помощью GetExtendedSignerDetails и SetExtendedSignerDetailsTask
    - корректные формализованные отказы в подписи для роуминговых ящиков
    - в COM-компоненте некорректно обращение к памяти при вызове AddExtendedSigner
    - зависание при вызове методов, если заданы неверные реквизиты прокси
    - обновление протобуферов, InvoiceCorrectionTable.Items[0].OriginalValues.SubtotalWithVatExcluded (поле **TotalWithVatExcluded** объекта InvoiceItemFields) теперь не обязателен
    - метод GetRecipientSignature не возвращал подпись для неформализованных документов
    - поле **Type** объекта DocumentToSend и поле **Type** объекта BaseContent для документов в формате 155 приказа возвращали соответствующие значения UtdInvoice, UtdAcceptanceCertificate и UtdTorg12, теперь поле **Type** объекта BaseContent для таких документов возвращет значение "UniversalTransferDocument"

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_