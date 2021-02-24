Organization
============

Организация на сервере Диадок


.. rubric:: Свойства

:Name:
  **Строка, чтение** - наименование организации

:Inn:
  **Строка, чтение** - ИНН организации

:Kpp:
  **Строка, чтение** - КПП организации

:Departments:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Department` **, чтение** - подразделения, родительским подразделением которых является "Головное" подразделение

:FnsParticipantId:
  **Строка, чтение** - идентификатор организации-участника документооборота

:FnsRegistrationDate:
  **Дата, чтение** - дата подачи заявляения в ФНС на регистрацию данной организации в качестве участника документооборота ЭСФ

:Guid:
  **Строка, чтение** - идентификатор ящика организации в Диадоке

  .. versionadded:: 5.31.0

:IsTest:
  **Булево, чтение** - организация работает в тестовом режиме

:IsPilot:
  **Булево, чтение** - организация работает в пилотном режиме

:IsLiquidated:
  **Булево, чтение** - организация ликвидирована

  .. versionadded:: 5.31.0

:AuthenticateType:
  **Строка, чтение** - тип авторизации

:Login:
  **Строка, чтение** - логин, по которому произошла авторизация к данной организации

:Certificate:
  :doc:`PersonalCertificate` **, чтение** - сертификат, по которому произошла авторизация в данной организации



.. rubric:: Методы

+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-GetDocumentById|_             | |Organization-GetCounteragentById|_              | |Organization-GetDocumentTypes|_           | |Organization-GetUserPermissions|_                 |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-GetDocumentsTask|_            | |Organization-GetCounteragentByOrgId|_           | |Organization-GetFeatures|_                | |Organization-CanSendInvoice|_                     |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-CreatePackageSendTask2|_      | |Organization-GetCounteragentListByStatus|_      | |Organization-GetUsers|_                   | |Organization-GetExtendedSignerDetails2|_          |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-GetReceiptGenerationProcess|_ | |Organization-GetCounteragentListByStatusAsync|_ | |Organization-GetResolutionRoutes|_        | |Organization-CreateSetExtendedSignerDetailsTask|_ |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-SaveUserDataXSD|_             | |Organization-GetCounteragentListByInnKpp|_      | |Organization-SendFnsRegistrationMessage|_ |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-GetBase64UserDataXSD|_        | |Organization-GetCounteragentListByInnKppAsync|_ | |Organization-CreateDataTask|_             |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-RestoreDocument|_             | |Organization-GetCounteragentListByInnList|_     |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-CreateSendDraftTask|_         | |Organization-CreateAcquireCounteragentTask|_    |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-RecycleDraft|_                |                                                  |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-GetDocumentEventList|_        |                                                  |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-GetTemplate|_                 |                                                  |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-CreateTemplateSendTask|_      |                                                  |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+
| |Organization-CreateTransformTemplateTask|_ |                                                  |                                            |                                                    |
+---------------------------------------------+--------------------------------------------------+--------------------------------------------+----------------------------------------------------+


.. |Organization-GetDocumentById| replace:: GetDocumentById()
.. |Organization-GetDocumentsTask| replace:: GetDocumentsTask()
.. |Organization-CreatePackageSendTask2| replace:: CreatePackageSendTask2()
.. |Organization-GetReceiptGenerationProcess| replace:: GetReceiptGenerationProcess()
.. |Organization-SaveUserDataXSD| replace:: SaveUserDataXSD()
.. |Organization-GetBase64UserDataXSD| replace:: GetBase64UserDataXSD()
.. |Organization-RestoreDocument| replace:: RestoreDocument()
.. |Organization-CreateSendDraftTask| replace:: CreateSendDraftTask()
.. |Organization-RecycleDraft| replace:: RecycleDraft()
.. |Organization-GetDocumentEventList| replace:: GetDocumentEventList()
.. |Organization-GetTemplate| replace:: GetTemplate()
.. |Organization-CreateTemplateSendTask| replace:: CreateTemplateSendTask()
.. |Organization-CreateTransformTemplateTask| replace:: CreateTransformTemplateTask()

.. |Organization-GetCounteragentById| replace:: GetCounteragentById()
.. |Organization-GetCounteragentByOrgId| replace:: GetCounteragentByOrgId()
.. |Organization-GetCounteragentListByStatus| replace:: GetCounteragentListByStatus()
.. |Organization-GetCounteragentListByStatusAsync| replace:: GetCounteragentListByStatusAsync()
.. |Organization-GetCounteragentListByInnKpp| replace:: GetCounteragentListByInnKpp()
.. |Organization-GetCounteragentListByInnKppAsync| replace:: GetCounteragentListByInnKppAsync()
.. |Organization-GetCounteragentListByInnList| replace:: GetCounteragentListByInnList()
.. |Organization-CreateAcquireCounteragentTask| replace:: CreateAcquireCounteragentTask()

.. |Organization-GetDocumentTypes| replace:: GetDocumentTypes()
.. |Organization-GetFeatures| replace:: GetFeatures()
.. |Organization-GetUsers| replace:: GetUsers()
.. |Organization-GetResolutionRoutes| replace:: GetResolutionRoutes()
.. |Organization-SendFnsRegistrationMessage| replace:: SendFnsRegistrationMessage()
.. |Organization-CreateDataTask| replace:: CreateDataTask()

.. |Organization-GetUserPermissions| replace:: GetUserPermissions()
.. |Organization-CanSendInvoice| replace:: CanSendInvoice()
.. |Organization-GetExtendedSignerDetails2| replace:: GetExtendedSignerDetails2()
.. |Organization-CreateSetExtendedSignerDetailsTask| replace:: CreateSetExtendedSignerDetailsTask()


.. _Organization-GetDocumentById:
.. method:: Organization.GetDocumentById(DocumentId, WithExternalId=FALSE)

  :DocumentId: ``строка`` идентифкатор документа
  :WithExternalId: ``булево`` нужно ли запрашивать дополнительный идентификатор учётной системы

  Возвращает :doc:`документ <Document>` в ящике по его идентификатору.
  При *WithExternalId* == ``TRUE`` у документа будет заполнено поле *OneSDocumentId*, если оно установлено для него, но сам метод отработает медленнее



.. _Organization-GetDocumentsTask:
.. method:: Organization.GetDocumentsTask()

  Возвращает :doc:`объект <DocumentsTask>` для поиска документов в ящике



.. _Organization-CreatePackageSendTask2:
.. method:: Organization.CreatePackageSendTask2()

  Возвращает :doc:`объект <PackageSendTask2>`, с помощью которого можно отправить :doc:`документы <CustomDocumentToSend>`

  .. versionadded:: 5.27.0



.. _Organization-GetReceiptGenerationProcess:
.. method:: Organization.GetReceiptGenerationProcess()

  Возвращает :doc:`объект <ReceiptGenerationProcess>`, с помощью которого можно запустить процесс автоматической отправки извещений о получении документов в текущем ящике



.. _Organization-SaveUserDataXSD:
.. method:: Organization.SaveUserDataXSD(TitleName, Function, Version, DocflowSide, FilePath)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа
  :DocflowSide: ``строка`` сторона документооборота. :doc:`Возможные значения <Enums/DocflowSide>`
  :FilePath: ``строка`` полное имя файла, в который нужно сохранить описание контента

  Сохраняет описание представления контента документа на диск.
  Значения для *TitleName*, *Function*, *Version* можно получить в ответе метода :meth:`Organization.GetDocumentTypes`

  .. versionadded:: 5.27.0



.. _Organization-GetBase64UserDataXSD:
.. method:: Organization.GetBase64UserDataXSD(TitleName, Function, Version, DocflowSide)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа
  :DocflowSide: ``строка`` сторона документооборота. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает ``Base64-строку`` описания представления контента документа.
  Значения для *TitleName*, *Function*, *Version* можно получить в ответе метода :meth:`Organization.GetDocumentTypes`

  .. versionadded:: 5.28.3



.. _Organization-RestoreDocument:
.. method:: Organization.RestoreDocument(DocumentId)

  :DocumentId: ``строка`` идентификатор документа

  Восстанавливает удалённый документ



.. _Organization-CreateSendDraftTask:
.. method:: Organization.CreateSendDraftTask(MessageId)

  :MessageId: ``строка`` идентификатор сообщения черновика

  Создаёт :doc:`объект <SendDraftTask>`, с помощью которого можно отправить черновик.
  *MessageId* - первая половина из *DocumentId* черновика

  .. versionadded:: 5.18.0



.. _Organization-RecycleDraft:
.. method:: Organization.RecycleDraft(MessageId)

  :MessageId: ``строка`` идентификатор сообщения черновика

  Метод удаляет черновик. Восстановить черновик невозможно.
  *MessageId* - первая половина из *DocumentId* черновика

  .. versionadded:: 5.25.0


.. _Organization-GetDocumentEventList:
.. method:: Organization.GetDocumentEventList([AfterEventId])

  :AfterEventId: ``строка`` Идентификатор события, после которого будет вычитываться лента событий

  Возвращает :doc:`список <Collection>` :doc:`событий <DocumentEvent>`, произошедших с документами в текущем ящике.
  Если *AfterEventId* не задан или пустой, то события начнут вычитываться с момента создания ящика Диадок



.. _Organization-GetTemplate:
.. method:: Organization.GetTemplate(TemplateId)

  :TemplateId: ``строка`` идентификатор шаблона

  Возвращает :doc:`шаблон документа <Template>` по его идентификатору

  .. versionadded:: 5.24.0



.. _Organization-CreateTemplateSendTask:
.. method:: Organization.CreateTemplateSendTask()

  Возвращает :doc:`объект <TemplateSendTask>`, с помощью которого можно отправить :doc:`шаблон документ <TemplateToSend>`

  .. versionadded:: 5.24.0



.. _Organization-CreateTransformTemplateTask:
.. method:: Organization.CreateTransformTemplateTask(TemplateId)

  :TemplateId: ``строка`` идентификатор шаблона

  Возвращает :doc:`задание для создания документов из шаблона <TransformTemplateTask>`

  .. versionadded:: 5.24.0



.. _Organization-GetCounteragentById:
.. method:: Organization.GetCounteragentById(BoxId)

  :BoxId: ``строка`` идентификатор ящика

  Возвращает :doc:`контрагента <Counteragent>` по идентификатору ящика.
  Идентификатор может быть как в виде GUID, так и в виде ``...@diadoc.ru``



.. _Organization-GetCounteragentByOrgId:
.. method:: Organization.GetCounteragentByOrgId(OrganizationId)

  :OrganizationId: ``строка`` идентификатор организации в Диадок

  Возвращает :doc:`контрагента <Counteragent>` по идентификатору организации



.. _Organization-GetCounteragentListByStatus:
.. method:: Organization.GetCounteragentListByStatus([CounteragentStatus])

  :CounteragentStatus: ``строка`` статус, по которому производится выборка контрагентов. :doc:`Возможные значения <./Enums/CounteragentStatus>`

  Возвращает :doc:`коллекцию <Collection>` :doc:`контрагентов <Counteragent>`, с указанным в запросе статусом.
  Если *CounteragentStatus* не задан или пустой, вернётся весь список контрагентов



.. _Organization-GetCounteragentListByStatusAsync:
.. method:: Organization.GetCounteragentListByStatusAsync([CounteragentStatus])

  :CounteragentStatus: ``строка`` статус, по которому производится выборка контрагентов. :doc:`Возможные значения <./Enums/CounteragentStatus>`

  Асинхронный запрос контрагентов с указанным статусом.
  Если *CounteragentStatus* не задан или пустой, вернётся весь список контрагентов.
  Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` :doc:`контрагентов <Counteragent>` в качестве результата



.. _Organization-GetCounteragentListByInnKpp:
.. method:: Organization.GetCounteragentListByInnKpp(Inn[, Kpp])

  :Inn: ``строка`` ИНН для поиска
  :Kpp: ``строка`` КПП для поиска

  Возвращает :doc:`коллекцию <Collection>` :doc:`контрагентов <Counteragent>` с указанными ИНН-КПП


.. _Organization-GetCounteragentListByInnKppAsync:
.. method:: Organization.GetCounteragentListByInnKppAsync(Inn[, Kpp])

  :Inn: ``строка`` ИНН для поиска
  :Kpp: ``строка`` КПП для поиска

  Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` :doc:`контрагентов <Counteragent>` с указанными ИНН-КПП в качестве результата



.. _Organization-GetCounteragentListByInnList:
.. method:: Organization.GetCounteragentListByInnList(INNs)

  :INNs: ``строка`` ИНН, перечисленные через запятую без пробелов

  Aсинхронный запрос контрагентов с перечисленными ИНН.
  Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` :doc:`контрагентов <CounteragentItem>` в качестве результата



.. _Organization-CreateAcquireCounteragentTask:
.. method:: Organization.CreateAcquireCounteragentTask([FilePath])

  :FilePath: ``строка`` путь до файла-вложения

  Создает :doc:`запрос на приглашение контрагента к сотрудничеству <AcquireCounteragentTask>`.
  Если *FilePath* задан, то вместе с приглашением будет отправлен и этот файл



.. _Organization-GetDocumentTypes:
.. method:: Organization.GetDocumentTypes()

  Возвращает :doc:`коллекцию <Collection>` с :doc:`описанием типов документов <DocumentTypeDescription>`, доступных в ящике организации

  .. versionadded:: 5.20.0



.. _Organization-GetFeatures:
.. method:: Organization.GetFeatures()

  Возвращает :doc:`коллекцию <Collection>` строк - включённых у организации возможностей. :doc:`Возможные значения <Enums/OrganizationFeatures>`

  .. versionadded:: 5.32.4



.. _Organization-GetUsers:
.. method:: Organization.GetUsers()

  Возращает :doc:`коллекцию <Collection>` :doc:`сотрудников <OrganizationUser>` организации



.. _Organization-GetResolutionRoutes:
.. method:: Organization.GetResolutionRoutes()

  Возвращает :doc:`коллекцию <Collection>` :doc:`маршрутов согласования <Route>`, настроенных в ящике



.. _Organization-SendFnsRegistrationMessage:
.. method:: Organization.SendFnsRegistrationMessage(Thumbprint)

  :Thumbprint: ``строка`` отпечаток сертификата

  Добавление в сообщение ФНС нового сертификата



.. _Organization-CreateDataTask:
.. method:: Organization.CreateDataTask()

  Возвращает :doc:`объект <DataTask>` для работы с хранилищем ключей-значений

  .. versionadded:: 5.29.9



.. _Organization-GetUserPermissions:
.. method:: Organization.GetUserPermissions()

  Возвращает :doc:`описание прав пользователя <UserPermissions>`, в контексте которого произошла авторизация, для данной организации



.. _Organization-CanSendInvoice:
.. method:: Organization.CanSendInvoice(Thumbprint)

  :Thumbprint: ``строка`` отпечаток сертификата

  Проверяет можно ли подписывать счёт-фактуры в текущей организации, используя сертификат с указанным сертификатом.
  Если возможно, то вернётся пустая строка. Если подписание невозможно, то вернётся текст с причиной невозможности это сделать



.. _Organization-GetExtendedSignerDetails2:
.. method:: Organization.GetExtendedSignerDetails2(Thumbprint, TitleType)

  :Thumbprint: ``строка`` отпечаток сертификата
  :TitleType: ``строка`` тип титула документа. :doc:`Возможные значения <Enums/DocumentTitleType>`

  Возвращает :doc:`параметры подписанта <ExtendedSignerDetails>` в текущей организации для указанного сертификата и указанного типа титула.
  Получить значение для *TitleType* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`
  Для *TitleType* == ``Absent`` и *TitleType* == ``UNKNOWN`` вызов невозможен.
  Метод может быть запрошен самим пользователем или администратором организации


.. _Organization-CreateSetExtendedSignerDetailsTask:
.. method:: Organization.CreateSetExtendedSignerDetailsTask(Thumbprint)

  :Thumbprint: ``строка`` отпечаток сертификата

  Возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта




.. rubric:: Устаревшие методы


.. _Organization-CreateSendTask:
.. method:: Organization.CreateSendTask(FormalDocumentType)

  :DocumentType: ``строка`` тип документа на отправку. :doc:`Возможные значения <Enums/FormalizedDocumentTypeToSend>`

  Создаёт :doc:`задание на отправку отдельного документа <SendTask>`

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.CreatePackageSendTask2`



.. _Organization-CreateSendTaskFromFile:
.. method:: Organization.CreateSendTaskFromFile(DocumentType, FilePath)

  :DocumentType: ``строка`` тип документа на отправку. :doc:`Возможные значения <Enums/FormalizedDocumentTypeToSend>`
  :FilePath: ``строка`` путь до файла контента документа

  Создаёт :doc:`задание на отправку отдельного документа <SendTask>`. Контент файл будет представлен в виде объектой модели, и при отправке, возможно, пропатчен недостающими данными

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.CreatePackageSendTask2`



.. _Organization-CreateSendTaskFromFileRaw:
.. method:: Organization.CreateSendTaskFromFileRaw(DocumentType, FilePath)

  :DocumentType: ``строка`` тип документа на отправку. :doc:`Возможные значения <Enums/DocumentToSend>`
  :FilePath: ``строка`` путь до файла контента документа

  Создаёт :doc:`задание на отправку отдельного документа <SendTask>`. Контент файл будет отправлен без изменений. Попытки разбора в объектную модель не будет

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.CreatePackageSendTask2`



.. _Organization-CreatePackageSendTask:
.. method:: Organization.CreatePackageSendTask()

  Возвращает :doc:`объект <PackageSendTask>`, с помощью которого можно отправить пакет :doc:`документов <DocumentToSend>`

  .. versionadded:: 5.5.0

  .. deprecated:: 5.27.0
    Используйте :meth:`Organization.CreatePackageSendTask2`


.. _Organization-SendDraftAsync:
.. method:: Organization.SendDraftAsync(MessageId)

  :MessageId: ``строка`` идентификатор сообщения черновика

  Асинхронно отправляет черновики. Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` объектов, производных от :doc:`Document` в качестве результата

  .. versionadded:: 4.1.0

  .. deprecated:: 5.18.0
    Используйте объект :doc:`SendDraftTask`, создаваемый методом :meth:`Organization.CreateSendDraftTask`

  .. versionchanged:: 5.33.0
    Метод ничего не делает



.. _Organization-SetAndValidateAddressForCounteragent:
.. method:: Organization.SetAndValidateAddressForCounteragent(key1S, addressTypeKey, isForeign, zipCode, regionCode, territory, city, locality, street, building, block, apartment)

  :key1S: ``строка`` идентификатор адресной информации
  :addressTypeKey: ``строка`` тип адресной информации
  :isForeign: ``строка`` признак того, что адрес является иностранным (за пределами РФ)
  :zipCode: ``строка`` индекс
  :regionCode: ``строка`` код региона РФ
  :territory: ``строка`` район
  :city: ``строка`` город
  :locality: ``строка`` населенный пункт
  :street: ``строка`` улица
  :building: ``строка`` дом
  :block: ``строка`` корпус
  :apartment: ``строка`` квартира

  Валидирует и загружает адресную информацию в хранилище. Возвращает :doc:`коллекцию <Collection>` :doc:`ошибок <ValidationError>`.
  Параметр **isForeign** ни на что не влияет, адрес можно задать только как российский

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.SetData`

  .. versionchanged:: 5.29.0
    Вовзращаемая коллекция всегда пустая. Валидации не происходит



.. _Organization-GetAddressForCounteragent:
.. method:: Organization.GetAddressForCounteragent(key1S, AddressTypeKey)

  :key1S: ``строка`` идентификатор адресной информации
  :addressTypeKey: ``строка`` тип адресной информации

  Возвращает :doc:`адресную информацию <AddressInfo>` из хранилища

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.GetData`



.. _Organization-GetSentDocuments:
.. method:: Organization.GetSentDocuments(OneSId, AsDiadocDocumentId=False)

  :OneSId: ``строка`` идентификаторы учётной системы, перечисленные через ``;``
  :AsDiadocDocumentId: ``булево`` возвращать идентификаторы документов в Диадок


  Возвращает :doc:`коллекцию <Collection>` строк - идентификаторов отправленных документов для запрашиваемых идентификаторов *OneSId*. Тип возвращаемых идентификаторов определяется параметром *AsDiadocDocumentId*:
  Если *AsDiadocDocumentId* == ``FALSE``, то будут возвращены идентификаторы учётной системы;
  Если *AsDiadocDocumentId* == ``TRUE``, то будут возвращены идентификаторы документов в Диадок


  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`


.. _Organization-SetData:
.. method:: Organization.SetData(Key, Value)

  :Key: ``строка`` уникальный ключ в хранилище
  :Value: ``строка`` значение, соответствующее ключу

  Добавляет пару *ключ-значение* в хранилище

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`


.. _Organization-GetData:
.. method:: Organization.GetData(Key)

  :Key: ``строка`` уникальный ключ в хранилище

  Возвращает значение, соответствующее ключу

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`


.. _Organization-GetExtendedSignerDetails:
.. method:: Organization.GetExtendedSignerDetails(Thumbprint, IsSeller=false, forCorrection=false)

  :Thumbprint: ``строка`` отпечаток сертификата
  :IsSeller: ``булево`` подписант для титула продавца
  :forCorrection: ``булево`` подписант для титула корректировочного документа

  Возвращает :doc:`данные подписанта <ExtendedSignerDetails>` из базы Диадок. Метод может быть запрошен самим пользователем или администратором организации

  .. deprecated:: 5.19.0
    Используйте :meth:`Organization.GetExtendedSignerDetails2`

  .. versionchanged:: 5.33.0
    Метод удалён
