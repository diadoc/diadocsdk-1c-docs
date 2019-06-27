Релиз 5.17.0
============

.. feed-entry::
   :date: 2017-05-05

- Различные изменения COM-компоненты связанные с поддержкой многопоточности, поддержка режима MTA
- Расширена поддержка прокси: добавлена поддержка HTTP-ответа 407(Proxy Authentication Required) - запрос авторизации на прокси-сервере
- Расширен метод :doc:`AddContent`, объекта :doc:`CloudSignTask`
- Автоматический расчет всех полей сумм в :doc:`Torg12Totals` для :doc:`Torg12Content`
- У объектов :doc:`Utd`, :doc:`UtdRevision`, :doc:`Ucd`, :doc:`UcdRevision` расширена поддержка работы с запросами на уточнение: добавлено свойство **AmendmentRequested** и метод :doc:`GetAmendmentRequestedComment`
- Измененено поведение метода :doc:`GetCounteragentListByInnList` - теперь для одного ИНН возвращаеться весь набор организаций
- В базовый объект документа :doc:`Document` добавлено свойство **AttachmentVersion** - информация о версии XSD схемы, в соотвествии с которой сформирован документ
- Оптимизация работы объекта :doc:`ReceiptGenerationProcess`

Исправлены ошибки:
    - Ошибка времени исполнения в COM-компоненте при добавлении элементов в некоторые коллекции объектов поддержки УКД
    - Ошибка, связи с которой у объектов :doc:`Invoice` :doc:`InvoiceRevision`, :doc:`InvoiceCorrection`, :doc:`InvoiceCorrectionRevision` не работал метод :doc:`SendReceiptsAsync`
    - Исправлена работа метода :doc:`GetRecipientSignature` для УПД с функцией "СЧФ" и УКД с функцией "КСЧФ"
    - Объект :doc:`InvoiceRevision` теперь поддерживает УПД-содержимое

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_