XmlTorg12
=========

Данный объект предназначен для работы с документами типа "ТОРГ-12 в
формате ФНС", и является производным объектом от
:doc:`Document <Document>`.

Свойства объекта
----------------


- **Total** (число, чтение) - cумма по документу

- **Vat** (число, чтение) - cумма НДС по документу

- **Grounds** (строка, чтение) - основание документа

- **Status** (строка, чтение) - текущий статус документа в Диадоке


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


-  :doc:`GetRejectionComment <GetRejectionComment-(XmlTorg12)>` - возвращает комментарий к отказу в подписании

-  :doc:`Reject <Reject-(XmlTorg12)>` - формирует отказ в подписании документа

-  :doc:`GetContent <GetContent-(XmlTorg12)>` - возвращает содержание документа (титул отправителя) в виде объектной модели

-  :doc:`GetBuyerContent <GetBuyerContent-(XmlTorg12)>` - возвращает содержание документа (титул получателя) в виде объектной модели

-  :doc:`SaveRecipientContent <SaveRecipientContent-(XmlTorg12)>` - сохраняет содержимое титула получателя на локальный диск


.. toctree::
   :name: Autofdsfdsfds
   :hidden:
   
   GetRejectionComment-(XmlTorg12) <GetRejectionComment-(XmlTorg12)>
   Reject-(XmlTorg12) <Reject-(XmlTorg12)>
   GetContent-(XmlTorg12) <GetContent-(XmlTorg12)>
   GetBuyerContent-(XmlTorg12) <GetBuyerContent-(XmlTorg12)>
   SaveRecipientContent-(XmlTorg12) <SaveRecipientContent-(XmlTorg12)>

