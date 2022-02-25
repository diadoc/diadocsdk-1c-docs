DiadocAPI
=========


Объект для создания контекста работы в Диадок


.. rubric:: Свойства

:ApiClientId:
  **Строка, чтение/запись** - ключ разработчика

:ServerUrl:
  **Строка, чтение/запись** - URL сервера Диадок

:ProxyMode:
  **Строка, чтение/запись** - режим использования прокси-сервера. :doc:`Возможные значения <./Enums/ProxyMode>`

:ProxySettings:
  :doc:`ProxySettings` **, чтение** - настройки прокси-сервера

:AutoLogonPolicy:
  **Строка, чтение/запись** - настройка `политики передачи авторизационных данных в запросах <https://docs.microsoft.com/en-us/windows/win32/winhttp/authentication-in-winhttp#automatic-logon-policy>`_ .
  :doc:`Возможные значения <./Enums/AutoLogonPolicy>`

  .. versionadded:: 5.32.0

:VerifySslCertificate:
  **Булево, чтение/запись** - флага проверки SSL сертиифкатов при выполнении запросов

  .. versionadded:: 5.32.0


.. rubric:: Методы

+----------------------------------+----------------------------------------------+---------------------------------------------+
| |DiadocAPI-GetFullVersion|_      | |DiadocAPI-VerifyThatUserHasAccessToAnyBox|_ | |DiadocAPI-CreateConnectionByCertificate2|_ |
+----------------------------------+----------------------------------------------+---------------------------------------------+
| |DiadocAPI-TestConnection2|_     | |DiadocAPI-GetPersonalCertificates|_         | |DiadocAPI-CreateConnectionByLogin|_        |
+----------------------------------+----------------------------------------------+---------------------------------------------+
| |DiadocApi-UpdateProxySettings|_ | |DiadocAPI-GetPersonalCertificate|_          |                                             |
+----------------------------------+----------------------------------------------+---------------------------------------------+


.. |DiadocAPI-GetFullVersion| replace:: GetFullVersion()
.. |DiadocAPI-TestConnection2| replace:: TestConnection2()
.. |DiadocApi-UpdateProxySettings| replace:: UpdateProxySettings()

.. |DiadocAPI-VerifyThatUserHasAccessToAnyBox| replace:: VerifyThatUserHasAccessToAnyBox()
.. |DiadocAPI-GetPersonalCertificates| replace:: GetPersonalCertificates()
.. |DiadocAPI-GetPersonalCertificate| replace:: GetPersonalCertificate()

.. |DiadocAPI-CreateConnectionByCertificate2| replace:: CreateConnectionByCertificate2()
.. |DiadocAPI-CreateConnectionByLogin| replace:: CreateConnectionByLogin()


.. _DiadocAPI-GetFullVersion:
.. method:: DiadocAPI.GetFullVersion()

    Возвращает строку с версией используемой компоненты в формате ``[AddIn|COM] [x86|x64] <номер сборки>``

  .. versionadded:: 5.29.4



.. _DiadocAPI-TestConnection2:
.. method:: DiadocAPI.TestConnection2()

  Возвращает :doc:`объект с результатами проверки соединения <TestConnectionResult>` с сервером Диадока, используя установленные параметры

  .. versionadded:: 5.26.3



.. _DiadocAPI-UpdateProxySettings:
.. method:: DiadocAPI.UpdateProxySettings(Connection)

  :Connection: :doc:`Connection` обновляемое подключение

  Метод обновляет настройки прокси у переданного объекта подключения и у всех объектов, полученных с помощью него

  .. versionadded:: 5.30.2



.. _DiadocAPI-VerifyThatUserHasAccessToAnyBox:
.. method:: DiadocAPI.VerifyThatUserHasAccessToAnyBox(Thumbprint)

  :Thumbprint: ``Строка`` Отпечаток сертификата

  Возвращает булевый признак, означающий есть ли у пользователя с указанным сертификатом доступ к какой-либо организации в Диадок



.. _DiadocAPI-GetPersonalCertificates:
.. method:: DiadocAPI.GetPersonalCertificates(UserStore=true)

  :UserStore: ``Булево`` Флаг определяющий `хранилище сертификатов <https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores>`_, где будет осуществлен поиск

  Возвращает :doc:`коллекцию <Collection>` :doc:`сертификатов <PersonalCertificate>`, установленных в подхранилище "Личное", хранилища определяемого флагом *UserStore*.
  Если флаг ``True`` - хранилище пользователя(по-умолчанию), ``False`` - хранилище компьютера.



.. _DiadocAPI-GetPersonalCertificate:
.. method:: DiadocAPI.GetPersonalCertificate(Thumbprint)

  :Thumbprint: ``Строка`` Отпечаток сертификата

  Возвращает :doc:`сертификат <PersonalCertificate>` с указанным отпечатком.
  Поиск происходит сначала в `хранилище <https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores>`_ "Личные" пользователя, затем - машины



.. _DiadocAPI-CreateConnectionByLogin:
.. method:: DiadocAPI.CreateConnectionByLogin(Login, Password)

  :Login:    ``Строка`` Логин пользователя
  :Password: ``Строка`` Пароль пользователя

  Возвращает :doc:`объект логического соединения <Connection>`, созданного по логину и паролю



.. _DiadocAPI-CreateConnectionByCertificate2:
.. method:: DiadocAPI.CreateConnectionByCertificate2(Certificate)

  :Certificate: :doc:`PersonalCertificate` объект сертификата

  Возвращает :doc:`объект логического соединения <Connection>`, созданного при помощи указанного сертификата

  .. versionadded:: 5.37.0



.. rubric:: Устаревшие методы


+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+
| **Метод**                                                     | **Когда устарел**                     | **Когда удалён**                   | **Рекомендуемая альтернатива**                       |
+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+
| :meth:`DiadocAPI.TestConnection`                              | :doc:`../History/release_info/5_26_3` |                                    | :meth:`DiadocAPI.TestConnection2`                    |
+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+
| :meth:`DiadocAPI.GetVersion`                                  | :doc:`../History/release_info/5_29_4` |                                    | :meth:`DiadocAPI.GetFullVersion`                     |
+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+
| :meth:`DiadocAPI.CreateConnectionByCertificate`               | :doc:`../History/release_info/5_37_0` |                                    | :meth:`DiadocAPI.CreateConnectionByCertificate2`     |
+---------------------------------------------------------------+---------------------------------------+------------------------------------+------------------------------------------------------+


.. method:: DiadocAPI.GetVersion()

    Возвращает строку с версией используемой компоненты



.. method:: DiadocAPI.TestConnection()

  Возвращает булевое значение успешности отправки запроса в Диадок, используя установленные параметры



.. method:: DiadocAPI.CreateConnectionByCertificate(Thumbprint[, Pin])

  :Thumbprint: ``Строка`` Отпечаток сертификата
  :Pin:        ``Строка`` Пин-код или пароль от контейнера сертификата

  Возвращает :doc:`объект логического соединения <Connection>`, созданного по сертификату с указанным отпечатком.
  Поиск сертификата происходит в хранилище `Личное` пользователя и, если там сертиифкат не найден - в хранилище `Личное` машины.
  Если *Pin* не задан, то будет использоваться пин-код/пароль, запомненный в крипто-провайдере или пустая строка
