Ошибки, исправленные в версии 5.27
==================================


v5.27.0 - 10.06.2019
--------------------

- Медленная работа компоненты при получении документа/списка документов
- Удален ошибочно добавленный метод CustomDocumentToSend.AddCustomData()
- Удалено поле CustomDocumentToSend.CustomData
- Ошибка при отправке приглашений "##100[Ошибка сервера Диадок]code:400, HTTP error: Too many INN in request"
- Падение клиента в методе :doc:`SendTask.SendAsync <SendAsync-(SendDraftTask)>`
- Ошибка при получении документа "##100[Ошибка сервера Диадок]code:404, HTTP error: Unknown box:"
- Исправлена работа методов Reject у документов с типом Contract, Nonformalized