Ошибки, исправленные в версии 5.18
==================================

v5.18.1 - 21.06.2017
--------------------

- метод :doc:`GetRecipientSignature <GetRecipientSignature>` не возвращал подпись получателя в случае "Отказа в подписи" и "Запроса согласования"
- некорректные правила валидации адресов для УПД на вызов метода :doc:`ValidateContent <ValidateContent-(SendTask)>`
- некорректная работа ReplySendTask для пакетов, для УПД/УКД не учитывалась функция
- невозможно отказать в подписи иУПД/иУКД
- поле метаданных библиотек компоненты "Версия файла" не соответствовало полю "Версия продукта"
- теперь, если была произведена автоизация по логину/паролю, при попытке запуска :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>` возникает специфическое исключение с сообщением "Обработка ИОП можеть быть запущена только при авторизации сертификатом"
- дамп при вызове :doc:`SendDraftAsync <SendDraftAsync>`

v5.18.2 - 18.07.2017
--------------------

- в результате вызова методов :doc:`SaveAllContent <SaveAllContent>` и :doc:`SaveAllContentAsync <SaveAllContentAsync>` печатная форма скачивалась без расширения
- в объекте :doc:`Document <Document>` получаемом в результате вызова :doc:`SendTask.Send <Send-(SendTask)>` или :doc:`SendTask.SendAsync <SendAsync>` не заполнялось поле OneSDocumentId
- ошибка при вызове :doc:`CreateReplySendTask("RejectDocument") <CreateReplySendTask-(Document)>` для NonformalizedAcceptanceCertificate, CertificateRegistry, PriceListAgreement, ReconciliationAct, NonformalizedTorg12, Contract, Nonformalized
- ошибка в COM-компоненте - исключение при чтении свойства **AmendmentRequested**
- :doc:`SendDraftTask.SendAsync <SendAsync-(SendDraftTask)>` не создавался объект результата выполнения задачи
- :doc:`DocumentsTask.GetDocuments <GetDocumentsAsync>` - если в результате поиска не было найдено документов, возвращалась не пустая коллекция, а неопределенное значение
- при подписи документа дважды запрашивался ПИН закрытого ключа
- :doc:`SendTask <SendTask>` - допускалось создание объекта для некорректного типа документа

v5.18.3 - 02.08.2017
--------------------

- для УКД исправлена проблема, связанная с тем, что при заполнении контента :doc:`UcdSellerContent <UcdSellerContent>`, если суммы корректировок в строках :doc:`ExtendedInvoiceCorrectionItem <ExtendedInvoiceCorrectionItem>` равны 0, то заполняются значения и AmountsInc и AmountsDec, что приводило к ошибкам валидации такого вида: SubtotalWithVatExcluded should be specified in Info.InvoiceCorrectionTable.Items
[0].AmountsInc and/or Info.InvoiceCorrectionTable.Items[0].AmountsDec
- отправка формализованных отказов в подписи XmlSignatureRejection для роуминговых документов