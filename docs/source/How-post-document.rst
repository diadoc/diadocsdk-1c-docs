Как отправить документы
=======================

Отправка документов возможна только тем контрагентам в Диадоке, с которыми :doc:`установлены партнерские отношения <How-trust>`


Способ 1
--------
Отправка документов производится с помощью объекта :doc:`PackageSendTask2 <PackageSendTask2>` путём добавления в него :doc:`документов на отправку <CustomDocumentToSend>`.

При использовании данного метода необходимо заполнить :doc:`мета информацию <DocumentMetadataItem>`, у которой источник (Source) указан *"User"*.



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
        MetaData = Third_DocumentToSend.AddMetadata();
        MetaData.Key   = "FileName";
        MetaData.Value = "Имя Файла Для Передачи.xml";

        ОтправленныеДокументы = SendTask.Send();

    КонецПроцедуры


Способ 2
--------

.. deprecated:: 5.27.0

Отправка документов производится с помощью объекта :doc:`PackageSendTask <PackageSendTask>`

.. code-block:: c#

    Процедура ОтправитьДокументы(Organization, Counteragent)

        // Создание задания на отправку
        SendTask = Organization.CreatePackageSendTask();
        SendTask.CounterAgentId = Counteragent.Id;

        // Добавление документа для заполнения контента средствами компоненты
        // Предполагаем, что процедура заполнения контента уже существует
        First_DocumentToSend = SendTask.AddDocument("UniversalTransferDocument");
        First_DocumentToSend.Comment = "Это УПД с заполнением контента средствами компоненты";
        ЗаполнитьКонтентДокумента(First_DocumentToSend.Content);

        // Добавление документа УПД с контентом, взятым из файла
        Second_DocumentToSend = SendTask.AddDocumentFromFileRaw("UniversalTransferDocument", "С:\\Moй УПД.xml");
        Second_DocumentToSend.Comment = "Это УПД с контентом, загруженным из файла";

        // Добавление неформализованного документа
        Third_DocumentToSend = SendTask.AddDocumentFromFileRaw("Nonformalized", "С:\\Документ.pdf");
        Third_DocumentToSend.Comment = "Это неформализованный документ";

        ОтправленныеДокументы = SendTask.Send();

    КонецПроцедуры


.. seealso:: :doc:`Organization.GetDocumentTypes <GetDocumentTypes>`
