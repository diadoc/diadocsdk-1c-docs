ResolutionStatus
================

Информация о статусе запрошенного согласования или подписи документа


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип/статус запроса. |ResolutionStatus-Type|_

:Author:
  :doc:`OrganizationUser <OrganizationUser>` **, чтение** - автор запроса

:TargetDepartment:
  :doc:`Department <Department>` **, чтение** - подразделение организации, в которое направлен запрос

:TargetUser:
  :doc:`OrganizationUser <OrganizationUser>` **, чтение** - пользователь, которому направлен запрос


.. rubric:: Дополнительная информация

.. |ResolutionStatus-Type| replace:: Возможные значения
.. _ResolutionStatus-Type:

====================== ==========================
Значение *Type*        Описание
====================== ==========================
Approved               согласован
ApprovementRequested   запрошено согласование
Disapproved            в согласовании отказано
SignatureDenied        в подписи отказано
SignatureRequested     запрошена подпись
None                   документ не согласовывался
ActionRequested        запрошено действие
====================== ==========================
