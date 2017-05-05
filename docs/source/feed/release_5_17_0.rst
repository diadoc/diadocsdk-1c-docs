Релиз 5.17.0
============

.. feed-entry::
   :date: 2017-05-05

- Различные изменения COM-компоненты связанные с поддержкой многопоточности, поддержка режима MTA
- Расширена поддержка прокси: добавлена поддержка HTTP-ответа 407(Proxy Authentication Required) - запрос авторизации на прокси-сервере
- Расширен метод :doc:`AddContent <AddContent>`, объекта :doc:`CloudSignTask <CloudSignTask>`
- Автоматический расчет всех полей сумм в :doc:`Torg12Totals <Torg12Totals>` для :doc:`Torg12Content <Torg12Content>`
- У объектов :doc:`Utd <Utd>`, :doc:`UtdRevision <UtdRevision>`, :doc:`Ucd <Ucd>`, :doc:`UcdRevision <UcdRevision>` расширена поддержка работы с запросами на уточнение: добавлено свойство **AmendmentRequested** и метод :doc:`GetAmendmentRequestedComment <GetAmendmentRequestedComment-(Utd)>`
- Измененено поведение метода :doc:`GetCounteragentListByInnList <GetCounteragentListByInnList>` - теперь для одного ИНН возвращаеться весь набор организаций
- В базовый объект документа :doc:`Document <Document>` добавлено свойство **AttachmentVersion** - информация о версии XSD схемы, в соотвествии с которой сформирован документ
- Оптимизация работы объекта :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>`

Исправлены ошибки:

- Ошибка времени исполнения в COM-компоненте при добавлении элементов в некоторые коллекции объектов поддержки УКД
- Ошибка, связи с которой у объектов :doc:`Invoice <Invoice>` :doc:`InvoiceRevision <InvoiceRevision>`, :doc:`InvoiceCorrection <InvoiceCorrection>`, :doc:`InvoiceCorrectionRevision <InvoiceCorrectionRevision>` не работал метод :doc:`SendReceiptsAsync <SendReceiptsAsync>`
- Исправлена работа метода :doc:`GetRecipientSignature <GetRecipientSignature>` для УПД с функцией "СЧФ" и УКД с функцией "КСЧФ"
- Объект :doc:`InvoiceRevision <InvoiceRevision>` теперь поддерживает УПД-содержимое

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_