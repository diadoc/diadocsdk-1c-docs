DocumentPackage
===============

Пакет документов. Объект предназначен для хранения информации о документах, входящих в пакет.


Свойства объекта
----------------

- **IsLocked** (булево, чтение) - признак того, что пакет является нередактируемым
- **Documents** (:doc:`коллекция <Collection>` объектов :doc:`Document <Document>`, чтение) - документы, входящие в пакет


Методы объекта
--------------

-  :doc:`Move <Move-(DocumentPackage)>` - перемещает пакет в указанное подразделение (только для редактируемых пакетов)
-  :doc:`Approve <Approve-(DocumentPackage)>` - ставит признак согласования документов в пакете (только для редактируемых пакетов)
-  :doc:`Disapprove <Disapprove-(DocumentPackage)>` - ставит признак отказа в согласовании документов в пакете (только для редактируемых пакетов)
-  :doc:`CreateResolutionRequestTask <CreateResolutionRequestTask-(DocumentPackage)>` - формирует задание для отправки запроса на согласование пакета документов (только для редактируемых пакетов)
-  :doc:`CreateReplySendTask <CreateReplySendTask-(DocumentPackage)>` - формирует задание для ответного действия с документом
-  :doc:`CreateOutDocumentSignTask <CreateOutDocumentSignTask-(DocumentPackage)>` - создает задание на подписание и отправку исходящего документа с отложенной отправкой.
-  :doc:`AssignToResolutionRoute <AssignToResolutionRoute>` - ставит пакет документов на маршрут согласования
-  :doc:`RemoveFromResolutionRoute <RemoveFromResolutionRoute>` - снимает пакет документов с маршрута согласования


.. toctree::
   :name: Auto_1
   :hidden:

   Move <Move-(DocumentPackage)>
   Approve <Approve-(DocumentPackage)>
   Disapprove <Disapprove-(DocumentPackage)>
   CreateResolutionRequestTask <CreateResolutionRequestTask-(DocumentPackage)>
   CreateReplySendTask <CreateReplySendTask-(DocumentPackage)>
   CreateOutDocumentSignTask <CreateOutDocumentSignTask-(DocumentPackage)>

