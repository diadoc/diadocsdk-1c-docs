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


:MyEmployee:
    :doc:`MyEmployee` **, чтение** - Информация о собственном сотруднике

    .. versionadded:: 5.37.0


.. warning:: Поля устарели

    .. csv-table::
        :header: "Поле", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

        Id,                        Guid,                                             :doc:`../History/release_info/5_31_0`,
        EncryptedDocumentsAllowed, :meth:`GetFeatures() <Organization.GetFeatures>`, :doc:`../History/release_info/5_32_4`,
        AuthenticateType,          MyEmployee.SessionInfo.AuthenticationType,        :doc:`../History/release_info/5_37_0`,
        Login,                     MyEmployee.SessionInfo.Login,                     :doc:`../History/release_info/5_37_0`,
        Certificate,               MyEmployee.SessionInfo.Certificate,               :doc:`../History/release_info/5_37_0`,

    :Id:
        **Строка, чтение** - идентификатор ящика организации в Диадоке в форме ``...@diadoc.ru``

    :EncryptedDocumentsAllowed:
        **Булево, чтение** - для организации включена возможность отправки зашифрованных документов

    :AuthenticateType:
        **Строка, чтение** - тип авторизации. :doc:`Возможные значения <./Enums/AuthenticationType>`

    :Login:
        **Строка, чтение** - логин, по которому произошла авторизация

    :Certificate:
        :doc:`PersonalCertificate` **, чтение** - информация о сертификате, использованном для авторизации. Может быть :doc:`пустым <Descriptions/Empty_Com_Object>`


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        .. csv-table::
            :header: Работа с документами, Работа с контрагентами, Работа с организацией
            
            :meth:`GetDocumentById() <Organization.GetDocumentById>`,                         :meth:`GetCounteragentById() <Organization.GetCounteragentById>`,                           :meth:`CreateAdminTools() <Organization.CreateAdminTools>`
            :meth:`GetDocumentsTask() <Organization.GetDocumentsTask>`,                       :meth:`GetCounteragentByOrgId() <Organization.GetCounteragentByOrgId>`,                     :meth:`GetDocumentTypes() <Organization.GetDocumentTypes>`
            :meth:`CreatePackageSendTask2() <Organization.CreatePackageSendTask2>`,           :meth:`GetCounteragentListByStatus() <Organization.GetCounteragentListByStatus>`,           :meth:`GetFeatures() <Organization.GetFeatures>`
            :meth:`GetReceiptGenerationProcess() <Organization.GetReceiptGenerationProcess>`, :meth:`GetCounteragentListByStatusAsync() <Organization.GetCounteragentListByStatusAsync>`, :meth:`GetEmployees() <Organization.GetEmployees>`
            :meth:`SaveUserDataXSD() <Organization.SaveUserDataXSD>`,                         :meth:`GetCounteragentListByInnKpp() <Organization.GetCounteragentListByInnKpp>`,           :meth:`GetResolutionRoutes() <Organization.GetResolutionRoutes>`
            :meth:`GetBase64UserDataXSD() <Organization.GetBase64UserDataXSD>`,               :meth:`GetCounteragentListByInnKppAsync() <Organization.GetCounteragentListByInnKppAsync>`, :meth:`CreateDataTask() <Organization.CreateDataTask>`
            :meth:`RestoreDocument() <Organization.RestoreDocument>`,                         :meth:`GetCounteragentListByInnList() <Organization.GetCounteragentListByInnList>`,         :meth:`RegisterPowerOfAttorneyById() <Organization.RegisterPowerOfAttorneyById>`
            :meth:`CreateSendDraftTask() <Organization.CreateSendDraftTask>`,                 :meth:`CreateAcquireCounteragentTask() <Organization.CreateAcquireCounteragentTask>`,       :meth:`RegisterPowerOfAttorneyByContent() <Organization.RegisterPowerOfAttorneyByContent>`
            :meth:`RecycleDraft() <Organization.RecycleDraft>`, ,
            :meth:`GetDocumentEventList() <Organization.GetDocumentEventList>`, ,
            :meth:`GetTemplate() <Organization.GetTemplate>`, ,
            :meth:`CreateTemplateSendTask() <Organization.CreateTemplateSendTask>`, ,
            :meth:`CreateTransformTemplateTask() <Organization.CreateTransformTemplateTask>`, ,

    .. tab:: Работа с документами

        * :meth:`GetDocumentById() <Organization.GetDocumentById>`
        * :meth:`GetDocumentsTask() <Organization.GetDocumentsTask>`
        * :meth:`CreatePackageSendTask2() <Organization.CreatePackageSendTask2>`
        * :meth:`GetReceiptGenerationProcess() <Organization.GetReceiptGenerationProcess>`
        * :meth:`SaveUserDataXSD() <Organization.SaveUserDataXSD>`
        * :meth:`GetBase64UserDataXSD() <Organization.GetBase64UserDataXSD>`
        * :meth:`RestoreDocument() <Organization.RestoreDocument>`
        * :meth:`CreateSendDraftTask() <Organization.CreateSendDraftTask>`
        * :meth:`RecycleDraft() <Organization.RecycleDraft>`
        * :meth:`GetDocumentEventList() <Organization.GetDocumentEventList>`
        * :meth:`GetTemplate() <Organization.GetTemplate>`
        * :meth:`CreateTemplateSendTask() <Organization.CreateTemplateSendTask>`
        * :meth:`CreateTransformTemplateTask() <Organization.CreateTransformTemplateTask>`

    .. tab:: Работа с контрагентами

        * :meth:`GetCounteragentById() <Organization.GetCounteragentById>`
        * :meth:`GetCounteragentByOrgId() <Organization.GetCounteragentByOrgId>`
        * :meth:`GetCounteragentListByStatus() <Organization.GetCounteragentListByStatus>`
        * :meth:`GetCounteragentListByStatusAsync() <Organization.GetCounteragentListByStatusAsync>`
        * :meth:`GetCounteragentListByInnKpp() <Organization.GetCounteragentListByInnKpp>`
        * :meth:`GetCounteragentListByInnKppAsync() <Organization.GetCounteragentListByInnKppAsync>`
        * :meth:`GetCounteragentListByInnList() <Organization.GetCounteragentListByInnList>`
        * :meth:`CreateAcquireCounteragentTask() <Organization.CreateAcquireCounteragentTask>`

    .. tab:: Работа с организацией

        * :meth:`CreateAdminTools() <Organization.CreateAdminTools>`
        * :meth:`GetDocumentTypes() <Organization.GetDocumentTypes>`
        * :meth:`GetFeatures() <Organization.GetFeatures>`
        * :meth:`GetEmployees() <Organization.GetEmployees>`
        * :meth:`GetResolutionRoutes() <Organization.GetResolutionRoutes>`
        * :meth:`CreateDataTask() <Organization.CreateDataTask>`
        * :meth:`RegisterPowerOfAttorneyById() <Organization.RegisterPowerOfAttorneyById>`
        * :meth:`RegisterPowerOfAttorneyByContent() <Organization.RegisterPowerOfAttorneyByContent>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

            :meth:`Organization.CreateSendTask`, :meth:`Organization.CreatePackageSendTask2`, :doc:`../History/release_info/5_5_0`, :doc:`../History/release_info/5_33_4`
            :meth:`Organization.CreateSendTaskFromFile`, :meth:`Organization.CreatePackageSendTask2`, :doc:`../History/release_info/5_5_0`, :doc:`../History/release_info/5_33_4`
            :meth:`Organization.CreateSendTaskFromFileRaw`, :meth:`Organization.CreatePackageSendTask2`, :doc:`../History/release_info/5_5_0`, :doc:`../History/release_info/5_33_4`
            :meth:`Organization.CreatePackageSendTask`, :meth:`Organization.CreatePackageSendTask2`, :doc:`../History/release_info/5_27_0`,
            :meth:`Organization.SendDraftAsync`, :meth:`Organization.CreateSendDraftTask`, :doc:`../History/release_info/5_18_0`,
            :meth:`Organization.SetAndValidateAddressForCounteragent`, :meth:`Organization.CreateDataTask`, :doc:`../History/release_info/5_5_0`,
            :meth:`Organization.GetSentDocuments`, :meth:`Organization.CreateDataTask`, :doc:`../History/release_info/5_5_0`,
            :meth:`Organization.SetData`, :meth:`Organization.CreateDataTask`, :doc:`../History/release_info/5_29_9`,
            :meth:`Organization.GetData`, :meth:`Organization.CreateDataTask`, :doc:`../History/release_info/5_29_9`,
            :meth:`Organization.GetAddressForCounteragent`, :meth:`Organization.CreateDataTask`, :doc:`../History/release_info/5_5_0`,
            :meth:`Organization.GetExtendedSignerDetails`, :meth:`MyEmployee.GetExtendedSignerDetails` или :meth:`AdminTools.GetExtendedSignerDetails`, :doc:`../History/release_info/5_33_0`,
            :meth:`Organization.GetExtendedSignerDetails2`, :meth:`MyEmployee.GetExtendedSignerDetails` или :meth:`AdminTools.GetExtendedSignerDetails`, :doc:`../History/release_info/5_37_0`,
            :meth:`Organization.SendFnsRegistrationMessage`, :meth:`MyEmployee.UpdateCertificateFNSRegistration` или :meth:`AdminTools.RegisterCertificateInFNS`, :doc:`../History/release_info/5_37_0`,
            :meth:`Organization.GetUsers`, :meth:`Organization.GetEmployees`, :doc:`../History/release_info/5_37_0`,
            :meth:`Organization.GetUserPermissions`, **MyEmployee.EmployeeInfo.Permissions**, :doc:`../History/release_info/5_37_0`,
            :meth:`Organization.CanSendInvoice`, :meth:`MyEmployee.CanSendInvoice` или :meth:`AdminTools.CanSendInvoice`, :doc:`../History/release_info/5_37_0`,
            :meth:`Organization.CreateSetExtendedSignerDetailsTask`, :meth:`MyEmployee.CreateSetExtendedSignerDetailsTask` или :meth:`AdminTools.CreateSetExtendedSignerDetailsTask`, :doc:`../History/release_info/5_37_0`,

        .. method:: Organization.CreateSendTask(FormalDocumentType)

            :DocumentType: ``строка`` тип документа на отправку. :doc:`Возможные значения <Enums/FormalizedDocumentTypeToSend>`

            Возвращает :doc:`задание отправки документа <SendTask>`


        .. method:: Organization.CreateSendTaskFromFile(DocumentType, FilePath)

            :DocumentType: ``строка`` тип документа на отправку. :doc:`Возможные значения <Enums/DocumentToSend>`
            :FilePath: ``строка`` путь до файла контента документа

            Возвращает :doc:`задание отправки документа <SendTask>`. Контент документа берётся из файла. Происходит попытка представить его в виде объектой модели


        .. method:: Organization.CreateSendTaskFromFileRaw(DocumentType, FilePath)

            :DocumentType: ``строка`` тип документа на отправку. :doc:`Возможные значения <Enums/DocumentToSend>`
            :FilePath: ``строка`` путь до файла контента документа

            Возвращает :doc:`задание отправки документа <SendTask>`. Контент документа берётся из файла. Представления контента в виде объектой модели не происходит


        .. method:: Organization.CreatePackageSendTask()

            Возвращает :doc:`задание отправки пакета документов <PackageSendTask>`


        .. method:: Organization.SendDraftAsync(MessageId)

            :MessageId: ``строка`` идентификатор сообщения черновика

            Асинхронно отправляет черновики. Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` объектов, производных от :doc:`Document` в качестве результата

            .. versionchanged:: 5.33.0
                Метод ничего не делает

            .. versionchanged:: 5.36.8
             Метод удалён


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

            .. versionchanged:: 5.29.0
                Вовзращаемая коллекция всегда пустая. Валидации не происходит


        .. method:: Organization.GetAddressForCounteragent(key1S, AddressTypeKey)

            :key1S: ``строка`` идентификатор адресной информации
            :addressTypeKey: ``строка`` тип адресной информации

            Возвращает :doc:`адресную информацию <AddressInfo>` из хранилища


        .. method:: Organization.GetSentDocuments(OneSId, AsDiadocDocumentId=False)

            :OneSId: ``строка`` идентификаторы учётной системы, перечисленные через ``;``
            :AsDiadocDocumentId: ``булево`` возвращать идентификаторы документов в Диадок

            Возвращает :doc:`коллекцию <Collection>` строк - идентификаторов отправленных документов для запрашиваемых идентификаторов *OneSId*. Тип возвращаемых идентификаторов определяется параметром *AsDiadocDocumentId*:
            Если *AsDiadocDocumentId* == ``FALSE``, то будут возвращены идентификаторы учётной системы;
            Если *AsDiadocDocumentId* == ``TRUE``, то будут возвращены идентификаторы документов в Диадок


        .. method:: Organization.SetData(Key, Value)

            :Key: ``строка`` уникальный ключ в хранилище
            :Value: ``строка`` значение, соответствующее ключу

            Добавляет пару *ключ-значение* в хранилище


        .. method:: Organization.GetData(Key)

            :Key: ``строка`` уникальный ключ в хранилище

            Возвращает значение, соответствующее ключу


        .. method:: Organization.GetExtendedSignerDetails(Thumbprint, IsSeller=false, forCorrection=false)

            :Thumbprint: ``строка`` отпечаток сертификата
            :IsSeller: ``булево`` подписант для титула продавца
            :forCorrection: ``булево`` подписант для титула корректировочного документа

            Возвращает :doc:`данные подписанта <ExtendedSignerDetails>` из базы Диадок. Метод может быть запрошен самим пользователем или администратором организации


        .. method:: Organization.GetExtendedSignerDetails2(Thumbprint, TitleType)

            :Thumbprint: ``строка`` отпечаток сертификата
            :TitleType: ``строка`` тип титула документа. :doc:`Возможные значения <Enums/DocumentTitleType>`

            Возвращает :doc:`параметры подписанта <ExtendedSignerDetails>` в текущей организации для указанного сертификата и указанного типа титула.
            Получить значение для *TitleType* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`
            Для *TitleType* == ``Absent`` и *TitleType* == ``UNKNOWN`` вызов невозможен.
            Метод может быть запрошен самим пользователем или администратором организации


        .. method:: Organization.CreateSetExtendedSignerDetailsTask(Thumbprint)

            :Thumbprint: ``строка`` отпечаток сертификата

            Возвращает :doc:`объект <SetExtendedSignerDetailsTask>`, с помощью которого можно установить параметры подписанта


        .. method:: Organization.GetUsers()

            Возращает :doc:`коллекцию <Collection>` :doc:`сотрудников <OrganizationUser>` организации


        .. method:: Organization.GetUserPermissions()

            Возвращает :doc:`описание прав пользователя <UserPermissions>`, в контексте которого произошла авторизация, для данной организации


        .. method:: Organization.CanSendInvoice(Thumbprint)

            :Thumbprint: ``строка`` отпечаток сертификата

            Проверяет можно ли подписывать счёт-фактуры в текущей организации, используя сертификат с указанным отпечатком.
            Если возможно, то вернётся пустая строка. Если подписание невозможно, то вернётся текст с причиной невозможности это сделать


        .. method:: Organization.SendFnsRegistrationMessage(Thumbprint)

            :Thumbprint: ``строка`` отпечаток сертификата

            Добавление в сообщение ФНС нового сертификата



.. method:: Organization.GetDocumentById(DocumentId, WithExternalId=FALSE)

    :DocumentId: ``строка`` идентифкатор документа
    :WithExternalId: ``булево`` нужно ли запрашивать дополнительный идентификатор учётной системы

    Возвращает :doc:`документ <DocumentBase>` в ящике по его идентификатору.
    При *WithExternalId* == ``TRUE`` у документа будет заполнено поле *OneSDocumentId*, если оно установлено для него, но сам метод отработает медленнее


.. method:: Organization.GetDocumentsTask()

    Возвращает :doc:`объект <DocumentsTask>` для поиска документов в ящике


.. method:: Organization.CreatePackageSendTask2()

    Возвращает :doc:`объект <PackageSendTask2>`, с помощью которого можно отправить :doc:`документы <CustomDocumentToSend>`

    .. versionadded:: 5.27.0


.. method:: Organization.GetReceiptGenerationProcess()

    Возвращает :doc:`объект <ReceiptGenerationProcess>`, с помощью которого можно запустить процесс автоматической отправки извещений о получении документов в текущем ящике


.. method:: Organization.SaveUserDataXSD(TitleName, Function, Version, DocflowSide, FilePath)

    :TitleName: ``строка`` название типа документа
    :Function: ``строка`` функция документа
    :Version: ``строка`` версия документа
    :DocflowSide: ``строка`` сторона документооборота. :doc:`Возможные значения <Enums/DocflowSide>`
    :FilePath: ``строка`` полное имя файла, в который нужно сохранить описание контента

    Сохраняет описание представления контента документа на диск.
    Значения для *TitleName*, *Function*, *Version* можно получить в ответе метода :meth:`Organization.GetDocumentTypes`

    .. versionadded:: 5.27.0


.. method:: Organization.GetBase64UserDataXSD(TitleName, Function, Version, DocflowSide)

    :TitleName: ``строка`` название типа документа
    :Function: ``строка`` функция документа
    :Version: ``строка`` версия документа
    :DocflowSide: ``строка`` сторона документооборота. :doc:`Возможные значения <Enums/DocflowSide>`

    Возвращает ``Base64-строку`` описания представления контента документа.
    Значения для *TitleName*, *Function*, *Version* можно получить в ответе метода :meth:`Organization.GetDocumentTypes`

    .. versionadded:: 5.28.3


.. method:: Organization.RestoreDocument(DocumentId)

    :DocumentId: ``строка`` идентификатор документа

    Восстанавливает удалённый документ


.. method:: Organization.CreateSendDraftTask(MessageId)

    :MessageId: ``строка`` идентификатор сообщения черновика

    Создаёт :doc:`объект <SendDraftTask>`, с помощью которого можно отправить черновик.
    *MessageId* - первая половина из *DocumentId* черновика

    .. versionadded:: 5.18.0


.. method:: Organization.RecycleDraft(MessageId)

    :MessageId: ``строка`` идентификатор сообщения черновика

    Метод удаляет черновик. Восстановить черновик невозможно.
    *MessageId* - первая половина из *DocumentId* черновика

    .. versionadded:: 5.25.0


.. method:: Organization.GetDocumentEventList([AfterEventId])

    :AfterEventId: ``строка`` Идентификатор события, после которого будет вычитываться лента событий

    Возвращает :doc:`список <Collection>` :doc:`событий <DocumentEvent>`, произошедших с документами в текущем ящике.
    Если *AfterEventId* не задан или пустой, то события начнут вычитываться с момента создания ящика Диадок


.. method:: Organization.GetTemplate(TemplateId)

    :TemplateId: ``строка`` идентификатор шаблона

    Возвращает :doc:`шаблон документа <Template>` по его идентификатору

    .. versionadded:: 5.24.0


.. method:: Organization.CreateTemplateSendTask()

    Возвращает :doc:`объект <TemplateSendTask>`, с помощью которого можно отправить :doc:`шаблон документ <TemplateToSend>`

    .. versionadded:: 5.24.0


.. method:: Organization.CreateTransformTemplateTask(TemplateId)

    :TemplateId: ``строка`` идентификатор шаблона

    Возвращает :doc:`задание для создания документов из шаблона <TransformTemplateTask>`

    .. versionadded:: 5.24.0


.. method:: Organization.GetCounteragentById(BoxId)

    :BoxId: ``строка`` идентификатор ящика

    Возвращает :doc:`контрагента <Counteragent>` по идентификатору ящика.
    Идентификатор может быть как в виде GUID, так и в виде ``...@diadoc.ru``


.. method:: Organization.GetCounteragentByOrgId(OrganizationId)

    :OrganizationId: ``строка`` идентификатор организации в Диадок

    Возвращает :doc:`контрагента <Counteragent>` по идентификатору организации


.. method:: Organization.GetCounteragentListByStatus([CounteragentStatus])

    :CounteragentStatus: ``строка`` статус, по которому производится выборка контрагентов. :doc:`Возможные значения <./Enums/GetCounteragentsByStatus_param>`

    Возвращает :doc:`коллекцию <Collection>` :doc:`контрагентов <Counteragent>`, с указанным в запросе статусом.
    Если *CounteragentStatus* не задан или пустой, вернётся весь список контрагентов


.. method:: Organization.GetCounteragentListByStatusAsync([CounteragentStatus])

    :CounteragentStatus: ``строка`` статус, по которому производится выборка контрагентов. :doc:`Возможные значения <./Enums/GetCounteragentsByStatus_param>`

    Асинхронный запрос контрагентов с указанным статусом.
    Если *CounteragentStatus* не задан или пустой, вернётся весь список контрагентов.
    Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` :doc:`контрагентов <Counteragent>` в качестве результата


.. method:: Organization.GetCounteragentListByInnKpp(Inn[, Kpp])

    :Inn: ``строка`` ИНН для поиска
    :Kpp: ``строка`` КПП для поиска

    Возвращает :doc:`коллекцию <Collection>` :doc:`контрагентов <Counteragent>` с указанными ИНН-КПП


.. method:: Organization.GetCounteragentListByInnKppAsync(Inn[, Kpp])

    :Inn: ``строка`` ИНН для поиска
    :Kpp: ``строка`` КПП для поиска

    Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` :doc:`контрагентов <Counteragent>` с указанными ИНН-КПП в качестве результата


.. method:: Organization.GetCounteragentListByInnList(INNs)

    :INNs: ``строка`` ИНН, перечисленные через запятую без пробелов

    Aсинхронный запрос контрагентов с перечисленными ИНН.
    Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` :doc:`контрагентов <CounteragentItem>` в качестве результата


.. method:: Organization.CreateAcquireCounteragentTask([FilePath])

    :FilePath: ``строка`` путь до файла-вложения

    Создает :doc:`запрос на приглашение контрагента к сотрудничеству <AcquireCounteragentTask>`.
    Если *FilePath* задан, то вместе с приглашением будет отправлен и этот файл


.. method:: Organization.CreateAdminTools()

    Создаёт :doc:`объект для администрирования организации <AdminTools>`

    .. versionadded:: 5.37.0


.. method:: Organization.GetDocumentTypes()

    Возвращает :doc:`коллекцию <Collection>` с :doc:`описанием типов документов <DocumentTypeDescription>`, доступных в ящике организации

    .. versionadded:: 5.20.0


.. method:: Organization.GetFeatures()

    Возвращает :doc:`коллекцию <Collection>` строк - включённых у организации возможностей. :doc:`Возможные значения <Enums/OrganizationFeatures>`

    .. versionadded:: 5.32.4


.. method:: Organization.GetEmployees()

    Возвращает :doc:`коллекцию <Collection>` :doc:`сотрудников <EmployeeInfo>` организации

    .. versionadded:: 5.37.0


.. method:: Organization.GetResolutionRoutes()

    Возвращает :doc:`коллекцию <Collection>` :doc:`маршрутов согласования <Route>`, настроенных в ящике


.. method:: Organization.CreateDataTask()

    Возвращает :doc:`объект <DataTask>` для работы с хранилищем ключей-значений

    .. versionadded:: 5.29.9


.. method:: Organization.RegisterPowerOfAttorneyById(RegNumber, IssuerInn)

    :RegNumber: ``Строка`` регистрационный номер МЧД
    :IssuerInn: ``Строка`` ИНН доверителя

    Регистрирует МЧД, в сервисе Диадок по её регистрационному номеру и ИНН доверителя

    .. versionadded:: 5.37.0


.. _Organization-RegisterPowerOfAttorneyByContent:
.. method:: Organization.RegisterPowerOfAttorneyByContent(XmlContent, XmlSignature)

    :XmlContent: ``Строка`` контент МЧД в виде base64 строки
    :XmlSignature: ``Строка`` контент подписи МЧД в виде base64 строки

    Регистрирует МЧД, в сервисе Диадок с помощью файла МЧД и подписи, которой она была подписана

    .. versionadded:: 5.37.0