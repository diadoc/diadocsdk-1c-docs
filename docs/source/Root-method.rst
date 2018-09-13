Объект интерфейса Диадок
========================


Объект DiadocInvoiceAPI предназначен для:

-  управления параметрами подключения к серверу Диадок;
-  авторизации на сервере Диадок.


Свойства объекта
----------------

- **ApiClientId** (cтрока, чтение/запись) - текущий ключ разработчика
- **ServerUrl** (строка, чтение/запись) - текущий URL сервера Диадок 
- **ProxySettings** (:doc:`ProxySettings <ProxySettings>`, чтение) - текущие настройки прокси-сервера 
- **ProxyMode** (строка, чтение/запись) - текущий режим использования прокси-сервера.

Свойство **ProxyMode** принимает одно из следующих значений:
-  "NoProxy" - не использовать прокси-сервер при подключении
-  "UseProxy" - при подключении использовать настройки прокси-сервера, указанные в ProxySettings
-  "UseDefaultProxy" - при подключении использовать прокси-сервер по умолчанию


Методы объекта
--------------

-  :doc:`TestConnection <TestConnection>` - проверяет возможность соединения с сервером Диадока, используя установленные параметры

-  :doc:`GetVersion <GetVersion>` - возвращает текущую версию внешней компоненты

-  :doc:`GetPersonalCertificates <GetPersonalCertificates>` - возвращает :doc:`коллекцию <Collection>` объектов :doc:`PersonalCertificate <PersonalCertificate>`

-  :doc:`VerifyThatUserHasAccessToAnyBox <VerifyThatUserHasAccessToAnyBox>` - проверяет, есть ли у пользователя с указанным сертификатом доступ в Диадок

-  :doc:`CreateConnectionByLogin <CreateConnectionByLogin>` - возвращает :doc:`объект логического соединения <Connection>`, созданного по логину и паролю

-  :doc:`CreateConnectionByCertificate <CreateConnectionByCertificate>` - возвращает :doc:`объект логического соединения <Connection>`, созданного по сертификату с указанным отпечатком


"Ключ разработчика" используется для идентификации интегратора, использующего внешнюю компоненту. Для получения ключа разработчика нужно отправить запрос через форму https://www.diadoc.ru/integrations/api#order-api. Интегратор не должен передавать свой "ключ разработчика" третьим лицам.


В качестве URL сервера Диадок необходимо передавать строку
"https://diadoc-api.kontur.ru:443"

.. toctree::
   :name: Auto
   :hidden:

   ProxySettings <ProxySettings>
   TestConnection <TestConnection>
   GetVersion <GetVersion>
   GetPersonalCertificates <GetPersonalCertificates>
   VerifyThatUserHasAccessToAnyBox <VerifyThatUserHasAccessToAnyBox>
   CreateConnectionByLogin <CreateConnectionByLogin>
   CreateConnectionByCertificate <CreateConnectionByCertificate>
