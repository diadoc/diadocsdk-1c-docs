Организация
===========

Объект Organization предназначен для работы с организацией на сервере Диадок. Позволяет:

-  Работать со списком контрагентов. С помощью метода
   :doc:`GetCounteragentListByStatus <GetCounteragentListByStatus>` можно
   получить список контрагентов, с которыми установлены взаимоотношения
   в Диадоке. С помощью методов
   :doc:`GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>`,
   :doc:`GetCounteragentListByInnList <GetCounteragentListByInnList>` можно
   найти контрагента (контрагентов) по ИНН.
-  Получать список документов организации с помощью метода
   :doc:`GetDocumentsTask <GetDocumentsTask>`.
-  Подписывать и отправлять документы через Диадок с помощью методов
   :doc:`CreateSendTask <CreateSendTask>`,
   :doc:`CreateSendTaskFromFile <CreateSendTaskFromFile>`.


Свойства объекта
----------------

- **Id** (строка, чтение) - идентификатор организации в Диадоке

- **Name** (строка, чтение) - наименование организации

- **Inn** (строка, чтение) - ИНН организации

- **Kpp** (строка, чтение) - КПП организации

- **Departments** (:doc:`коллекция <Collection>` объектов :doc:`Department <Department>`, чтение) - подразделения, родительским подразделением которых является "Головное" подразделение

- **AuthenticateType** (строка, чтение) - тип авторизации

- **Login** (строка, чтение) - логин, по которому произошла авторизация к данной организации

- **Certificate** (:doc:`PersonalCertificate <PersonalCertificate>`, чтение) - сертификат, по которому произошла авторизация к данной организации

- **FnsParticipantId** (строка, чтение) - идентификатор организации-участника документооборота

- **FnsRegistrationDate** (дата, чтение) - дата подачи заявляения в ФНС на регистрацию данной организации в качестве участника документооборота ЭСФ. В случае, если организация не подавала заявления, возвращается пустая дата

- **IsTest** (булево, чтение) - признак того, что организация работает в тестовом режиме

- **IsPilot** (булево, чтение) - признак того, что организация работает в пилотном режиме

- **EncryptedDocumentsAllowed** (булево, чтение) - признак того, что для организации разрешена отправка зашифрованных документов


Методы объекта
--------------

-  :doc:`GetCounteragentListByStatus <GetCounteragentListByStatus>` - возвращает контрагентов, с которыми у организации установлены отношения

-  :doc:`GetCounteragentListByStatusAsync <GetCounteragentListByStatusAsync>` - асинхронный запрос контрагентов, с которыми у организации установлены отношения

-  :doc:`GetCounteragentById <GetCounteragentById>` - возвращает контрагента по его идентификатору

-  :doc:`GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>` - Возвращает список ящиков организаций, у которых ИНН и КПП совпадают с заданными.

-  :doc:`GetCounteragentListByInnList <GetCounteragentListByInnList>` - инициирует асинхронную операцию получения списка контрагентов по списку ИНН

-  :doc:`GetDocumentById <GetDocumentById>` - возвращает документ в ящике по его идентификатору

-  :doc:`GetDocumentsTask <GetDocumentsTask>` - возвращает объект, который позволяет позволяет получить список документов, отправленных из выбранного ящика или пришедших в него

-  :doc:`CreateSendTask <CreateSendTask>` - позволяет создать задание для отправки формализованного документа на сервер Диадок

-  :doc:`CreateSendTaskFromFile <CreateSendTaskFromFile>` - позволяет получить задание для отправки документа, загруженного из файла

-  :doc:`CreateSendTaskFromFileRaw <CreateSendTaskFromFileRaw>` - позволяет получить задание для отправки документа, загруженного из файла (без парсинга)

-  :doc:`GetUsers <GetUsers>` - вовзращает список всех пользователей организации

-  :doc:`GetUserPermissions <GetUserPermissions>` - возвращает описание прав пользователя, в контексте которого произошла авторизация, для данной организации

-  :doc:`GetDocumentEventList <GetDocumentEventList>` - возвращает список событий

-  :doc:`GetReceiptGenerationProcess <GetReceiptGenerationProcess>` - возвращает объект, с помощью которого можно запустить процесс автоматического формирования документов по регламентному документообороту счетов-фактур

-  :doc:`SendFnsRegistrationMessage <SendFnsRegistrationMessage>` - добавление в сообщение ФНС нового сертификата

-  :doc:`SendDraftAsync <SendDraftAsync>` - инициирует асинхронную операцию отправки черновика по его уникальному идентификатору

-  :doc:`CreateAcquireCounteragentTask <CreateAcquireCounteragentTask>` - создает запрос на приглашение контрагента к сотрудничеству

-  :doc:`CreatePackageSendTask <CreatePackageSendTask>` - создает задание на отправку пакета документов

-  :doc:`CreateSetExtendedSignerDetailsTask <CreateSetExtendedSignerDetailsTask>` - создает задание на добавление или обновление данных подписанта в базе Диадок

-  :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>` - возвращает данные подписанта из базы Диадок

-  :doc:`GetExtendedSignerDetails2 <GetExtendedSignerDetails2>` - возвращает данные подписанта из базы Диадок 

-  :doc:`SetData <SetData>` - добавляет пару "ключ-значение" в хранилище

-  :doc:`GetData <GetData>` - извлекает пару "ключ-значение" из хранилища по ее ключу

-  :doc:`GetSentDocuments <GetSentDocuments>` - возвращает список идентификаторов отправленных документов

-  :doc:`GetAddressForCounteragent <GetAddressForCounteragent>` - возвращает адресную информацию :doc:`AddressInfo <AddressInfo>` из хранилища

-  :doc:`SetAndValidateAddressForCounteragent <SetAndValidateAddressForCounteragent>` - валидирует и загружает адресную информацию в хранилище

-  :doc:`CanSendInvoice <CanSendInvoice>` - определяет может ли указанный сертификат ЭП использоваться для подписания ЭСФ

-  :doc:`CreateSendDraftTask <CreateSendDraftTask>` - создает задание на отправку черновика документа

-  :doc:`GetCounteragentByOrgId <GetCounteragentByOrgId>` - возвращает контрагента по идентификатору организации

-  :doc:`GetDocumentTypes <GetDocumentTypes>` - возвращает описание типов документов, доступных в ящике.

.. toctree::
   :name: Auto
   :hidden:

   GetCounteragentListByStatus <GetCounteragentListByStatus>
   GetCounteragentListByStatusAsync <GetCounteragentListByStatusAsync>
   GetCounteragentById <GetCounteragentById>
   GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>
   GetCounteragentListByInnList <GetCounteragentListByInnList>
   GetDocumentById <GetDocumentById>
   GetDocumentsTask <GetDocumentsTask>
   CreateSendTask <CreateSendTask>
   CreateSendTaskFromFile <CreateSendTaskFromFile>
   CreateSendTaskFromFileRaw <CreateSendTaskFromFileRaw>
   GetUsers <GetUsers>
   GetUserPermissions <GetUserPermissions>
   GetDocumentEventList <GetDocumentEventList>
   GetReceiptGenerationProcess <GetReceiptGenerationProcess>
   AddCertToFnsRegistrationMessage <AddCertToFnsRegistrationMessage>
   SendFnsRegistrationMessage <SendFnsRegistrationMessage>
   SendDraftAsync <SendDraftAsync>
   CreateAcquireCounteragentTask <CreateAcquireCounteragentTask>
   CreatePackageSendTask <CreatePackageSendTask>
   CreateSetExtendedSignerDetailsTask <CreateSetExtendedSignerDetailsTask>
   GetExtendedSignerDetails <GetExtendedSignerDetails>
   GetExtendedSignerDetails2 <GetExtendedSignerDetails2>
   SetData <SetData>
   GetData <GetData>
   GetSentDocuments <GetSentDocuments>
   GetAddressForCounteragent <GetAddressForCounteragent>
   SetAndValidateAddressForCounteragent <SetAndValidateAddressForCounteragent>
   CanSendInvoice <CanSendInvoice>
   CreateSendDraftTask <CreateSendDraftTask>
   GetCounteragentByOrgId <GetCounteragentByOrgId>
   GetDocumentTypes <GetDocumentTypes>