ResolutionRequest
=================

Запрос согласования документа


.. rubric:: Свойства

:Author:
    **Строка, чтение** - ФИО инициатора запроса согласования

:CreationDate:
    **Дата и время, чтение** - дата и время создания запроса согласования

:Comment:
    **Строка, чтение** - комментарий к запросу согласования

:ResolutionType:
   **Строка, чтение** - тип запроса согласования. :doc:`Возможные значения <./Enums/ResolutionRequestType>`

:TargetDepartment:
    :doc:`Department` **, чтение** - подразделение организации, в которое направлен запрос

:TargetUser:
    :doc:`OrganizationUser` **, чтение** - пользователь, которому направлен запрос

:Id:
    **Строка, чтение** - идентификатор запроса согласования

:AvaliableActions:
    :doc:`Коллекция <Collection>` **строк, чтение** - список действий, которые можно выполнить в рамках текущего запроса на согласование. :doc:`Возможные значения <./Enums/ResolutionAction>`


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`Deny() <ResolutionRequest.Deny>`
        * :meth:`Cancel() <ResolutionRequest.Cancel>`

.. method:: ResolutionRequest.Deny([Comment])

    :Comment: ``строка`` комментарий к отказу в резолюции

    Выполняет отказ в запрошенной резолюции


.. method:: ResolutionRequest.Cancel()

    Отменяет запрошенную резолюцию