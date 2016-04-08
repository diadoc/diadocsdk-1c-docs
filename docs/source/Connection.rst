Соединение
==========

Объект DiadocConnection предназначен для управления логическим
соединением с сервером Диадока.

Свойства объекта
----------------


- **Login** (строка, чтение ) - имя пользователя, по которому произошла авторизация

- **AuthenticateType** (строка, чтение ) - способ аутентификации

- **Certificate** (объект :doc:`PersonalCertificate <PersonalCertificate>`, чтение ) - сертификат, по которому произошла авторизация


Свойство AuthenticateType принимает одно из следующих значений:

-  "Login" - возвращается в случае, когда при подключении к серверу
   Диадока использовались логин и пароль
-  "Certificate" - возвращается в случае, когда при подключении к
   серверу Диадока использовался сертификат

Методы объекта
--------------


-  :doc:`GetOrganizationList <GetOrganizationList>` - возвращает список организаций, к которым текущий пользователь имеет доступ

-  :doc:`GetOrganizationById <GetOrganizationById>` - возвращает организацию, к которой текущий пользователь имеет доступ, по идентификатору организации

-  :doc:`CreateCloudSignTask <CreateCloudSignTask>` - возвращает объект, с помощью которого можно подписать документы облачной подписью

-  :doc:`GetCloudCertificates <GetCloudCertificates>` - возвращает список облачных сертификатов, которые доступны
  текущему пользователю. Доступны только в случае, если соединение выполнено по логину и паролю.

-  :doc:`GetMyUser <GetMyUser>` - возвращает объект, содержащий информацию о текущем авторизованном пользователе


Объект можно получить, вызвав метод
:doc:`CreateConnectionByLogin <CreateConnectionByLogin>` (авторизация по
логину и паролю пользователя), либо вызвав метод
:doc:`CreateConnectionByCertificate <CreateConnectionByCertificate>`
(авторизация по сертификату с указанным отпечатком) `объекта интерфейса
:doc:«Диадок» <Root-method>`.

.. toctree::
   :name: Auto
   :hidden:

   GetOrganizationList <GetOrganizationList>
   GetOrganizationById <GetOrganizationById>
   CreateCloudSignTask <CreateCloudSignTask>
   GetCloudCertificates <GetCloudCertificates>
   GetMyUser <GetMyUser>

