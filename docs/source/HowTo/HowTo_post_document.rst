Как отправить документы
=======================

Отправка документов возможна только тем контрагентам в Диадоке, с которыми :doc:`установлены партнерские отношения <HowTo_trust_counteragent>`

Отправка документов производится с помощью объекта :doc:`PackageSendTask2 <../ComObjects/PackageSendTask2>`.
Формализованные документы поддерживают заполнение контента через :doc:`../ComObjects/DynamicContent`

Для отправляемого документа необходимо заполнить :doc:`мета информацию <../ComObjects/DocumentMetadataItem>`, у которой источник (поле **Source**) указан ``User``



.. code-block:: c#

    Процедура ОтправитьДокументы(Organization, Counteragent)

        // Создание задания на отправку
        SendTask = Organization.CreatePackageSendTask2();
        SendTask.CounterAgentId = Counteragent.Id;

        // Добавление документа для заполнения контента средствами компоненты
        // Предполагаем, что процедура заполнения контента уже существует
        First_DocumentToSend = SendTask.AddDocument("UniversalTransferDocument", "СЧФДОП", "utd820_05_01_01");
        First_DocumentToSend.Comment = "Это УПД с заполнением контента средствами компоненты";
        ЗаполнитьДинамическийКонтентДокумента(First_DocumentToSend.Content);

        // Добавление документа УПД с контентом, взятым из файла
        Second_DocumentToSend = SendTask.AddDocumentFromFile("UniversalTransferDocument", "СЧФДОП", "utd820_05_01_01", "С:\\Moй УПД.xml");
        Second_DocumentToSend.Comment = "Это УПД с контентом, загруженным из файла";

        // Добавление неформализованного документа
        Third_DocumentToSend = SendTask.AddDocumentFromFile("Nonformalized", "default", "v1", "С:\\Документ.pdf");
        Third_DocumentToSend.Comment = "Это неформализованный документ";
        MetaDataItem = Third_DocumentToSend.AddMetadata();
        MetaDataItem.Key   = "FileName";
        MetaDataItem.Value = "Имя Файла Для Передачи.xml";

        ОтправленныеДокументы = SendTask.Send();

    КонецПроцедуры


.. seealso:: :meth:`Organization.GetDocumentTypes`
