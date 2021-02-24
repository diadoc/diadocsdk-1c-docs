Connection
==========

Логическое соединение с сервером Диадока


.. rubric:: Свойства

:Login:
  **Строка, чтение** - имя пользователя, по которому произошла авторизация

:AuthenticateType:
  **Строка, чтение** - способ аутентификации. :doc:`Возможные значения <./Enums/AuthenticateType>`

:Certificate:
  :doc:`PersonalCertificate` **, чтение** - сертификат, по которому произошла авторизация

:Token:
  **Строка, чтение** - авторизационный токен текущей сессии


.. rubric:: Методы

+-----------------------------------+
| |Connection-GetOrganizationList|_ |
+-----------------------------------+
| |Connection-GetOrganizationById|_ |
+-----------------------------------+
| |Connection-GetMyUser|_           |
+-----------------------------------+


.. |Connection-GetOrganizationList| replace:: GetOrganizationList()
.. |Connection-GetOrganizationById| replace:: GetOrganizationById()
.. |Connection-GetMyUser| replace:: GetMyUser()


.. _Connection-GetOrganizationList:
.. method:: Connection.GetOrganizationList()

  Возвращает :doc:`коллекцию <Collection>` :doc:`организаций <Organization>`, к которым текущий пользователь имеет доступ



.. _Connection-GetOrganizationById:
.. method:: Connection.GetOrganizationById(BoxID)

  :BoxID: ``строка`` идентификатор ящика организации

  Возвращает :doc:`организацию <Organization>`, к которой текущий пользователь имеет доступ



.. _Connection-GetMyUser:
.. method:: Connection.GetMyUser()

  Возвращает :doc:`информацию <User>` об авторизованном пользователе

  .. versionadded:: 5.6.0



.. seealso:: :doc:`../HowTo/HowTo_auth`


.. rubric:: Устаревшие методы


.. method:: Connection.CreateCloudSignTask(Thumbprint)

  :Thumbprint: ``строка`` отпечаток Контур.Сертификата

  Возвращает :doc:`объект <CloudSignTask>`, с помощью которого можно подписать документы Контур.Сертификатом

  .. versionadded:: 5.2.0

  .. versionchanged:: 5.33.0
    Метод удалён


.. method:: Connection.GetCloudCertificates()

  Возвращает :doc:`коллекцию <Collection>` :doc:`Контур.Сертификатов <CloudCertificateInfo>`, доступных текущему пользователю

  .. versionadded:: 5.2.0

  .. versionchanged:: 5.33.0
    Метод удалён
