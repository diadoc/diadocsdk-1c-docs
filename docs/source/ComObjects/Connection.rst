Connection
==========

Логическое соединение с сервером Диадока


.. rubric:: Свойства


:SessionInfo:
  :doc:`SessionInfo` **, чтение** - информация о сессии


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


.. rubric:: Устаревшие поля и методы

+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| **Метод**                               | **Когда устарел**                     | **Когда удалён**                      | **Рекомендуемая альтернатива**                       |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| **Connection.Login**                    | :doc:`../History/release_info/5_37_0` |                                       | **Connection.SessionInfo.Login**                     |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| **Connection.AuthenticateType**         | :doc:`../History/release_info/5_37_0` |                                       | **Connection.SessionInfo.AuthenticationType**        |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| **Connection.Certificate**              | :doc:`../History/release_info/5_37_0` |                                       | **Connection.SessionInfo.Certificate**               |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| **Connection.Token**                    | :doc:`../History/release_info/5_37_0` |                                       | **Connection.SessionInfo.Token**                     |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| :meth:`Connection.CreateCloudSignTask`  | :doc:`../History/release_info/5_26_0` | :doc:`../History/release_info/5_33_0` |                                                      |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+
| :meth:`Connection.GetCloudCertificates` | :doc:`../History/release_info/5_26_0` | :doc:`../History/release_info/5_33_0` |                                                      |
+-----------------------------------------+---------------------------------------+---------------------------------------+------------------------------------------------------+


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
