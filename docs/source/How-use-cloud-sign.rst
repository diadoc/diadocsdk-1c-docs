Как работать с облачной подписью
================================

Если у пользователя имеется облачная подпись, он может использовать ее 
для подписания исходящих и входящих документов (о получении списка облачных 
сертификатов см. :doc:`GetCloudCertificates <GetCloudCertificates>`).


Как подписать исходящие документы облачной подписью
---------------------------------------------------

Для того, чтобы отправить документ и подписать его облачной подписью, нужно:
 
-  создать задание на отправку методом :doc:`CreateSendTask <CreateSendTask>` или 
   :doc:`CreateSendTaskFromFile <CreateSendTaskFromFile>` объекта :doc:`Organization <Organization>` 
   и заполнить параметры отправки документа;

-  получить список облачных сертификатов пользователя методом :doc:`GetCloudCertificates <GetCloudCertificates>` 
   объекта :doc:`DiadocConnection <Connection>`;

-  создать задание на облачную подпись методом :doc:`CreateCloudSignTask <CreateCloudSignTask>` 
   объекта :doc:`DiadocConnection <Connection>`, указав в качестве параметра отпечаток нужного облачного сертификата;

-  добавить содержимое документа в задание на облачную подпись методом метод :doc:`AddContent <AddContent>` 
   объекта :doc:`CloudSignTask <CloudSignTask>`;

-  подписать документ, содержимое которого добавлено в задание на облачную подпись, 
   последовательными вызвами методов :doc:`Sign <Sign>` и :doc:`Confirm <Confirm>` объекта 
   :doc:`CloudSignTask <CloudSignTask>`;

-  отправить документ.

Например, следующая процедура позволяет отправить контрагенту счет-фактуру, 
подписанную облачной подписью:

::

            Процедура ОтправитьСчетФактуру(Organization, CounteragentId)

              SendTask = Organization.CreateSendTask("InvoiceContent");	
              SendTask.CounterAgentId    = CounteragentId;

              InvoiceContent = SendTask.Content;
              InvoiceContent.Date        = '20130101';
              InvoiceContent.Number      = "1";
              InvoiceContent.Currency    = "643";

              InvoiceContent.Seller.Name = "ООО Продавец";
              InvoiceContent.Seller.Inn  = "2012500001";
              InvoiceContent.Seller.Kpp  = "111111111";
              InvoiceContent.Seller.Address.RegionCode = "66";

              InvoiceContent.Buyer.Name  = "ООО Покупатель";
              InvoiceContent.Buyer.Inn   = "2012600006";
              InvoiceContent.Buyer.Kpp   = "222222222 ID   ";
              InvoiceContent.Buyer.Address.RegionCode = "66";

              Item = InvoiceContent.AddItem();
              Item.Product               = "Товар";
              Item.UnitCode              = "166";
              Item.Quantity              = 10;
              Item.Price                 = 100;
              Item.TotalWithVatExcluded  = 1000;
              Item.TaxRate               = "18";
              Item.Vat                   = 180;
              Item.Total                 = 1180;

              CloudCerts = Connection.GetCloudCertificates();
              SignTask = Connection.CreateCloudSignTask(CloudCerts.GetItem(0).Thumbprint);
              SignTask.AddContent(InvoiceContent, CounteragentId);
              SignTask.Sign();

              pin = "";
              ВвестиСтроку(pin);
              SignTask.Confirm(pin);

              SendTask.Send();

            КонецПроцедуры
          

Как подписать входящие документы облачной подписью
--------------------------------------------------

Для подписания входящего документа облачной подписью, нужно:

-  создать ответное задание на отправку методом :doc:`CreateReplySendTask <CreateReplySendTask-(Document)>` 
   объекта :doc:`Document <Document>` или методом :doc:`CreateReplySendTask <CreateReplySendTask-(DocumentPackage)>` 
   объекта :doc:`DocumentPackage <DocumentPackage>` и заполнить параметры отправки ответного документа;

-  получить список облачных сертификатов пользователя методом :doc:`GetCloudCertificates <GetCloudCertificates>` 
   объекта :doc:`DiadocConnection <Connection>`;

-  создать задание на облачную подпись методом :doc:`CreateCloudSignTask <CreateCloudSignTask>` 
   объекта :doc:`DiadocConnection <Connection>`, указав в качестве параметра отпечаток нужного облачного сертификата;

-  добавить содержимое ответного документа в задание на облачную подпись методом метод :doc:`AddContent <AddContent>` 
   объекта :doc:`CloudSignTask <CloudSignTask>`;

-  подписать ответный документ, содержимое которого добавлено в задание на облачную подпись, 
   последовательными вызвами методов :doc:`Sign <Sign>` и :doc:`Confirm <Confirm>` объекта 
   :doc:`CloudSignTask <CloudSignTask>`;

-  отправить ответный документ.

Например, следующая процедура позволяет подписать входящий формализованный акт о выполненных работах:

::

            Процедура ПодписатьАкт(Document, Organization, CounteragentId)

              ReplySendTask = Document.CreateReplySendTask("AcceptDocument");
              ReplySendTaskContent = ReplySendTask.Content;

              ReplySendTaskContent.ShipmentReceiptDate = ТекущаяДата();
              ReplySendTaskContent.Signer.Inn          = "2012600006";
              ReplySendTaskContent.Signer.FirstName    = "Signer.FirstName";
              ReplySendTaskContent.Signer.Surname      = "Signer.Surname";
              
              CloudCerts = Connection.CloudCertificates();
              SignTask = Connection.CreateCloudSignTask(CloudCerts.GetItem(0).Thumbprint);
              SignTask.AddContent(ReplySendTaskContent, CounteragentId);
              SignTask.Sign();

              pin = "";
              ВвестиСтроку(pin);
              SignTask.Confirm(pin);

              ReplySendTask.Send();


            КонецПроцедуры
