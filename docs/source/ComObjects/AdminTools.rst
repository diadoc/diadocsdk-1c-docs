AdminTools
==========


Набор инструментов для администрирования организации

Может быть создан методом :meth:`Organization.CreateAdminTools`

  .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        .. csv-table::
            :header: "Машиночитаемые доверенности", "Данные сертификатов"

            :meth:`GetEmployeePowersOfAttorney() <AdminTools.GetEmployeePowersOfAttorney>`, :meth:`CanSendInvoice() <AdminTools.CanSendInvoice>`
            :meth:`SetDefaultPowerOfAttorney() <AdminTools.SetDefaultPowerOfAttorney>`, :meth:`GetExtendedSignerDetails() <AdminTools.GetExtendedSignerDetails>`
            :meth:`AddPowerOfAttorneyToEmployee() <AdminTools.AddPowerOfAttorneyToEmployee>`, :meth:`CreateSetExtendedSignerDetailsTask() <AdminTools.CreateSetExtendedSignerDetailsTask>`
            :meth:`RemovePowerOfAttorney() <AdminTools.RemovePowerOfAttorney>`, :meth:`RegisterCertificateInFNS() <AdminTools.RegisterCertificateInFNS>`

    .. tab:: Машиночитаемые доверенности

        * :meth:`GetEmployeePowersOfAttorney() <AdminTools.GetEmployeePowersOfAttorney>`

        * :meth:`SetDefaultPowerOfAttorney() <AdminTools.SetDefaultPowerOfAttorney>`

        * :meth:`AddPowerOfAttorneyToEmployee() <AdminTools.AddPowerOfAttorneyToEmployee>`

        * :meth:`RemovePowerOfAttorney() <AdminTools.RemovePowerOfAttorney>`

    .. tab:: Данные сертификатов

        * :meth:`CanSendInvoice() <AdminTools.CanSendInvoice>`

        * :meth:`GetExtendedSignerDetails() <AdminTools.GetExtendedSignerDetails>`

        * :meth:`CreateSetExtendedSignerDetailsTask() <AdminTools.CreateSetExtendedSignerDetailsTask>`

        * :meth:`RegisterCertificateInFNS() <AdminTools.RegisterCertificateInFNS>`



.. method:: AdminTools.GetPowersOfAttorney(Employee, OnlyActual=``True``)

    :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
    :OnlyActual: ``булево`` признак того, что нужно возвращать только действующие доверенности

    Возвращает :doc:`коллекцию <Collection>` :doc:`доверенностей текущего сотрудника <EmployeePowerOfAttorney>`.
    Если флаг ``OnlyActual`` истинен, то вернутся только действующие доверенности


.. method:: AdminTools.SetDefaultPowerOfAttorney(Employee, PowerOfAttorney)

    :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
    :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

    Устанавливает переданную доверенность как доверенность по умолчанию для указанного сотрудника.
    Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`


.. method:: AdminTools.AddPowerOfAttorney(Employee, PowerOfAttorney)

    :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
    :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

    Привязывает доверенность к указанному сотруднику.
    Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`


.. method:: AdminTools.RemovePowerOfAttorney(Employee, PowerOfAttorney)

    :Employee: :doc:`EmployeeInfo` сотрудник, для которого выполняется операция
    :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

    Отвязывает довереность от указанного сотрудника


.. method:: AdminTools.CanSendInvoice(Certificate)

    :Certificate: :doc:`PersonalCertificate` объект сертификата

    Проверяет можно ли подписывать счета-фактуры, используя указанный сертфикат. Если невозможно, то вернёт текст с причиной, иначе - пустую строку.


.. method:: AdminTools.GetExtendedSignerDetails(Certificate, DocumentTitleName=``UNKNOWN``)

    :Certificate: :doc:`PersonalCertificate` объект сертификата
    :DocumentTitleName: ``строка`` тип титула документа. :doc:`Возможные значения <Enums/DocumentTitleType>`

    Возвращает :doc:`параметры подписанта <ExtendedSignerDetails>` в текущей организации для указанного типа титула и сертификата.
    Получить значение для *DocumentTitleName* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`
    Для *DocumentTitleName* == ``Absent`` и *DocumentTitleName* == ``UNKNOWN`` вызов невозможен.


.. method:: AdminTools.CreateSetExtendedSignerDetailsTask(Certificate)

    :Certificate: :doc:`PersonalCertificate` объект сертификата

    Возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта для указанного сертификата.


.. method:: AdminTools.RegisterCertificateInFNS(Certificate)

    :Certificate: :doc:`PersonalCertificate` объект сертификата

    Добавляет в сообщение для ФНС указанный сертификат.