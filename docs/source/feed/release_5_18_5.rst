Релиз 5.18.5
=============

.. feed-entry::
   :date: 2017-08-14

Исправлены ошибки:

- невозможно задать и получить информацию о подписанте для УКД с помощью :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>` и :doc:`SetExtendedSignerDetailsTask <SetExtendedSignerDetailsTask>`
- корректные формализованные отказы в подписи для роуминговых ящиков
- в COM-компоненте некорректно обращение к памяти при вызове :doc:`AddExtendedSigner <AddExtendedSigner>`
- зависание при вызове методов, если заданы неверные реквизиты прокси
- обновление протобуферов, InvoiceCorrectionTable.Items[0].OriginalValues.SubtotalWithVatExcluded (поле **TotalWithVatExcluded** объекта :doc:`InvoiceItemFields <InvoiceItemFields>`) теперь не обязателен
- метод :doc:`GetRecipientSignature <GetRecipientSignature>` не возвращал подпись для неформализованных документов
- поле **Type** объекта :doc:`DocumentToSend <DocumentToSend>` и поле **Type** объекта :doc:`BaseContent <BaseContent>` для документов в формате 155 приказа возвращали соответствующие значения UtdInvoice, UtdAcceptanceCertificate и UtdTorg12, теперь поле **Type** объекта :doc:`BaseContent <BaseContent>` для таких документов возвращет значение UniversalTransferDocument

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_