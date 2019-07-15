Релиз 5.17.0
============

.. feed-entry::
   :date: 2017-05-05

- Различные изменения COM-компоненты связанные с поддержкой многопоточности, поддержка режима MTA
- Расширена поддержка прокси: добавлена поддержка HTTP-ответа 407(Proxy Authentication Required) - запрос авторизации на прокси-сервере
- Расширен метод AddContent объекта CloudSignTask
- Автоматический расчет всех полей сумм в Torg12Totals для Torg12Content
- У объектов Utd, UtdRevision, Ucd, UcdRevision расширена поддержка работы с запросами на уточнение: добавлено свойство **AmendmentRequested** и метод GetAmendmentRequestedComment
- Измененено поведение метода GetCounteragentListByInnList - теперь для одного ИНН возвращаеться весь набор организаций
- В базовый объект документа Document добавлено свойство **AttachmentVersion** - информация о версии XSD схемы, в соотвествии с которой сформирован документ
- Оптимизация работы объекта ReceiptGenerationProcess

Исправлены ошибки:
    - Ошибка времени исполнения в COM-компоненте при добавлении элементов в некоторые коллекции объектов поддержки УКД
    - Ошибка, связи с которой у объектов Invoice, InvoiceRevision, InvoiceCorrection, InvoiceCorrectionRevision не работал метод SendReceiptsAsync
    - Исправлена работа метода GetRecipientSignature для УПД с функцией "СЧФ" и УКД с функцией "КСЧФ"
    - Объект InvoiceRevision теперь поддерживает УПД-содержимое

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_
