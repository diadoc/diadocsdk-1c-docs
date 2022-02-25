AdminTools
==========


Набор инструментов для администрирования организации

  .. versionadded:: 5.37.0


.. rubric:: Методы


+--------------------------------------------------+--------------------------------------------+
| |AdminTools-CanSendInvoice|_                     | |AdminTools-GetEmployeePowersOfAttorney|_  |
+--------------------------------------------------+--------------------------------------------+
| |AdminTools-GetExtendedSignerDetails|_           | |AdminTools-SetDefaultPowerOfAttorney|_    |
+--------------------------------------------------+--------------------------------------------+
| |AdminTools-CreateSetExtendedSignerDetailsTask|_ | |AdminTools-AddPowerOfAttorneyToEmployee|_ |
+--------------------------------------------------+--------------------------------------------+
| |AdminTools-RegisterCertificateInFNS|_           | |AdminTools-RemovePowerOfAttorney|_        |
+--------------------------------------------------+--------------------------------------------+


.. |AdminTools-CanSendInvoice| replace:: CanSendInvoice()
.. |AdminTools-GetExtendedSignerDetails| replace:: GetExtendedSignerDetails()
.. |AdminTools-CreateSetExtendedSignerDetailsTask| replace:: CreateSetExtendedSignerDetailsTask()
.. |AdminTools-RegisterCertificateInFNS| replace:: RegisterCertificateInFNS()
.. |AdminTools-GetEmployeePowersOfAttorney| replace:: GetEmployeePowersOfAttorney()
.. |AdminTools-SetDefaultPowerOfAttorney| replace:: SetDefaultPowerOfAttorney()
.. |AdminTools-AddPowerOfAttorneyToEmployee| replace:: AddPowerOfAttorneyToEmployee()
.. |AdminTools-RemovePowerOfAttorney| replace:: RemovePowerOfAttorney()


.. _AdminTools-CanSendInvoice:
.. method:: AdminTools.CanSendInvoice(Certificate)

  :Certificate: :doc:`PersonalCertificate` объект сертификата

  Проверяет можно ли подписывать счета-фактуры, используя указанный сертфикат. Если невозможно, то вернёт текст с причиной, иначе - пустую строку.



.. _AdminTools-GetExtendedSignerDetails:
.. method:: AdminTools.GetExtendedSignerDetails(Certificate, DocumentTitleName=``UNKNOWN``)

  :Certificate: :doc:`PersonalCertificate` объект сертификата

  :DocumentTitleName: ``строка`` тип титула документа. :doc:`Возможные значения <Enums/DocumentTitleType>`

  Возвращает :doc:`параметры подписанта <ExtendedSignerDetails>` в текущей организации для указанного типа титула и сертификата.
  Получить значение для *DocumentTitleName* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`
  Для *DocumentTitleName* == ``Absent`` и *DocumentTitleName* == ``UNKNOWN`` вызов невозможен.



.. _AdminTools-CreateSetExtendedSignerDetailsTask:
.. method:: AdminTools.CreateSetExtendedSignerDetailsTask(Certificate)

  :Certificate: :doc:`PersonalCertificate` объект сертификата

  Возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта для указанного сертификата.



.. _AdminTools-RegisterCertificateInFNS:
.. method:: AdminTools.RegisterCertificateInFNS(Certificate)

  :Certificate: :doc:`PersonalCertificate` объект сертификата

  Добавляет в сообщение для ФНС указанный сертификат.



.. _AdminTools-GetEmployeePowersOfAttorney:
.. method:: AdminTools.GetPowersOfAttorney(Employee, OnlyActual=``True``)

  :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
  :OnlyActual: ``булево`` признак того, что нужно возвращать только действующие доверенности

  Возвращает :doc:`коллекцию <Collection>` :doc:`доверенностей текущего сотрудника <EmployeePowerOfAttorney>`.
  Если флаг ``OnlyActual`` истинен, то вернутся только действующие доверенности



.. _AdminTools-SetDefaultPowerOfAttorney:
.. method:: AdminTools.SetDefaultPowerOfAttorney(Employee, PowerOfAttorney)

  :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
  :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

  Устанавливает переданную доверенность как доверенность по умолчанию для указанного сотрудника.
  Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`



.. _AdminTools-AddPowerOfAttorneyToEmployee:
.. method:: AdminTools.AddPowerOfAttorney(Employee, PowerOfAttorney)

  :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
  :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

  Привязывает доверенность к указанному сотруднику.
  Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`



.. _AdminTools-RemovePowerOfAttorney:
.. method:: AdminTools.RemovePowerOfAttorney(Employee, PowerOfAttorney)

  :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
  :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

  Отвязывает довереность от указанного сотрудника
