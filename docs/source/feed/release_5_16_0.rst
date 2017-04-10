Релиз 5.16.0
============

.. feed-entry::
   :date: 2017-04-10

- Поддержка УКД в компоненте:
    - Новый тип отправляемого документа для :doc:`CreateSendTask <CreateSendTask>`: **UniversalCorrectionDocument**
    - Новые типы отправляемых документов для :doc:`AddDocument <AddDocument>`: **UniversalCorrectionDocument** и **UniversalCorrectionDocumentRevision**. Соответствующий новый тип возвращаемого значения - :doc:`UcdToSend <UcdToSend>`
    - Новый тип контента :doc:`UcdSellerContent <UcdSellerContent>`
    - Новые типы документов :doc:`Document <Document>`: :doc:`Ucd <Ucd>` и :doc:`UcdRevision <UcdRevision>`
    - Изменилась сигнатура :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>`, теперь принимает аргумент **forCorrection**
    - В :doc:`SetExtendedSignerDetailsTask <SetExtendedSignerDetailsTask>` появилось свойство **ForCorrection**
- Изменилась сигнатура и семантика :doc:`CanSendInvoice <CanSendInvoice>` - определяет можно ли подписывать счета-фактуры переданным сертификатом
- Для :doc:`Utd <Utd>` и :doc:`UtdRevision <UtdRevision>` реализована отправка ИоП - методы: :doc:`SendReceiptsAsync <SendReceiptsAsync-(Utd)>` и :doc:`SendReceiptsAsync <SendReceiptsAsync-(UtdRevision)>`
- Поддержка отправки "с полки" в :doc:`SendTask <SendTask>` и :doc:`PackageSendTask <PackageSendTask>` - свойство **UseShelf**
- Методы :doc:`Send <Send-(AcquireCounteragentTask)>` и :doc:`SendAsync <SendAsync-(AcquireCounteragentTask)>` теперь возвращают идентификатор организации
- Исправлены ошибки:
    - В COM-компоненте, в :doc:`DocumentsTask <DocumentsTask>` не искались иУПД
    - Пустая строка в свойстве **Type** объекта :doc:`Utd <Utd>` для иУПД
    - Запись значений по-умолчанию в свойства **InvoiceRevisionDate** и **InvoiceRevisionNumber**, объекта :doc:`InvoiceContent <InvoiceContent>` приводила к измению типа документа на исправительный счет-фактура
    - Свойство **EventType** объекта :doc:`DocumentEvent <DocumentEvent>` теперь принимает корректные значения для событий документов УПД и УКД

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_