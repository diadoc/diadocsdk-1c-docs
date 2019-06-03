Как выполнить ответные действия по документам
=============================================

Большинство ответных действий с документом выполняется с помощью объекта :doc:`ReplySendTask <ReplySendTask>`.
Создать этот объект можно из контекста :doc:`документа <Document>` или :doc:`пакета документов <DocumentPackage>` методом CreateReplySendTask


Подписание входящего документа:
-------------------------------

::
    
    Процедура Заполнить_PackageContent(ReplyContent)

        КоличествоКонтентовОтвета = ReplyContent.ContentItems.Count();
        Для ц = 0 По КоличествоКонтентовОтвета - 1 Цикл
            PackageContentItem = ReplyContent.ContentItems.GetItem(ц);
            ЗаполнитьКонтентОтвета(PackageContentItem.Content);
        КонецЦикла;

    КонецПроцедуры

    // Предполагаем, что есть функции заполнения контента второго титула формализованных документов
    Процедура ЗаполнитьКонтентОтвета(ReplyContent)

        ContentType = ReplyContent.Type;
        Если ContentType = "PackageContent" Тогда
            Заполнить_PackageContent(ReplyContent)

        ИначеЕсли ContentType = "XmlTorg12BuyerTitle" Тогда
            Заполнить_Torg12BuyerContent(ReplyContent)

        ИначеЕсли ContentType = "TovTorgBuyerTitle" Тогда
            Заполнить_TovTorgBuyerContent(ReplyContent)

        ИначеЕсли ContentType = "XmlAcceptanceCertificateBuyerTitle" Тогда
            Заполнить_XmlAcceptanceCertificateBuyerTitle(ReplyContent)
                
        ИначеЕсли ContentType = "XmlAcceptanceCertificate552BuyerTitle" Тогда
            Заполнить_Act552BuyerContent(ReplyContent)

        ИначеЕсли ContentType = "UniversalTransferDocumentBuyerTitle" Тогда
            Заполнить_UtdBuyerContent(ReplyContent)

        ИначеЕсли ContentType = "AcceptanceContent" Тогда
            // Ничего дополнительно заполнять не нужно

        КонецЕсли;
        
    КонецПроцедуры


    Процедура ПодписатьДокументы (DocumentPackage)

        ReplySendTask = DocumentPackage.CreateReplySendTask("Accept");
        ЗаполнитьКонтентОтвета(ReplySendTask.Content);
        ReplySendTask.Send();

    КонецПроцедуры



Отказ в подписи
---------------

::

    Процедура ОтказатьВПодписиПоДокументу (Document)

        ReplySendTask = Document.CreateReplySendTask("RejectDocument");
        FormalizedRejectionContent = ReplySendTask.Content;
        FormalizedRejectionContent.Comment = "Комментарий отказа";
        
        Signer = FormalizedRejectionContent.Signer;
        
        Signer.Surname    = "Фамилия";
        Signer.FirstName  = "Имя";
        Signer.Patronymic = "Отчество";
        Signer.JobTitle   = "Должность";
        Signer.Inn        = "966785367420";
        
        ReplySendTask.Send();

    КонецПроцедуры



Запрос корректировки
--------------------

::

    Процедура ЗапроситьКорректировку(Document)
    
        ReplySendTask = Document.CreateReplySendTask("CorrectionRequest");
        CorrectionRequestContent = ReplySendTask.Content;
        CorrectionRequestContent.Comment = "Комментарий запроса корректировки";
        
        Signer = CorrectionRequestContent.Signer;
        
        Signer.Surname    = "Фамилия";
        Signer.FirstName  = "Имя";
        Signer.Patronymic = "Отчество";
        Signer.JobTitle   = "Должность";
        Signer.Inn        = "966785367420";
        
        ReplySendTask.Send();
    
    КонецПроцедуры


Запрос аннулирования
--------------------

::

    Процедура ЗапроситьАннулирование(Document)
    
        ReplySendTask = Document.CreateReplySendTask("RevocationRequest");
        RevocationRequestContent = ReplySendTask.Content;
        RevocationRequestContent.Comment = "Комментарий запроса аннулирования";
        
        Signer = RevocationRequestContent.Signer;
        
        Signer.Surname    = "Фамилия";
        Signer.FirstName  = "Имя";
        Signer.Patronymic = "Отчество";
        Signer.JobTitle   = "Должность";
        Signer.Inn        = "966785367420";
        
        ReplySendTask.Send();
    
    КонецПроцедуры


Подтверждение аннулирования
---------------------------

::

    Процедура ПодтвердитьАннулирование(Document)
    
        ReplySendTask = Document.CreateReplySendTask("AcceptRevocation");
        ReplySendTask.Send();
    
    КонецПроцедуры



Отказать в аннулировании
------------------------

::

    Процедура ОтказатьВАннулирвоании (Document)

        ReplySendTask = Document.CreateReplySendTask("RejectRevocation");
        FormalizedRejectionContent = ReplySendTask.Content;
        FormalizedRejectionContent.Comment = "Комментарий отказа";
        
        Signer = FormalizedRejectionContent.Signer;
        
        Signer.Surname    = "Фамилия";
        Signer.FirstName  = "Имя";
        Signer.Patronymic = "Отчество";
        Signer.JobTitle   = "Должность";
        Signer.Inn        = "966785367420";
        
        ReplySendTask.Send();

    КонецПроцедуры
