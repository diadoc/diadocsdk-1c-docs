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
  **Строка, чтение** - тип запроса согласования. |ResolutionRequest-Type|_

:TargetDepartment:
  :doc:`Department` **, чтение** - подразделение организации, в которое направлен запрос

:TargetUser:
  :doc:`OrganizationUser <OrganizationUser>` **, чтение** - пользователь, которому направлен запрос

:Id:
  **Строка, чтение** - идентификатор запроса согласования

:AvaliableActions:
  :doc:`Коллекция <Collection>` **строк, чтение** - список действий, которые можно выполнить в рамках текущего запроса на согласование/ |ResolutionRequest-AvaliableActions|_


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


.. rubric:: Дополнительная информация

.. |ResolutionRequest-Type| replace:: Возможные значения
.. _ResolutionRequest-Type:

============================ ==========================================================================================
Значение *ResolutionType*    Описание
============================ ==========================================================================================
ApprovementRequest           запрос на согласование документа
SignatureRequest             запрос на подпись документа
ApprovementSignatureRequest  запрос на согласующую подпись под документом
Custom                       запрос был создан на основе шага маршрута согласования и не вписывается в стандартные типы
UnknownResolutionRequestType неизвестный тип запроса
============================ ==========================================================================================


.. |ResolutionRequest-AvaliableActions| replace:: Возможные значения
.. _ResolutionRequest-AvaliableActions:

============================ ============================
Значение *AvaliableActions*  Описание
============================ ============================
ApproveAction                согласование
DisapproveAction             отказ в согласовании
SignWithApprovementSignature подпись согласующей подписью
SignWithPrimarySignature     подпись завершающей подписью
DenySignatureRequest         отказ в подписи сотруднику
RejectSigning                отказ в подписи контрагенту
UnknownAction                неизвестное действие
============================ ============================
