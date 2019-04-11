Релиз 5.16.0
============

.. feed-entry::
   :date: 2017-04-10

    - Поддержка УКД в компоненте:
        - Новый тип отправляемого документа для :doc:`CreateSendTask`: **UniversalCorrectionDocument**
        - Новые типы отправляемых документов для :doc:`AddDocument`: **UniversalCorrectionDocument** и **UniversalCorrectionDocumentRevision**. Соответствующий новый тип возвращаемого значения - :doc:`UcdToSend`
        - Новый тип контента :doc:`UcdSellerContent`
        - Новые типы документов :doc:`Document`: :doc:`Ucd` и :doc:`UcdRevision`
        - Изменилась сигнатура :doc:`GetExtendedSignerDetails`, теперь принимает аргумент **forCorrection**
        - В :doc:`SetExtendedSignerDetailsTask` появилось свойство **ForCorrection**
    - Изменилась сигнатура и семантика :doc:`CanSendInvoice` - определяет можно ли подписывать счета-фактуры переданным сертификатом
    - Для :doc:`Utd` и :doc:`UtdRevision` реализована отправка ИоП - методы: :doc:`SendReceiptsAsync` и :doc:`SendReceiptsAsync`
    - Поддержка отправки "с полки" в :doc:`SendTask` и :doc:`PackageSendTask` - свойство **UseShelf**
    - Методы :doc:`Send` и :doc:`SendAsync` теперь возвращают идентификатор организации

Исправлены ошибки:
    - В COM-компоненте, в :doc:`DocumentsTask` не искались иУПД
    - Пустая строка в свойстве **Type** объекта :doc:`Utd` для иУПД
    - Запись значений по-умолчанию в свойства **InvoiceRevisionDate** и **InvoiceRevisionNumber**, объекта :doc:`InvoiceContent` приводила к измению типа документа на исправительный счет-фактура
    - Свойство **EventType** объекта :doc:`DocumentEvent` теперь принимает корректные значения для событий документов УПД и УКД

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_