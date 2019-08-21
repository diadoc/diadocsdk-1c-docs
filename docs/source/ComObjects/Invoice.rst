Invoice
=======

Документ *Счет-фактура*.
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
  **Число, чтение** - сумма НДС по документу

:Status:
  **Строка, чтение** - статус документа. |Invoice-Status|_


.. rubric:: Методы

+-----------------------+-----------------------------------------+------------------------------+
| |Invoice-GetContent|_ | |Invoice-GetAmendmentRequestedComment|_ | |Invoice-SendReceiptsAsync|_ |
+-----------------------+-----------------------------------------+------------------------------+

.. |Invoice-GetContent| replace:: GetContent()
.. |Invoice-GetAmendmentRequestedComment| replace:: GetAmendmentRequestedComment()
.. |Invoice-SendReceiptsAsync| replace:: SendReceiptsAsync()



.. _Invoice-GetContent:
.. method:: Invoice.GetContent()

  Возвращает :doc:`представление контента <InvoiceContent>` счета-фактуры

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`



.. _Invoice-GetAmendmentRequestedComment:
.. method:: Invoice.GetAmendmentRequestedComment()

  Возвращает комментарий к уведомлению об уточнении

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``AmendmentComment``



.. _Invoice-SendReceiptsAsync:
.. method:: Invoice.SendReceiptsAsync()

  Асинхронно формирует и подписывает документы по :doc:`регламентному документообороту счетов-фактур <../HowTo/HowTo_invoice_docflow>`. Возвращает :doc:`AsyncResult` с булевым типом результата

  .. versionadded:: 3.0.10


.. rubric:: Дополнительная информация


.. |Invoice-Status| replace:: Возможные значения
.. _Invoice-Status:

================================= ====================================================================================================
Значения *Status*                 Описание
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
