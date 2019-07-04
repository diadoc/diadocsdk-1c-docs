Как работать с Контур.Сертификатом
==================================

.. deprecated:: 5.26.0
    На данный момент вопрос дальнейшей поддержки работы с Контур.Сертификатами не решён

.. note:: Статья устарела и в ближайшее время обновлений по ней не предвидится. В примерах в статье используются объекты, которые считаются устаревшими. После обновления API ядра Диадок для работы с КриптоПро DSS планируется полнстью переделать данную часть компоненты


Если у пользователя имеется Контур.Сертификат, он может использовать его для подписания исходящих и входящих документов


Как подписать исходящие документы Контур.Сертификатом
-----------------------------------------------------


Для того, чтобы отправить документ и подписать его Контур.Сертификатом, нужно:

* создать задание на отправку методом :func:`Organization.CreateSendTask` и заполнить параметры отправки документа
* получить список доступных пользователю Контур.Сертификатов методом :func:`Connection.GetCloudCertificates`
* создать задание на подписание методом :func:`Connection.CreateCloudSignTask`, указав в качестве параметра отпечаток нужного сертификата
* добавить содержимое документа в задание на подписание методом :func:`CloudSignTask.AddContent`
* подписать документ, содержимое которого добавлено в задание на подписание, последовательными вызвами методов :func:`CloudSignTask.Sign` и :func:`CloudSignTask.Confirm`
* отправить документ

Например, следующая процедура позволяет отправить контрагенту счет-фактуру, подписанную Контур.Сертификатом:


.. code-block:: c#

    Процедура ОтправитьСчетФактуру(Organization, CounteragentId)

        SendTask = Organization.CreateSendTask("InvoiceContent");
        SendTask.CounterAgentId = CounteragentId;

        InvoiceContent = SendTask.Content;
        InvoiceContent.Date     = ТекущаяДата();
        InvoiceContent.Number   = "1";
        InvoiceContent.Currency = "643";

        InvoiceContent.Seller.Name = "ООО Продавец";
        InvoiceContent.Seller.Inn  = "2012500001";
        InvoiceContent.Seller.Kpp  = "111111111";
        InvoiceContent.Seller.Address.RegionCode = "66";

        InvoiceContent.Buyer.Name = "ООО Покупатель";
        InvoiceContent.Buyer.Inn  = "2012600006";
        InvoiceContent.Buyer.Kpp  = "222222222";
        InvoiceContent.Buyer.Address.RegionCode = "66";

        Item = InvoiceContent.AddItem();
        Item.Product              = "Товар";
        Item.UnitCode             = "166";
        Item.Quantity             = 10;
        Item.Price                = 100;
        Item.TotalWithVatExcluded = 1000;
        Item.TaxRate              = "18";
        Item.Vat                  = 180;
        Item.Total                = 1180;

        CloudCerts = Connection.GetCloudCertificates();
        SignTask = Connection.CreateCloudSignTask(CloudCerts.GetItem(0).Thumbprint);
        SignTask.AddContent(InvoiceContent, CounteragentId);
        SignTask.Sign();

        pin = "";
        ВвестиСтроку(pin);
        SignTask.Confirm(pin);

        SendTask.Send();

    КонецПроцедуры


Как подписать входящие документы Контур.Сертификатом
----------------------------------------------------

Для подписания входящего документа Контур.Сертификатом, нужно:

* создать ответное задание на отправку методом :func:`Document.CreateReplySendTask` и заполнить параметры отправки ответного документа
* получить список доступных пользователю Контур.Сертификатов методом :func:`Connection.GetCloudCertificates`
* создать задание на подписание методом :func:`Connection.CreateCloudSignTask`, указав в качестве параметра отпечаток нужного сертификата
* добавить содержимое ответного документа в задание на подписание методом метод :func:`CloudSignTask.AddContent`
* подписать ответный документ, содержимое которого добавлено в задание на подписание, последовательными вызвами методов :func:`CloudSignTask.Sign` и :func:`CloudSignTask.Confirm`
* отправить ответный документ

Например, следующая процедура позволяет подписать входящий формализованный акт о выполненных работах:


.. code-block:: c#

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
