XmlAcceptanceCertificate
========================

Данный объект предназначен для работы с документами типа «акт о
выполнении работ в формате ФНС», и является производным объектом от
:doc:`Document <Document>`.

Свойства объекта
----------------


- **Total** (число, чтение ) - cумма по документу

- **Vat** (число, чтение ) - cумма НДС по документу

- **Grounds** (строка, чтение ) - основание документа

- **Status** (строка, чтение ) - текущий статус документа в Диадоке


Значения свойства **Status**

- UnknownBilateralDocumentStatus - неизвестное состояние документа 
- OutboundWaitingForRecipientSignature - документ исходящий, ответная подпись, либо отказ от ее формирования еще не получены 
- OutboundWithRecipientSignature - документ исходящий, ответная подпись получена 
- OutboundRecipientSignatureRequestRejected - документ исходящий, получен отказ от формирования ответной подписи 
- OutboundWaitingForSenderSignature - документ исходящий, документ не отправлен, поскольку не подписан отправителем 
- OutboundInvalidSenderSignature - документ исходящий, документ не отправлен, поскольку подпись отправителя не является корректной 
- InboundWaitingForRecipientSignature - документ входящий, ответная подпись, либо отказ от ее формирования еще не отправлены 
- InboundWithRecipientSignature - документ входящий, ответная подпись поставлена 
- InboundRecipientSignatureRequestRejected - документ входящий, отправлен отказ от формирования ответной подписи 
- InboundInvalidRecipientSignature - документ входящий, документооборот не завершен, поскольку подпись отправителя не является корректной 
- InternalWaitingForRecipientSignature - документ внутренний, ответная подпись 
- InternalWithRecipientSignature - документ внутренний, ответная подпись поставлена 
- InternalRecipientSignatureRequestRejected - документ внутренний, отправлен отказ от формирования ответной подписи 
- InternalWaitingForSenderSignature - документ внутренний, документ не отправлен, поскольку не подписан отправителем 
- InternalInvalidSenderSignature - документ внутренний, документ не отправлен, поскольку подпись отправителя не является корректной 
- InternalInvalidRecipientSignature - документ внутренний, документооборот не завершен, поскольку подпись отправителя не является корректной

Методы объекта
--------------


-  :doc:`GetRejectionComment <GetRejectionComment-(XmlAcceptanceCertificate)>` - возвращает комментарий к отказу в подписании

-  :doc:`Reject <Reject-(XmlAcceptanceCertificate)>` - формирует отказ в подписании документа

-  :doc:`GetContent <GetContent-(XmlAcceptanceCertificate)>` - возвращает содержание документа (титул исполнителя) в виде объектной модели

-  :doc:`GetBuyerContent <GetBuyerContent-(XmlAcceptanceCertificate)>` - возвращает содержание документа (титул заказчика) в виде объектной модели

-  :doc:`CreateReplySendTask <CreateReplySendTask-(XmlAcceptanceCertificate)>` - формирует задание для отправки титула заказчика (для подписания документа со стороны заказчика)

-  :doc:`SaveRecipientContent <SaveRecipientContent-(XmlAcceptanceCertificate)>` - сохраняет содержимое титула покупателя на локальный диск


.. toctree::
   :name: Auto
   :hidden:

   GetRejectionComment-(XmlAcceptanceCertificate) <GetRejectionComment-(XmlAcceptanceCertificate)>
   Reject-(XmlAcceptanceCertificate) <Reject-(XmlAcceptanceCertificate)>
   GetContent-(XmlAcceptanceCertificate) <GetContent-(XmlAcceptanceCertificate)>
   GetBuyerContent-(XmlAcceptanceCertificate) <GetBuyerContent-(XmlAcceptanceCertificate)>
   CreateReplySendTask-(XmlAcceptanceCertificate) <CreateReplySendTask-(XmlAcceptanceCertificate)>
   SaveRecipientContent-(XmlAcceptanceCertificate) <SaveRecipientContent-(XmlAcceptanceCertificate)>

