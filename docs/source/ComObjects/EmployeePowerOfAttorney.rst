EmployeePowerOfAttorney
=======================

Представление данных об МЧД, выданной пользователю

.. versionadded:: 5.37.0


.. rubric:: Свойства

:IsDefault:
  **Булево, чтение** - МЧД установлена для сотрудника как МЧД по-умолчанию

:PowerOfAttorneyInfo:
  :doc:`PowerOfAttorneyInfo` **, чтение** - реквизиты МЧД

:ApplicabilityForCurrentCertificate:
  :doc:`PowerOfAttorneyStatus` **, чтение** - статус применимости МЧД для сертификата, по которому авторизовался пользователь.
  Если пользователь авторизовался по логину, то поле будет :doc:`пустым <Descriptions/Empty_Com_Object>`
