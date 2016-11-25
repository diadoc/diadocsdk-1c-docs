Nonformalized
=============

Данный объект предназначен для работы с документами в неформализованном
формате (в том числе акт сверки, детализация, дополнительное соглашение к договору, 
протокол согласования цены, реестр сертификатов, ценовой лист), 
и является производным объектом от :doc:`Document <Document>`.

Свойства объекта
----------------


- **Status** (строка, чтение) - текущий статус документа в Диадоке


Значения свойства **Status**

- UnknownNonformalizedDocumentStatus - неизвестное состояние документа 
- OutboundNoRecipientSignatureRequest - документ исходящий, без запроса ответной подписи 
- OutboundWaitingForRecipientSignature - документ исходящий, ответная подпись, либо отказ от ее формирования еще не получены 
- OutboundWithRecipientSignature - документ исходящий, ответная подпись получена 
- OutboundRecipientSignatureRequestRejected - документ исходящий, получен отказ от формирования ответной подписи 
- OutboundWaitingForSenderSignature - документ исходящий, документ не отправлен, поскольку не подписан отправителем 
- OutboundInvalidSenderSignature - документ исходящий, документ не отправлен, поскольку подпись отправителя не является корректной 
- InboundNoRecipientSignatureRequest - документ входящий, без запроса ответной подписи 
- InboundWaitingForRecipientSignature - документ входящий, ответная подпись, либо отказ от ее формирования еще не отправлены 
- InboundWithRecipientSignature - документ входящий, ответная подпись поставлена 
- InboundRecipientSignatureRequestRejected - документ входящий, отправлен отказ от формирования ответной подписи 
- InboundInvalidRecipientSignature - документ входящий, документооборот не завершен, поскольку подпись отправителя не является корректной 
- InternalNoRecipientSignatureRequest - документ внутренний, документ без запроса ответной подписи 
- InternalWaitingForRecipientSignature - документ внутренний, ответная подпись 
- InternalWithRecipientSignature - документ внутренний, ответная подпись поставлена 
- InternalRecipientSignatureRequestRejected - документ внутренний, отправлен отказ от формирования ответной подписи 
- InternalWaitingForSenderSignature - документ внутренний, документ не отправлен, поскольку не подписан отправителем 
- InternalInvalidSenderSignature - документ внутренний, документ не отправлен, поскольку подпись отправителя не является корректной 
- InternalInvalidRecipientSignature - документ внутренний, документооборот не завершен, поскольку подпись отправителя не является корректной

Методы объекта
--------------


-  :doc:`GetRejectionComment <GetRejectionComment-(Nonformalized)>` - возвращает комментарий к отказу в подписании

-  :doc:`Accept <Accept-(Nonformalized)>` - формирует подпись получателя документа

-  :doc:`Reject <Reject-(Nonformalized)>` - формирует отказ в подписании документа


.. toctree::
   :name: Auto
   :hidden:

   GetRejectionComment-(Nonformalized) <GetRejectionComment-(Nonformalized)>
   Accept-(Nonformalized) <Accept-(Nonformalized)>
   Reject-(Nonformalized) <Reject-(Nonformalized)>

