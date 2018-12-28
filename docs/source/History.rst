История изменений внешней компоненты
====================================

v5.25.1 - 10.12.2018
--------------------

- Добавлено свойство Version у объекта :doc:`документа <Document>`. Поле AttachmentVersion использовать не рекомендуется
- У :doc:`сущностей <Entity>`, содержащих шаблон документа добавлено свойство CreatedDocumentIds - коллекция идентификаторов документов, созданных из данной сущности.
- Поддержаны новые версии аттачментов сервера Диадок (см. https://www.diadoc.ru/blog/7840)
- :doc:`Исправлены ошибки <Bugs_5_25>`

v5.25.1 - 10.12.2018
--------------------

- Добавлен :doc:`метод воостановления удалённого документа <RestoreDocument>`
- :doc:`Исправлены ошибки <Bugs_5_25>`

v5.25.0 - 23.11.2018
--------------------

- Добавлена поддержка ставки НДС "20/120"
- Добавлен метод удаления черновика :doc:`Organization.RecycleDraft <RecycleDraft>`
- :doc:`Исправлены ошибки <Bugs_5_25>`

v5.24.2 - 16.11.2018
--------------------

- Добавлена возможность работы с шаблонами документов
- :doc:`Исправлены ошибки <Bugs_5_24>`

v5.23.0 - 10.10.2018
--------------------

- поддержка криптографии по ГОСТ Р 34.10-2012

v5.22.5 - 01.10.2018
--------------------
- :doc:`Исправлены ошибки <Bugs_5_22>`

v5.22.4 - 03.09.2018
--------------------
- :doc:`Исправлена ошибка <Bugs_5_22>`

v5.22.3 - 31.08.2018
--------------------

- Объекту :doc:`PersonalCertificate <PersonalCertificate>` добавлено поле **CanEncrypt**
- :doc:`Исправлены ошибки <Bugs_5_22>`

v5.22.2 - 20.08.2018
--------------------

- Поле объекта :doc:`ContractToSend <ContractToSend>` ContractPrice устаревшее. Вместо него используйте поле Price
- Добавлено поле IsLiquidated для объекта :doc:`Counteragent <Counteragent>`
- Улучшена стабильность
- :doc:`Исправлены ошибки <Bugs_5_22>`

v5.22.1 - 09.08.2018
--------------------

- В объект :doc:`UserPermissions <UserPermissions>` добавлено индикатор права пользователя на создание документов CanCreateDocuments
- Улучшена стабильность
- :doc:`Исправлены ошибки <Bugs_5_22>`


v5.22.0 - 31.07.2018
--------------------

- У объекта :doc:`Document <Document>` появился метод SaveBuyerContent для сохранения только ответного титула двухтитульного документа
- :doc:`Исправлены ошибки <Bugs_5_22>`

v5.21.10 - 05.07.2018
---------------------

- Поле **Type** объекта :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` больше не имеет значения по умолчанию
- В документации по контентам отправки формализованных документов добавлены ссылки на формат
- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.21.9 - 20.06.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.21.8 - 30.05.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.21.7 - 29.05.2018
--------------------

- Добавлено логирование ошибок у объекта :doc:`ReceiptGenerationProcess`

- Метод :doc:`GetDocumentEventList` стал быстрее и стал возвращать информацию по событиям, не изменяющим статус документа

v5.21.6 - 21.05.2018
--------------------

- возможность сохранения сгенерированных xml-файлов содержимого формализованных документов при отправке - свойства :doc:`PackageSendTask.SaveContentPath <PackageSendTask>` и :doc:`SendTask.SaveContentPath <SendTask>`

v5.21.5 - 18.05.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.21.4 - 08.05.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.21.3 - 17.04.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.21.2 - 30.03.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_21>`


v5.21.1 - 26.03.2018
--------------------

- поддержка ставки НДС - "ИсчНалАг" - НДС исчисляется налоговым агентом
- :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>` и методы SendReceiptsAsync у различных документов теперь поддерживают работу с неформализованными документами с запросом ИОП
- метод :doc:`GetAnyComment <GetAnyComment>` теперь поддерживает получение комментария к титулу покупателя - "RecipientAttachmentComment"
- поддержка версий содержимого для документов "любого типа": utd_05_01_01, utd_05_01_02, ucd_05_01_01, rezru_05_01_01, tovtorg_05_01_02, act_05_01_01, act_05_01_02, invoice_05_01_01, invoice_05_01_03, invoice_05_02_01, invoicecor_05_01_03, invoicecor_05_02_01, torg12_05_01_01, torg12_05_01_02

v5.21.0 - 13.03.2018
--------------------

- расширена поддержка документов "любого типа":
    - у базового объекта :doc:`Document <Document>` появились новые свойства:
        - **TypeNamedId** - строковый идентификатор типа документа
        - **DocumentFunction** - функция документа 
        - **WorkflowId** - идентификатор типа документооборота
        - **Metadata** - коллекция метаданных
        - новые статусы и метаданные **RecipientReceiptMetadata**, **ConfirmationMetadata**, **RecipientResponseStatus**, **AmendmentRequestMetadata**
    - мапинг содержимого документов "любого типа" на объектную модель документов компоненты:
        - поддержка получения документов "любого типа" в представлении :doc:`BaseDocument <BaseDocument>`
        - поддержка отправки документов "любого типа" в :doc:`PackageSendTask <PackageSendTask>` - возможность добавлять :doc:`CustomDocumentToSend <CustomDocumentToSend>` для конкретного типа содержимого AttachmentVersion Diadoc API (поддерживаются: utd_05_01_01, utd_05_01_02, ucd_05_01_01, rezru_05_01_01, tovtorg_05_01_02)

- новое свойство **Title** у объекта :doc:`Document <Document>` - название документа
- :doc:`Исправлены ошибки <Bugs_5_21>`

v5.20.3 - 06.02.2018
--------------------

- добавлен универсальный метод получения комментариев - :doc:`GetAnyComment <GetAnyComment>`

- в :doc:`Utd <Utd>` и :doc:`Ucd <Ucd>` появились признаки: **Revised** (было ли исправление данного документа) и **Corrected** (была ли корректировка данного документа)

- методы используемые для получения контрагентов (:doc:`GetCounteragentById <GetCounteragentById>`, :doc:`GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>`) теперь используют /V2/GetCounteragent АПИ Диадок

- метод :doc:`AcquireCounteragent <AcquireCounteragent>` стал блокирующим, теперь ожидается завершение асинхронного вызова со стороны АПИ Диадок - генерирует исключения в случае получения ошибочных кодов состояния со стороны АПИ Диадок

- свойство **AdressText** объекта :doc:`AddressInfo <AddressInfo>` для  :doc:`XmlTorg12 <XmlTorg12>` и :doc:`XmlAcceptanceCertificate <XmlAcceptanceCertificate>`, теперь предтавляет строку иностранного адреса или неструктурированного российского адреса.

- улучшена совместимость COM-компоненты с Microsoft VB6 и Microsoft VBA (Microsoft Office)

- :doc:`Исправлены ошибки <Bugs_5_20>`

v5.20.2 - 29.01.2018
--------------------

- :doc:`Исправлены ошибки <Bugs_5_20>`

v5.20.1 - 17.01.2018
---------------------

- :doc:`Исправлены ошибки <Bugs_5_20>`

v5.20.0 - 25.12.2017
---------------------

- добавлена поддержка работы с "документом любого типа":
    
    - поддержка типа документа "Document" для методов :doc:`AddDocumentFromFile <AddDocumentFromFile>` и :doc:`AddDocumentFromFileRaw <AddDocumentFromFileRaw>` объекта :doc:`PackageSendTask <PackageSendTask>`

    - метод :doc:`GetDocumentTypes <GetDocumentTypes>` - возвращает описание типов документов, доступных в ящике

- :doc:`Исправлены ошибки <Bugs_5_20>`

v5.19.4 - 12.12.2017
---------------------

- :doc:`Исправлены ошибки <Bugs_5_19>`

v5.19.3 - 11.12.2017
--------------------

- :doc:`Исправлены ошибки <Bugs_5_19>`

v5.19.2 - 27.11.2017
--------------------

- исправлена ошибка: при отправке шифрованного счета-фактуры с помощью :doc:`PackageSendTask <PackageSendTask>` и :doc:`SendTask <SendTask>` не заполнялось свойство DocumentNumber, что приводило к исключению "Incorrect EncryptedInvoiceAttachment: Metadata.DocumentDateAndNumber.DocumentNumber should be filled"

v5.19.1 - 20.11.2017
--------------------

- CustomData - коллекция "ключ-значение" для объекта :doc:`Document <Document>`:
    
    - свойство :doc:`Document.CustomData <Document>` - коллекция объектов :doc:`CustomDataItem <CustomDataItem>` содержащих записи "ключ-значение"

    - метод :doc:`Document.CreateCustomDataPatchTask <Document>` - создает :doc:`CustomDataPatchTask <CustomDataPatchTask>`, позволяющий редактировать коллекцию :doc:`Document.CustomData <Document>`

- В :doc:`Ucd <Ucd>` добавлены свойства OriginalInvoiceNumber, OriginalInvoiceDate, OriginalInvoiceRevisionNumber, OriginalInvoiceRevisionDate

- :doc:`Исправлены ошибки <Bugs_5_19>`

v5.19.0 - 20.10.2017
--------------------

- Новые типы :doc:`документов <Document>`: TovTorg (формат 551-го приказа ФНС для торг-12), XmlAcceptanceCertificate552 (формат 552-го приказа ФНС для актов)
- "Ленивая" загрузка свойства **TargetUser** объекта :doc:`Resolution <Resolution>`
- COM-компонента, проверка функции УПД/УКД для действий :doc:`ReplySendTask <ReplySendTask>`

v5.18.7 - 05.09.2017
--------------------

- в :doc:`PersonalCertificate <PersonalCertificate>` добавлено поле **JobTitle** - должность
- в COM-компоненте добавлена поддержка типа UcdInvoiceCorrection для объекта :doc:`PackageSendTask <PackageSendTask>`
- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.6 - 18.08.2017
--------------------

- оптимизация получения поля **ResolutionStatus** объектов :doc:`Document <Document>`
- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.5 - 14.08.2017
--------------------

- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.4 - 03.08.2017
----------------------

- Исправлена ошибка: попытка получения объекта :doc:`Counteragent <Counteragent>`, для удаленной организации, с помощью :doc:`GetCounteragentById <GetCounteragentById>` приводила к краху компоненты
- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.3 - 02.08.2017
----------------------

- В :doc:`Document <Document>` добавлено свойство **SenderSignatureStatus** - статус проверки ЭЦП отправителя
- Тип объекта :doc:`UtdToSend <UtdToSend>` - свойство **Type**, теперь соответствует типу создаваемого документа UniversalTransferDocument, UtdInvoice, UtdTorg12 или UtdAcceptanceCertificate
- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.2 - 18.07.2017
----------------------

- Свойство **EncryptedDocumentsAllowed** у объекта :doc:`Organization <Organization>` -  для организации разрешена отправка зашифрованных документов
- Теперь файлы подписи получаемые в результате выполнения метода :doc:`SaveAllContent <SaveAllContent>` сохраняются с расширением .sgn
- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.1 - 21.06.2017
----------------------

- В :doc:`Organization <Organization>` добавлен метод :doc:`GetCounteragentByOrgId <GetCounteragentByOrgId>` - возвращает контрагента, по указанному идентификатору организации
- В объекте :doc:`Department <Department>` появилось поле **Address** - адрес подразделения организации
- :doc:`Исправлены ошибки <Bugs_5_18>`

v5.18.0 - 29.05.2017
----------------------

- Поддержка корректировочных счетов-фактур(:doc:`InvoiceCorrection <InvoiceCorrection>` и :doc:`InvoiceCorrectionRevision <InvoiceCorrectionRevision>`) с УКД-контентом(:doc:`UcdSellerContent <UcdSellerContent>`) - новый тип контента при отправке **UcdInvoiceCorrection**
- К :doc:`OrganizationInfo <OrganizationInfo>` добавлено поле **FnsParticipantId** - идентификатор участника ЭДО
- Появилась возможность задавать атрибуты подписантов при отправке черновиков сообщений: новый тип :doc:`SendDraftTask <SendDraftTask>`,а также метод-конструктор :doc:`CreateSendDraftTask <CreateSendDraftTask>`.

v5.17.1 - 18.05.2017
----------------------

- Поддержка документов старых типов с упд-контентом(UtdInvoice, UtdAcceptanceCertificate, UtdTorg12) в :doc:`AddDocumentFromFileRaw <AddDocumentFromFileRaw>` и :doc:`CreateSendTaskFromFileRaw <CreateSendTaskFromFileRaw>`
- Поддержка шифрования для InvoiceCorrection и InvoiceCorrectionRevision

Исправлены ошибки:

- генерация корректных метаданных для шифрованных документов
- корректное получение титула покупателя для шифрованных документов - методы GetBuyerContent

v5.17 - 05.05.2017
----------------------

- Различные изменения COM-компоненты связанные с поддержкой многопоточности, поддержка режима MTA
- Расширена поддержка прокси: добавлена поддержка HTTP-ответа 407(Proxy Authentication Required) - запрос авторизации на прокси-сервере
- Расширен метод :doc:`AddContent <AddContent>`, объекта :doc:`CloudSignTask <CloudSignTask>`
- Автоматический расчет всех полей сумм в :doc:`Torg12Totals <Torg12Totals>` для :doc:`Torg12Content <Torg12Content>`
- У объектов :doc:`Utd <Utd>`, :doc:`UtdRevision <UtdRevision>`, :doc:`Ucd <Ucd>`, :doc:`UcdRevision <UcdRevision>` расширена поддержка работы с запросами на уточнение: добавлено свойство **AmendmentRequested** и метод :doc:`GetAmendmentRequestedComment <GetAmendmentRequestedComment-(Utd)>`
- Измененено поведение метода :doc:`GetCounteragentListByInnList <GetCounteragentListByInnList>` - теперь для одного ИНН возвращаеться весь набор организаций
- В базовый объект документа :doc:`Document <Document>` добавлено свойство **AttachmentVersion** - информация о версии XSD схемы, в соотвествии с которой сформирован документ
- Оптимизация работы объекта :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>`

Исправлены ошибки:

- Ошибка времени исполнения в COM-компоненте при добавлении элементов в некоторые коллекции объектов поддержки УКД
- Ошибка, связи с которой у объектов :doc:`Invoice <Invoice>` :doc:`InvoiceRevision <InvoiceRevision>`, :doc:`InvoiceCorrection <InvoiceCorrection>`, :doc:`InvoiceCorrectionRevision <InvoiceCorrectionRevision>` не работал метод :doc:`SendReceiptsAsync <SendReceiptsAsync>`
- Исправлена работа метода :doc:`GetRecipientSignature <GetRecipientSignature>` для УПД с функцией "СЧФ" и УКД с функцией "КСЧФ"
- :doc:`InvoiceRevision <InvoiceRevision>` теперь поддерживает УПД-содержимое

v5.16 - 10.04.2017
----------------------

- Поддержка УКД в компоненте:
    - Новый тип отправляемого документа для :doc:`CreateSendTask <CreateSendTask>`: **UniversalCorrectionDocument**
    - Новые типы отправляемых документов для :doc:`AddDocument <AddDocument>`: **UniversalCorrectionDocument** и **UniversalCorrectionDocumentRevision**. Соответствующий новый тип возвращаемого значения - :doc:`UcdToSend <UcdToSend>`
    - Новый тип контента :doc:`UcdSellerContent <UcdSellerContent>`
    - Новые типы документов :doc:`Document <Document>`: :doc:`Ucd <Ucd>` и :doc:`UcdRevision <UcdRevision>`
    - Изменилась сигнатура :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>`, теперь принимает аргумент **forCorrection**
    - В :doc:`SetExtendedSignerDetailsTask <SetExtendedSignerDetailsTask>` появилось свойство **ForCorrection**
- Изменилась сигнатура и семантика :doc:`CanSendInvoice <CanSendInvoice>` - определяет можно ли подписывать счета-фактуры переданным сертификатом
- Для :doc:`Utd <Utd>` и :doc:`UtdRevision <UtdRevision>` реализована отправка ИоП - методы: :doc:`SendReceiptsAsync <SendReceiptsAsync-(Utd)>` и :doc:`SendReceiptsAsync <SendReceiptsAsync-(UtdRevision)>`
- Поддержка отправки "с полки" в :doc:`SendTask <SendTask>` и :doc:`PackageSendTask <PackageSendTask>` - свойство **UseShelf**
- Методы :doc:`Send <Send-(AcquireCounteragentTask)>` и :doc:`SendAsync <SendAsync-(AcquireCounteragentTask)>` теперь возвращают идентификатор организации
- :doc:`Исправлены ошибки <Bugs_5_16>`


v5.15 - 15.03.2017
----------------------

- Асинхронная отправка извещений о получении конкретного УПД. У объекта документа УПД :doc:`Utd <Utd>` появился метод :doc:`SendReceiptsAsync <SendReceiptsAsync-(Utd)>`
- В объекте :doc:`Organization <Organization>` появился метод :doc:`CanSendInvoice <CanSendInvoice>` - позволяет узнать, был ли переданный сертификат зарегистрирован в ФНС в качестве сертификата, используемого для подписания электронных счетов-фактур, отправляемых участником ЭДО, которому принадлежит ящик boxId
- В объекте :doc:`Counteragent <Counteragent>` появилось свойство **LastEventTimestampTicks** - метка времени последнего события из истории взаимодействия с данным контрагентом
- В объекте :doc:`UserPermissions <UserPermissions>` появилось свойство **JobTitle** - должность сотрудника
- В объекте базового документа :doc:`Document <Document>` появилось свойство **PackageId** - идентификатор пакета
- Полная поддержка исправительных УПД
- Исправлена работа :doc:`CreateReplySendTask <CreateReplySendTask-(Document)>` для старых типов документов с УПД-содержимым

v5.14 - 20.01.2017
----------------------

- Поддержка УПД-содержимого для "старых" типов документов (Торг12, Акт, Счет-фактура):
    - Новые типы документов для :doc:`SendTask <SendTask>` и :doc:`PackageSendTask <PackageSendTask>`: UtdTorg12, UtdAcceptanceCertificate, UtdInvoice.
    - Содержимое типа UniversalTransferDocument в :doc:`Invoice <Invoice>`, :doc:`XmlTorg12 <XmlTorg12>` и :doc:`XmlAcceptanceCertificate <XmlAcceptanceCertificate>`.
- Поддержка УПД и УКД при скачивании файлов по документообороту - :doc:`SaveAllContent <SaveAllContent>` и :doc:`SaveAllContentAsync <SaveAllContentAsync>`.
- Реализована поддержка шифрования для акта, торг12 и счета-фактуры:
    - Список сертификатов контрагента :doc:`GetCertificates <GetCertificates>`.
    - Возможность задать сертификаты шифрования :doc:`AddEncryptCertificate <AddEncryptCertificate-(SendTask)>` в :doc:`SendTask <SendTask>` и :doc:`AddEncryptCertificate <AddEncryptCertificate-(PackageSendTask)>` в :doc:`PackageSendTask <PackageSendTask>`.
    - Флаг шифрованного документа **IsEncryptedContent** в :doc:`Document <Document>`.
- Возможность отказа от запроса подписи сотрудника:
    - :doc:`ResolutionRequest <ResolutionRequest>` - запрос на согласование, возможен отказ и отмена.
    - :doc:`ResolutionRequestDenial <ResolutionRequestDenial>` - объект отмены запроса на согласование, возможен отказ. 
    - Свойство **ResolutionRequests** в :doc:`Document <Document>` - коллекция запросов на согласование(:doc:`коллекция <Collection>` объектов :doc:`ResolutionRequest <ResolutionRequest>`).
    - Свойство **ResolutionRequestDenials** в :doc:`Document <Document>` - коллекция объектов отмены запросов на согласование(:doc:`коллекция <Collection>` объектов :doc:`ResolutionRequestDenial <ResolutionRequestDenial>`).
- Возможность "сырой" отправки xml-файлов формализованных документов:
    - Метод :doc:`CreateSendTaskFromFileRaw <CreateSendTaskFromFileRaw>`.
    - Метод :doc:`AddDocumentFromFileRaw <AddDocumentFromFileRaw>`.
- :doc:`AddCertToFnsRegistrationMessage <AddCertToFnsRegistrationMessage>` переименован в :doc:`SendFnsRegistrationMessage <SendFnsRegistrationMessage>`.
- Исправлен :doc:`MarkAsRead <MarkAsRead>`.
- Сериализация счета-фактуры с учетом версии формата.
- :doc:`Исправлены ошибки <Bugs_5_14>`

v5.10 - 25.11.2016
-----------------------

- Реализована поддержка универсального передаточного документа:
    - добавлен :doc:`Utd <Utd>`, предназначенные для работы с УПД.
    - добавлен :doc:`UtdSellerContent <UtdSellerContent>`, предназначенный для работы с титулом продавца в УПД.
    - добавлен :doc:`UtdBuyerContent <UtdBuyerContent>`, предназначенный для работы с титулом покупателя в УПД.
    - в объекты :doc:`SendTask <SendTask>`, :doc:`PackageSendTask <PackageSendTask>` и :doc:`ReplySendTask <ReplySendTask>` добавлена поддержка УПД.
    - в :doc:`OutDocumentSignTask <OutDocumentSignTask>` добавлен метод :doc:`AddExtendedSigner <AddExtendedSigner>` для поддержки подписания исходящих УПД.
- Реализованы методы для работы с базой подписантов Диадок:
    - в :doc:`Organization <Organization>` добавлены методы :doc:`CreateSetExtendedSignerDetailsTask <CreateSetExtendedSignerDetailsTask>` и :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>`.
- В :doc:`Document <Document>` добавлен статус "прочтен":
    - свойство **IsRead**.
    - метод :doc:`MarkAsRead <MarkAsRead>`.
- :doc:`Исправлены ошибки <Bugs_5_10>`

v5.9 - 17.11.2016
-----------------------

- В :doc:`AcquireCounteragentTask <AcquireCounteragentTask>` добавлен метод :doc:`Send <Send-(AcquireCounteragentTask)>` для синхронной отправки приглашений.
- Исправлено поведение для неформализованных актов, накладных и счетов на оплату: налоговая ставка устанавливается в значение "без НДС", если не указывать ее значение в поле содержимого Vat.
- Исправлена проблема при отправке счетов-фактур с участием агента.
- Исправлена ошибка при отправке контрагенту приглашения к сотрудничеству с вложением файла.


v5.8 - 26.10.2016
-----------------------

- Добавлена возможность сохранять содержимое документа в ZIP-архив:
    - в :doc:`Document <Document>` добавлен метод :doc:`SaveAllContentZip <SaveAllContentZip>` и :doc:`SaveAllContentZipAsync <SaveAllContentZipAsync>`.


v5.7 - 15.09.2016
-----------------------

- Исправлены ошибки при работе через прокси	
- Исправлена ошибка валидации номера ГТД в счете-фактуре.


v5.6 - 18.04.2016
-----------------------

- Добавлена возможность подписания и отправки исходящих документов с отложенной отправкой:
    - в :doc:`Document <Document>` добавлен метод :doc:`CreateOutDocumentSignTask <CreateOutDocumentSignTask-(Document)>` и
      в :doc:`DocumentPackage <DocumentPackage>` добавлен метод :doc:`CreateOutDocumentSignTask <CreateOutDocumentSignTask-(DocumentPackage)>` 
      для создания задания на подписание и отправку исходящего документа или пакета  документов соответственно. Эти методы возвращают объект
      :doc:`OutDocumentSignTask <OutDocumentSignTask>`.
    - добавлен :doc:`OutDocumentSignTask <OutDocumentSignTask>`, представляющий собой задание на подписание и отправку исходящего документа.
      С помощью его методов :doc:`Send <Send-(OutDocumentSignTask)>` или :doc:`SendAsync <SendAsync-(OutDocumentSignTask)>` можно подписать
      и отправить исходящий документ, который прежде был отправлен с выставленным флагом **DelaySend**.
- :doc:`Исправлены ошибки <Bugs_5_6>`


v5.5 - 08.04.2016
-----------------------

- Добавлена возможность для отправки пакета документов:
    - в объекте :doc:`Organization <Organization>` добавлен метод :doc:`CreatePackageSendTask <CreatePackageSendTask>` для создания задания на отправку пакета документов, который возвращает :doc:`PackageSendTask <PackageSendTask>`.
    - добавлен :doc:`PackageSendTask <PackageSendTask>` для работы с заданием на отправку пакета документов.
    - добавлен :doc:`DocumentToSend <DocumentToSend>` и производные от него объекты, предназначенные для работы с документами на отправку, входящими в пакет.
    - добавлен :doc:`SentPackageContent <SentPackageContent>` для передачи в задание на подпись содержимого сертификатом электронной подписи СКБ Контур всех документов из пакета на отправку.
- В :doc:`DiadocConnection <Connection>` добавлен метод :doc:`GetMyUser <GetMyUser>`, позволяющий получить данные о текущем 
  авторизованном пользователе.
- В :doc:`Organization <Organization>` добавлены методы :doc:`SetData <SetData>` и :doc:`GetData <GetData>`, позволяющие 
  добавлять и извлекать пары вида "ключ-значение" в хранилище.
- В метод :doc:`GetPersonalCertificates <GetPersonalCertificates>` объекта :doc:`интерфейса "Диадок" <Root-method>` добавлен входной параметр UserStore,
  позволяющий искать сертификаты не только в хранилище текущего пользователя, но и в хранилище машины.
- :doc:`Исправлены ошибки <Bugs_5_5>`


v5.4 - 22.01.2016
-----------------------

- Добавлены инструменты для отслеживания роуминговых документов:
    - в объекте :doc:`Document <Document>` добавлены свойства RoamingNotificationStatus и RoamingNotificationStatusDescription.
    - в объекте :doc:`Counteragent <Counteragent>` добавлено свойство IsRoaming.
- :doc:`Исправлены ошибки <Bugs_5_4>`



v5.3 - 21.12.2015
-----------------------

- Добавлена возможность работы с пакетами документов:
    - в объекте :doc:`Document <Document>` добавлено свойство IsLockedPackage и метод :doc:`GetDocumentPackage <GetDocumentPackage>`
      для получаения пакета, в который включен документ.
    - добавлен :doc:`DocumentPackage <DocumentPackage>` для работы с пакетами документов.
- :doc:`Исправлены ошибки <Bugs_5_3>`



v5.2.0 - 01.12.2015
-----------------------

- Добавлена возможность подписания документов электронной подписью СКБ Контур:
    - добавлен метод :doc:`GetCloudCertificates <GetCloudCertificates>` в :doc:`DiadocConnection <Connection>` для получения списка сертификатов СКБ Контур, доступных пользователю
    - добавлены объекты: :doc:`CloudCertificateInfo <CloudCertificateInfo>` (для информации о сертификате СКБ Контур), :doc:`CloudSignTask <CloudSignTask>` (для задание на подписание документов электронной подписью СКБ Контур).
- :doc:`Исправлены ошибки <Bugs_5_2>`


v5.1 - 28.10.2015
-----------------------

- Добавлена возможность указания отрицательного количества единицы товара (услуги) в актах.
- Добавлена поддержка множественных ГТД в счетах-фактурах.
- Добавлена поддержка нулевых значений суммы с учетом НДС для документов ТОРГ-12.
- :doc:`Исправлены ошибки <Bugs_5_1>`


v5.0.0 - 03.07.2015
-------------------

Реализованы новые модели для работы с документами "счет-фактура", "корректировочный счет-фактура", учитывающие все особенности формата 5.02

- для объекта  :doc:`InvoiceContent <InvoiceContent>`
   - вместо реквизита **AdditionalInfo** с типом "строка" введен реквизит **StructedAdditionalInfos**, который представляет собой :doc:`коллекцию <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`
   - налогичные изменения произведены для :doc:`InvoiceItem <InvoiceItem>`

- для объекта  :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>`
   - вместо реквизита **AdditionalInfo** с типом "строка" введен реквизит **StructedAdditionalInfos**, который представляет собой :doc:`коллекцию <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`
   - налогичные изменения произведены для :doc:`InvoiceCorrectionItem <InvoiceCorrectionItem>`
   - свойства  **Date**, **Number**, **InvoiceRevision Date**, **InvoiceRevisionNumber** удалены из объекта. Вместо них добавлено свойство **OriginalInvoices**
 

v4.2.0 - 13.04.2015
-------------------

Реализована работа с форматом 5.02 для документов "счет-фактура", "корректировочный счет-фактура":

- Для объектов :doc:`InvoiceContent <InvoiceContent>`, :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>` добавлено свойство **InvoiceVersion**, которое возвращает формат счета-фактуры.

- При отправке счета-фактуры, корректировочного счета-фактуры с помощью объекта :doc:`CreateSendTask <CreateSendTask>`, по умолчанию для отправляемого счета-фактуры устанавливается формат, актуальный на дату отправки. При необходимости отправки счета-фактуры в другом формате, необходимо его указывать в свойстве **InvoiceVersion**.


v4.1.0 - 24.02.2014
-------------------

-  Появилась возможность отправки черновиков :doc:`SendDraftAsync <SendDraftAsync>`


v4.0.0 - 13.02.2014
-------------------

-  Появилась сборка COM-объекта, скомпилированная для 64-битных ОС


v3.10.0.27 - 08.09.2014
-----------------------

- Объекту Документ добавлено свойство **HasCustomPrintForm**.

- Появилась возможность формирование печатной формы документа GetPrintForm.

- Для СФ появилась возможность формировать и подписывать документы по регламентному документооборота.


v3.0.08.21 - 23.07.2014
-----------------------

- Появилась поддержка внутренних документов. Для отправки внутреннего документа, в задании на отправку документа (объект SendTask), необходимо установить флаг IsInternal, и указать идентификаторы подразделений FromDepartmentId/ToDepartmentId. Значение свойства CounterAgentId при этом, должно оставаться пустым.

- Объекту Документ добавлены свойства FromDepartment/ToDepartment.

- Объекту Контрагент добавлено свойство Address.


v3.0.07.01 - 09.04.2014
-----------------------

- Появилась поддержка новых типов полуформализованных документов - договоров, протоколов согласования цены, детализаций, реестров сертификатов.

- При установке соединения через метод CreateConnectionByCertificate, можно указать пароль к ключевому контейнеру сертификата. При указании пароля, окно крипто-провайдера для его ввода, отображаться не будет.﻿


v3.0.03.01 - 15.02.2014
-----------------------

-  Появилась возможность аннулирования документов. Для отправки предложения об аннулировании используется метод :doc:`SendRevocationRequest <SendRevocationRequest>` документа. Для принятия предложения об аннулировании необходимо вызвать :doc:`AcceptRevocationRequest <AcceptRevocationRequest>`, для отказа от предложения об аннулировании -  :doc:`RejectRevocationRequest <RejectRevocationRequest>`.


v3.0.2 - 21.01.2014
-------------------

-  Выпущена редакция компоненты 3.0.
