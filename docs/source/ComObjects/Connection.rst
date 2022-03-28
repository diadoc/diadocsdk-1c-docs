Connection
==========

Логическое соединение с сервером Диадока


.. rubric:: Свойства


:SessionInfo:
    :doc:`SessionInfo` **, чтение** - информация о сессии

.. warning:: Поля устарели

    .. csv-table::
        :header: "Поле", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

        Login,            :doc:`SessionInfo`.Login,              :doc:`../History/release_info/5_37_0`,
        AuthenticateType, :doc:`SessionInfo`.AuthenticationType, :doc:`../History/release_info/5_37_0`,
        Certificate,      :doc:`SessionInfo`.Certificate,        :doc:`../History/release_info/5_37_0`,
        Token,            :doc:`SessionInfo`.Token,              :doc:`../History/release_info/5_37_0`,


.. rubric:: Методы


.. tabs::

    .. tab:: Все актуальные

        * :meth:`GetOrganizationList() <Connection.GetOrganizationList>`
        * :meth:`GetOrganizationById() <Connection.GetOrganizationById>`
        * :meth:`GetMyUser() <Connection.GetMyUser>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён",

            :meth:`CreateCloudSignTask() <Connection.CreateCloudSignTask>`,   , :doc:`../History/release_info/5_26_0`, :doc:`../History/release_info/5_33_0`
            :meth:`GetCloudCertificates() <Connection.GetCloudCertificates>`, , :doc:`../History/release_info/5_26_0`, :doc:`../History/release_info/5_33_0`


        .. method:: Connection.CreateCloudSignTask(Thumbprint)

            :Thumbprint: ``Строка`` отпечаток Контур.Сертификата

            Возвращает :doc:`объект <CloudSignTask>`, с помощью которого можно подписать документы Контур.Сертификатом

            .. versionadded:: 5.2.0

            .. versionchanged:: 5.33.0
                Метод удалён


        .. method:: Connection.GetCloudCertificates()

            Возвращает :doc:`коллекцию <Collection>` :doc:`Контур.Сертификатов <CloudCertificateInfo>`, доступных текущему пользователю

            .. versionadded:: 5.2.0

            .. versionchanged:: 5.33.0
                Метод удалён


.. method:: Connection.GetOrganizationList()

    Возвращает :doc:`коллекцию <Collection>` :doc:`организаций <Organization>`, к которым текущий пользователь имеет доступ


.. method:: Connection.GetOrganizationById(BoxID)

    :BoxID: ``строка`` идентификатор ящика организации

    Возвращает :doc:`организацию <Organization>`, к которой текущий пользователь имеет доступ


.. method:: Connection.GetMyUser()

    Возвращает :doc:`информацию <User>` об авторизованном пользователе

    .. versionadded:: 5.6.0


.. seealso:: :doc:`../HowTo/HowTo_auth`