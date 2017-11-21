Документы
=========

Объект Document является базовым объектом для всех типов документов. Он обладает базовым набором свойств и методов, которые также
работают для всех производных типов документов. Объекты всех производных
типов предназначены для:

-  получения данных о документе в системе Диадок
-  выполнением действий, подразумеваемых документооборотом по
   конкретному типу документа.

Тип ConnectionRequest имеет те же свойства и методы, что и тип Document.

Свойства объекта
----------------


- **Type** (строка, чтение) - тип документа

- **OrganizationId** (строка, чтение) - идентификатор организации, которой принадлежит документ

- **DocumentId** (строка, чтение) - идентификатор документа

- **PathURL** (строка, чтение) - URL документа, по которому он доступен в web-интерфейсе

- **Direction** (строка, чтение) - направление документа

- **Organization** (объект :doc:`Organization <Organization>`, чтение) - организация, которая отправила исходящий документ, либо получила входящий документ

- **Department** (объект :doc:`Department <Department>`, чтение) - подразделение организации, к которому привязан документ

- **FromDepartment** (объект :doc:`Department <Department>`, чтение) - подразделение организации, из которого был отправлен документ

- **ToDepartment** (объект :doc:`Department <Department>`, чтение) - подразделение организации, в которое был отправлен документ

- **Counteragent** (объект :doc:`Counteragent <Counteragent>`, чтение) - контрагент документа

- **Timestamp** (дата и время, чтение) - дата и время отправки документа (в текущем часовом поясе)

- **TimestampSeconds** (число, чтение) - дата и время отправки документа в секундах

- **FileName** (строка, чтение) - имя документа в Диадоке

- **DocumentDate** (дата, чтение) - дата документа

- **DocumentNumber** (строка, чтение) - номер документа

- **Status** (строка, чтение) - текущий статус документа в Диадоке. Перечень возможных значений зависит от типа документа и описан в спецификации соответствующего производного объекта.

- **InitialDocumentIds** (объект :doc:`Collection <Collection>`, чтение) - коллекция идентификаторов документов, на который ссылается данный документ (т.е. документы, которые по отношению к данному документы являются "родительскими"

- **SubordinateDocumentIds** (объект :doc:`Collection <Collection>`, чтение) - коллекция идентификаторов документов, которые ссылаются на данный документ (т.е. документы, которые по отношению к данному документу являются "дочерними")

- **IsDeleted** (булево, чтение) - признак того, что данный документ был удален

- **IsTest** (булево, чтение) - признак того, что данный документ является тестовым и не имеет юридической силы

- **OneSDocumentId** (строка, чтение) - идентификатор документа в 1С

- **ResolutionStatus** (объект :doc:`ResolutionStatus <ResolutionStatus>`, чтение) - текущий статус согласования документа

- **Resolutions** (:doc:`коллекция <Collection>` объектов :doc:`Resolution <Resolution>`, чтение) - история согласования документа

- **CustomDocumentId** (строка, чтение) - идентификатор документа, определяемый внешней системой

- **RevocationStatus** (строка, чтение) - статус аннулирования документа

- **HasCustomPrintForm** (булево, чтение) - признак того, что данный документ имеет нестандартную печатную форму

- **IsLockedPackage** (булево, чтение) - признак того, что документ является частью нередактируемого пакета

- **RoamingNotificationStatus** (строка, чтение) - статус передачи документа через роуминг

- **RoamingNotificationStatusDescription** (строка, чтение) - описание статуса передачи документа через роуминг.

- **IsRead** (булево, чтение) - флаг, указывающий на то, что документ был прочитан сотрудником организации

- **ResolutionRequests** (:doc:`коллекция <Collection>` объектов :doc:`ResolutionRequest <ResolutionRequest>`, чтение) - коллекция запросов на согласование

- **ResolutionRequestDenials** (:doc:`коллекция <Collection>` объектов :doc:`ResolutionRequestDenial <ResolutionRequestDenial>`, чтение) - коллекция объектов отмены запросов на согласование

- **IsEncryptedContent** (булево, чтение) - флаг, указывающий на то, что содержимое документа зашифровано

- **PackageId** (строка, чтение) - идентификатор пакета

- **AttachmentVersion** (строка, чтение) -  информация о версии XSD схемы, в соотвествии с которой сформирован документ

- **SenderSignatureStatus** (строка, чтение) - статус проверки ЭЦП отправителя

- **CustomData** (коллекция :doc:`Collection <Collection>` объектов :doc:`CustomDataItem <CustomDataItem>`, чтение) - коллекция элементов "ключ-значение"

Свойство **Direction** принимает одно из следующих значений:

-  "Inbound" - входящий документ
-  "Outbound" - исходящий документ
-  "Internal" - внутренний документ

Свойство **RevocationStatus** принимает одно из следующих значений:

-  "RevocationStatusNone" - документ не аннулирован, и не было
   предложений об аннулировании
-  "RevocationIsRequestedByMe" - отправлено исходящее предложение об
   аннулировании документа
-  "RequestsMyRevocation" - получено входящее предложение об
   аннулировании документа
-  "RevocationAccepted" - документ аннулирован
-  "RevocationRejected" - получен или отправлен отказ от предложения об
   аннулировании документа
-  "UnknownRevocationStatus" - неизвестный статус аннулирования
   документа

Свойство **RoamingNotificationStatus** принимает одно из следующих значений:

-  "RoamingNotificationStatusNone" - документ не роуминговый или документ без подтверждения доставки в роуминг
-  "RoamingNotificationStatusSuccess" - документ с подтверждением успешной доставки в роуминг
-  "RoamingNotificationStatusError" - документ с ошибкой доставки в роуминг
-  "UnknownRoamingNotificationStatus" - неизвестный роуминговый статус документа

Свойство **SenderSignatureStatus** принимает одно из следующих значений:

- "WaitingForSenderSignature" - ожидается подпись отправителя
- "SenderSignatureUnchecked" - подпись отправителя еще не проверена
- "SenderSignatureCheckedAndValid" - подпись отправителя проверена и валидна
- "SenderSignatureCheckedAndInvalid" - подпись отправителя проверена и невалидна
- "UnknownSenderSignatureStatus" - неизвестный статус проверки подписи

Методы объекта
--------------

-  :doc:`SaveAllContent <SaveAllContent>` - сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию

-  :doc:`SaveAllContentAsync <SaveAllContentAsync>` - асинхронно сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию

-  :doc:`SaveAllContentZip <SaveAllContentZip>` - формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанную директорию

-  :doc:`SaveAllContentZipAsync <SaveAllContentZipAsync>` - асинхронно формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанную директорию

-  :doc:`GetComment <GetComment>` - возвращает комментарий к документу, заданный при отправке

-  :doc:`Move <Move>` - перемещает документ в указанное подразделение

-  :doc:`Delete <Delete>` - помечает документ как удаленный

-  :doc:`SaveContent <SaveContent>` - сохраняет содержимое документа на локальный диск

-  :doc:`Approve <Approve>` - ставит признак согласования документа

-  :doc:`Disapprove <Disapprove>` - ставит признак отказа в согласовании документа

-  :doc:`SetOneSDocumentId <SetOneSDocumentId>` - устанавливает идентификатор 1С для данного документа

-  :doc:`ReSetOneSDocumentId <ReSetOneSDocumentId>` - сбрасывает идентификатор 1С для данного документа

-  :doc:`AddSubordinateOneSDocumentId <AddSubordinateOneSDocumentId-(Document)>` - добавляет дополнительный идентификатор 1С для документа

-  :doc:`RemoveSubordinateOneSDocumentId <RemoveSubordinateOneSDocumentId>` - удаляет дополнительный идентификатор 1С для документа

-  :doc:`CreateResolutionRequestTask <CreateResolutionRequestTask>` - создает задание для отправки запроса на согласование

-  :doc:`GetSenderSignature <GetSenderSignature>` - возвращает подпись отправителя, приложенную к документу

-  :doc:`GetRecipientSignature <GetRecipientSignature>` - возвращает подпись получателя, приложенную к документу

-  :doc:`GetStructuredDataAttachment <GetStructuredDataAttachment>` - возвращает структурированные данные, описывающими те или иные документы, представленные в виде печатных форм

-  :doc:`SendRevocationRequest <SendRevocationRequest>` - отправляет запрос на аннулирование документа

-  :doc:`AcceptRevocationRequest <AcceptRevocationRequest>` - принимает запрос об аннулировании документа

-  :doc:`RejectRevocationRequest <RejectRevocationRequest>` - отклоняет запрос на аннулирование документа

-  :doc:`GetPrintForm <GetPrintForm>` - получает печатную форму документа в формате pdf

-  :doc:`GetDocumentPackage <GetDocumentPackage>` - возвращает пакет, в котором находится документ

-  :doc:`CreateReplySendTask <CreateReplySendTask-(Document)>` - создает задание на выполнение ответного действия с документом

-  :doc:`CreateOutDocumentSignTask <CreateOutDocumentSignTask-(Document)>` - создает задание на подписание и отправку исходящего документа с отложенной отправкой.

-  :doc:`MarkAsRead <MarkAsRead>` - помечает, что документ был прочитан сотрудником организации (устанавливает флаг IsRead)

-  :doc:`CreateCustomDataPatchTask <CreateCustomDataPatchTask>` - создает объект :doc:`CustomDataPatchTask <CustomDataPatchTask>`, позволяющий редактировать коллекцию **CustomData**

.. toctree::
   :name: Auto
   :hidden:

   SaveAllContent <SaveAllContent>
   SaveAllContentAsync <SaveAllContentAsync>
   SaveAllContentZip <SaveAllContentZip>
   SaveAllContentZipAsync <SaveAllContentZipAsync>
   GetComment <GetComment>
   Move <Move>
   Delete <Delete>
   SaveContent <SaveContent>
   Approve <Approve>
   Disapprove <Disapprove>
   SetOneSDocumentId <SetOneSDocumentId>
   ReSetOneSDocumentId <ReSetOneSDocumentId>
   AddSubordinateOneSDocumentId <AddSubordinateOneSDocumentId-(Document)>
   RemoveSubordinateOneSDocumentId <RemoveSubordinateOneSDocumentId>
   CreateResolutionRequestTask <CreateResolutionRequestTask>
   GetSenderSignature <GetSenderSignature>
   GetRecipientSignature <GetRecipientSignature>
   GetStructuredDataAttachment <GetStructuredDataAttachment>
   SendRevocationRequest <SendRevocationRequest>
   AcceptRevocationRequest <AcceptRevocationRequest>
   RejectRevocationRequest <RejectRevocationRequest>
   GetPrintForm <GetPrintForm>
   GetDocumentPackage <GetDocumentPackage>
   CreateReplySendTask <CreateReplySendTask-(Document)>
   CreateOutDocumentSignTask <CreateOutDocumentSignTask-(Document)>
   MarkAsRead <MarkAsRead>
   CreateCustomDataPatchTask <CreateCustomDataPatchTask>

   
Производные объекты 
------------------------------------

Следующие объекты являются производными от Document:

.. toctree::
   :name: DocumentsChild
   :maxdepth: 1
   :caption: Производные объекты
   :hidden:

   Contract <Contract>
   Invoice <Invoice> 
   InvoiceRevision <InvoiceRevision>  
   InvoiceCorrection <InvoiceCorrection>
   InvoiceCorrectionRevision <InvoiceCorrectionRevision>
   Nonformalized <Nonformalized>
   NonformalizedAcceptanceCertificate <NonformalizedAcceptanceCertificate>
   NonformalizedTorg12 <NonformalizedTorg12>
   NonformalizedProforma <NonformalizedProformaInvoice>
   XmlAcceptanceCertificate <XmlAcceptanceCertificate>
   XmlTorg12 <XmlTorg12>
   Utd <Utd>
   UtdRevision <UtdRevision>
   Ucd <Ucd>
   UcdRevision <UcdRevision>

-  :doc:`Contract <Contract>` - договор
-  :doc:`Invoice <Invoice>` - счет-фактура
-  :doc:`InvoiceRevision <InvoiceRevision>` - исправление счета-фактуры
-  :doc:`InvoiceCorrection <InvoiceCorrection>` - корректировочный счет-фактура
-  :doc:`InvoiceCorrectionRevision <InvoiceCorrectionRevision>` - исправление корректировочного счета-фактуры
-  :doc:`Nonformalized <Nonformalized>` - неформализованный документ (в том числе акт сверки, детализация, дополнительное соглашение к договору, протокол согласования цены, реестр сертификатов, ценовой лист)
-  :doc:`NonformalizedAcceptanceCertificate <NonformalizedAcceptanceCertificate>` - акт о выполнении работ в неформализованном виде
-  :doc:`NonformalizedTorg12 <NonformalizedTorg12>` - ТОРГ-12 в неформализованном виде
-  :doc:`NonformalizedProforma <NonformalizedProformaInvoice>` - счет на оплату
-  :doc:`XmlAcceptanceCertificate <XmlAcceptanceCertificate>` - акт о выполнении работ в формализованном виде
-  :doc:`XmlTorg12 <XmlTorg12>` - ТОРГ-12 в формализованном виде
-  :doc:`Utd <Utd>` - универсальный передаточный документ
-  :doc:`UtdRevision <UtdRevision>` - исправление универсального передаточного документа
-  :doc:`Ucd <Ucd>` - универсальный корректировочный документ
-  :doc:`UcdRevision <UcdRevision>` - исправление универсального корректировочного документа


Структуры для работы с содержимым документов
---------------------------------------------

Для работы с содержимым формализованных документов можно использовать специальные объекты, которые представляют данные xml-файла в виде объектной модели.

Объектные модели документов
"""""""""""""""""""""""""""

В компоненте реализованы следующие объекты:

- :doc:`AcceptanceCertificateContent <AcceptanceCertificateContent>` - для работы с неформализованным актом выполненных работ
- :doc:`AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>`, :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - для работы с формализованным :doc:`актом выполненных работ <XmlAcceptanceCertificate>`
- :doc:`ContractContent <ContractContent>` - для работы с документом :doc:`договор <Contract>`
- :doc:`InvoiceContent <InvoiceContent>` - для работы с документами :doc:`счет-фактура <Invoice>`, :doc:`исправление счета-фактуры <InvoiceRevision>`
- :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>` - для работы с документами :doc:`корректировочный счет-фактура <InvoiceCorrection>`, :doc:`исправление корректировочного счета-фактуры <InvoiceCorrectionRevision>`
- :doc:`NonformilizedContent <NonformilizedContent>` - для работы с :doc:`неформализованным документом <Nonformalized>`
- :doc:`ProformaInvoiceContent <ProformaInvoiceContent>` - для работы с :doc:`счетом на оплату <NonformalizedProformaInvoice>`
- :doc:`Torg12Content <Torg12Content>` - для работы с неформализованной Торг-12
- :doc:`Torg12SellerContent <Torg12SellerContent>`, :doc:`Torg12BuyerContent <Torg12BuyerContent>` - для работы с формализованной :doc:`Торг-12 <XmlTorg12>`
- :doc:`UtdSellerContent <UtdSellerContent>`, :doc:`UcdSellerContent <UcdSellerContent>`, :doc:`UtdBuyerContent <UtdBuyerContent>` - для работы с :doc:`УПД <Utd>` и :doc:`УКД <Ucd>`
- :doc:`TovTorgSellerContent <TovTorgSellerContent>` и :doc:`TovTorgBuyerContent <TovTorgBuyerContent>` - для работы с Торг-12 в формате 551-го приказа
- :doc:`Act552SellerContent <Act552SellerContent>` и :doc:`Act552BuyerContent <Act552BuyerContent>` - для работы с актами в формате 552-го приказа

.. toctree::
   :name: Auto2
   :hidden:

   AcceptanceCertificateContent <AcceptanceCertificateContent>
   AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>
   AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>
   ContractContent <ContractContent>
   InvoiceContent <InvoiceContent>
   InvoiceCorrectionContent <InvoiceCorrectionContent>
   NonformilizedContent <NonformilizedContent>
   ProformaInvoiceContent <ProformaInvoiceContent> 
   Torg12Content <Torg12Content>
   Torg12SellerContent <Torg12SellerContent>
   Torg12BuyerContent <Torg12BuyerContent>
   UtdSellerContent <UtdSellerContent>
   UtdBuyerContent <UtdBuyerContent>
   UcdSellerContent <UcdSellerContent>
   TovTorgSellerContent <TovTorgSellerContent>
   TovTorgBuyerContent <TovTorgBuyerContent>
   Act552SellerContent <Act552SellerContent>
   Act552BuyerContent <Act552BuyerContent>
   
Вспомогательные объекты
""""""""""""""""""""""""""""""

Для работы с содержимым также используются следующие вспомогательные объекты:

- :doc:`AdditionalInfoId <AdditionalInfoId>` - для работы с информационным полем документа
- :doc:`AddressInfo <AddressInfo>` - для работы с данными об адресе
- :doc:`Attorney <Attorney>` - для работы с данными о доверенности
- :doc:`Employee <Employee>` - для работы с данными о работнике организации продавца или покупателя
- :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` - для работы с данными об организации
- :doc:`ExtendedSigner <ExtendedSigner>` - для работы с данными о лице, подписавшем документ
- :doc:`OrganizationInfo <OrganizationInfo>` - для работы с данными об организации
- :doc:`OtherIssuer <OtherIssuer>` - для работы с данными о третьем лице
- :doc:`PaymentDocument <PaymentDocument>` - для работы с данными о платежно-расчетном документе
- :doc:`Signer <Signer>` - для работы с данными о лице, подписавшем документ
- :doc:`Shipper <Shipper>` - для работы с данными об грузоотправителе
- :doc:`ShipperOrConsigneeInfo <ShipperOrConsigneeInfo>` - для работы с данными об грузоотправителе и грузополучателе
- :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` - для работы с дополнительными сведениями
- :doc:`Official <Official>` - для работы с данными о должностном лице
- :doc:`GroundInfo <GroundInfo>` - для работы с документом - основанием
- :doc:`CustomDataItem <CustomDataItem>` - запись "ключ-значение"

.. toctree::
   :name: Auto3
   :hidden:

   AdditionalInfoId <AdditionalInfoId>
   AddressInfo <AddressInfo>
   Attorney <Attorney>
   ExtendedOrganizationInfo <ExtendedOrganizationInfo>
   ExtendedSigner <ExtendedSigner>
   OrganizationInfo <OrganizationInfo>
   PaymentDocument <PaymentDocument>
   Signer <Signer>
   Shipper <Shipper>
   ShipperOrConsigneeInfo <ShipperOrConsigneeInfo>
   StructedAdditionalInfo <StructedAdditionalInfo>
   Official <Official>
   ResolutionRequest <ResolutionRequest>
   ResolutionRequestDenial <ResolutionRequestDenial>
   GroundInfo <GroundInfo>
   CustomDataItem <CustomDataItem>