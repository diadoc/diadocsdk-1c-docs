PowerOfAttorneyInfo
===================

Реквизиты МЧД

.. versionadded:: 5.37.0

:RegistrationNumber:
  **Строка, чтение** - регистрационный номер МЧД

:Issuer:
  :doc:`PowerOfAttorneyParticipant` **, чтение** - информация о доверителе

:Confidant:
  :doc:`PowerOfAttorneyParticipant` **, чтение** - информация о доверенном лице. Поле может быть :doc:`пустым <Descriptions/Empty_Com_Object>`

:BeginDate:
  **Дата, чтение** - дата и время начала действия доверенности

:EndDate:
  **Дата, чтение** - дата и время окончания действия доверенности

:ValidationInfo:
  :doc:`PowerOfAttorneyValidationInfo` **, чтение** - информация о валидации доверенности. Может :doc:`отсутствовать <Descriptions/Empty_Com_Object>`

:RegistrationInfo:
  :doc:`PowerOfAttorneyRegistrationInfo` **, чтение** - информация о регистрации доверенности. Может :doc:`отсутствовать <Descriptions/Empty_Com_Object>`
