MyEmployee
==========


Информация о своём пользователе как сотруднике организации

  .. versionadded:: 5.37.0



.. rubric:: Свойства

:EmployeeInfo:
  :doc:`EmployeeInfo` **, чтение** - информация о сотруднике


:SessionInfo:
  :doc:`SessionInfo` **, чтение** - Информация об авторизационной сессии


:NeedToAttachPowerOfAttorney:
  **Булево, чтение** - флаг необходимости использовать МЧД



.. rubric:: Методы


+--------------------------------------------------+-----------------------------------------+
| |MyEmployee-CanSendInvoice|_                     | |MyEmployee-GetPowersOfAttorney|_       |
+--------------------------------------------------+-----------------------------------------+
| |MyEmployee-GetExtendedSignerDetails|_           | |MyEmployee-SetDefaultPowerOfAttorney|_ |
+--------------------------------------------------+-----------------------------------------+
| |MyEmployee-CreateSetExtendedSignerDetailsTask|_ | |MyEmployee-AddPowerOfAttorney|_        |
+--------------------------------------------------+-----------------------------------------+
| |MyEmployee-UpdateCertificateFNSRegistration|_   | |MyEmployee-RemovePowerOfAttorney|_     |
+--------------------------------------------------+-----------------------------------------+


.. |MyEmployee-CanSendInvoice| replace:: CanSendInvoice()
.. |MyEmployee-GetExtendedSignerDetails| replace:: GetExtendedSignerDetails()
.. |MyEmployee-CreateSetExtendedSignerDetailsTask| replace:: CreateSetExtendedSignerDetailsTask()
.. |MyEmployee-UpdateCertificateFNSRegistration| replace:: UpdateCertificateFNSRegistration()
.. |MyEmployee-GetPowersOfAttorney| replace:: GetPowersOfAttorney()
.. |MyEmployee-SetDefaultPowerOfAttorney| replace:: SetDefaultPowerOfAttorney()
.. |MyEmployee-AddPowerOfAttorney| replace:: AddPowerOfAttorney()
.. |MyEmployee-RemovePowerOfAttorney| replace:: RemovePowerOfAttorney()


.. _MyEmployee-CanSendInvoice:
.. method:: MyEmployee.CanSendInvoice()

  Проверяет можно ли подписывать счета-фактуры, используя сертфиикат, с которым произошла авторизация. Если невозможно, то вернёт текст с причиной, иначе - пустую строку



.. _MyEmployee-GetExtendedSignerDetails:
.. method:: MyEmployee.GetExtendedSignerDetails(DocumentTitleName=``UNKNOWN``)

  :DocumentTitleName: ``строка`` тип титула документа. :doc:`Возможные значения <Enums/DocumentTitleType>`

  Возвращает :doc:`параметры подписанта <ExtendedSignerDetails>` в текущей организации для указанного типа титула и сертификата, использованного в авторизации (можно найти в **SessionInfo**).
  Получить значение для *DocumentTitleName* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`
  Для *DocumentTitleName* == ``Absent`` и *DocumentTitleName* == ``UNKNOWN`` вызов невозможен.



.. _MyEmployee-CreateSetExtendedSignerDetailsTask:
.. method:: MyEmployee.CreateSetExtendedSignerDetailsTask()

  Возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта для сертификата, использованного в авторизации (можно найти в **SessionInfo**)



.. _MyEmployee-UpdateCertificateFNSRegistration:
.. method:: MyEmployee.UpdateCertificateFNSRegistration()

  Добавляет в сообщение для ФНС сертификат, использованный в авторизации (можно найти в **SessionInfo**)



.. _MyEmployee-GetPowersOfAttorney:
.. method:: MyEmployee.GetPowersOfAttorney(OnlyActual=``True``)

  :OnlyActual: ``булево`` признак того, что нужно возвращать только действующие доверенности

  Возвращает :doc:`коллекцию <Collection>` :doc:`доверенностей текущего сотрудника <EmployeePowerOfAttorney>`.
  Если флаг ``OnlyActual`` истинен, то вернутся только действующие доверенности



.. _MyEmployee-SetDefaultPowerOfAttorney:
.. method:: MyEmployee.SetDefaultPowerOfAttorney(PowerOfAttorney)

  :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

  Устанавливает для текущего пользователя переданную доверенность как доверенность по умолчанию.
  Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`



.. _MyEmployee-AddPowerOfAttorney:
.. method:: MyEmployee.AddPowerOfAttorney(PowerOfAttorney)

  :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

  Привязывает доверенность к текущему сотруднику.
  Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`



.. _MyEmployee-RemovePowerOfAttorney:
.. method:: MyEmployee.RemovePowerOfAttorney(PowerOfAttorney)

  :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

  Отвязывает довереность от текущего сотрудника
