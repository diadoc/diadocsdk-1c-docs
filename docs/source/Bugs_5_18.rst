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