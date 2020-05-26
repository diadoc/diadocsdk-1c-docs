InvoiceCorrectionRevision
=========================

Документ *Исправление корректировочного счета-фактура*.
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

:OriginalInvoiceCorrectionDate:
  **Дата, чтение** - дата первоначального корректировочного счета-фактуры

:OriginalInvoiceCorrectionNumber:
  **Строка, чтение** - номер первоначального корректировочного счета-фактуры

:Status:
  **Строка, чтение** - статус документа. :doc:`Возможные значения <./Enums/InvoiceStatus>`


.. rubric:: Методы

+-----------------------------------------+-----------------------------------------------------------+------------------------------------------------+
| |InvoiceCorrectionRevision-GetContent|_ | |InvoiceCorrectionRevision-GetAmendmentRequestedComment|_ | |InvoiceCorrectionRevision-SendReceiptsAsync|_ |
+-----------------------------------------+-----------------------------------------------------------+------------------------------------------------+

.. |InvoiceCorrectionRevision-GetContent| replace:: GetContent()
.. |InvoiceCorrectionRevision-GetAmendmentRequestedComment| replace:: GetAmendmentRequestedComment()
.. |InvoiceCorrectionRevision-SendReceiptsAsync| replace:: SendReceiptsAsync()



.. _InvoiceCorrectionRevision-GetContent:
.. method:: InvoiceCorrectionRevision.GetContent()

  Возвращает :doc:`представление контента <InvoiceCorrectionContent>` исправления корректировочного счета-фактуры

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`



.. _InvoiceCorrectionRevision-GetAmendmentRequestedComment:
.. method:: InvoiceCorrectionRevision.GetAmendmentRequestedComment()

  Возвращает комментарий к уведомлению об уточнении

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``AmendmentComment``



.. _InvoiceCorrectionRevision-SendReceiptsAsync:
.. method:: InvoiceCorrectionRevision.SendReceiptsAsync()

  Асинхронно формирует и подписывает документы по :doc:`регламентному документообороту счетов-фактур <../HowTo/HowTo_invoice_docflow>`. Возвращает :doc:`AsyncResult` с булевым типом результата
