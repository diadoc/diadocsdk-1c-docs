DocumentBase
============

Базовый объект для всех :ref:`типов документов <DocumentBase-Inheritable>`.


.. rubric:: Свойства

:TypeNamedId:
    **Строка, чтение** - строковый идентификатор типа документа

:DocumentFunction:
    **Строка, чтение** - функция документа

:Version:
    **Строка, чтение** - информация о версии XSD схемы, в соотвествии с которой сформирован документ

:Organization:
    :doc:`Organization` **, чтение** - организация, которая отправила исходящий документ, либо получила входящий документ

:OrganizationGuid:
    **Строка, чтение** - идентификатор организации, которой принадлежит документ

    .. versionadded:: 5.31.0

:Direction:
    **Строка, чтение** - направление документа. :doc:`Возможные значения <Enums/DocumentDirection>`

:Counteragent:
    :doc:`BoxInfo` **, чтение** - контрагент документа. Для внутренних документов будет пустым

:ProxyBox:
    :doc:`BoxInfo` **, чтение** - промежуточный получатель документа

    .. versionadded:: 5.34.0

:FromDepartment:
    :doc:`Department` **, чтение** - подразделение организации, из которого был отправлен документ

    .. versionadded:: 3.0.8

:ToDepartment:
    :doc:`Department` **, чтение** - подразделение организации, в которое был отправлен документ

    .. versionadded:: 3.0.8

:ProxyDepartment:
    :doc:`Department` **, чтение** - подразделение промежуточного получателя

    .. versionadded:: 5.34.0

:Department:
    :doc:`Department` **, чтение** - подразделение организации, к которому привязан документ

:RouteId:
    **Строка, чтение** - идентификатор маршрута согласования, на котором находится документ

:DocumentId:
    **Строка, чтение** - идентификатор документа

:InitialDocumentIds:
    :doc:`Коллекция  <Collection>` **строк, чтение** - коллекция идентификаторов документов, на который ссылается данный документ (т.е. документы, которые по отношению к данному документы являются "родительскими"

:SubordinateDocumentIds:
    :doc:`Коллекция <Collection>` **строк, чтение** - коллекция идентификаторов документов, которые ссылаются на данный документ (т.е. документы, которые по отношению к данному документу являются "дочерними")

:OneSDocumentId:
    **Строка, чтение** - дополнительный идентификатор документа

:PackageId:
    **Строка, чтение** - идентификатор пакета

:CustomDocumentId:
    **Строка, чтение** - идентификатор документа, определяемый внешней системой

:Metadata:
    :doc:`Коллекция <Collection>` **объектов** :doc:`MetadataItem` **, чтение** - коллекция метаданных

:Timestamp:
    **Дата и время, чтение** - дата и время отправки документа (в текущем часовом поясе)

:DocumentDate:
    **Дата, чтение** - дата документа

:DocumentNumber:
    **Строка, чтение** - номер документа

:FileName:
    **Строка, чтение** - имя файла документа, с которым он загружался в Диадок

:Title:
    **Строка, чтение** - название документа, например, ``Счет-фактура №123 от 20.02.18``

:PathURL:
    **Строка, чтение** - URL документа, по которому он доступен в web-интерфейсе

:EditingSettingId:
    **Строка, чтение** - идентификатор настройки редактирования содержимого документа.
    Наличие данной настройки означает, что в содержимом файла может отсутствовать контент, редактирование которого разрешено данной настройкой

    .. versionadded:: 5.29.13

:WorkflowId:
    **Целое число, чтение** - идентификатор типа документооборота

:CustomData:
    :doc:`Коллекция <Collection>` **объектов** :doc:`CustomDataItem` **, чтение** - коллекция тэгов документа

:IsDeleted:
    **Булево, чтение** - флаг, показывающий, был ли удален данный документ

:IsTest:
    **Булево, чтение** - флаг, показывающий, что документ является тестовым и не имеет юридической силы

:IsLockedPackage:
    **Булево, чтение** - флаг, показывающий, что документ является частью нередактируемого пакета

    .. versionadded:: 5.3.0

:IsEncryptedContent:
    **Булево, чтение** - флаг, показывающий, что содержимое документа зашифровано

    .. versionadded:: 5.3.0

:IsRead:
    **Булево, чтение** - флаг, показывающий, что документ был прочитан сотрудником организации

:DocflowStatus:
    :doc:`DocflowStatus` **, чтение** - текстовое представление статуса документа.
    Поле рекомендуется использовать для отоборажения статуса документа аналогично веб-интерфейсу Диадок.
    Для реализации логики интеграционного решения рекомендуется использовать поля, отвечающие за частичные статусы документооборота, например **SenderSignatureStatus**, **RecipientResponseStatus** и т.п.

:SenderSignatureStatus:
    **Строка, чтение** - статус проверки ЭЦП отправителя. :doc:`Возможные значения <./Enums/SenderSignatureStatus>`

:RecipientResponseStatus:
    **Строка, чтение** - статус ответного действия со стороны получателя. :doc:`Возможные значения <./Enums/RecipientResponseStatus>`

:ProxySignatureStatus:
    **Строка, чтение** -  статус промежуточной подписи. :doc:`Возможные значения <./Enums/ProxySignatureStatus>`

    .. versionadded:: 5.31.0

:RoamingNotificationStatus:
    **Строка, чтение** - статус передачи документа через роуминг. :doc:`Возможные значения <./Enums/RoamingNotificationStatus>`

    .. versionadded:: 5.3.1

:RoamingNotificationStatusDescription:
    **Строка, чтение** - описание статуса передачи документа через роуминг

    .. versionadded:: 5.3.1

:RevocationStatus:
    **Строка, чтение** - статус аннулирования документа. :doc:`Возможные значения <./Enums/RevocationStatus>`

:ResolutionStatus:
    :doc:`ResolutionStatus` **, чтение** - текущий статус запрошенного согласования или подписи документа

:LastExternalStatuses:
    :doc:`коллекция <Collection>` **объектов** :doc:`ExternalStatusLite` **, чтение** - набор последних статусов внешнего документооборота

    .. versionadded:: 5.32.0

:RecipientReceiptMetadata:
    :doc:`RecipientReceiptMetadata` **, чтение** - метаданные извещения о получении документа получателем

:ConfirmationMetadata:
    :doc:`ConfirmationMetadata` **, чтение** - метаданные подтверждения оператором отправки/получения документа или служебного документа

:AmendmentRequestMetadata:
    :doc:`AmendmentRequestMetadata` **, чтение** - метаданные уведомления об уточнении


.. warning:: Поля устарели

    .. csv-table::
        :header: "Поле", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

        AttachmentVersion,        **Version**,                                                                      :doc:`../History/release_info/5_21_0`,
        Type,                     **TypeNamedId**,                                                                  :doc:`../History/release_info/5_21_0`,
        OrganizationId,           **OrganizationGuid**,                                                             :doc:`../History/release_info/5_31_0`,
        TimestampSeconds,         **Timestamp**,                                                                    :doc:`../History/release_info/5_30_2`,
        Status,                   **DocflowStatus** или поля со статусами отдельных сущностей ,                     :doc:`../History/release_info/5_34_0`,
        HasCustomPrintForm,       :meth:`DetectCustomPrintForm() <DocumentBase.DetectCustomPrintForm>`,             :doc:`../History/release_info/5_35_0`,
        ResolutionRequests,       :meth:`GetResolutionRequests() <DocumentBase.GetResolutionRequests>`,             :doc:`../History/release_info/5_34_0`,
        Resolutions,              :meth:`GetResolutions() <DocumentBase.GetResolutions>`,                           :doc:`../History/release_info/5_34_0`,
        ResolutionRequestDenials, :meth:`GetResolutionRequestDenials() <DocumentBase.GetResolutionRequestDenials>`, :doc:`../History/release_info/5_34_0`,

    :AttachmentVersion:
        **Строка, чтение** - версия документа

    :Type:
        **Строка, чтение** - тип документа

    :OrganizationId:
        **Строка, чтение** - идентификатор ящика собственной организации в Диадок в формате ``...@diadoc.ru``

    :TimestampSeconds:
        **Вещественное число, чтение** - количество секунд, прошедших с начала дня до отправки документа

    :Status:
        **Строка, чтение** - общий статус документа. Возможные значения зависят от типа документа

    :HasCustomPrintForm:
        **Булево, чтение** - признак того, что документ имеет печатную форму, отличную от стандартной

    :ResolutionRequests:
        :doc:`Коллекция <Collection>` **объектов** :doc:`ResolutionRequest` - коллекция запросов согласований, подписаний, аннулирований

    :Resolutions:
        :doc:`Коллекция <Collection>` **объектов** :doc:`Resolution` - коллекция согласований, подписаний, аннулирований, их запросов и т.д.

    :ResolutionRequestDenials:
        :doc:`Коллекция <Collection>` **объектов** :doc:`ResolutionRequestDenial` - коллекция отказов в запросах согласований, подписаний, аннулирований


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        .. csv-table::
            :header: Информация о контенте и подписях, Сохранение данных на диск, Получение дополнительной информации, Изменение состояния документа

            :meth:`GetSenderSignature() <DocumentBase.GetSenderSignature>`,                 :meth:`SaveContent() <DocumentBase.SaveContent>`,                       :meth:`GetAnyComment() <DocumentBase.GetAnyComment>`,                             :meth:`CreateReplySendTask2() <DocumentBase.CreateReplySendTask2>`
            :meth:`GetRecipientSignature() <DocumentBase.GetRecipientSignature>`,           :meth:`SaveBuyerContent() <DocumentBase.SaveBuyerContent>`,             :meth:`GetExternalStatuses() <DocumentBase.GetExternalStatuses>`,                 :meth:`SendReceiptsAsync() <DocumentBase.SendReceiptsAsync>`
            :meth:`GetDynamicContent() <DocumentBase.GetDynamicContent>`,                   :meth:`SaveAllContent() <DocumentBase.SaveAllContent>`,                 :meth:`GetDocumentPackage() <DocumentBase.GetDocumentPackage>`,                   :meth:`SendReceiptsWithPowerOfAttorney() <DocumentBase.SendReceiptsWithPowerOfAttorney>`
            :meth:`GetBase64Content() <DocumentBase.GetBase64Content>`,                     :meth:`SaveAllContentAsync() <DocumentBase.SaveAllContentAsync>`,       :meth:`GetPackageDocuments() <DocumentBase.GetPackageDocuments>`,                 :meth:`Approve() <DocumentBase.Approve>`
            :meth:`GetBase64ContentAsync() <DocumentBase.GetBase64ContentAsync>`,           :meth:`SaveAllContentZip() <DocumentBase.SaveAllContentZip>`,           :meth:`GetResolutions() <DocumentBase.GetResolutions>`,                           :meth:`Disapprove() <DocumentBase.Disapprove>`
            :meth:`GetBase64Signature() <DocumentBase.GetBase64Signature>`,                 :meth:`SaveAllContentZipAsync() <DocumentBase.SaveAllContentZipAsync>`, :meth:`GetResolutionRequests() <DocumentBase.GetResolutionRequests>`,             :meth:`CreateOutDocumentSignTask() <DocumentBase.CreateOutDocumentSignTask>`
            :meth:`GetBase64OriginalSignature() <DocumentBase.GetBase64OriginalSignature>`, :meth:`GetPrintForm() <DocumentBase.GetPrintForm>`,                     :meth:`GetResolutionRequestDenials() <DocumentBase.GetResolutionRequestDenials>`, :meth:`CreateResolutionRequestTask() <DocumentBase.CreateResolutionRequestTask>`
                                                                                          ,                                                                       , :meth:`GetPowersOfAttorney() <DocumentBase.GetPowersOfAttorney>`,                 :meth:`CreateCustomDataPatchTask() <DocumentBase.CreateCustomDataPatchTask>`
                                                                                          ,                                                                       , :meth:`DetectCustomPrintForm() <DocumentBase.DetectCustomPrintForm>`,             :meth:`Delete() <DocumentBase.Delete>`
                                                                                          ,                                                                       ,                                                                                 , :meth:`Move() <DocumentBase.Move>`
                                                                                          ,                                                                       ,                                                                                 , :meth:`MarkAsRead() <DocumentBase.MarkAsRead>`
                                                                                          ,                                                                       ,                                                                                 , :meth:`AssignToResolutionRoute() <DocumentBase.AssignToResolutionRoute>`
                                                                                          ,                                                                       ,                                                                                 , :meth:`RemoveFromResolutionRoute() <DocumentBase.RemoveFromResolutionRoute>`

    .. tab:: Информация о контенте и подписях

        * :meth:`GetSenderSignature() <DocumentBase.GetSenderSignature>`
        * :meth:`GetRecipientSignature() <DocumentBase.GetRecipientSignature>`
        * :meth:`GetDynamicContent() <DocumentBase.GetDynamicContent>`
        * :meth:`GetBase64Content() <DocumentBase.GetBase64Content>`
        * :meth:`GetBase64ContentAsync() <DocumentBase.GetBase64ContentAsync>`
        * :meth:`GetBase64Signature() <DocumentBase.GetBase64Signature>`
        * :meth:`GetBase64OriginalSignature() <DocumentBase.GetBase64OriginalSignature>`

    .. tab:: Сохранение данных на диск

        * :meth:`SaveContent() <DocumentBase.SaveContent>`
        * :meth:`SaveBuyerContent() <DocumentBase.SaveBuyerContent>`
        * :meth:`SaveAllContent() <DocumentBase.SaveAllContent>`
        * :meth:`SaveAllContentAsync() <DocumentBase.SaveAllContentAsync>`
        * :meth:`SaveAllContentZip() <DocumentBase.SaveAllContentZip>`
        * :meth:`SaveAllContentZipAsync() <DocumentBase.SaveAllContentZipAsync>`
        * :meth:`GetPrintForm() <DocumentBase.GetPrintForm>`

    .. tab:: Получение дополнительной информации

        * :meth:`GetAnyComment() <DocumentBase.GetAnyComment>`
        * :meth:`GetExternalStatuses() <DocumentBase.GetExternalStatuses>`
        * :meth:`GetDocumentPackage() <DocumentBase.GetDocumentPackage>`
        * :meth:`GetPackageDocuments() <DocumentBase.GetPackageDocuments>`
        * :meth:`GetResolutions() <DocumentBase.GetResolutions>`
        * :meth:`GetResolutionRequests() <DocumentBase.GetResolutionRequests>`
        * :meth:`GetResolutionRequestDenials() <DocumentBase.GetResolutionRequestDenials>`
        * :meth:`GetPowersOfAttorney() <DocumentBase.GetPowersOfAttorney>`
        * :meth:`DetectCustomPrintForm() <DocumentBase.DetectCustomPrintForm>`

    .. tab:: Изменение состояния документа

        * :meth:`CreateReplySendTask2() <DocumentBase.CreateReplySendTask2>`
        * :meth:`SendReceiptsAsync() <DocumentBase.SendReceiptsAsync>`
        * :meth:`SendReceiptsWithPowerOfAttorney() <DocumentBase.SendReceiptsWithPowerOfAttorney>`
        * :meth:`Approve() <DocumentBase.Approve>`
        * :meth:`Disapprove() <DocumentBase.Disapprove>`
        * :meth:`CreateOutDocumentSignTask() <DocumentBase.CreateOutDocumentSignTask>`
        * :meth:`CreateResolutionRequestTask() <DocumentBase.CreateResolutionRequestTask>`
        * :meth:`CreateCustomDataPatchTask() <DocumentBase.CreateCustomDataPatchTask>`
        * :meth:`Delete() <DocumentBase.Delete>`
        * :meth:`Move() <DocumentBase.Move>`
        * :meth:`MarkAsRead() <DocumentBase.MarkAsRead>`
        * :meth:`AssignToResolutionRoute() <DocumentBase.AssignToResolutionRoute>`
        * :meth:`RemoveFromResolutionRoute() <DocumentBase.RemoveFromResolutionRoute>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

            :meth:`GetContent() <DocumentBase.GetContent>`,                                           :meth:`DocumentBase.GetDynamicContent`,    :doc:`../History/release_info/5_28_0`, 
            :meth:`GetContentAsync() <DocumentBase.GetContentAsync>`,                                                                       ,    :doc:`../History/release_info/5_28_0`, 
            :meth:`GetBuyerContent() <DocumentBase.GetBuyerContent>`,                                 :meth:`DocumentBase.GetDynamicContent`,    :doc:`../History/release_info/5_28_0`, 
            :meth:`CreateReplySendTask() <DocumentBase.CreateReplySendTask>`,                         :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`Accept() <DocumentBase.Accept>`,                                                   :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`Reject() <DocumentBase.Reject>`,                                                   :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`RejectAsync() <DocumentBase.RejectAsync>`,                                         :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`SendRevocationRequest() <DocumentBase.SendRevocationRequest>`,                     :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`AcceptRevocationRequest() <DocumentBase.AcceptRevocationRequest>`,                 :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`RejectRevocationRequest() <DocumentBase.RejectRevocationRequest>`,                 :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`SendCorrectionRequest() <DocumentBase.SendCorrectionRequest>`,                     :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`SendCorrectionRequestAsync() <DocumentBase.SendCorrectionRequestAsync>`,           :meth:`DocumentBase.CreateReplySendTask2`, :doc:`../History/release_info/5_27_0`, :doc:`../History/release_info/5_37_0`
            :meth:`GetComment() <DocumentBase.GetComment>`,                                           :meth:`DocumentBase.GetAnyComment`,        :doc:`../History/release_info/5_20_3`, 
            :meth:`GetRejectionComment() <DocumentBase.GetRejectionComment>`,                         :meth:`DocumentBase.GetAnyComment`,        :doc:`../History/release_info/5_20_3`, 
            :meth:`GetAmendmentRequestedComment() <DocumentBase.GetAmendmentRequestedComment>`,       :meth:`DocumentBase.GetAnyComment`,        :doc:`../History/release_info/5_20_3`, 
            :meth:`SetOneSDocumentId() <DocumentBase.SetOneSDocumentId>`,                             :meth:`DocumentBase.CreateDataTask`,       :doc:`../History/release_info/5_29_9`, 
            :meth:`ReSetOneSDocumentId() <DocumentBase.ReSetOneSDocumentId>`,                         :meth:`DocumentBase.CreateDataTask`,       :doc:`../History/release_info/5_29_9`, 
            :meth:`AddSubordinateOneSDocumentId() <DocumentBase.AddSubordinateOneSDocumentId>`,       :meth:`DocumentBase.CreateDataTask`,       :doc:`../History/release_info/5_29_9`, 
            :meth:`RemoveSubordinateOneSDocumentId() <DocumentBase.RemoveSubordinateOneSDocumentId>`, :meth:`DocumentBase.CreateDataTask`,       :doc:`../History/release_info/5_29_9`, 


        .. method:: DocumentBase.GetContent()

            Возвращает объектное представление контента первого титула документа. Тип контента зависит от типа документа


        .. method:: DocumentBase.GetContentAsync()

            Возвращает :doc:`AsyncResult` с объектным представлением контента первого титула документа в качестве результата. Тип контента зависит от типа документа


        .. method:: DocumentBase.GetBuyerContent()

            Возвращает объектное представление контента первого титула документа. Тип контента зависит от типа документа


        .. method:: DocumentBase.CreateReplySendTask(ReplyType="AcceptDocument")

            :ReplyType: **Строка** - тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

            Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask>`


        .. method:: DocumentBase.Accept()

            Подписывает однотитульный документ


        .. method:: DocumentBase.Reject()

            Отказывает контрагенту в подписи документа


        .. method:: DocumentBase.RejectAsync()

            Асинхронно отказывает контрагенту в подписи документа. Возвращает :doc:`AsyncResult` с булевым значением в качестве результата


        .. method:: DocumentBase.SendRevocationRequest(Comment="")

            :Comment: **Строка** - комментарий к запросу аннулирования

            Запрашивает аннулирование документа


        .. method:: DocumentBase.AcceptRevocationRequest()

            Принимает запрос аннулирования


        .. method:: DocumentBase.RejectRevocationRequest(Comment="")

            :Comment: **Строка** - комментарий отказа в аннулировании

            Отказывает в аннулировании


        .. method:: DocumentBase.SendCorrectionRequest(Comment="")

            :Comment: **Строка** - комментарий запроса корректировки документа

            Запрашивает корректировку документа


        .. method:: DocumentBase.SendCorrectionRequestAsync(Comment="")

            :Comment: **Строка** - комментарий запроса корректировки документа

            А синхронно запрашивает корректировку документа. Возвращает :doc:`AsyncResult` с булевым значением в качестве результата


        .. method:: DocumentBase.GetComment()

            Возвращает комментарий к первому титулу документа


        .. method:: DocumentBase.GetRejectionComment()

            Возвращает комментарий отказа в подписи


        .. method:: DocumentBase.GetAmendmentRequestedComment()

            Возвращает комментарий запроса аннулирования


        .. method:: DocumentBase.GetComment()

            Возвращает строку с комментарием к документу, заданным при отправке


        .. method:: DocumentBase.SetOneSDocumentId(ID)

            :ID: **Строка** - любая строка, идентифицирующая документ в учётной системе

            Присваивает документу дополнительный идентификатор из учётной системы


        .. method:: DocumentBase.ReSetOneSDocumentId()

            Сбрасывает дополнительный идентификатор учётной системы у документа в Диадоке


        .. method:: DocumentBase.AddSubordinateOneSDocumentId(ID)

            :ID: **Строка** - любая строка, идентифицирующая документ в учётной системе

            Добавляет документу дополнительный идентификатор из учётной системы как подчинённый. Обычно используется чтобы обозначить связь документов друг с другом


        .. method:: DocumentBase.RemoveSubordinateOneSDocumentId(ID)

            :ID: **Строка** - любая строка, идентифицирующая документ в учётной системе

            Удаляет дополнительный подчинённый идентификатор



.. method:: DocumentBase.GetSenderSignature()

    Возвращает :doc:`представление подписи <Signature>` титула отправителя


.. method:: DocumentBase.GetRecipientSignature()

    Возвращает :doc:`представление подписи <Signature>` получателя документа


.. method:: DocumentBase.GetDynamicContent(DocflowSide)

    :DocflowSide: **Строка** - сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

    Возвращает :doc:`упрощённое представление контента <DynamicContent>` титула документа со стороны **DocflowSide**.
    Если запрашиваемого титула нет или для него не существует упрощённого представления контента (см. :doc:`DocumentTitle`), то вернётся :doc:`Descriptions/EmptyVariant`


.. method:: DocumentBase.GetBase64Content(DocflowSide)

    :DocflowSide: **Строка** - сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

    Возвращает контент титула документа со стороны **DocflowSide** в виде Base64 строки


.. method:: DocumentBase.GetBase64ContentAsync(DocflowSide)

    :DocflowSide: **Строка** - сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

    Возвращает контент титула документа со стороны **DocflowSide** в виде Base64 строки


.. method:: DocumentBase.GetBase64Signature(DocflowSide)

    :DocflowSide: **Строка** - сторона документооборота, подпись титула которой будет представлена. :doc:`Возможные значения <Enums/DocflowSide>`

    Возвращает подпись с меткой времени к титулу документа со стороны **DocflowSide** в виде Base64 строки


.. method:: DocumentBase.GetBase64OriginalSignature(DocflowSide)

    :DocflowSide: **Строка** - сторона документооборота, подпись титула которой будет представлена. :doc:`Возможные значения <Enums/DocflowSide>`

    Возвращает оригинальную подпись (обычно без метки времени) титула документа со стороны **DocflowSide** в виде Base64 строки


.. method:: DocumentBase.SaveContent(FilePath)

    :FilePath: **Строка** - путь до файла, в который будет записан контент

    Сохраняет титул отправителя на диск в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан


.. method:: DocumentBase.SaveBuyerContent(FilePath)

    :FilePath: **Строка** - путь до файла, в который будет записан контент

    Сохраняет титул получателя документа в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан. Если титул отсутсвует, то ничего не произойдёт


.. method:: DocumentBase.SaveAllContent(DirectoryPath, WithProtocol=False)

    :DirectoryPath: **Строка** - путь до директории, в которой будут сохранены файлы
    :WithProtocol:  **Строка** - признак необходимости сохранения протокола передачи документа

    Сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию


.. method:: DocumentBase.SaveAllContentAsync(DirectoryPath, WithProtocol=False)

    :DirectoryPath: **Строка** - путь до директории, в которой будут сохранены файлы
    :WithProtocol:  **Строка** - признак необходимости сохранения протокола передачи документа

    Асинхронно сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию


.. method:: DocumentBase.SaveAllContentZip(FilePath)

    :FilePath: **Строка** - путь до файла, в который будет сохранён архив

    Формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан


.. method:: DocumentBase.SaveAllContentZipAsync(FilePath)

    :FilePath: **Строка** - путь до файла, в который будет сохранён архив

    Асинхронно формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан


.. method:: DocumentBase.GetPrintForm(FilePath, Timeout=30)

    :FilePath: **Строка** - путь до файла, в который будет сохранена печатная форма
    :Timeout:  **Целое беззнаковое число** - таймаут за который необходимо получить печатную форму в секундах

    Получает печатную форму документа в формате ``.pdf`` и сохраняет её в указанный файл. Если расширение файла отличается от ``.pdf``, то такой файл будет создан

    .. versionadded:: 3.0.10


.. method:: DocumentBase.GetAnyComment(CommentType)

    :CommentType: **Строка** - тип комментария. :doc:`Возможные значения <Enums/CommentType>`

    Возвращает строку с комментарием определённого типа, связанным с документом

    .. versionadded:: 5.20.3


.. method:: DocumentBase.GetExternalStatuses()

    Возвращает :doc:`коллекцию <Collection>` :doc:`внешних статусов <ExternalStatus>` документа

    .. versionadded:: 5.32.0


.. method:: DocumentBase.GetDocumentPackage()

    Возвращает :doc:`документы <DocumentPackage>`, отправленные одновременно с данным.
    У документов в результате будет совпадать :doc:`MessageId <Descriptions/MessageId>`

    .. versionadded:: 5.3.0


.. method:: DocumentBase.GetPackageDocuments(DetectCustomPrintForm=False)

    :DetectCustomPrintForm: **Булево** - Флаг необходимости определить наличие нестандартной печатной формы (КПФ) у документов.

    Возвращает :doc:`коллекцию <Collection>` :doc:`документов <DocumentBase>`, объединённых в один пакет.
    У документов в результате будет совпадать **PackageId**.

    Если решение предполагает использование признака наличия у документов КПФ, то рекомендуется устанавливать параметр **DetectCustomPrintForm** в истину -
    определение наличия КПФ для документов из результата будет выполняться пакетно, вместо необходимости :meth:`запрашивать <DocumentBase.DetectCustomPrintForm>` этот признак для каждого документа в отдельности


.. method:: DocumentBase.GetResolutions()

    Метод возвращает :doc:`коллекцию <Collection>` :doc:`резолюций <Resolution>` документа: согласований, подписаний, аннулирований, их запросов и т.д.


.. method:: DocumentBase.GetResolutionRequests()

    Метод возвращает :doc:`коллекцию <Collection>` :doc:`запросов резолюций <ResolutionRequest>` документа: запросов согласований, запросов подписаний, запросов аннулирований и т.д.


.. method:: DocumentBase.GetResolutionRequestDenials()

    Метод возвращает :doc:`коллекцию <Collection>` :doc:`отказов в резолюциях <ResolutionRequestDenial>` документа


.. method:: DocumentBase.GetPowersOfAttorney()

    Метод возвращает :doc:`коллекцию <Collection>` :doc:`МЧД <AttachedPowerOfAttorney>` , использованных для подписания сущностей документа


.. method:: DocumentBase.DetectCustomPrintForm()

    Метод возвращает признак наличия у документа нетиповой печатной формы (КПФ)

    .. versionadded:: 5.35.0


.. method:: DocumentBase.CreateReplySendTask2(ReplyType="AcceptDocument")

    :ReplyType: **Строка** - тип ответа. :doc:`Возможные значения <Enums/ReplyType>`

    Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask2>`

    .. versionadded:: 5.27.0


.. method:: DocumentBase.SendReceiptsAsync()

    Отправляет извещения о получении документа, необходимые для завершения документооборота.
    Возвращает объект :doc:`AsyncResult` с типом результата ``Булево``


.. method:: DocumentBase.SendReceiptsWithPowerOfAttorney(PowerOfAttorney)

    :PowerOfAttorney: :doc:`PowerOfAttorney` объект МЧД

    Отправляет извещения о получении документа, необходимые для завершения документооборота. При подписании извещений будет прикладываться указанная МЧД.
    Возвращает объект :doc:`AsyncResult` с типом результата ``Булево``


.. method:: DocumentBase.Approve([Comment])

    :Comment: ``Строка`` комментарий, который будет указан при согласовании

    Согласует документ


.. method:: DocumentBase.Disapprove([Comment])

    :Comment: **Строка** - комментарий, который будет указан при отказе согласования

    Отказывает в согласовании документа


.. method:: DocumentBase.CreateOutDocumentSignTask()

    Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

    .. versionadded:: 5.6.0


.. method:: DocumentBase.CreateResolutionRequestTask()

    Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`


.. method:: DocumentBase.CreateCustomDataPatchTask()

    Создает :doc:`задание на редактирование коллекции **CustomData** <CustomDataPatchTask>`


.. method:: DocumentBase.Delete()

    Помечает документ как удаленный


.. method:: DocumentBase.Move(DepartmentId)

    :DepartmentId: **Строка** - идентификатор подразделения

    Перемещает документ в указанное подразделение


.. method:: DocumentBase.MarkAsRead()

    Помечает, что документ как прочитанный


.. method:: DocumentBase.AssignToResolutionRoute(RouteId[, Comment])

    :RouteId: **Строка** - идентификатор маршрута
    :Comment: **Строка** - комментарий, который будет добавлен при постановке документа на маршрут

    Ставит документ на маршрут согласования. Получить доступные маршруты согласования можно методом :meth:`Organization.GetResolutionRoutes`


.. method:: DocumentBase.RemoveFromResolutionRoute(RouteId[, Comment])

    :RouteId: **Строка** - идентификатор маршрута
    :Comment: **Строка** - комментарий, который будет добавлен при снятии документа с маршрута

    Снимает документ с маршрута согласования



.. rubric:: Дополнительная информация

.. _DocumentBase-Inheritable:

========================================= ======================================================
Объекты, производные от *DocumentBase*    Описание
========================================= ======================================================
:doc:`Contract`                           договор
:doc:`Invoice`                            счет-фактура
:doc:`InvoiceRevision`                    исправление счета-фактуры
:doc:`InvoiceCorrection`                  корректировочный счет-фактура
:doc:`InvoiceCorrectionRevision`          исправление корректировочного счета-фактуры
:doc:`Nonformalized`                      неформализованный документ
:doc:`NonformalizedAcceptanceCertificate` акт о выполнении работ в неформализованном виде
:doc:`NonformalizedTorg12`                ТОРГ-12 в неформализованном виде
:doc:`NonformalizedProforma`              счет на оплату
:doc:`XmlAcceptanceCertificate`           акт о выполнении работ в формализованном виде
:doc:`XmlTorg12`                          ТОРГ-12 в формализованном виде
:doc:`Utd`                                универсальный передаточный документ
:doc:`UtdRevision`                        исправление универсального передаточного документа
:doc:`Ucd`                                универсальный корректировочный документ
:doc:`UcdRevision`                        исправление универсального корректировочного документа
:doc:`Document`                           документ произвольного типа
========================================= ======================================================