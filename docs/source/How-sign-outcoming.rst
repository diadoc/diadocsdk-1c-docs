Как подписать и отправить документ
==================================

Отправка документов возможна только тем контрагентам в Диадоке, с
которыми установлены партнерские отношения (см. раздел :doc:`Как установить 
партнерские отношения <How-trust>`).

Отправка документа на основании сформированного файла
--------------------------------------------------------

Данный способ доступен для всех типов документов: как составленных в
формате xml, так и составленных в произвольном формате.

Для отправки заранее сформированного документа необходимо использовать
метод :doc:`CreateSendTaskFromFile <CreateSendTaskFromFile>` объекта
:doc:`Organization <Organization>`. В качестве параметров при вызове метода
необходимо путь до файла, в котором находится отправляемый документ, а
также тип отправляемого документа. Данный метод возвращает объект
:doc:`SendTask <SendTask>`, устанавливая свойства которого можно задать
различные параметры отправки документа.

Например, следующая процедура позволяет отправить контрагенту счет на
оплату:

::

            Процедура ОтправитьСчетНаОплату()

              SendTask = Organization.CreateSendTaskFromFile(ПутьКФайлу, "ProformaInvoiceContent");
              SendTask.CounterаgentId   = CounteragentId;
              SendTask.Content.Date     = ДатаДокумента;
              SendTask.Content.Number   = НомерДокумента;
              SendTask.Content.Total    = СуммаДокумента;
              SendTask.Content.Vat      = СуммаНДСДокумента;
              SendTask.Send();

            КонецПроцедуры
          

Отправка документа на основании данных учетной системы
----------------------------------------------------------

Данный способ применим только для документов в формате xml, утвержденном
ФНС.

В случае, когда необходимо отправить документ в формате ФНС, учетная
система, как правило, не умеет формировать документы требуемого формата.
В компоненте реализован механизм, позволяющий переложить "заботу" о
формировании xml-файла на внешнюю компоненту. От учетной системы, в этом
случае, требуется только предоставить исходные данные, необходимые для
формирования файла

Чтобы сформировать и отправить документ нужно:

-  Вызвать метод CreateSendTask объекта Organization, в качестве
   параметра указав тип формируемого документа
-  Получив в результате вызова метода объект SendTask, заполнить
   параметры отправки документа
-  заполнить информацию о документе, заполнив структуру, которая
   содержится в SendTask.Content
-  отправить документ

Пример формирования и отправки счета-фактуры

::

            Процедура ОтправитьЭлектронныйCчетФактуру(Organization, CounteragentId)

              SendTask = Organization.CreateSendTask("InvoiceContent");
              SendTask.CounterаgentId   = CounteragentId;

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

              SendTask.Send();

            КонецПроцедуры
