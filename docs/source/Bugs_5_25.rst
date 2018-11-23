Ошибки, исправленные в версии 5.25
==================================

v5.25.0 - 23.11.2018
--------------------

- исправлена ошибка связанная с ответным действием "AcceptDocument" (:doc:`Document.CreateReplySendTask <CreateReplySendTask-(Document)>`): если в структуре документа Диадок АПИ у титула отправителя есть дочерние элементы типа Attachment это приводило к тому, что :doc:`ReplySendTask.Content <ReplySendTask>` возвращал объект типа :doc:`AcceptanceContent <AcceptanceContent>` для любых типов документов
- при вызове метода :doc:`OutDocumentSignTask.Send <OutDocumentSignTask>` или :doc:`OutDocumentSignTask.SendAsync <OutDocumentSignTask>` в Диадок АПИ не отправлялись данные подписанта типа :doc:`ExtendedSigner <ExtendedSigner>`
- исправлена совместимость с Windows XP
