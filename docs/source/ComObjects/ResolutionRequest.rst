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
  **Строка, чтение** - тип запроса согласования. :doc:`Возможные значения <Enums/ResolutionRequestType>`

:TargetDepartment:
  :doc:`Department` **, чтение** - подразделение организации, в которое направлен запрос

:TargetUser:
  :doc:`OrganizationUser <OrganizationUser>` **, чтение** - пользователь, которому направлен запрос

:Id:
  **Строка, чтение** - идентификатор запроса согласования

:AvaliableActions:
  :doc:`Коллекция <Collection>` **строк, чтение** - список действий, которые можно выполнить в рамках текущего запроса на согласование. :doc:`Возможные значения <Enums/ResolutionAction>`


.. rubric:: Методы

+---------------------------+-----------------------------+
| |ResolutionRequest-Deny|_ | |ResolutionRequest-Cancel|_ |
+---------------------------+-----------------------------+

.. |ResolutionRequest-Deny| replace:: Deny()
.. |ResolutionRequest-Cancel| replace:: Cancel()



.. _ResolutionRequest-Deny:
.. method:: ResolutionRequest.Deny([Comment])

  :Comment: ``строка`` комментарий к отказу в резолюции

  Выполняет отказ в запрошенной резолюции



.. _ResolutionRequest-Cancel:
.. method:: ResolutionRequest.Cancel()

  Отменяет запрошенную резолюцию
