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

.. tabs::

    .. tab:: Все актуальные

        .. csv-table::
            :header: Управление машиночитаемыми довереностями, "Управление данными, привязанными к сертификатам"

            :meth:`GetPowersOfAttorney() <MyEmployee.GetPowersOfAttorney>`,             :meth:`CanSendInvoice() <MyEmployee.CanSendInvoice>`
            :meth:`SetDefaultPowerOfAttorney() <MyEmployee.SetDefaultPowerOfAttorney>`, :meth:`GetExtendedSignerDetails() <MyEmployee.GetExtendedSignerDetails>`
            :meth:`AddPowerOfAttorney() <MyEmployee.AddPowerOfAttorney>`,               :meth:`CreateSetExtendedSignerDetailsTask() <MyEmployee.CreateSetExtendedSignerDetailsTask>`
            :meth:`RemovePowerOfAttorney() <MyEmployee.RemovePowerOfAttorney>`,         :meth:`UpdateCertificateFNSRegistration() <MyEmployee.UpdateCertificateFNSRegistration>`

    .. tab:: Управление машиночитаемыми довереностями

        * :meth:`GetPowersOfAttorney() <MyEmployee.GetPowersOfAttorney>`
        * :meth:`SetDefaultPowerOfAttorney() <MyEmployee.SetDefaultPowerOfAttorney>`
        * :meth:`AddPowerOfAttorney() <MyEmployee.AddPowerOfAttorney>`
        * :meth:`RemovePowerOfAttorney() <MyEmployee.RemovePowerOfAttorney>`

    .. tab:: Управление данными, привязанными к сертификатам

        * :meth:`CanSendInvoice() <MyEmployee.CanSendInvoice>`
        * :meth:`GetExtendedSignerDetails() <MyEmployee.GetExtendedSignerDetails>`
        * :meth:`CreateSetExtendedSignerDetailsTask() <MyEmployee.CreateSetExtendedSignerDetailsTask>`
        * :meth:`UpdateCertificateFNSRegistration() <MyEmployee.UpdateCertificateFNSRegistration>`


.. method:: MyEmployee.GetPowersOfAttorney(OnlyActual=True)

    :OnlyActual: **Булево** - признак того, что нужно возвращать только действующие доверенности

    Возвращает :doc:`коллекцию <Collection>` :doc:`доверенностей текущего сотрудника <EmployeePowerOfAttorney>`.
    Если флаг ``OnlyActual`` истинен, то вернутся только действующие доверенности


.. method:: MyEmployee.SetDefaultPowerOfAttorney(PowerOfAttorney)

    :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

    Устанавливает для текущего пользователя переданную доверенность как доверенность по умолчанию.
    Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`


.. method:: MyEmployee.AddPowerOfAttorney(PowerOfAttorney)

    :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

    Привязывает доверенность к текущему сотруднику.
    Возвращает :doc:`доверенность сотрудника <EmployeePowerOfAttorney>`


.. method:: MyEmployee.RemovePowerOfAttorney(PowerOfAttorney)

    :PowerOfAttorney: :doc:`PowerOfAttorney` объект доверенности

    Отвязывает доверенность от текущего сотрудника


.. method:: MyEmployee.CanSendInvoice()

    Проверяет можно ли подписывать счета-фактуры, используя сертификат, с которым произошла авторизация. Если невозможно, то вернёт текст с причиной, иначе - пустую строку


.. method:: MyEmployee.GetExtendedSignerDetails(DocumentTitleName="UNKNOWN")

    :DocumentTitleName: **Строка** - тип титула документа. :doc:`Возможные значения <Enums/DocumentTitleType>`

    Возвращает :doc:`параметры подписанта <ExtendedSignerDetails>` в текущей организации для указанного типа титула и сертификата, использованного в авторизации (можно найти в **SessionInfo**).
    Получить значение для *DocumentTitleName* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`.
    Для ``DocumentTitleName == "Absent"`` и ``DocumentTitleName == "UNKNOWN"`` вызов невозможен


.. method:: MyEmployee.CreateSetExtendedSignerDetailsTask()

    Возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта для сертификата, использованного в авторизации (можно найти в **SessionInfo**)


.. method:: MyEmployee.UpdateCertificateFNSRegistration()

    Добавляет в сообщение для ФНС сертификат, использованный в авторизации (можно найти в **SessionInfo**)