DocumentPackage
===============

Инфомация о пакете документов

.. versionadded:: 5.3.0


.. rubric:: Свойства

:IsLocked:
  **Булево, чтение** - признак того, что пакет является нередактируемым

:LockMode:
  **Строка, чтение** - редактируемость пакета. |DocumentPackage-LockMode|_

:Documents:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Document <Document>` **, чтение** - документы, входящие в пакет



.. rubric:: Методы

+-------------------------------+------------------------------------------------+----------------------------------------------+
| |DocumentPackage-Move|_       | |DocumentPackage-CreateResolutionRequestTask|_ | |DocumentPackage-AssignToResolutionRoute|_   |
+-------------------------------+------------------------------------------------+----------------------------------------------+
| |DocumentPackage-Delete|_     | |DocumentPackage-CreateReplySendTask|_         | |DocumentPackage-RemoveFromResolutionRoute|_ |
+-------------------------------+------------------------------------------------+----------------------------------------------+
| |DocumentPackage-Approve|_    | |DocumentPackage-CreateReplySendTask2|_        |                                              |
+-------------------------------+------------------------------------------------+----------------------------------------------+
| |DocumentPackage-Disapprove|_ | |DocumentPackage-CreateOutDocumentSignTask|_   |                                              |
+-------------------------------+------------------------------------------------+----------------------------------------------+

.. |DocumentPackage-Move| replace:: Move()
.. |DocumentPackage-Delete| replace:: Delete()
.. |DocumentPackage-Approve| replace:: Approve()
.. |DocumentPackage-Disapprove| replace:: Disapprove()
.. |DocumentPackage-CreateResolutionRequestTask| replace:: CreateResolutionRequestTask()
.. |DocumentPackage-CreateReplySendTask| replace:: CreateReplySendTask()
.. |DocumentPackage-CreateReplySendTask2| replace:: CreateReplySendTask2()
.. |DocumentPackage-CreateOutDocumentSignTask| replace:: CreateOutDocumentSignTask()
.. |DocumentPackage-AssignToResolutionRoute| replace:: AssignToResolutionRoute()
.. |DocumentPackage-RemoveFromResolutionRoute| replace:: RemoveFromResolutionRoute()



.. _DocumentPackage-Move:
.. method:: DocumentPackage.Move(DepartmentID)

  :DepartmentID: ``строка`` идентификатор подразделения

  Перемещает документы в указанное подразделение. Идентификатор головного подразделения всегда ``00000000-0000-0000-0000-000000000000``



.. _DocumentPackage-Delete:
.. method:: DocumentPackage.Delete()

  Помечает документы как удалённый



.. _DocumentPackage-Approve:
.. method:: DocumentPackage.Approve([Comment])

  :Comment: ``строка`` комментарий, который будет добавлен при согласовании документов пакета

  Согласует документы пакета



.. _DocumentPackage-Disapprove:
.. method:: DocumentPackage.Disapprove([Comment])

  :Comment: ``строка`` комментарий, который будет добавлен при отказе согласования документов пакета

  Отказывает в согласовании документов пакета



.. _DocumentPackage-CreateResolutionRequestTask:
.. method:: DocumentPackage.CreateResolutionRequestTask()

  Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`



.. _DocumentPackage-CreateReplySendTask:
.. method:: DocumentPackage.CreateReplySendTask(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. |DocumentPackage-ReplyType|_

  Создает :doc:`задание на выполнение ответного действия с пакетом документов <ReplySendTask>`

  .. deprecated:: 5.27.0
    Используйте :func:`DocumentPackage.CreateReplySendTask2`



.. _DocumentPackage-CreateReplySendTask2:
.. method:: DocumentPackage.CreateReplySendTask2(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. |DocumentPackage-ReplyType|_

  Создает :doc:`задание на выполнение ответного действия с пакетом документов <ReplySendTask2>`

  .. versionadded:: 5.27.0



.. _DocumentPackage-CreateOutDocumentSignTask:
.. method:: DocumentPackage.CreateOutDocumentSignTask()

  Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

.. versionadded:: 5.6.0


.. _DocumentPackage-AssignToResolutionRoute:
.. method:: DocumentPackage.AssignToResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при постановке документов на маршрут

  Ставит документы на маршрут согласования. Получить доступные маршруты согласования можно методом :func:`Organization.GetResolutionRoutes`


.. _DocumentPackage-RemoveFromResolutionRoute:
.. method:: DocumentPackage.RemoveFromResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при снятии документов с маршрута

  Снимает документы с маршрута согласования



.. rubric:: Дополнительная информация


.. |DocumentPackage-LockMode| replace:: Возможные значения

.. _DocumentPackage-LockMode:

=================== =======================================
Значение *LockMode* Описание
=================== =======================================
None                Пакет можно редактировать
Send                Пакет нередактируем до момента отправки
Full                Пакет нередактируем
=================== =======================================

.. |DocumentPackage-ReplyType| replace:: Возможные значения

.. _DocumentPackage-ReplyType:

==================== ==================================
Значение *ReplyType* Описание
==================== ==================================
AcceptDocument       подписание документов
RejectDocument       отказ в подписи документов
CorrectionRequest    запроc на уточнение документов
RevocationRequest    запроc на аннулирование документов
AcceptRevocation     принятие аннулирования документов
RejectRevocation     отказ от аннулирования документов
==================== ==================================
