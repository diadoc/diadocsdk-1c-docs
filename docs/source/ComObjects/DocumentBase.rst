DocumentBase
============

Базовый объект для всех |DocumentBase-Inheritable|_ .


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

:HasCustomPrintForm:
  **Булево, чтение** - флаг, показывающий, что документ имеет нестандартную печатную форму

  .. versionadded:: 3.0.10

:IsLockedPackage:
  **Булево, чтение** - флаг, показывающий, что документ является частью нередактируемого пакета

  .. versionadded:: 5.3.0

:IsEncryptedContent:
  **Булево, чтение** - флаг, показывающий, что содержимое документа зашифровано

  .. versionadded:: 5.3.0

:IsRead:
  **Булево, чтение** - флаг, показывающий, что документ был прочитан сотрудником организации

:DocflowStatus:
  :doc:`DocflowStatus` **, чтение** - статус документа

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



.. rubric:: Методы

+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetSenderSignature|_         | |DocumentBase-SaveContent|_            | |DocumentBase-GetAnyComment|_               | |DocumentBase-CreateReplySendTask2|_        |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetRecipientSignature|_      | |DocumentBase-SaveBuyerContent|_       | |DocumentBase-GetExternalStatuses|_         | |DocumentBase-SendReceiptsAsync|_           |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetDynamicContent|_          | |DocumentBase-SaveAllContent|_         | |DocumentBase-GetDocumentPackage|_          | |DocumentBase-Approve|_                     |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetBase64Content|_           | |DocumentBase-SaveAllContentAsync|_    | |DocumentBase-Delete|_                      | |DocumentBase-Disapprove|_                  |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetBase64ContentAsync|_      | |DocumentBase-SaveAllContentZip|_      | |DocumentBase-Move|_                        | |DocumentBase-CreateOutDocumentSignTask|_   |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetBase64Signature|_         | |DocumentBase-SaveAllContentZipAsync|_ | |DocumentBase-MarkAsRead|_                  | |DocumentBase-CreateResolutionRequestTask|_ |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
| |DocumentBase-GetBase64OriginalSignature|_ | |DocumentBase-GetPrintForm|_           | |DocumentBase-AssignToResolutionRoute|_     | |DocumentBase-CreateCustomDataPatchTask|_   |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
|                                            |                                        | |DocumentBase-RemoveFromResolutionRoute|_   |                                             |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
|                                            |                                        | |DocumentBase-GetResolutions|_              |                                             |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
|                                            |                                        | |DocumentBase-GetResolutionRequests|_       |                                             |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+
|                                            |                                        | |DocumentBase-GetResolutionRequestDenials|_ |                                             |
+--------------------------------------------+----------------------------------------+---------------------------------------------+---------------------------------------------+


.. |DocumentBase-GetSenderSignature| replace:: GetSenderSignature()
.. |DocumentBase-GetRecipientSignature| replace:: GetRecipientSignature()
.. |DocumentBase-GetDynamicContent| replace:: GetDynamicContent()
.. |DocumentBase-GetBase64Content| replace:: GetBase64Content()
.. |DocumentBase-GetBase64ContentAsync| replace:: GetBase64ContentAsync()
.. |DocumentBase-GetBase64Signature| replace:: GetBase64Signature()
.. |DocumentBase-GetBase64OriginalSignature| replace:: GetBase64OriginalSignature()

.. |DocumentBase-SaveContent| replace:: SaveContent()
.. |DocumentBase-SaveBuyerContent| replace:: SaveBuyerContent()
.. |DocumentBase-SaveAllContent| replace:: SaveAllContent()
.. |DocumentBase-SaveAllContentAsync| replace:: SaveAllContentAsync()
.. |DocumentBase-SaveAllContentZip| replace:: SaveAllContentZip()
.. |DocumentBase-SaveAllContentZipAsync| replace:: SaveAllContentZipAsync()
.. |DocumentBase-GetPrintForm| replace:: GetPrintForm()

.. |DocumentBase-GetAnyComment| replace:: GetAnyComment()
.. |DocumentBase-GetExternalStatuses| replace:: GetExternalStatuses()
.. |DocumentBase-GetDocumentPackage| replace:: GetDocumentPackage()
.. |DocumentBase-Delete| replace:: Delete()
.. |DocumentBase-Move| replace:: Move()
.. |DocumentBase-MarkAsRead| replace:: MarkAsRead()
.. |DocumentBase-AssignToResolutionRoute| replace:: AssignToResolutionRoute()
.. |DocumentBase-RemoveFromResolutionRoute| replace:: RemoveFromResolutionRoute()
.. |DocumentBase-GetResolutions| replace:: GetResolutions()
.. |DocumentBase-GetResolutionRequests| replace:: GetResolutionRequests()
.. |DocumentBase-GetResolutionRequestDenials| replace:: GetResolutionRequestDenials()

.. |DocumentBase-CreateReplySendTask2| replace:: CreateReplySendTask2()
.. |DocumentBase-SendReceiptsAsync| replace:: SendReceiptsAsync()
.. |DocumentBase-Approve| replace:: Approve()
.. |DocumentBase-Disapprove| replace:: Disapprove()
.. |DocumentBase-CreateOutDocumentSignTask| replace:: CreateOutDocumentSignTask()
.. |DocumentBase-CreateResolutionRequestTask| replace:: CreateResolutionRequestTask()
.. |DocumentBase-CreateCustomDataPatchTask| replace:: CreateCustomDataPatchTask()



.. _DocumentBase-GetSenderSignature:
.. method:: DocumentBase.GetSenderSignature()

  Возвращает :doc:`представление подписи <Signature>` титула отправителя



.. _DocumentBase-GetRecipientSignature:
.. method:: DocumentBase.GetRecipientSignature()

  Возвращает :doc:`представление подписи <Signature>` получателя документа


.. _DocumentBase-GetDynamicContent:
.. method:: DocumentBase.GetDynamicContent(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает :doc:`упрощённое представление контента <DynamicContent>` титула документа со стороны *DocflowSide*.
  Если запрашиваемого титула у документа нет, то результатом будет :doc:`пустым <Descriptions/Empty_Com_Object>`.
  Если для данного документа не существует схемы, в которой можно представить контент документа, то так же результатом будет :doc:`пустым <Descriptions/Empty_Com_Object>`


.. _DocumentBase-GetBase64Content:
.. method:: DocumentBase.GetBase64Content(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает контент титула документа со стороны *DocflowSide* в виде Base64 строки



.. _DocumentBase-GetBase64ContentAsync:
.. method:: DocumentBase.GetBase64ContentAsync(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает контент титула документа со стороны *DocflowSide* в виде Base64 строки



.. _DocumentBase-GetBase64Signature:
.. method:: DocumentBase.GetBase64Signature(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, подпись титула которой будет представлена. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает подпись с меткой времени к титулу документа со стороны *DocflowSide* в виде Base64 строки



.. _DocumentBase-GetBase64OriginalSignature:
.. method:: DocumentBase.GetBase64OriginalSignature(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, подпись титула которой будет представлена. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает оригинальную подпись (обычно без метки времени) титула документа со стороны *DocflowSide* в виде Base64 строки



.. _DocumentBase-SaveContent:
.. method:: DocumentBase.SaveContent(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет записан контент

  Сохраняет титул отправителя на диск в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан



.. _DocumentBase-SaveBuyerContent:
.. method:: DocumentBase.SaveBuyerContent(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет записан контент

  Сохраняет титул получателя документа в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан. Если титул отсутсвует, то ничего не произойдёт



.. _DocumentBase-SaveAllContent:
.. method:: DocumentBase.SaveAllContent(DirectoryPath, WithProtocol=false)

  :DirectoryPath: ``Строка`` Путь до директории, в которой будут сохранены файлы
  :WithProtocol:  ``Булево`` Признак необходимости сохранения протокола передачи документа

  Сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию



.. _DocumentBase-SaveAllContentAsync:
.. method:: DocumentBase.SaveAllContentAsync(DirectoryPath, WithProtocol=false)

  :DirectoryPath: ``Строка`` Путь до директории, в которой будут сохранены файлы
  :WithProtocol:  ``Булево`` Признак необходимости сохранения протокола передачи документа

  Асинхронно сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию



.. _DocumentBase-SaveAllContentZip:
.. method:: DocumentBase.SaveAllContentZip(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет сохранён архив

  Формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан



.. _DocumentBase-SaveAllContentZipAsync:
.. method:: DocumentBase.SaveAllContentZipAsync(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет сохранён архив

  Асинхронно формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан



.. _DocumentBase-GetPrintForm:
.. method:: DocumentBase.GetPrintForm(FilePath, Timeout=30)

  :FilePath: ``Строка`` Путь до файла, в который будет сохранена печатная форма
  :Timeout:  ``Беззнаковое целое число`` Таймаут за который необходимо получить печатную форму в секундах

  Получает печатную форму документа в формате ``.pdf`` и сохраняет её в указанный файл. Если расширение файла отличается от ``.pdf``, то такой файл будет создан

  .. versionadded:: 3.0.10



.. _DocumentBase-GetAnyComment:
.. method:: DocumentBase.GetAnyComment(CommentType)

  :CommentType: ``строка`` Тип комментария. :doc:`Возможные значения <Enums/CommentType>`

  Возвращает строку с комментарием определённого типа, связанным с документом

  .. versionadded:: 5.20.3



.. _DocumentBase-GetExternalStatuses:
.. method:: DocumentBase.GetExternalStatuses()

  Возвращает :doc:`коллекцию <Collection>` :doc:`внешних статусов <ExternalStatus>` документа

  .. versionadded:: 5.32.0


.. _DocumentBase-GetDocumentPackage:
.. method:: DocumentBase.GetDocumentPackage()

  Возвращает :doc:`пакет документов <DocumentPackage>`, в котором находится документ

  .. versionadded:: 5.3.0

  .. note:: понятие пакета в терминах компоненты и в терминах `HTTP-API <http://api-docs.diadoc.ru/ru/latest/index.html>`_ или Веб-интерфейса разные.
    В данном случае в пакете будут содержаться только документы с одинаковым :doc:`MessageId <Descriptions/MessageId>`


.. _DocumentBase-Delete:
.. method:: DocumentBase.Delete()

  Помечает документ как удаленный



.. _DocumentBase-Move:
.. method:: DocumentBase.Move(DepartmentId)

  :DepartmentId: ``Строка`` Идентификатор подразделения

  Перемещает документ в указанное подразделение



.. _DocumentBase-MarkAsRead:
.. method:: DocumentBase.MarkAsRead()

  Помечает, что документ как прочитанный



.. _DocumentBase-AssignToResolutionRoute:
.. method:: DocumentBase.AssignToResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при постановке документа на маршрут

  Ставит документ на маршрут согласования. Получить доступные маршруты согласования можно методом :meth:`Organization.GetResolutionRoutes`



.. _DocumentBase-RemoveFromResolutionRoute:
.. method:: DocumentBase.RemoveFromResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при снятии документа с маршрута

  Снимает документ с маршрута согласования


.. _DocumentBase-GetResolutions:
.. method:: DocumentBase.GetResolutions()

  Метод возвращает :doc:`коллекцию <Collection>` :doc:`резолюций <Resolution>` документа: согласований, подписаний, аннулирований, их запросов и т.д.



.. _DocumentBase-GetResolutionRequests:
.. method:: DocumentBase.GetResolutionRequests()

  Метод возвращает :doc:`коллекцию <Collection>` :doc:`запросов резолюций <ResolutionRequest>` документа: запросов согласований, запросов подписаний, запросов аннулирований и т.д.



.. _DocumentBase-GetResolutionRequestDenials:
.. method:: DocumentBase.GetResolutionRequestDenials()

  Метод возвращает :doc:`коллекцию <Collection>` :doc:`отказов в резолюциях <ResolutionRequestDenial>` документа



.. _DocumentBase-CreateReplySendTask2:
.. method:: DocumentBase.CreateReplySendTask2(ReplyType="AcceptDocument")

  :ReplyType: ``строка`` Тип ответа. :doc:`Возможные значения <Enums/ReplyType>`

  Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask2>`

    .. versionadded:: 5.27.0


.. _DocumentBase-SendReceiptsAsync:
.. method:: DocumentBase.SendReceiptsAsync()

  Отправляет извещения о получении документа, необходимые для завершения документооборота. Возвращает объект :doc:`AsyncResult` с типом результата ``Булево``



.. _DocumentBase-Approve:
.. method:: DocumentBase.Approve([Comment])

  :Comment: ``Строка`` Комментарий, который будет указан при согласовании

  Согласует документ



.. _DocumentBase-Disapprove:
.. method:: DocumentBase.Disapprove([Comment])

  :Comment: ``Строка`` Комментарий, который будет указан при отказе согласования

  Отказывает в согласовании документа



.. _DocumentBase-CreateOutDocumentSignTask:
.. method:: DocumentBase.CreateOutDocumentSignTask()

  Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

  .. versionadded:: 5.6.0



.. _DocumentBase-CreateResolutionRequestTask:
.. method:: DocumentBase.CreateResolutionRequestTask()

  Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`



.. _DocumentBase-CreateCustomDataPatchTask:
.. method:: DocumentBase.CreateCustomDataPatchTask()

  Создает :doc:`задание на редактирование коллекции CustomData <CustomDataPatchTask>`



.. rubric:: Дополнительная информация

.. |DocumentBase-Inheritable| replace:: типов документов
.. _DocumentBase-Inheritable:

========================================= ======================================================
Объекты, производные от *Document*        Описание
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



.. rubric:: Устаревшие методы


.. method:: DocumentBase.GetComment()

  Возвращает строку с комментарием к документу, заданным при отправке

  .. deprecated:: 5.20.3
    Используйте :meth:`GetAnyComment` с типом ``AttachmentComment``


.. method:: DocumentBase.SetOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Присваивает документу дополнительный идентификатор из учётной системы

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: DocumentBase.ReSetOneSDocumentId()

  Сбрасывает дополнительный идентификатор учётной системы у документа в Диадоке

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: DocumentBase.AddSubordinateOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Добавляет документу дополнительный идентификатор из учётной системы как подчинённый. Обычно используется чтобы обозначить связь документов друг с другом

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: DocumentBase.RemoveSubordinateOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Удаляет дополнительный подчинённый идентификатор

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: DocumentBase.CreateReplySendTask(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

  Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask>`

  .. deprecated:: 5.27.0
    Используйте :meth:`DocumentBase.CreateReplySendTask2`



.. method:: DocumentBase.SendRevocationRequest([Comment])

  :Comment: ``строка`` комментарий к запросу аннулирования

  Запрашивает аннулирование документа

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`DocumentBase.CreateReplySendTask2`



.. method:: DocumentBase.AcceptRevocationRequest()

  Принимает запрос аннулирования

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`DocumentBase.CreateReplySendTask2`



.. method:: DocumentBase.RejectRevocationRequest()

  Отказывает в аннулировании

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`DocumentBase.CreateReplySendTask2`
