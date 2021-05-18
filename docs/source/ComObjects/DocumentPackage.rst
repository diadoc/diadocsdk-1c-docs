DocumentPackage
===============

Инфомация о пакете документов

.. versionadded:: 5.3.0


.. rubric:: Свойства

:IsLocked:
  **Булево, чтение** - признак того, что пакет является нередактируемым

:LockMode:
  **Строка, чтение** - редактируемость пакета. :doc:`Возможные зачения <./Enums/LockMode>`

:Documents:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Document` **, чтение** - документы, входящие в пакет



.. rubric:: Методы

+------------------------------------------------+---------------------------+
| |DocumentPackage-CreateReplySendTask2|_        | |DocumentPackage-Move|_   |
+------------------------------------------------+---------------------------+
| |DocumentPackage-CreateResolutionRequestTask|_ | |DocumentPackage-Delete|_ |
+------------------------------------------------+---------------------------+
| |DocumentPackage-CreateOutDocumentSignTask|_   |                           |
+------------------------------------------------+---------------------------+
| |DocumentPackage-AssignToResolutionRoute|_     |                           |
+------------------------------------------------+---------------------------+
| |DocumentPackage-RemoveFromResolutionRoute|_   |                           |
+------------------------------------------------+---------------------------+
| |DocumentPackage-Approve|_                     |                           |
+------------------------------------------------+---------------------------+
| |DocumentPackage-Disapprove|_                  |                           |
+------------------------------------------------+---------------------------+


.. |DocumentPackage-CreateReplySendTask2| replace:: CreateReplySendTask2()
.. |DocumentPackage-CreateResolutionRequestTask| replace:: CreateResolutionRequestTask()
.. |DocumentPackage-CreateOutDocumentSignTask| replace:: CreateOutDocumentSignTask()
.. |DocumentPackage-AssignToResolutionRoute| replace:: AssignToResolutionRoute()
.. |DocumentPackage-RemoveFromResolutionRoute| replace:: RemoveFromResolutionRoute()
.. |DocumentPackage-Approve| replace:: Approve()
.. |DocumentPackage-Disapprove| replace:: Disapprove()

.. |DocumentPackage-Move| replace:: Move()
.. |DocumentPackage-Delete| replace:: Delete()



.. _DocumentPackage-CreateReplySendTask2:
.. method:: DocumentPackage.CreateReplySendTask2(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

  Создает :doc:`задание на выполнение ответного действия с пакетом документов <ReplySendTask2>`

  .. versionadded:: 5.27.0



.. _DocumentPackage-CreateResolutionRequestTask:
.. method:: DocumentPackage.CreateResolutionRequestTask()

  Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`




.. _DocumentPackage-CreateOutDocumentSignTask:
.. method:: DocumentPackage.CreateOutDocumentSignTask()

  Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

.. versionadded:: 5.6.0



.. _DocumentPackage-AssignToResolutionRoute:
.. method:: DocumentPackage.AssignToResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при постановке документов на маршрут

  Ставит документы на маршрут согласования. Получить доступные маршруты согласования можно методом :meth:`Organization.GetResolutionRoutes`



.. _DocumentPackage-RemoveFromResolutionRoute:
.. method:: DocumentPackage.RemoveFromResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при снятии документов с маршрута

  Снимает документы с маршрута согласования



.. _DocumentPackage-Approve:
.. method:: DocumentPackage.Approve([Comment])

  :Comment: ``строка`` комментарий, который будет добавлен при согласовании документов пакета

  Согласует документы пакета



.. _DocumentPackage-Disapprove:
.. method:: DocumentPackage.Disapprove([Comment])

  :Comment: ``строка`` комментарий, который будет добавлен при отказе согласования документов пакета

  Отказывает в согласовании документов пакета



.. _DocumentPackage-Move:
.. method:: DocumentPackage.Move(DepartmentID)

  :DepartmentID: ``строка`` идентификатор подразделения



.. _DocumentPackage-Delete:
.. method:: DocumentPackage.Delete()

  Помечает документы как удалённый





.. rubric:: Устаревшие методы


+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+
| **Метод или свойство**                                        | **Устарел**                           | **Удалён**                         | **Рекомендуется использовать**                       |
+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+
| :meth:`DocumentPackage.CreateReplySendTask`                   | :doc:`../History/release_info/5_27_0` |                                    | :meth:`DocumentPackage.CreateReplySendTask2`         |
+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+


.. method:: DocumentPackage.CreateReplySendTask(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

  Создает :doc:`задание на выполнение ответного действия с пакетом документов <ReplySendTask>`
