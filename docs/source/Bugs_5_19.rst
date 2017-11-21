Ошибки, исправленные в версии 5.19
==================================

v5.19.1 - 20.11.2017
--------------------

- исправлена ошибка в алгоритме определения КЭП - свойство :doc:`PersonalCertificate.IsQualifiedElectronicSignature <PersonalCertificate>` возвращает ложное значение в случае, если сертификат юр. лица и в ОГРН(1.2.643.100.1) нет нолей
- теперь кидается исключение в случае если задано неверное значение в свойстве :doc:`AcquireCounteragentTask.CounteragentBoxId <AcquireCounteragentTask>` и вызвана отправка методом :doc:`AcquireCounteragentTask.Send <Send-(AcquireCounteragentTask)>` или :doc:`AcquireCounteragentTask.SendAsync <SendAsync-(AcquireCounteragentTask)>`, ранее это приводило к неверному обращению к памяти
- COM-компонента: при попытке получения содержимого документов в формате 551 и 552-го приказа методами :doc:`GetContent <GetContent-(XmlTorg12)>`, :doc:`GetBuyerContent <GetBuyerContent-(XmlTorg12)>`, :doc:`GetContent <GetContent-(XmlAcceptanceCertificate)>`, :doc:`GetBuyerContent <GetBuyerContent-(XmlAcceptanceCertificate)>` возвращался неверный контент