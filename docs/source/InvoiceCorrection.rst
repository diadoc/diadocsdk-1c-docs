InvoiceCorrection
=================

Данный объект предназначен для работы с документами типа
«корректировочный счет-фактура», и является производным объектом от
:doc:`Document <Document>`.

Свойства объекта
----------------


- **Currency** (число, чтение) - код валюты

- **ConfirmationDate** (дата и время, чтение) - дата и время подтверждения спец. оператора передачи ЭСФ

- **AmendmentRequested** (булево, чтение) - признак, был ли запрос на уточнение

- **Revised** (булево, чтение) - признак, было ли исправление данного ЭСФ

- **Corrected** (булево, чтение) - признак, была ли корректировка данного ЭСФ

- **TotalInc** (число, чтение) - сумма к увеличению по документу

- **TotalDec** (число, чтение) - сумма к уменьшению по документу

- **VatInc** (число, чтение) - сумма НДС к увеличению по документу

- **VatDec** (число, чтение) - сумма НДС к уменьшению по документу

- **OriginalDocumentDate** (дата, чтение) - дата первоначального счета-фактуры

- **OriginalDocumentNumber** (строка, чтение) - номер первоначального счета-фактуры

- **OriginalInvoiceRevisionDate** (дата, чтение) - дата исправления первоначального счета-фактуры

- **OriginalInvoiceRevisionNumber** (строка, чтение) - номер исправления первоначального счета-фактуры

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


-  :doc:`GetContent <GetContent-(InvoiceCorrection)>` - возвращает содержание корректировочного счета-фактуры в виде объектной модели

-  :doc:`GetAmendmentRequestedComment <GetAmendmentRequestedComment-(InvoiceCorrection)>` - возвращает комментарий к уведомлению об уточнении

-  :doc:`SendCorrectionRequest <SendCorrectionRequest-(InvoiceCorrection)>` - отправляет уведомление об уточнении корректировочного счета-фактуры

-  :doc:`SendReceiptsAsync <SendReceiptsAsync-(InvoiceCorrection)>` - формирует и подписывает документы по регламентному документообороту счетов-фактур


.. toctree::
   :name: Auto
   :hidden:

   GetContent-(InvoiceCorrection) <GetContent-(InvoiceCorrection)>
   GetAmendmentRequestedComment-(InvoiceCorrection) <GetAmendmentRequestedComment-(InvoiceCorrection)>
   SendCorrectionRequest-(InvoiceCorrection) <SendCorrectionRequest-(InvoiceCorrection)>
   SendReceiptsAsync-(InvoiceCorrection) <SendReceiptsAsync-(InvoiceCorrection)>

