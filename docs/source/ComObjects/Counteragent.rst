Counteragent
============

Представление контрагента


.. rubric:: Свойства

:Guid:
    **Строка, чтение** - Идентификатор ящика контрагента в системе Диадок

    .. versionadded:: 5.31.0

:Name:
    **Строка, чтение** - наименование контрагента

:Inn:
    **Строка, чтение** - ИНН контрагента

:Kpp:
    **Строка, чтение** - КПП контрагента

:Address:
    :doc:`AddressInfo` **, чтение** - юридический адрес контрагента

    .. versionadded:: 3.0.8

:Status:
    **Строка, чтение** - текущий статус отношений с контрагентом. :doc:`Возможные значения <./Enums/CounteragentStatus>`

    .. versionadded:: 5.31.1

:Departments:
    :doc:`Коллекция <Collection>` **объектов** :doc:`Department` **, чтение** - список подразделений первого уровня вложенности

:LastEventTimestampTicks:
    **Дата и время, чтение** - метка времени последнего события из истории взаимодействия с данным контрагентом

:FnsParticipantId:
    **Строка, чтение** - идентификатор контрагента как участника документооборота

:MessageFromCounteragent:
    **Строка, чтение** - текст последнего комментария, полученного от контрагента, из истории взаимодействия ним

:MessageToCounteragent:
    **Строка, чтение** - текст последнего комментария, отправленного контрагенту, из истории взаимодействия ним

:Organization:
    :doc:`Organization` **, чтение** - организация, в контексте которой получен контрагент

:OrganizationGuid:
    **Строка, чтение** - идентификатор ящика организации, в контексте которой получен контрагент

    .. versionadded:: 5.31.0

:IsTest:
    **Булево, чтение** - признак того, что контрагент работает в тестовом режиме

:IsPilot:
    **Булево, чтение** - признак того, что контрагент работает в пилотном режиме

:IsActive:
    **Булево, чтение** - признак того, что контрагент активен (отправляет либо получает документы в Диадоке)

:IsRoaming:
    **Булево, чтение** - признак того, что организация работает через роуминг, то есть подключена к другому оператору ЭДО

    .. versionadded:: 5.4.0

:IsLiquidated:
    **Булево, чтение** - признак того, что организация ликвидирована

:IsBranch:
    **Булево, чтение** - признак того, что контрагент является филиалом


.. warning:: Поля устарели

    .. csv-table::
        :header: "Поле", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

        Id,             Guid,             :doc:`../History/release_info/5_31_0`,
        OrganizationId, OrganizationGuid, :doc:`../History/release_info/5_31_0`,

.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AcquireCounteragent() <Counteragent.AcquireCounteragent>`
        * :meth:`BreakWithCounteragent() <Counteragent.BreakWithCounteragent>`
        * :meth:`GetCertificates() <Counteragent.GetCertificates>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён",

            :meth:`GetStatus() <Counteragent.GetStatus>`, поле **Status**, :doc:`../History/release_info/5_31_1`,


        .. method:: Counteragent.GetStatus()

            Возвращает строковое представление текущего статуса отношений с контрагентом. :doc:`Возможные значения <./Enums/CounteragentStatus>`

            .. deprecated:: 5.31.1
              Используйте свойство **Status**


.. method:: Counteragent.AcquireCounteragent([Comment])

    :Comment: ``строка`` Комментарий к приглашению

    Отправляет контрагенту "приглашение" на обмен документами


.. method:: Counteragent.BreakWithCounteragent([Comment])

    :Comment: ``строка`` Комментарий к разрыву дружбы

    Разрывает действующее "приглашение" об обмене документами


.. method:: Counteragent.GetCertificates()

    Возвращает :doc:`коллекцию <Collection>` :doc:`сертификатов <PersonalCertificate>` контрагента. Доступно для организаций с возможностью отправки зашифрованных документов

    .. versionadded:: 5.0.0


.. seealso:: :doc:`../HowTo/HowTo_trust_counteragent`