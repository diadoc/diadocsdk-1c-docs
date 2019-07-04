Organization
============

Объект предназначен для работы с организацией на сервере Диадок


.. rubric:: Свойства объекта

:Id: (строка, чтение) - идентификатор ящика организации в Диадоке
:Name: (строка, чтение) - наименование организации
:Inn: (строка, чтение) - ИНН организации
:Kpp: (строка, чтение) - КПП организации
:Departments: (:doc:`коллекция <Collection>` объектов :doc:`Department <Department>`, чтение) - подразделения, родительским подразделением которых является "Головное" подразделение
:AuthenticateType: (строка, чтение) - тип авторизации
:Login: (строка, чтение) - логин, по которому произошла авторизация к данной организации
:Certificate: (:doc:`PersonalCertificate <PersonalCertificate>`, чтение) - сертификат, по которому произошла авторизация в данной организации
:FnsParticipantId: (строка, чтение) - идентификатор организации-участника документооборота
:FnsRegistrationDate: (дата, чтение) - дата подачи заявляения в ФНС на регистрацию данной организации в качестве участника документооборота ЭСФ. В случае, если организация не подавала заявления, возвращается пустая дата
:IsTest: (булево, чтение) - признак того, что организация работает в тестовом режиме
:IsPilot: (булево, чтение) - признак того, что организация работает в пилотном режиме
:EncryptedDocumentsAllowed: (булево, чтение) - признак того, что для организации разрешена отправка зашифрованных документов


.. rubric:: Методы объекта

* :doc:`GetUsers <GetUsers>` - вовзращает :doc:`список <Collection>` всех :doc:`пользователей <User>` организации
* :doc:`GetUserPermissions <GetUserPermissions>` - возвращает :doc:`описание прав пользователя <UserPermissions>`, в контексте которого произошла авторизация, для данной организации

.. function:: Organization.GetCounteragentById

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Сделано ради теста. Надо доделать
возвращает :doc:`контрагента <Counteragent>` по идентификатору ящика


* :doc:`GetCounteragentByOrgId <GetCounteragentByOrgId>` - возвращает :doc:`контрагента <Counteragent>` по идентификатору организации
* :doc:`GetCounteragentListByStatus <GetCounteragentListByStatus>` - возвращает :doc:`список <Collection>` :doc:`контрагентов <Counteragent>`, с указанным в запросе статусом
* :doc:`GetCounteragentListByStatusAsync <GetCounteragentListByStatusAsync>` - асинхронный запрос :doc:`списка <Collection>` :doc:`контрагентов <CounteragentItem>`, с указанным в запросе статусом
* :doc:`GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>` - возвращает :doc:`список <Collection>` :doc:`контрагентов <Counteragent>` с указанными ИНН/КПП
* :doc:`GetCounteragentListByInnList <GetCounteragentListByInnList>` - асинхронный запрос :doc:`списка <Collection>` :doc:`контрагентов <CounteragentItem>` с указанными ИНН
* :doc:`CreateAcquireCounteragentTask <CreateAcquireCounteragentTask>` - создает :doc:`запрос на приглашение контрагента к сотрудничеству <AcquireCounteragentTask>`

* :doc:`GetDocumentById <GetDocumentById>` - возвращает :doc:`документ <Document>` в ящике по его идентификатору
* :doc:`GetDocumentsTask <GetDocumentsTask>` - возвращает :doc:`объект <DocumentsTask>`, который позволяет позволяет получить :doc:`список <Collection>` исходящих и отправленных :doc:`документов <Document>` текущего ящика
* :doc:`RestoreDocument <RestoreDocument>` - восстанавливает удалённый документ

* :doc:`GetReceiptGenerationProcess <GetReceiptGenerationProcess>` - возвращает :doc:`объект <ReceiptGenerationProcess>`, с помощью которого можно запустить процесс автоматической отправки извещений о получении документов в текущем ящике
* :doc:`GetDocumentEventList <GetDocumentEventList>` - возвращает :doc:`список <Collection>` :doc:`событий <DocumentEvent>`, произошедших с документами в текущем ящике

* :doc:`CreatePackageSendTask <CreatePackageSendTask>` - возвращает :doc:`объект <PackageSendTask>`, с помощью которого можно отправить пакет :doc:`документов <DocumentToSend>`
* :doc:`CreatePackageSendTask2 <CreatePackageSendTask2>` - возвращает :doc:`объект <PackageSendTask2>`, с помощью которого можно отправить пакет :doc:`документов <CustomDocumentToSend>`
* :doc:`CreateSendDraftTask <CreateSendDraftTask>` - возвращает :doc:`объект <SendDraftTask>`, с помощью которого можно отправить черновик
* :doc:`SendDraftAsync <SendDraftAsync>` - асинхронный запрос отправки черновика

* :doc:`SetAndValidateAddressForCounteragent <SetAndValidateAddressForCounteragent>` - валидирует и загружает адресную информацию в хранилище
* :doc:`GetAddressForCounteragent <GetAddressForCounteragent>` - возвращает :doc:`адресную информацию <AddressInfo>` из хранилища
* :doc:`GetSentDocuments <GetSentDocuments>` - возвращает список идентификаторов отправленных документов
* :doc:`SetData <SetData>` - добавляет пару "ключ-значение" в хранилище
* :doc:`GetData <GetData>` - извлекает значение по ключу из хранилища

* :doc:`CreateSetExtendedSignerDetailsTask <CreateSetExtendedSignerDetailsTask>` - возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта в Диадоке
* :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>` - возвращает :doc:`данные подписанта <ExtendedSignerDetails>` из базы Диадок
* :doc:`GetExtendedSignerDetails2 <GetExtendedSignerDetails2>` - возвращает :doc:`данные подписанта <ExtendedSignerDetails>` из базы Диадок

* :doc:`SendFnsRegistrationMessage <SendFnsRegistrationMessage>` - добавление в сообщение ФНС нового сертификата
* :doc:`CanSendInvoice <CanSendInvoice>` - определяет может ли указанный сертификат ЭП использоваться для подписания формализованных документов
* :doc:`GetDocumentTypes <GetDocumentTypes>` - возвращает :doc:`коллекцию <Collection>` :doc:`типов документов <DocumentTypeDescription>`, доступных в ящике для отправки
* :doc:`GetResolutionRoutes <GetResolutionRoutes>` - возвращает :doc:`коллекцию <Collection>` :doc:`маршрутов согласования <Route>`, настроенных в ящике

* :doc:`CreateTemplateSendTask <CreateTemplateSendTask>` - возвращает :doc:`объект <TemplateSendTask>`, с помощью которого можно отправить :doc:`шаблон пакета документов <Template>`
* :doc:`GetTemplate <GetTemplate>` - возвращает :doc:`шаблон <Template>` по его идентификатору
* :doc:`CreateTransformTemplateTask` - возвращает :doc:`объект <TransformTemplateTask>`, с помощью которого можно из шаблона создать :doc:`документы <DocumentPackage>`

* :doc:`RecycleDraft <RecycleDraft>` - удаляет черновик

* :doc:`SaveUserDataXSD <SaveUserDataXSD>` - сохраняет описание контента документа на диск
