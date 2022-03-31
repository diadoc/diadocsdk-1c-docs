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
    :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentBase` **, чтение** - документы, входящие в пакет



.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`CreateReplySendTask2() <DocumentPackage.CreateReplySendTask2>`
        * :meth:`CreateResolutionRequestTask() <DocumentPackage.CreateResolutionRequestTask>`
        * :meth:`CreateOutDocumentSignTask() <DocumentPackage.CreateOutDocumentSignTask>`
        * :meth:`AssignToResolutionRoute() <DocumentPackage.AssignToResolutionRoute>`
        * :meth:`RemoveFromResolutionRoute() <DocumentPackage.RemoveFromResolutionRoute>`
        * :meth:`Approve() <DocumentPackage.Approve>`
        * :meth:`Disapprove() <DocumentPackage.Disapprove>`
        * :meth:`Move() <DocumentPackage.Move>`
        * :meth:`Delete() <DocumentPackage.Delete>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

            :meth:`CreateReplySendTask() <DocumentPackage.CreateReplySendTask>`, :meth:`CreateReplySendTask2() <DocumentPackage.CreateReplySendTask2>`, :doc:`../History/release_info/5_27_0`,

        .. method:: DocumentPackage.CreateReplySendTask(ReplyType="AcceptDocument")

            :ReplyType: ``Строка`` Тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

            Создает :doc:`задание на выполнение ответного действия с пакетом документов <ReplySendTask>`


.. method:: DocumentPackage.CreateReplySendTask2(ReplyType="AcceptDocument")

    :ReplyType: ``Строка`` Тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

    Создает :doc:`задание на выполнение ответного действия с пакетом документов <ReplySendTask2>`

    .. versionadded:: 5.27.0


.. method:: DocumentPackage.CreateResolutionRequestTask()

    Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`


.. method:: DocumentPackage.CreateOutDocumentSignTask()

    Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

    .. versionadded:: 5.6.0


.. method:: DocumentPackage.AssignToResolutionRoute(RouteId[, Comment])

    :RouteId: ``строка`` Идентификатор маршрута
    :Comment: ``строка`` Комментарий, который будет добавлен при постановке документов на маршрут

    Ставит документы на маршрут согласования. Получить доступные маршруты согласования можно методом :meth:`Organization.GetResolutionRoutes`


.. method:: DocumentPackage.RemoveFromResolutionRoute(RouteId[, Comment])

    :RouteId: ``строка`` Идентификатор маршрута
    :Comment: ``строка`` Комментарий, который будет добавлен при снятии документов с маршрута

    Снимает документы с маршрута согласования


.. method:: DocumentPackage.Approve([Comment])

    :Comment: ``строка`` комментарий, который будет добавлен при согласовании документов пакета

    Согласует документы пакета


.. method:: DocumentPackage.Disapprove([Comment])

    :Comment: ``строка`` комментарий, который будет добавлен при отказе согласования документов пакета

    Отказывает в согласовании документов пакета


.. method:: DocumentPackage.Move(DepartmentID)

    :DepartmentID: ``строка`` идентификатор подразделения


.. method:: DocumentPackage.Delete()

    Помечает документы как удалённый