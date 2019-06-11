Релиз 5.27.0
============

.. feed-entry::
   :date: 2019-06-10
   
- Добавлена поддержка УПД в формате 820 приказа:
     - Добавлен объект :doc:`PackageSendTask2 <PackageSendTask2>`
     - Добавлен объект :doc:`ReplySendTask2 <ReplySendTask2>`
     - Добавлен объект :doc:`DynamicContent <DynamicContent>`
     - Добавлен метод :doc:`Organization.SaveUserDataXSD <SaveUserDataXSD>`
     - Тип объекта :doc:`PackageContentItem.Content <PackageContentItem>` изменён при использовании новых объектов
     - Тип объекта :doc:`CustomDocumentToSend.Content <PackageContentItem>` изменён при использовании новых объектов
     - В объект :doc:`DocumentTitle <DocumentTitle>` добавлено поле HaveUserDataXSD
     - Добавлены методы :doc:`Document.GetDynamicContent() <Document_GetDynamicContent>` для представления контента документов в виде :doc:`DynamicContent <DynamicContent>`
     - Расширен набор статусов подписанта в объекте :doc:`ExtendedSignerDetailsToPost <ExtendedSignerDetailsToPost>`
     
- Уменьшено количество различных текстов ошибок. Исправлены опечатки

- Объекту :doc:`Counteragent <Counteragent>` добавлено поле IsBranch

- Добавлены новые типы для объекта :doc:`ReplySendTask <ReplySendTask>`

- Нерекомендуемыми к использованию помечены:
    - :doc:`SendTask <SendTask>`
    - :doc:`PackageSendTask <PackageSendTask>`
    - :doc:`ReplySendTask <ReplySendTask>`
    - :doc:`Contract.Accept <Accept-(Contract)>`
    - :doc:`Nonformalized.Accept <Accept-(Nonformalized)>`
    - :doc:`NonformalizedAcceptanceCertificate.Accept <Accept-(NonformalizedAcceptanceCertificate)>`
    - :doc:`NonformalizedTorg12.Accept <Accept-(NonformalizedTorg12)>`
    - :doc:`Contract.Reject <Reject-(Contract)>`
    - :doc:`Nonformalized.Reject <Reject-(Nonformalized)>`
    - :doc:`NonformalizedAcceptanceCertificate.Reject <Reject-(NonformalizedAcceptanceCertificate)>`
    - :doc:`NonformalizedTorg12.Reject <Reject-(NonformalizedTorg12)>`
    - :doc:`XmlAcceptanceCertificate.Reject <Reject-(XmlAcceptanceCertificate)>`
    - :doc:`XmlTorg12.Reject <Reject-(XmlTorg12)>`
    - :doc:`InvoiceCorrection.SendCorrectionRequest <SendCorrectionRequest-(InvoiceCorrection)>`
    - :doc:`InvoiceCorrectionRevision.SendCorrectionRequest <SendCorrectionRequest-(InvoiceCorrectionRevision)>`
    - :doc:`InvoiceRevision.SendCorrectionRequest <SendCorrectionRequest-(InvoiceRevision)>`
    - :doc:`Invoice.SendCorrectionRequest <SendCorrectionRequest-Invoice>`
    - :doc:`AcceptRevocationRequest <AcceptRevocationRequest>`
    - :doc:`CreateSendTask <CreateSendTask>`
    - :doc:`CreateSendTaskFromFile <CreateSendTaskFromFile>`
    - :doc:`CreateSendTaskFromFileRaw <CreateSendTaskFromFileRaw>`
    
- внутренние улучшения и оптимизации
    
- Исправлены ошибки:
    - Медленная работа компоненты при получении документа/списка документов
    - Удален ошибочно добавленный метод CustomDocumentToSend.AddCustomData()
    - Удалено поле CustomDocumentToSend.CustomData
    - Ошибка при отправке приглашений "##100[Ошибка сервера Диадок]code:400, HTTP error: Too many INN in request"
    - Падение клиента в методе :doc:`SendTask.SendAsync <SendAsync-(SendDraftTask)>`
    - Ошибка при получении документа "##100[Ошибка сервера Диадок]code:404, HTTP error: Unknown box:"
    - Исправлена работа методов Reject у документов с типом Contract, Nonformalized


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_