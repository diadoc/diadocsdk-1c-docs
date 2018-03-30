Ошибки, исправленные в версии 5.21
==================================

v5.21.0 - 13.03.2018
--------------------

- метод :doc:`GetDocumentEventList <GetDocumentEventList>` имел ограничение на количество возвращаемых объектов(100), что приводило к фрагментации результатов

- не заполнялось свойство :doc:`TovTorgTransferInfo.Waybills <TovTorgTransferInfo>`

v5.21.2 - 30.03.2018
--------------------

- происходил крах приложения при вызове :doc:`CreateReplySendTask.Send <CreateReplySendTask-(Document)>`, созданного для документа "TovTorg"

- :doc:`GetContent <GetContent-(Utd)>` для УПД не учитывал версию содержимого