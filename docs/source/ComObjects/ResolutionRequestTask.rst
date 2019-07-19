ResolutionRequestTask
=====================

Задание для отправки запроса согласования или подписи

.. rubric:: Свойства

:InitialDocumentId:
  **Строка, чтение** - идентификатор документа, для которого формируется запрос

  .. deprecated:: 5.3.0
    Используйте коллекцию *InitialDocuments*

:InitialDocuments:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Document <Document>` **, чтение** - документы, для которых формируется запрос


:ResolutionRequestType:
  **Строка, чтение/запись** - тип запроса. |ResolutionRequestTask-Type|_

:Comment:
  **Строка, чтение/запись** - комментарий к запросу

:TargetDepartmentId:
  **Строка, чтение/запись** - идентификатор подразделения, в которое направлен запрос

:TargetUserId:
  **Строка, чтение/запись** - идентификатор пользователя, которому направлен запрос



.. rubric:: Методы

+-------------------------------+
| |ResolutionRequestTask-Send|_ |
+-------------------------------+

.. |ResolutionRequestTask-Send| replace:: Send()



.. _ResolutionRequestTask-Send:
.. method:: ResolutionRequestTask.Send()

  Отправить запрос на сервер Диадок



.. rubric:: Дополнительная информация

.. |ResolutionRequestTask-Type| replace:: Возможные значения
.. _ResolutionRequestTask-Type:

================================ =============================
Значение *ResolutionRequestType* Описание
================================ =============================
ApprovementRequest               запрос согласования документа
SignatureRequest                 запрос подписи документа
================================ =============================
