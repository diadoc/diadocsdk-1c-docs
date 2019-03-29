ResolutionRequest
=================

Объект соответствующий запросу согласования.

Свойства
--------

-  Author (строка, чтение) - ФИО согласователя
-  CreationDate (дата и время, чтение) - дата-время создания согласования
-  Comment (строка, чтение) - комментарий к согласованию
-  ResolutionType (строка, чтение) - тип действия по согласованию
-  TargetDepartment (объект Department, чтение) - подразделение организации, в которое направлен запрос
-  TargetUser (объект OrganizationUser, чтение) - пользователь, которому направлен запрос
-  Id (строка, чтение) - идентификатор сущности

Свойство ResolutionType принимает одно из следующих значений:

- "ApprovementRequest" - запрос на согласование документа
- "SignatureRequest" - запрос на подпись документа
- "ApprovementSignatureRequest" - запрос на согласующую подпись под документом
- "Custom" - запрос был создан на основе шага маршрута согласования и не вписывается в стандартные типы
- "UnknownResolutionRequestType" - неизвестный тип запроса


Методы
------

- :doc:`Deny <Deny-(ResolutionRequest)>` -  отказ от запроса подписи к документу.

- :doc:`Cancel <Cancel-(ResolutionRequest)>` -  отмена запроса на согласование документа.

.. toctree::
   :name: Auto
   :hidden:

   Deny <Deny-(ResolutionRequest)>
   Cancel <Cancel-(ResolutionRequest)>