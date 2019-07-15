Релиз 5.16.0
============

.. feed-entry::
   :date: 2017-04-10

- Поддержка УКД в компоненте:
    - Новый тип отправляемого документа для CreateSendTask: **UniversalCorrectionDocument**
    - Новые типы отправляемых документов для AddDocument: **UniversalCorrectionDocument** и **UniversalCorrectionDocumentRevision**. Соответствующий новый тип возвращаемого значения - UcdToSend
    - Новый тип контента UcdSellerContent
    - Новые типы документов Document: Ucd и UcdRevision
    - Изменилась сигнатура GetExtendedSignerDetails, теперь принимает аргумент **forCorrection**
    - В SetExtendedSignerDetailsTask появилось свойство **ForCorrection**
- Изменилась сигнатура и семантика CanSendInvoice - определяет можно ли подписывать счета-фактуры переданным сертификатом
- Для Utd и UtdRevision реализована отправка ИоП - методы: SendReceiptsAsync и SendReceiptsAsync
- Поддержка отправки "с полки" в SendTask и PackageSendTask - свойство **UseShelf**
- Методы Send и SendAsync теперь возвращают идентификатор организации

Исправлены ошибки:
    - В COM-компоненте, в DocumentsTask не искались иУПД
    - Пустая строка в свойстве **Type** объекта Utd для иУПД
    - Запись значений по-умолчанию в свойства **InvoiceRevisionDate** и **InvoiceRevisionNumber**, объекта InvoiceContent приводила к измению типа документа на исправительный счет-фактура
    - Свойство **EventType** объекта DocumentEvent теперь принимает корректные значения для событий документов УПД и УКД

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_
