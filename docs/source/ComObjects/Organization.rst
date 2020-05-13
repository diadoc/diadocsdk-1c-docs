Organization
============

Организация на сервере Диадок


.. rubric:: Свойства

:Id:
  **Строка, чтение** - идентификатор ящика организации в Диадоке

:Name:
  **Строка, чтение** - наименование организации

:Inn:
  **Строка, чтение** - ИНН организации

:Kpp:
  **Строка, чтение** - КПП организации

:Departments:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Department <Department>` **, чтение** - подразделения, родительским подразделением которых является "Головное" подразделение

:AuthenticateType:
  **Строка, чтение** - тип авторизации

:Login:
  **Строка, чтение** - логин, по которому произошла авторизация к данной организации

:Certificate:
  :doc:`PersonalCertificate <PersonalCertificate>` **, чтение** - сертификат, по которому произошла авторизация в данной организации

:FnsParticipantId:
  **Строка, чтение** - идентификатор организации-участника документооборота

:FnsRegistrationDate:
  **Дата, чтение** - дата подачи заявляения в ФНС на регистрацию данной организации в качестве участника документооборота ЭСФ

:IsTest:
  **Булево, чтение** - организация работает в тестовом режиме

:IsPilot:
  **Булево, чтение** - организация работает в пилотном режиме

:EncryptedDocumentsAllowed:
  **Булево, чтение** - организации разрешена отправка зашифрованных документов



.. rubric:: Методы

+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-GetUsers|_                             | |Organization-GetUserPermissions|_           | |Organization-GetCounteragentById|_                | |Organization-CreateDataTask|_              |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-GetCounteragentByOrgId|_               | |Organization-GetCounteragentListByStatus|_  | |Organization-GetCounteragentListByStatusAsync|_   | |Organization-GetCounteragentListByInnKpp|_ |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-GetCounteragentListByInnKppAsync|_     | |Organization-GetCounteragentListByInnList|_ | |Organization-CreateAcquireCounteragentTask|_      |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-GetDocumentById|_                      | |Organization-GetDocumentsTask|_             | |Organization-RestoreDocument|_                    |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-GetReceiptGenerationProcess|_          | |Organization-GetDocumentEventList|_         | |Organization-CreateSendTask|_                     |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-CreateSendTaskFromFile|_               | |Organization-CreateSendTaskFromFileRaw|_    | |Organization-CreatePackageSendTask|_              |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-CreatePackageSendTask2|_               | |Organization-CreateSendDraftTask|_          | |Organization-SendDraftAsync|_                     |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-SetAndValidateAddressForCounteragent|_ | |Organization-GetAddressForCounteragent|_    | |Organization-GetSentDocuments|_                   |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-SetData|_                              | |Organization-GetData|_                      | |Organization-CreateSetExtendedSignerDetailsTask|_ |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-GetExtendedSignerDetails|_             | |Organization-GetExtendedSignerDetails2|_    | |Organization-SendFnsRegistrationMessage|_         |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-CanSendInvoice|_                       | |Organization-GetDocumentTypes|_             | |Organization-GetResolutionRoutes|_                |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-CreateTemplateSendTask|_               | |Organization-GetTemplate|_                  | |Organization-CreateTransformTemplateTask|_        |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+
| |Organization-RecycleDraft|_                         | |Organization-SaveUserDataXSD|_              | |Organization-GetBase64UserDataXSD|_               |                                             |
+------------------------------------------------------+----------------------------------------------+----------------------------------------------------+---------------------------------------------+


.. |Organization-GetUsers| replace:: GetUsers()
.. |Organization-GetUserPermissions| replace:: GetUserPermissions()
.. |Organization-GetCounteragentById| replace:: GetCounteragentById()
.. |Organization-GetCounteragentByOrgId| replace:: GetCounteragentByOrgId()
.. |Organization-GetCounteragentListByStatus| replace:: GetCounteragentListByStatus()
.. |Organization-GetCounteragentListByStatusAsync| replace:: GetCounteragentListByStatusAsync()
.. |Organization-GetCounteragentListByInnKpp| replace:: GetCounteragentListByInnKpp()
.. |Organization-GetCounteragentListByInnKppAsync| replace:: GetCounteragentListByInnKppAsync()
.. |Organization-GetCounteragentListByInnList| replace:: GetCounteragentListByInnList()
.. |Organization-CreateAcquireCounteragentTask| replace:: CreateAcquireCounteragentTask()
.. |Organization-GetDocumentById| replace:: GetDocumentById()
.. |Organization-GetDocumentsTask| replace:: GetDocumentsTask()
.. |Organization-RestoreDocument| replace:: RestoreDocument()
.. |Organization-GetReceiptGenerationProcess| replace:: GetReceiptGenerationProcess()
.. |Organization-GetDocumentEventList| replace:: GetDocumentEventList()
.. |Organization-CreateSendTask| replace:: CreateSendTask()
.. |Organization-CreateSendTaskFromFile| replace:: CreateSendTaskFromFile()
.. |Organization-CreateSendTaskFromFileRaw| replace:: CreateSendTaskFromFileRaw()
.. |Organization-CreatePackageSendTask| replace:: CreatePackageSendTask()
.. |Organization-CreatePackageSendTask2| replace:: CreatePackageSendTask2()
.. |Organization-CreateSendDraftTask| replace:: CreateSendDraftTask()
.. |Organization-SendDraftAsync| replace:: SendDraftAsync()
.. |Organization-SetAndValidateAddressForCounteragent| replace:: SetAndValidateAddressForCounteragent()
.. |Organization-GetAddressForCounteragent| replace:: GetAddressForCounteragent()
.. |Organization-GetSentDocuments| replace:: GetSentDocuments()
.. |Organization-SetData| replace:: SetData()
.. |Organization-GetData| replace:: GetData()
.. |Organization-CreateSetExtendedSignerDetailsTask| replace:: CreateSetExtendedSignerDetailsTask()
.. |Organization-GetExtendedSignerDetails| replace:: GetExtendedSignerDetails()
.. |Organization-GetExtendedSignerDetails2| replace:: GetExtendedSignerDetails2()
.. |Organization-SendFnsRegistrationMessage| replace:: SendFnsRegistrationMessage()
.. |Organization-CanSendInvoice| replace:: CanSendInvoice()
.. |Organization-GetDocumentTypes| replace:: GetDocumentTypes()
.. |Organization-GetResolutionRoutes| replace:: GetResolutionRoutes()
.. |Organization-CreateTemplateSendTask| replace:: CreateTemplateSendTask()
.. |Organization-GetTemplate| replace:: GetTemplate()
.. |Organization-CreateTransformTemplateTask| replace:: CreateTransformTemplateTask()
.. |Organization-RecycleDraft| replace:: RecycleDraft()
.. |Organization-SaveUserDataXSD| replace:: SaveUserDataXSD()
.. |Organization-GetBase64UserDataXSD| replace:: GetBase64UserDataXSD()
.. |Organization-CreateDataTask| replace:: CreateDataTask()



.. _Organization-GetUsers:
.. method:: Organization.GetUsers()

  Возращает :doc:`коллекцию <Collection>` :doc:`пользователей <OrganizationUser>` организации



.. _Organization-GetUserPermissions:
.. method:: Organization.GetUserPermissions()

  Возвращает :doc:`описание прав пользователя <UserPermissions>`, в контексте которого произошла авторизация, для данной организации



.. _Organization-GetCounteragentById:
.. method:: Organization.GetCounteragentById(BoxId)

  :BoxId: ``строка`` идентификатор ящика

  Возвращает :doc:`контрагента <Counteragent>` по идентификатору ящика



.. _Organization-GetCounteragentByOrgId:
.. method:: Organization.GetCounteragentByOrgId(OrgId)

  :OrgId: ``строка`` идентификатор организации в Диадок

  Возвращает :doc:`контрагента <Counteragent>` по идентификатору организации



.. _Organization-GetCounteragentListByStatus:
.. method:: Organization.GetCounteragentListByStatus([CounteragentStatus])

  :CounteragentStatus: ``строка`` статус, по которому производится выборка контрагентов. |Organization-CounteragentStatus|_

  Возвращает :doc:`коллекцию <Collection>` :doc:`контрагентов <Counteragent>`, с указанным в запросе статусом.
  Если параметр не задан, вернётся весь список контрагентов



.. _Organization-GetCounteragentListByStatusAsync:
.. method:: Organization.GetCounteragentListByStatusAsync([CounteragentStatus])

  :CounteragentStatus: ``строка`` статус, по которому производится выборка контрагентов. |Organization-CounteragentStatus|_

  Асинхронный запрос контрагентов с указанным статусом. Если параметр не задан, вернётся весь список контрагентов.
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

  Создает :doc:`запрос на приглашение контрагента к сотрудничеству <AcquireCounteragentTask>`. Если *FilePath* задан, то вместе с приглашением будет отправлен и этот файл



.. _Organization-GetDocumentById:
.. method:: Organization.GetDocumentById(DocumentId, WithOneSId=falst)

  :DocumentId: ``строка`` идентифкатор документа
  :WithOneSId: ``булево`` нужно ли запрашивать дополнительный идентификатор учётной системы

  Возвращает :doc:`документ <Document>` в ящике по его идентификатору.
  При *WithOneSId* == ``TRUE`` у документа будет заполнено поле *OneSDocumentId*, если оно установлено для него, но сам метод отработает медленнее



.. _Organization-GetDocumentsTask:
.. method:: Organization.GetDocumentsTask()

  Возвращает :doc:`задачу поиска документов в ящике <DocumentsTask>`



.. _Organization-RestoreDocument:
.. method:: Organization.RestoreDocument(DocumentId)

  :DocumentId: ``строка`` идентификатор документа

  Восстанавливает удалённый документ



.. _Organization-GetReceiptGenerationProcess:
.. method:: Organization.GetReceiptGenerationProcess()

  Возвращает :doc:`объект <ReceiptGenerationProcess>`, с помощью которого можно запустить процесс автоматической отправки извещений о получении документов в текущем ящике



.. _Organization-GetDocumentEventList:
.. method:: Organization.GetDocumentEventList([AfterEventId])

  :AfterEventId: ``строка`` Идентификатор события, после которого будет вычитываться лента событий

  Возвращает :doc:`список <Collection>` :doc:`событий <DocumentEvent>`, произошедших с документами в текущем ящике.
  Если *AfterEventId* не задан, то события начнут вычитываться с момента создания ящика Диадок



.. _Organization-CreateSendTask:
.. method:: Organization.CreateSendTask(FormalDocumentType)

  :DocumentType: ``строка`` тип документа на отправку. |Organization-FormalDocumentType|_

  Создаёт :doc:`задание на отправку отдельного документа <SendTask>`

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.CreatePackageSendTask2`



.. _Organization-CreateSendTaskFromFile:
.. method:: Organization.CreateSendTaskFromFile(DocumentType, FilePath)

  :DocumentType: ``строка`` тип документа на отправку. |Organization-DocumentType|_
  :FilePath: ``строка`` путь до файла контента документа

  Создаёт :doc:`задание на отправку отдельного документа <SendTask>`. Контент файл будет представлен в виде объектой модели, и при отправке, возможно, пропатчен недостающими данными

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.CreatePackageSendTask2`



.. _Organization-CreateSendTaskFromFileRaw:
.. method:: Organization.CreateSendTaskFromFileRaw(DocumentType, FilePath)

  :DocumentType: ``строка`` тип документа на отправку. |Organization-DocumentType|_
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



.. _Organization-CreatePackageSendTask2:
.. method:: Organization.CreatePackageSendTask2()

  Возвращает :doc:`объект <PackageSendTask2>`, с помощью которого можно отправить пакет :doc:`документов <CustomDocumentToSend>`

  .. versionadded:: 5.27.0



.. _Organization-CreateSendDraftTask:
.. method:: Organization.CreateSendDraftTask(MessageId)

  :MessageId: ``строка`` идентификатор сообщения черновика

  Создаёт :doc:`задание для отправки черновика документа <SendDraftTask>`

  .. versionadded:: 5.18.0



.. _Organization-SendDraftAsync:
.. method:: Organization.SendDraftAsync(MessageId)

  :MessageId: ``строка`` идентификатор сообщения черновика

  Асинхронно отправляет черновики. Возвращает :doc:`AsyncResult` с :doc:`коллекцией <Collection>` объектов, производных от :doc:`Document` в качестве результата

  .. versionadded:: 4.1.0

  .. deprecated:: 5.18.0
    Используйте объект :doc:`SendDraftTask`, создаваемый методом :meth:`Organization.SendDraftAsync`



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
    Используйте :meth:`Organization.CreateDataTask`

  .. versionchanged:: 5.29.0
    Вовзращаемая коллекция всегда пустая. Валидации не происходит



.. _Organization-GetAddressForCounteragent:
.. method:: Organization.GetAddressForCounteragent(key1S, AddressTypeKey)

  :key1S: ``строка`` идентификатор адресной информации
  :addressTypeKey: ``строка`` тип адресной информации

  Возвращает :doc:`адресную информацию <AddressInfo>` из хранилища

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.CreateDataTask`



.. _Organization-GetSentDocuments:
.. method:: Organization.GetSentDocuments(OneSId, AsDiadocDocumentId=False)

  :OneSId: ``строка`` идентификаторы учётной системы, перечисленные через ``;``
  :AsDiadocDocumentId: ``булево`` возвращать идентификаторы документов в Диадок


  Возвращает :doc:`коллекцию <Collection>` строк - идентификаторов отправленных документов для запрашиваемых идентификаторов *OneSId*. Тип возвращаемых идентификаторов определяется параметром *AsDiadocDocumentId*:
  Если *AsDiadocDocumentId* == ``FALSE``, то будут возвращены идентификаторы учётной системы;
  Если *AsDiadocDocumentId* == ``TRUE``, то будут возвращены идентификаторы документов в Диадок


  .. deprecated:: 5.5.0
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



.. _Organization-CreateSetExtendedSignerDetailsTask:
.. method:: Organization.CreateSetExtendedSignerDetailsTask(Thumbprint)

  :Thumbprint: ``строка`` отпечаток сертификата

  Возвращает :doc:`задание для установки параметры подписанта <SetExtendedSignerDetailsTask>`



.. _Organization-GetExtendedSignerDetails:
.. method:: Organization.GetExtendedSignerDetails(Thumbprint, IsSeller=false, forCorrection=false)

  :Thumbprint: ``строка`` отпечаток сертификата
  :IsSeller: ``булево`` подписант для титула продавца
  :forCorrection: ``булево`` подписант для титула корректировочного документа

  Возвращает :doc:`данные подписанта <ExtendedSignerDetails>` из базы Диадок. Метод может быть запрошен самим пользователем или администратором организации

  .. deprecated:: 5.19.0
    Используйте :meth:`Organization.GetExtendedSignerDetails2`



.. _Organization-GetExtendedSignerDetails2:
.. method:: Organization.GetExtendedSignerDetails2(Thumbprint, TitleType)

  :Thumbprint: ``строка`` отпечаток сертификата
  :TitleType: ``строка`` тип титула документа. |Organization-TitleType|_

  Возвращает :doc:`данные подписанта <ExtendedSignerDetails>` из базы Диадок. . Метод может быть запрошен самим пользователем или администратором организации



.. _Organization-SendFnsRegistrationMessage:
.. method:: Organization.SendFnsRegistrationMessage(Thumbprint)

  :Thumbprint: ``строка`` отпечаток сертификата

  Добавление в сообщение ФНС нового сертификата



.. _Organization-CanSendInvoice:
.. method:: Organization.CanSendInvoice(Thumbprint)

  :Thumbprint: ``строка`` отпечаток сертификата

  Возвращает пустую строку, если указанный сертификат может использоваться для подписания счетов-фактур в текущей организации, или строку с причиной невозможности такого использования



.. _Organization-GetDocumentTypes:
.. method:: Organization.GetDocumentTypes()

  Возвращает :doc:`коллекцию <Collection>` :doc:`типов документов <DocumentTypeDescription>`, доступных в ящике организации



.. _Organization-GetResolutionRoutes:
.. method:: Organization.GetResolutionRoutes()

  Возвращает :doc:`коллекцию <Collection>` :doc:`маршрутов согласования <Route>`, настроенных в ящике



.. _Organization-CreateTemplateSendTask:
.. method:: Organization.CreateTemplateSendTask()

  Возвращает :doc:`задание для отправки шаблонов документов <TemplateSendTask>`



.. _Organization-GetTemplate:
.. method:: Organization.GetTemplate(TemplateId)

  :TemplateId: ``строка`` идентификатор шаблона

  Возвращает :doc:`шаблон документа <Template>` по его идентификатору



.. _Organization-CreateTransformTemplateTask:
.. method:: Organization.CreateTransformTemplateTask(TemplateId)

  :TemplateId: ``строка`` идентификатор шаблона

  Возвращает :doc:`задание для создания документов из шаблона <TransformTemplateTask>`



.. _Organization-RecycleDraft:
.. method:: Organization.RecycleDraft(DraftId)

  :DraftId: ``строка`` идентификатор черновика

  удаляет черновик



.. _Organization-SaveUserDataXSD:
.. method:: Organization.SaveUserDataXSD(TitleName, Function, Version, DocflowSide, FilePath)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа
  :DocflowSide: ``строка`` сторона документооборота. |Organization-DocflowSide|_
  :FilePath: ``строка`` полное имя файла, в который нужно сохранить описание контента

  Сохраняет описание контента документа на диск. Значения для **TitleName**, **Function**, **Version** можно получить в ответе метода :meth:`Organization.GetDocumentTypes`

  .. versionadded:: 5.27.0


.. _Organization-GetBase64UserDataXSD:
.. method:: Organization.GetBase64UserDataXSD(TitleName, Function, Version, DocflowSide)

  :TitleName: ``строка`` название типа документа
  :Function: ``строка`` функция документа
  :Version: ``строка`` версия документа
  :DocflowSide: ``строка`` сторона документооборота. |Organization-DocflowSide|_

  Возвращает Base64 строку описания контента документа. Значения для **TitleName**, **Function**, **Version** можно получить в ответе метода :meth:`Organization.GetDocumentTypes`

  .. versionadded:: 5.28.3


.. _Organization-CreateDataTask:
.. method:: Organization.CreateDataTask()

  Создаёт :doc:`задание для работы с хранилищем ключей-значений Диадок <DataTask>`

  .. versionadded:: 5.29.9



.. rubric:: Дополнительная информация

.. |Organization-CounteragentStatus| replace:: Возможные значения
.. _Organization-CounteragentStatus:

============================= ==============================================================================
Значение *CounteragentStatus* Описание
============================= ==============================================================================
IsMyCounteragent              отношение партнерства установлено и действует
InvitesMe                     контрагент прислал запрос на установление отношения партнерства
IsInvitedByMe                 в адрес контрагента был отправлен запрос на установление отношения партнерства
Rejected                      отношение партнерства было разорвано или запрос партнёрства был отклонен
============================= ==============================================================================


.. |Organization-FormalDocumentType| replace:: Возможные значения
.. _Organization-FormalDocumentType:

=============================== ======================================================================================================
Значение *FormalDocumentType*   Описание
=============================== ======================================================================================================
InvoiceContent                  счет-фактура или исправительный счет-фактура в формате 93 приказа ФНС
InvoiceCorrectionContent        корректировочный счет-фактура или исправление корректировочного счета-фактуры в формате 93 приказа ФНС
XmlAcceptanceCertificateContent акт о выполнении работ в формате 172 приказа ФНС
XmlTorg12Content                ТОРГ-12 в формате 172 приказа ФНС
UniversalTransferDocument       универсальный передаточный документ в формате 155 приказа ФНС
UniversalCorrectionDocument     универсальный корректировочный документ в формате 189 приказа ФНС
UtdTorg12                       формализованный ТОРГ-12 в формате 155 приказа ФНС
UtdAcceptanceCertificate        формализованный акт о выполнении работ в формате 155 приказа ФНС
UtdInvoice                      счет-фактура в формате 155 приказа ФНС
UcdInvoiceCorrection            корректировка счета-фактуры в формате 189 приказа ФНС
TovTorg                         Торг-12 в формате 551-го приказа ФНС
XmlAcceptanceCertificate552     акт в формате 552-го приказа ФНС
=============================== ======================================================================================================


.. |Organization-DocumentType| replace:: Возможные значения
.. _Organization-DocumentType:

=============================== ======================================================================================================
Значение *DocumentType*         Описание
=============================== ======================================================================================================
InvoiceContent                  счет-фактура, исправление счета-фактуры в формате 93 приказа ФНС
UtdInvoice                      счет-фактура в формате 155 приказа ФНС
InvoiceCorrectionContent        корректировочный счет-фактура, исправление корректировочного счета-фактуры в формате 93 приказа ФНС
UcdInvoiceCorrection            корректировка счета-фактуры в формате 189 приказа ФНС
AcceptanceCertificateContent    неформализованный акт о выполнении работ
XmlAcceptanceCertificateContent акта в формате 172 приказа ФНС
UtdAcceptanceCertificate        формализованный акт о выполнении работ в формате 155 приказа ФНС
XmlAcceptanceCertificate552     акт в формате 552-го приказа ФНС
Torg12Content                   неформализованный ТОРГ-12
XmlTorg12Content                Торг-12 в формате 172 приказа ФНС
UtdTorg12                       формализованный ТОРГ-12 в формате 155 приказа ФНС
TovTorg                         Торг-12 в формате 551 приказа ФНС
UniversalTransferDocument       УПД в формате 155 приказа ФНС
NonformilizedDocumentContent    произвольный неформализованный документ
ProformaInvoiceContent          неформализованный счета на оплату
XmlContent                      произвольный формализованный документ в формате xml
Contract                        договор
CertificateRegistry             реестр сертификатов
PriceListAgreement              протокол согласования цены
ReconciliationAct               акт сверки
ServiceDetails                  детализация
=============================== ======================================================================================================


.. |Organization-TitleType| replace:: Возможные значения
.. _Organization-TitleType:

==================== =====================================================
Значение *TitleType* Описание
==================== =====================================================
UtdSeller            титул продавца УПД, сформированного по 155 приказу
UtdBuyer             титул покупателя УПД, сформированного по 155 приказу
Utd820Buyer          титул покупателя УПД, сформированного по 820 приказу
UcdSeller            титул продавца УКД
UcdBuyer             титул покупателя УКД
TovTorg551Seller     титул продавца торг-12 в формате 551-го приказа ФНС
TovTorg551Buyer      титул покупателя торг-12 в формате 551-го приказа ФНС
AccCert552Seller     титул продавца акта в формате 552-го приказа ФНС
AccCert552Buyer      титул покупателя акта в формате 552-го приказа ФНС
==================== =====================================================


.. |Organization-DocflowSide| replace:: Возможные значения
.. _Organization-DocflowSide:

======================= =================
Значение *DocflowSide*  Описание
======================= =================
Seller                  Титул отправителя
Buyer                   Титул получателя
======================= =================
