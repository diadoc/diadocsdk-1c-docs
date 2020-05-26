InvoiceCorrection
=================

Документ *Корректировочный счет-фактура*.
Является производным объектом от :doc:`Document`



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

:TotalInc:
  **Число, чтение** - сумма к увеличению по документу

:TotalDec:
  **Число, чтение** - сумма к уменьшению по документу

:VatInc:
  **Число, чтение** - сумма НДС к увеличению по документу

:VatDec:
  **Число, чтение** - сумма НДС к уменьшению по документу

:OriginalDocumentDate:
  **Дата, чтение** - дата первоначального счета-фактуры

:OriginalDocumentNumber:
  **Строка, чтение** - номер первоначального счета-фактуры

:OriginalInvoiceRevisionDate:
  **Дата, чтение** - дата исправления первоначального счета-фактуры

:OriginalInvoiceRevisionNumber:
  **Строка, чтение** - номер исправления первоначального счета-фактуры

:Status:
  **Строка, чтение** - статус документа. :doc:`Возможные значения <./Enums/InvoiceStatus>`


.. rubric:: Методы

+---------------------------------+---------------------------------------------------+----------------------------------------+
| |InvoiceCorrection-GetContent|_ | |InvoiceCorrection-GetAmendmentRequestedComment|_ | |InvoiceCorrection-SendReceiptsAsync|_ |
+---------------------------------+---------------------------------------------------+----------------------------------------+

.. |InvoiceCorrection-GetContent| replace:: GetContent()
.. |InvoiceCorrection-GetAmendmentRequestedComment| replace:: GetAmendmentRequestedComment()
.. |InvoiceCorrection-SendReceiptsAsync| replace:: SendReceiptsAsync()



.. _InvoiceCorrection-GetContent:
.. method:: InvoiceCorrection.GetContent()

  Возвращает :doc:`представление контента <InvoiceCorrectionContent>` корректировочного счета-фактуры

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`



.. _InvoiceCorrection-GetAmendmentRequestedComment:
.. method:: InvoiceCorrection.GetAmendmentRequestedComment()

  Возвращает комментарий к уведомлению об уточнении

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``AmendmentComment``



.. _InvoiceCorrection-SendReceiptsAsync:
.. method:: InvoiceCorrection.SendReceiptsAsync()

  Асинхронно формирует и подписывает документы по :doc:`регламентному документообороту счетов-фактур <../HowTo/HowTo_invoice_docflow>`. Возвращает :doc:`AsyncResult` с булевым типом результата
