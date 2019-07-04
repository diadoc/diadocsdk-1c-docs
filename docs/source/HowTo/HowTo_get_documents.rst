Как получить список документов
==============================

Список документов можно получить только в контексте :doc:`организации <Organization>`.

Для получения документов используется объект :doc:`DocumentTask <DocumentsTask>`.

.. code-block:: c#

    // Создаем объект DocumentsTask
    DocumentsTask = Organization.GetDocumentsTask();

    // Заполняем параметры отбора документов
    DocumentsTask.FromSendDate = НачалоГода(ТекущаяДата());
    DocumentsTask.ToSendDate   = КонецГода(ТекущаяДата());
    DocumentsTask.Category     = "XmlTorg12.InboundWaitingForRecipientSignature";

    // Получаем коллекцию документов
    DocumentList = DocumentsTask.GetDocuments();

    Ц = 0;
    Пока ц < DocumentList.Count Цикл
        Document = DocumentList.GetItem(Ц);
        Сообщить("Не подписан торг-12 №" + Document.Number + " от " + Document.Date);
        Ц = Ц + 1;
    КонецЦикла;
