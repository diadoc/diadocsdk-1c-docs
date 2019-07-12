Релиз 5.27.0
============

.. feed-entry::
   :date: 2019-06-17

- Добавлена поддержка УПД в формате 820 приказа:
     - Добавлен объект :doc:`../../ComObjects/PackageSendTask2`
     - Добавлен объект ReplySendTask2
     - Добавлен объект DynamicContent
     - Добавлен метод Organization.SaveUserDataXSD
     - Тип объекта PackageContentItem.Content изменён при использовании новых объектов
     - Тип объекта CustomDocumentToSend.Content изменён при использовании новых объектов
     - В объект DocumentTitle добавлено поле HaveUserDataXSD
     - Добавлены методы Document.GetDynamicContent() для представления контента документов в виде DynamicContent
     - Расширен набор статусов подписанта в объекте ExtendedSignerDetailsToPost

- Уменьшено количество различных текстов ошибок. Исправлены опечатки

- Объекту Counteragent добавлено поле IsBranch

- Добавлены новые типы для объекта ReplySendTask

- Нерекомендуемыми к использованию помечены:
    - SendTask
    - PackageSendTask
    - ReplySendTask
    - Contract.Accept
    - Nonformalized.Accept
    - NonformalizedAcceptanceCertificate.Accept
    - NonformalizedTorg12.Accept
    - Contract.Reject
    - Nonformalized.Reject
    - NonformalizedAcceptanceCertificate.Reject
    - NonformalizedTorg12.Reject
    - XmlAcceptanceCertificate.Reject
    - XmlTorg12.Reject
    - InvoiceCorrection.SendCorrectionRequest
    - InvoiceCorrectionRevision.SendCorrectionRequest
    - InvoiceRevision.SendCorrectionRequest
    - Invoice.SendCorrectionRequest
    - AcceptRevocationRequest
    - CreateSendTask
    - CreateSendTaskFromFile
    - CreateSendTaskFromFileRaw

- внутренние улучшения и оптимизации

- Исправлены ошибки:
    - Медленная работа компоненты при получении документа/списка документов
    - Удален ошибочно добавленный метод CustomDocumentToSend.AddCustomData()
    - Удалено поле CustomDocumentToSend.CustomData
    - Ошибка при отправке приглашений "##100[Ошибка сервера Диадок]code:400, HTTP error: Too many INN in request"
    - Падение клиента в методе SendTask.SendAsync
    - Ошибка при получении документа "##100[Ошибка сервера Диадок]code:404, HTTP error: Unknown box:"
    - Исправлена работа методов Reject у документов с типом Contract, Nonformalized


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_
