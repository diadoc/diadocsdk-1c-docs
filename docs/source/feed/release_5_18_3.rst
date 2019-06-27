Релиз 5.18.3
============

.. feed-entry::
   :date: 2017-08-02

- В объект Document добавлено свойство **SenderSignatureStatus** - статус проверки ЭЦП отправителя
- Тип объекта UtdToSend - свойство **Type**, теперь соответствует типу создаваемого документа UniversalTransferDocument, UtdInvoice, UtdTorg12 или UtdAcceptanceCertificate
    
Исправлены ошибки:
    - для УКД исправлена проблема, связанная с тем, что при заполнении контента UcdSellerContent, если суммы корректировок в строках ExtendedInvoiceCorrectionItem равны 0, то заполняются значения и AmountsInc и AmountsDec, что приводило к ошибкам валидации такого вида: SubtotalWithVatExcluded should be specified in Info.InvoiceCorrectionTable.Items[0].AmountsInc and/or Info.InvoiceCorrectionTable.Items[0].AmountsDec
    - отправка формализованных отказов в подписи XmlSignatureRejection для роуминговых документов


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_