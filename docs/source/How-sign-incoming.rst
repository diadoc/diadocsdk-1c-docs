Как подписать входящий документ
===============================

Входящие электронные документы, который требуют ответной подписи, можно
обработать несколькими способами

1. Подписать документ

   -  Для формализованных документов требуется сначала сформировать т.н.
      титул покупателя :doc:`Torg12BuyerContent <Torg12BuyerContent>` или
      :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` или
      :doc:`UtdBuyerContent <UtdBuyerContent>`,
      и создать задание методом
      :doc:`CreateReplySendTask <CreateReplySendTask-(XmlTorg12)>`

      Пример кода, формирующий задание на подписание торг-12:

      ::

                          ReplySendTask=  Document.CreateReplySendTask();

                          ReplySendTask.Content.ShipmentReceiptDate = ТекущаяДата();

                          ReplySendTask.Content.Signer.IsSoleProprietor = Ложь;
                          ReplySendTask.Content.Signer.Surname = "Иванов";
                          ReplySendTask.Content.Signer.FirstName = "Иван";
                          ReplySendTask.Content.Signer.Patronymic = "Иванович";
                          ReplySendTask.Content.Signer.JobTitle = "Директор";
                          ReplySendTask.Content.Signer.INN = "123456789";
                          ReplySendTask.Content.Signer.SoleProprietorRegistrationCertificate = "";

                          ReplySendTask.Send();

   -  Неформализованные документы подписываются методом Accept (:doc:`Accept объекта NonformalizedTorg12 <Accept-(NonformalizedTorg12)>`,
      :doc:`Accept объекта Nonformalized <Accept-(Nonformalized)>` и т.д.)

      Пример:

      ::

                          Document.Accept();

2. Отказать в подписи

   Для всех типов документов применятся метод Reject (:doc:`Reject объекта NonformalizedTorg12 <Reject-(NonformalizedTorg12)>`, `Reject объекта :doc:   XmlTorg12 <Reject-(XmlTorg12)>` и т.д.), где параметром можно передать
   свой комментарий отказа в подписи

   Пример:

   ::

                   СвойКомментарийКОтказу = "Не удовлетворяет условиям договора";
                   Document.Reject(СвойКомментарийКОтказу);
