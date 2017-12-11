Ошибки, исправленные в версии 5.19
==================================

v5.19.1 - 20.11.2017
--------------------

- исправлена ошибка в алгоритме определения КЭП - свойство :doc:`PersonalCertificate.IsQualifiedElectronicSignature <PersonalCertificate>` возвращает ложное значение в случае, если сертификат юр. лица и в ОГРН(1.2.643.100.1) нет нолей
- теперь кидается исключение в случае если задано неверное значение в свойстве :doc:`AcquireCounteragentTask.CounteragentBoxId <AcquireCounteragentTask>` и вызвана отправка методом :doc:`AcquireCounteragentTask.Send <Send-(AcquireCounteragentTask)>` или :doc:`AcquireCounteragentTask.SendAsync <SendAsync-(AcquireCounteragentTask)>`, ранее это приводило к неверному обращению к памяти
- COM-компонента: при попытке получения содержимого документов в формате 551 и 552-го приказа методами :doc:`GetContent <GetContent-(XmlTorg12)>`, :doc:`GetBuyerContent <GetBuyerContent-(XmlTorg12)>`, :doc:`GetContent <GetContent-(XmlAcceptanceCertificate)>`, :doc:`GetBuyerContent <GetBuyerContent-(XmlAcceptanceCertificate)>` возвращался неверный контент

v5.19.2 - 27.11.2017
--------------------

- при отправке шифрованного счета-фактуры с помощью :doc:`PackageSendTask <PackageSendTask>` и :doc:`SendTask <SendTask>` не заполнялось свойство DocumentNumber, что приводило к исключению "Incorrect EncryptedInvoiceAttachment: Metadata.DocumentDateAndNumber.DocumentNumber should be filled"

v5.19.3 - 11.12.2017
--------------------

- при создании :doc:`SendTask <SendTask>` для неформализованных типов документов возникало исключение с комментарием "Неверный тип вложения" 
- поле **TaxRate** в :doc:`TovTorgItem <TovTorgItem>` и :doc:`Act552WorkItem <Act552WorkItem>` всегда десериализовалось со значением "без НДС"