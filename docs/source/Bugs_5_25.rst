Ошибки, исправленные в версии 5.25
==================================

v5.25.1 - 07.12.2018
--------------------

- При попытке подписания документа возникала ошибка "CreateReplySendTask. Access to Box is denied"
- Исправлена совместимость c Windows XP

v5.25.0 - 23.11.2018
--------------------

- исправлена ошибка связанная с ответным действием "AcceptDocument" (:doc:`Document.CreateReplySendTask <CreateReplySendTask-(Document)>`): если в структуре документа Диадок АПИ у титула отправителя есть дочерние элементы типа Attachment это приводило к тому, что :doc:`ReplySendTask.Content <ReplySendTask>` возвращал объект типа :doc:`AcceptanceContent <AcceptanceContent>` для любых типов документов
- при вызове метода :doc:`OutDocumentSignTask.Send <OutDocumentSignTask>` или :doc:`OutDocumentSignTask.SendAsync <OutDocumentSignTask>` в Диадок АПИ не отправлялись данные подписанта типа :doc:`ExtendedSigner <ExtendedSigner>`
- улучшена совместимость с Windows XP
- При получении некоторых документов возникала ошибка "vector<T> too long"
