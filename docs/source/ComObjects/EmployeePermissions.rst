EmployeePermissions
===================

Права сотрудника организации


.. rubric:: Свойства


:IsAdministrator:
  **Булево, чтение** - сотрудник является администратором

:Department:
  :doc:`Department` **, чтение** - подразделение к которому прикреплён пользователь. Может быть :doc:`пустым <Descriptions/Empty_Com_Object>`

:VisibleDepartments:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Department` **, чтение** - видимые сотруднику подразделения

:DocumentsAccessLevel:
  **Строка, чтение** - уровень доступа к документам. :doc:`Возможные значения <./Enums/DocumentsAccessLevel>`

:AuthorizationPermission:
  :doc:`AuthorizationPermission` **, чтение** - ограничения доступа сотрудника к организации. Может быть :doc:`пустым <Descriptions/Empty_Com_Object>`

:Actions:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Flag` **, чтение** - доступность действий
