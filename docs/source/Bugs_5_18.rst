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

- для УКД исправлена проблема, связанная с тем, что при заполнении контента :doc:`UcdSellerContent <UcdSellerContent>`, если суммы корректировок в строках :doc:`ExtendedInvoiceCorrectionItem <ExtendedInvoiceCorrectionItem>` равны 0, то заполняются значения и AmountsInc и AmountsDec, что приводило к ошибкам валидации такого вида: SubtotalWithVatExcluded should be specified in Info.InvoiceCorrectionTable.Items[0].AmountsInc and/or Info.InvoiceCorrectionTable.Items[0].AmountsDec
- отправка формализованных отказов в подписи XmlSignatureRejection для роуминговых документов

v5.18.4 - 03.08.2017
------------------------

- попытка получения объекта :doc:`Counteragent <Counteragent>`, для удаленной организации, с помощью :doc:`GetCounteragentById <GetCounteragentById>` приводила к обращению к нулевому оказателю и краху компоненты

v5.18.5 - 14.08.2017
--------------------

- невозможно задать и получить информацию о подписанте для УКД с помощью :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>` и :doc:`SetExtendedSignerDetailsTask <SetExtendedSignerDetailsTask>`
- корректные формализованные отказы в подписи для роуминговых ящиков
- в COM-компоненте некорректно обращение к памяти при вызове :doc:`AddExtendedSigner <AddExtendedSigner>`
- зависание при вызове методов, если заданы неверные реквизиты прокси
- обновление протобуферов, InvoiceCorrectionTable.Items[0].OriginalValues.SubtotalWithVatExcluded (поле **TotalWithVatExcluded** объекта :doc:`InvoiceItemFields <InvoiceItemFields>`) теперь не обязателен
- метод :doc:`GetRecipientSignature <GetRecipientSignature>` не возвращал подпись для неформализованных документов
- поле **Type** объекта :doc:`DocumentToSend <DocumentToSend>` и поле **Type** объекта :doc:`BaseContent <BaseContent>` для документов в формате 155 приказа возвращали соответствующие значения UtdInvoice, UtdAcceptanceCertificate и UtdTorg12, теперь поле **Type** объекта :doc:`BaseContent <BaseContent>` для таких документов возвращет значение UniversalTransferDocument

v5.18.6 - 18.08.2017
--------------------

- объект :doc:`SendTask <SendTask>` не позволяет создавать документы в формате 155-го приказа
- метод :doc:`Reject <Reject-(Nonformalized)>` для неформализованных документов не позволяет отказать документам из роуминговых ящиков