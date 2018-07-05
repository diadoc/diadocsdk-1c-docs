Как формировать и отправлять пакеты документов
==============================================

Отправка пакетов документов возможна только тем контрагентам в Диадоке, с
которыми установлены партнерские отношения (см. раздел :doc:`Как установить 
партнерские отношения <How-trust>`).

Для отправки пакета необходимо использовать
метод :doc:`CreatePackageSendTask <CreatePackageSendTask>` объекта
:doc:`Organization <Organization>`. Данный метод возвращает объект
:doc:`PackageSendTask <PackageSendTask>`, который позволяет добавлять документы в пакет и задавать
различные параметры отправки пакета.

:doc:`PackageSendTask <PackageSendTask>`, позволяет добавить документы в пакет в следующих вариантах:

- :doc:`AddDocument <AddDocument>` - добавляет формализованный документ, возвращает объект титула документа
- :doc:`AddDocumentFromFile <AddDocumentFromFile>` - добавляет формализованный или неформализованный документ из файла. Для формализованных документов возвращает объект титула. Для неформаллизованных возвращает объект позволяющий задать метаданные.
- :doc:`AddDocumentFromFileRaw <AddDocumentFromFileRaw>` - добавляет формализованный или неформализованный документ из файла. Документ добавляеться "как есть". Возвращает объект позволяющий задать базовые метаданные.

Например, следующая процедура позволяет отправить накладную и неформализованный счет:

::

          Процедура ОтправитьПакетДокументов(Organization, CounteragentId, PackageOperationId, CustomIdXmlTorg12, CustomIdNonformalizedProforma)

            PackageSendTask = Organization.CreatePackageSendTask();
                  
            PackageSendTask.CounteragentId 	= CounteragentId;
            PackageSendTask.DelaySend 		= Ложь;
            PackageSendTask.OperationId 	= PackageOperationId;

            // добавляем в сообщение расходную накладную
            DocumentXmlTorg12 = PackageSendTask.AddDocument("XmlTorg12");

            DocumentXmlTorg12.CustomDocumentId 		= CustomIdXmlTorg12;
            DocumentXmlTorg12.Content.Date   		= '20170606';
            DocumentXmlTorg12.Content.Number 		= "РН1";
            DocumentXmlTorg12.Content.WaybillDate   = '20170606'; 
            DocumentXmlTorg12.Content.WaybillNumber = "ТН1";

            DocumentXmlTorg12.Content.GroundName   	= "Заказ покупателя"; 
            DocumentXmlTorg12.Content.GroundDate   	= '20170606'; 
            DocumentXmlTorg12.Content.GroundNumber 	= "ЗП1"; 

            DocumentXmlTorg12.Content.Seller.Name = "ООО Продавец";
            DocumentXmlTorg12.Content.Seller.Inn  = "2012600006";
            DocumentXmlTorg12.Content.Seller.Kpp  = "111111111";
            DocumentXmlTorg12.Content.Seller.Address.RegionCode = "66"; 

            DocumentXmlTorg12.Content.Buyer.Name = "ООО Покупатель";
            DocumentXmlTorg12.Content.Buyer.Inn  = "2012600006";
            DocumentXmlTorg12.Content.Buyer.Kpp  = "222222222";
            DocumentXmlTorg12.Content.Buyer.Address.RegionCode = "66";

            //DocumentXmlTorg12.Content.Shipper и DocumentXmlTorg12.Content.Consignee
            //заполняются по аналогии

            Item = DocumentToSend.Content.AddItem();

            Item.Product               = "Товар";
            Item.UnitCode              = "166";
            Item.Quantity              = 10;
            Item.Price                 = 100;
            Item.TotalWithVatExcluded  = 1000;
            Item.TaxRate               = "18";
            Item.Vat                   = 180;
            Item.Total                 = 1180;

            DocumentXmlTorg12.Content.Totals.Quantity 				= 10;
            DocumentXmlTorg12.Content.Totals.TotalWithVatExcluded 	= 1000;
            DocumentXmlTorg12.Content.Totals.Vat 					= 180;
            DocumentXmlTorg12.Content.Totals.Total 					= 1180;

            DocumentXmlTorg12.Content.SupplyAllowedBy.Surname		= "Иванов";
            DocumentXmlTorg12.Content.SupplyAllowedBy.FirstName  	= "Иван";
            DocumentXmlTorg12.Content.SupplyAllowedBy.Patronymic 	= "Иванович";
            DocumentXmlTorg12.Content.SupplyAllowedBy.JobTitle   	= "Руководитель складской службы";

            DocumentXmlTorg12.Content.Signer.Surname.Surname	= "Петров";
            DocumentXmlTorg12.Content.Signer.Surname.FirstName  = "Петр";
            DocumentXmlTorg12.Content.Signer.Surname.Patronymic = "Петрович";
            DocumentXmlTorg12.Content.Signer.Surname.JobTitle   = "Главный (старший) бухгалтер";

            // добавляем в сообщение счет на оплату

            DocumentNonformalizedProforma = PackageSendTask.AddDocumentFromFile("NonformalizedProforma", "С:\\Счет12от06062017.pdf");

            DocumentNonformalizedProforma.CustomDocumentId 	= CustomIdNonformalizedProforma;

            DocumentNonformalizedProforma.DocumentDate 		= '20170606';
            DocumentNonformalizedProforma.DocumentNumber	= "Сч1";
            DocumentNonformalizedProforma.Total 			= 1180;
            DocumentNonformalizedProforma.Vat				= 180;
            DocumentNonformalizedProforma.Filename			= "Счет12от06062017.pdf";					

            // устанавливаем связи между документами сообщения
            DocumentXmlTorg12.AddSubordinateDocumentFromPackage(CustomIdNonformalizedProforma); 
            DocumentNonformalizedProforma.AddInitialDocumentFromPackage(CustomIdXmlTorg12);

            PackageSendTask.Send();
            
          КонецПроцедуры