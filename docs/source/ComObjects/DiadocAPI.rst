DiadocAPI
=========


Объект для создания контекста работы в Диадок


.. rubric:: Свойства

:ApiClientId:
  **Строка, чтение/запись** - ключ разработчика

:ServerUrl:
  **Строка, чтение/запись** - URL сервера Диадок

:ProxyMode:
  **Строка, чтение/запись** - режим использования прокси-сервера

:ProxySettings:
  :doc:`ProxySettings <ProxySettings>` **, чтение** - настройки прокси-сервера


.. rubric:: Методы

+--------------------------------------------+------------------------------+----------------------------------------------+
| |DiadocAPI-CreateConnectionByCertificate|_ | |DiadocAPI-GetVersion|_      | |DiadocAPI-GetFullVersion|_                   |
+--------------------------------------------+------------------------------+----------------------------------------------+
| |DiadocAPI-CreateConnectionByLogin|_       | |DiadocAPI-TestConnection|_  | |DiadocAPI-VerifyThatUserHasAccessToAnyBox|_ |
+--------------------------------------------+------------------------------+----------------------------------------------+
| |DiadocAPI-GetPersonalCertificates|_       | |DiadocAPI-TestConnection2|_ |                                              |
+--------------------------------------------+------------------------------+----------------------------------------------+


.. |DiadocAPI-CreateConnectionByCertificate| replace:: CreateConnectionByCertificate()
.. |DiadocAPI-CreateConnectionByLogin| replace:: CreateConnectionByLogin()
.. |DiadocAPI-GetPersonalCertificates| replace:: GetPersonalCertificates()
.. |DiadocAPI-GetVersion| replace:: GetVersion()
.. |DiadocAPI-GetFullVersion| replace:: GetFullVersion()
.. |DiadocAPI-TestConnection| replace:: TestConnection()
.. |DiadocAPI-TestConnection2| replace:: TestConnection2()
.. |DiadocAPI-VerifyThatUserHasAccessToAnyBox| replace:: VerifyThatUserHasAccessToAnyBox()



.. _DiadocAPI-CreateConnectionByCertificate:
.. method:: DiadocAPI.CreateConnectionByCertificate(Thumbprint[, Pin])

  :Thumbprint: ``Строка`` Отпечаток сертификата
  :Pin:        ``Строка`` Пин-код или пароль от контейнера сертификата

  Возвращает :doc:`объект логического соединения <Connection>`, созданного по сертификату с указанным отпечатком.
  Поиск сертификата происходит в хранилище `Личное` пользователя и, если там сертиифкат не найден - в хранилище `Личное` машины.
  Если *Pin* не задан, то будет использоваться пин-код/пароль, запомненный в крипто-провайдере или пустая строка



.. _DiadocAPI-CreateConnectionByLogin:
.. method:: DiadocAPI.CreateConnectionByLogin(Login, Password)

  :Login:    ``Строка`` Логин пользователя
  :Password: ``Строка`` Пароль пользователя

  Возвращает :doc:`объект логического соединения <Connection>`, созданного по логину и паролю



.. _DiadocAPI-GetPersonalCertificates:
.. method:: DiadocAPI.GetPersonalCertificates(UserStore=true)

  :UsePersonalStore: ``Булево`` Поиск производится в хранилище пользователя

  Возвращает :doc:`коллекцию <Collection>` :doc:`сертификатов <PersonalCertificate>`, установленных в хранилище `Личное <https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores>`_. Поиск может производиться в хранилище пользователя или машины



.. _DiadocAPI-GetVersion:
.. method:: DiadocAPI.GetVersion()

  Возвращает строку с версией используемой компоненты



.. _DiadocAPI-GetFullVersion:
  .. method:: DiadocAPI.GetFullVersion()

    Возвращает строку с версией используемой компоненты в формате ``[AddIn|COM] [x86|x64] <номер сборки>``

  .. versionadded:: 5.29.4


.. _DiadocAPI-TestConnection:
.. method:: DiadocAPI.TestConnection()

  Проверяет возможность соединения с сервером Диадока, используя установленные параметры. Возвращает булево значение

  .. deprecated:: 5.26.3
      Используйте :meth:`.TestConnection2`



.. _DiadocAPI-TestConnection2:
.. method:: DiadocAPI.TestConnection2()

  Возвращает :doc:`объект с результатами проверки соединения <TestConnectionResult>` с сервером Диадока, используя установленные параметры

  .. versionadded:: 5.26.3



.. _DiadocAPI-VerifyThatUserHasAccessToAnyBox:
.. method:: DiadocAPI.VerifyThatUserHasAccessToAnyBox(Thumbprint)

  :Thumbprint: ``Строка`` Отпечаток сертификата

  Возвращает булевый признак, означающий есть ли у пользователя с указанным сертификатом доступ к какой-либо организации в Диадок.



.. rubric:: Дополнительная информация

==================== ================================================================
Значение *ProxyMode* Описание
==================== ================================================================
NoProxy              не использовать прокси-сервер при подключении
UseProxy             использовать настройки прокси-сервера, указанные в ProxySettings
UseDefaultProxy      использовать прокси-сервер по умолчанию
==================== ================================================================
