Как выполнить ответные действия по документам
=============================================

Большинство ответных действий с документом выполняется с помощью объекта :doc:`ReplySendTask2 <ReplySendTask2>`.
Создать этот объект можно из контекста :doc:`документа <Document>` или :doc:`пакета документов <DocumentPackage>` методом CreateReplySendTask2

.. code-block:: c#

    Процедура ВыполнитьОтветноеДействие(DocumentPackage, ТипОтвета)

        ReplyTask = DocumentPackage.CreateReplySendTask2(ТипОтвета);
        ContentItems = ReplyTask.ContentItems;

        Если ТипОтвета = "AcceptDocument" Тогда
            ЗаполнитьКонтентПодписания(ContentItems);

        ИначеЕсли ТипОтвета = "RejectDocument" Тогда
            ЗаполнитьКонтентОтказаПодписи(ContentItems);

        ИначеЕсли ТипОтвета = "CorrectionRequest" Тогда
            ЗаполнитьКонтентЗапросаКорректировки(ContentItems);

        ИначеЕсли ТипОтвета = "RevocationRequest" Тогда
            ЗаполнитьКонтентЗапросаАннулирования(ContentItems);

        ИначеЕсли ТипОтвета = "AcceptRevocation" Тогда
            ЗаполнитьКонтентПодтвержденияАннулирования(ContentItems);

        ИначеЕсли ТипОтвета = "RejectRevocation" Тогда
            ЗаполнитьКонтентОтказаАннулирования(ContentItems);
        КонецЕсли;

        ReplyTask.Send();

    КонецПроцедуры


Подписание входящего документа:
-------------------------------

.. code-block:: c#
    



    Функция НуженВторойТитул(WorkflowId)
    
        Возврат  WorkflowId = 3
             ИЛИ WorkflowId = 5
             ИЛИ WorkflowId = 8
             ИЛИ WorkflowId = 11;
             
    КонецФункции


    Процедура ЗаполнитьКонтентПодписания(ContentItems)

        КоличествоКонтентов = ContentItems.Count();

        Для ц = 0 По КоличествоКонтентов - 1 Цикл

            ContentItem = ContentItems.GetItem(ц);

            Если НуженВторойТитул(ContentItem.Document.WorkflowId) Тогда
            // Предполагаем, что есть функции заполнения контента второго титула формализованных документов
            Заполнить_DynamicContent(ContentItem.Content);
            КонецЕсли;

        КонецЦикла;

    КонецПроцедуры



Отказ в подписи
---------------

.. code-block:: c#

    Процедура ЗаполнитьКонтентОтказаПодписи(ContentItems)

        КоличествоКонтентов = ContentItems.Count();

        Для ц = 0 По КоличествоКонтентов - 1 Цикл

            FormalizedRejectionContent = ContentItems.GetItem(ц).Content;
            FormalizedRejectionContent.Comment = "Комментарий отказа";

            Signer = FormalizedRejectionContent.Signer;

            Signer.Surname    = "Фамилия";
            Signer.FirstName  = "Имя";
            Signer.Patronymic = "Отчество";
            Signer.JobTitle   = "Должность";
            Signer.Inn        = "966785367420";

        КонецЦикла;

    КонецПроцедуры



Запрос корректировки
--------------------

.. code-block:: c#

    Процедура ЗаполнитьКонтентЗапросаКорректировки(ContentItems)

        КоличествоКонтентов = ContentItems.Count();

        Для ц = 0 По КоличествоКонтентов - 1 Цикл

            CorrectionRequestContent = ContentItems.GetItem(ц).Content;
            CorrectionRequestContent.Comment = "Комментарий запроса корректировки";

            Signer = CorrectionRequestContent.Signer;

            Signer.Surname    = "Фамилия";
            Signer.FirstName  = "Имя";
            Signer.Patronymic = "Отчество";
            Signer.JobTitle   = "Должность";
            Signer.Inn        = "966785367420";

        КонецЦикла;

    КонецПроцедуры



Запрос аннулирования
--------------------

.. code-block:: c#

    Процедура ЗаполнитьКонтентЗапросаАннулирования(ContentItems)

        КоличествоКонтентов = ContentItems.Count();

        Для ц = 0 По КоличествоКонтентов - 1 Цикл

            RevocationRequestContent = ContentItems.GetItem(ц).Content;
            RevocationRequestContent.Comment = "Комментарий запроса аннулирования";

            Signer = RevocationRequestContent.Signer;

            Signer.Surname    = "Фамилия";
            Signer.FirstName  = "Имя";
            Signer.Patronymic = "Отчество";
            Signer.JobTitle   = "Должность";
            Signer.Inn        = "966785367420";

        КонецЦикла;

    КонецПроцедуры



Подтверждение аннулирования
---------------------------

.. code-block:: c#

    Процедура ЗаполнитьКонтентПодтвержденияАннулирования(ContentItems)

        // Ничего дополнительно заполнять не требуется

    КонецПроцедуры



Отказать в аннулировании
------------------------

.. code-block:: c#

    Процедура ЗаполнитьКонтентОтказаАннулирования(ContentItems)

        КоличествоКонтентов = ContentItems.Count();

        Для ц = 0 По КоличествоКонтентов - 1 Цикл

            FormalizedRejectionContent = ContentItems.GetItem(ц).Content;
            FormalizedRejectionContent.Comment = "Комментарий отказа";

            Signer = FormalizedRejectionContent.Signer;

            Signer.Surname    = "Фамилия";
            Signer.FirstName  = "Имя";
            Signer.Patronymic = "Отчество";
            Signer.JobTitle   = "Должность";
            Signer.Inn        = "966785367420";

        КонецЦикла;

    КонецПроцедуры