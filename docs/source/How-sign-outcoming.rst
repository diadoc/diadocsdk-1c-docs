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

         Процедура ОтправитьУПД(Organization, CounterAgentId)
            
             PackageSendTask = Organization.CreatePackageSendTask();
             
             PackageSendTask.CounterAgentId  = CounterAgentId;
             
             DocumentToSend = PackageSendTask.AddDocument("UniversalTransferDocument");
             
             Content = DocumentToSend.Content;
             
             Content.Number = "1";
             Content.Date   = ТекущаяДата();
             
             Content.Function = "InvoiceAndBasic";
             Content.Creator  = "ООО Продавец, ИНН/КПП: 2012500001/111111111";
             
             Content.Currency     = "643";
             Content.CurrencyRate = "1";
             
             Content.Seller.Name = "ООО Продавец";
             Content.Seller.Inn  = "2012500001";
             Content.Seller.Kpp  = "111111111";
             Content.Seller.type = "LegalEntity";
             Content.Seller.Address.RegionCode = "66";
             
             Content.Buyer.Name = "ООО Покупатель";
             Content.Buyer.Inn  = "2012600006";
             Content.Buyer.Kpp  = "222222222";
             Content.Buyer.type = "LegalEntity";
             Content.Buyer.Address.RegionCode = "66";
             
             Content.TransferInfo.OperationInfo = "Результаты работ переданы (услуги оказаны)";
             Content.TransferInfo.TransferDate  = ТекущаяДата();
             
             Item = Content.InvoiceTable.AddItem();
             
             Item.Product  = "Товар №1";
             Item.UnitName = "шт";
             Item.UnitCode = "796";
             Item.TaxRate  = "18";
             
             // Вместо числовых значений рекомендуется передавать их XML представление.
             Item.Quantity = XMLСтрока(1); 
             Item.Price    = XMLСтрока(100);
             Item.Vat      = XMLСтрока(18);
             Item.Subtotal = XMLСтрока(118);
             Item.SubtotalWithVatExcluded = XMLСтрока(100);
             
             Content.InvoiceTable.TotalNet = XMLСтрока(1);
             Content.InvoiceTable.Vat      = XMLСтрока(18);
             Content.InvoiceTable.Total    = XMLСтрока(118);
             Content.InvoiceTable.TotalWithVatExcluded = XMLСтрока(100);
             
             Signer = Content.AddSigner();
             Signer.SignerDetails.Surname    = "Иванов";
             Signer.SignerDetails.FirstName  = "Иван";
             Signer.SignerDetails.Patronymic = "Иванович";
             Signer.SignerDetails.JobTitle   = "Директор";
             Signer.SignerDetails.SignerType = "LegalEntity";
             Signer.SignerDetails.Inn        = "2012500001";
             Signer.SignerDetails.Powers     = "MadeAndResponsibleForOperationAndSignedInvoice";
             
             DocumentPackage = PackageSendTask.Send();
             
         КонецПроцедуры
