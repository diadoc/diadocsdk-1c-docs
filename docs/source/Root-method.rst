Объект интерфейса Диадок
========================

Объект DiadocInvoiceAPI предназначен для:

-  управления параметрами подключения к серверу Диадок;
-  авторизации на сервере Диадок.

Свойства объекта
----------------

- **ApiClientId** (cтрока, чтение/запись) - текущий ключ разработчика
- **ServerUrl** (строкаб чтение/запись) - текущий URL сервера Диадок 
- **ProxySettings** (объект :doc:`ProxySettings <ProxySettings>`, чтение) - текущие настройки прокси-сервера 
- **ProxyMode** (строка, чтение/запись) - текущий режим использования прокси-сервера.

Свойство **ProxyMode** принимает одно из
следующих значений:

-  "NoProxy" - не использовать прокси-сервер при подключении
-  "UseProxy" - при подключении использовать настройки прокси-сервера,
   указанные в ProxySettings
-  "UseDefaultProxy" - при подключении использовать прокси-сервер по
   умолчанию

Методы объекта
--------------


-  :doc:`TestConnection <TestConnection>` - проверяет возможность соединения с сервером Диадока, используя установленные параметры

-  :doc:`GetVersion <GetVersion>` - возвращает текущую версию внешней компоненты

-  :doc:`GetPersonalCertificates <GetPersonalCertificates>` - возвращает список личных серитифакатов пользователя

-  :doc:`VerifyThatUserHasAccessToAnyBox <VerifyThatUserHasAccessToAnyBox>` - проверяет, есть ли у пользователя с указанным сертификатом доступ в Диадок

-  :doc:`CreateConnectionByLogin <CreateConnectionByLogin>` - производит авторизацию и создание логического соединения по логину и паролю пользователя

-  :doc:`CreateConnectionByCertificate <CreateConnectionByCertificate>` - производит авторизацию и создание логического соединения по сертификату с указанным отпечатком



"Ключ разработчика" используется для идентификации интегратора,
использующего внешнюю компоненту. Для получения ключа разработчика нужно
написать запрос по адресу diadoc-api@skbkontur.ru. Интегратор не должен
передавать свой "ключ разработчика" третьим лицам.

В качестве URL сервера Диадок необходимо передавать строку
"https://diadoc-api.kontur.ru:443"

.. toctree::
   :name: Auto
   :hidden:

   TestConnection <TestConnection>
   GetVersion <GetVersion>
   GetPersonalCertificates <GetPersonalCertificates>
   VerifyThatUserHasAccessToAnyBox <VerifyThatUserHasAccessToAnyBox>
   CreateConnectionByLogin <CreateConnectionByLogin>
   CreateConnectionByCertificate <CreateConnectionByCertificate>
