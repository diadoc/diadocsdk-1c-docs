ResolutionStatus
================

Объект предназначен для получения информации о текущем статусе согласования документа.


Свойства
--------

-  Type (строка, чтение) - тип статуса согласования
-  Author (:doc:`OrganizationUser <OrganizationUser>`, чтение) - ФИО согласователя
-  TargetDepartment (объект :doc:`Department <Department>`, чтение) - подразделение организации, в которое направлен запрос
-  TargetUser (объект :doc:`OrganizationUser <OrganizationUser>`, чтение) - пользователь, которому направлен запрос


Свойство **Type** принимает одно из следующих значений:

    -  Approved - согласован
    -  ApprovementRequested - запрошено согласование
    -  Disapproved - в согласовании отказано
    -  SignatureDenied - в подписи отказано
    -  SignatureRequested - запрошена подпись
    -  None - документ не согласовывался
    -  ActionRequested - запрошено действие. Список доступных действий доступен в коллекции AvaliableActions объекта :doc:`ResolutionRequest <ResolutionRequest>`


Методы
------

Отсутствуют
