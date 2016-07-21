Invoice
=======

Данный объект предназначен для работы с документами типа «счет-фактура»,
и является производным объектом от :doc:`Document <Document>`.

Свойства объекта
----------------


- **Currency** (число, чтение) - код валюты

- **ConfirmationDate** (дата и время, чтение) - дата и время подтверждения спец. оператора передачи ЭСФ

- **AmendmentRequested** (булево, чтение) - признак, был ли запрос на уточнение

- **Revised** (булево, чтение) - признак, было ли исправление данного ЭСФ

- **Corrected** (булево, чтение) - признак, была ли корректировка данного ЭСФ

- **Total** (число, чтение) - сумма по документу

- **Vat** (число, чтение) - сумма НДС по документу

- **Status** (строка, чтение) - текущий статус документа в Диадоке


Значения свойства **Status**

- UnknownInvoiceStatus - неизвестное состояние документа 
- OutboundWaitingForInvoiceReceipt - документ исходящий, ожидается извещение о получении от покупателя 
- OutboundNotFinished - документ исходящий, извещение о получении от покупателя уже есть, но документооборот еще не завершен
- OutboundFinished - документ исходящий, документооборот завершен 
- OutboundWaitingForSenderSignature - документ исходящий, документ не отправлен, поскольку не подписан отправителем 
- OutboundInvalidSenderSignature - документ исходящий, документ не отправлен, поскольку подпись отправителя не является корректной 
- InboundNotFinished - документ входящий, документооборот не завершен 
- InboundFinished - документ входящий, документооборот завершен

Методы объекта
--------------


-  :doc:`GetContent <GetContent-Invoice>` - возвращает содержание счета-фактуры в виде объектной модели

-  :doc:`GetAmendmentRequestedComment <GetAmendmentRequestedComment-Invoice>` - возвращает комментарий к уведомлению об уточнении

-  :doc:`SendCorrectionRequest <SendCorrectionRequest-Invoice>` - отправляет уведомление об уточнении счета-фактуры

-  :doc:`SendReceiptsAsync <SendReceiptsAsync>` - формирует и подписывает документы по регламентному документообороту счетов-фактур


.. toctree::
   :name: Auto
   :hidden:

   GetContent-Invoice <GetContent-Invoice>
   GetAmendmentRequestedComment-Invoice <GetAmendmentRequestedComment-Invoice>
   SendCorrectionRequest-Invoice <SendCorrectionRequest-Invoice>
   SendReceiptsAsync <SendReceiptsAsync>
 

