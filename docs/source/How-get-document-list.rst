Как получить список документов
==============================

Список документов можно получить только в контексте :doc:`организации <Organization>`.
Получение контекста организации описано в разделе :doc:`Как авторизоваться в системе Диадок <How-auth>`.

Получение документов производится с помощью объекта :doc:`DocumentTask <DocumentsTask>`.

::

    //Создаем объект DocumentsTask
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
