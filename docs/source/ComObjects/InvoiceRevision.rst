InvoiceRevision
===============

Документ *Исправление счета-фактуры*.
Является производным объектом от :doc:`Document <Document>`


.. rubric:: Свойства

:Currency:
  **Число, чтение** - код валюты

:ConfirmationDate:
  **Дата и время, чтение** - дата и время подтверждения спец. оператора передачи ЭСФ

:AmendmentRequested:
  **Булево, чтение** - признак, был ли запрос на уточнение

:Revised:
  **Булево, чтение** - признак, было ли исправление данного ЭСФ

:Corrected:
  **Булево, чтение** - признак, была ли корректировка данного ЭСФ

:Total:
  **Число, чтение** - сумма по документу

:Vat:
  **Число, чтение** - сумма НДС по документ

:OriginalDocumentDate:
  **Дата, чтение** - дата первоначального счета-фактуры

:OriginalDocumentNumber:
  **Строка, чтение** - номер первоначального счета-фактуры

:Status:
  **Строка, чтение** - текущий статус документа в Диадоке


.. rubric:: Методы

+-------------------------------+-------------------------------------------------+--------------------------------------+
| |InvoiceRevision-GetContent|_ | |InvoiceRevision-GetAmendmentRequestedComment|_ | |InvoiceRevision-SendReceiptsAsync|_ |
+-------------------------------+-------------------------------------------------+--------------------------------------+

.. |InvoiceRevision-GetContent| replace:: GetContent()
.. |InvoiceRevision-GetAmendmentRequestedComment| replace:: GetAmendmentRequestedComment()
.. |InvoiceRevision-SendReceiptsAsync| replace:: SendReceiptsAsync()



.. _InvoiceRevision-GetContent:
.. method:: InvoiceRevision.GetContent()

  Возвращает :doc:`представление контента <InvoiceContent>` счета-фактуры

  .. deprecated:: 5.27.0
    Используйте :func:`Document.GetDynamicContent`



.. _InvoiceRevision-GetAmendmentRequestedComment:
.. method:: InvoiceRevision.GetAmendmentRequestedComment()

  Возвращает комментарий к уведомлению об уточнении

  .. deprecated:: 5.20.3
    Используйте Используйте :func:`Document.GetAnyComment` с типом ``AmendmentComment``



.. _InvoiceRevision-SendReceiptsAsync:
.. method:: InvoiceRevision.SendReceiptsAsync()

  Асинхронно формирует и подписывает документы по :doc:`регламентному документообороту счетов-фактур <../HowTo/HowTo_invoice_docflow>`. Возвращает :doc:`AsyncResult` с булевым типом результата



.. rubric:: Дополнительная информация

================================= ====================================================================================================
Значение *Status*                 Описание
================================= ====================================================================================================
UnknownInvoiceStatus              неизвестное состояние документа
OutboundWaitingForInvoiceReceipt  документ исходящий, ожидается извещение о получении от покупателя
OutboundNotFinished               документ исходящий, извещение о получении от покупателя уже есть, но документооборот еще не завершен
OutboundFinished                  документ исходящий, документооборот завершен
OutboundWaitingForSenderSignature документ исходящий, документ не отправлен, поскольку не подписан отправителем
OutboundInvalidSenderSignature    документ исходящий, документ не отправлен, поскольку подпись отправителя не является корректной
InboundNotFinished                документ входящий, документооборот не завершен
InboundFinished                   документ входящий, документооборот завершен
================================= ====================================================================================================
