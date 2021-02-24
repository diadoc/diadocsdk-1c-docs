DocumentBase
============

Базовый объект для всех |Document-Inheritable|_ .


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

:FromDepartment:
  :doc:`Department` **, чтение** - подразделение организации, из которого был отправлен документ

  .. versionadded:: 3.0.8

:ToDepartment:
  :doc:`Department` **, чтение** - подразделение организации, в которое был отправлен документ

  .. versionadded:: 3.0.8

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

:Status:
  **Строка, чтение** - Общий статус документа в Диадоке. Возможный набор значений зависит от типа объекта-наследника

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

:ResolutionRequests:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ResolutionRequest` **, чтение** - история запросов резолюций документа: запросов согласований, запросов подписаний, запросов аннулирований

:Resolutions:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Resolution` **, чтение** - история резолюций документа: согласований, подписаний, аннулирований

:ResolutionRequestDenials:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ResolutionRequestDenial` **, чтение** - коллекция объектов отказов по резолюциям

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

+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetSenderSignature|_         | |Document-SaveContent|_            | |Document-GetAnyComment|_             | |Document-CreateReplySendTask2|_        |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetRecipientSignature|_      | |Document-SaveBuyerContent|_       | |Document-GetExternalStatuses|_       | |Document-SendReceiptsAsync|_           |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetDynamicContent|_          | |Document-SaveAllContent|_         | |Document-GetDocumentPackage|_        | |Document-Approve|_                     |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetBase64Content|_           | |Document-SaveAllContentAsync|_    | |Document-Delete|_                    | |Document-Disapprove|_                  |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetBase64ContentAsync|_      | |Document-SaveAllContentZip|_      | |Document-Move|_                      | |Document-CreateOutDocumentSignTask|_   |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetBase64Signature|_         | |Document-SaveAllContentZipAsync|_ | |Document-MarkAsRead|_                | |Document-CreateResolutionRequestTask|_ |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
| |Document-GetBase64OriginalSignature|_ | |Document-GetPrintForm|_           | |Document-AssignToResolutionRoute|_   | |Document-CreateCustomDataPatchTask|_   |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+
|                                        |                                    | |Document-RemoveFromResolutionRoute|_ |                                         |
+----------------------------------------+------------------------------------+---------------------------------------+-----------------------------------------+


.. |Document-GetSenderSignature| replace:: GetSenderSignature()
.. |Document-GetRecipientSignature| replace:: GetRecipientSignature()
.. |Document-GetDynamicContent| replace:: GetDynamicContent()
.. |Document-GetBase64Content| replace:: GetBase64Content()
.. |Document-GetBase64ContentAsync| replace:: GetBase64ContentAsync()
.. |Document-GetBase64Signature| replace:: GetBase64Signature()
.. |Document-GetBase64OriginalSignature| replace:: GetBase64OriginalSignature()

.. |Document-SaveContent| replace:: SaveContent()
.. |Document-SaveBuyerContent| replace:: SaveBuyerContent()
.. |Document-SaveAllContent| replace:: SaveAllContent()
.. |Document-SaveAllContentAsync| replace:: SaveAllContentAsync()
.. |Document-SaveAllContentZip| replace:: SaveAllContentZip()
.. |Document-SaveAllContentZipAsync| replace:: SaveAllContentZipAsync()
.. |Document-GetPrintForm| replace:: GetPrintForm()

.. |Document-GetAnyComment| replace:: GetAnyComment()
.. |Document-GetExternalStatuses| replace:: GetExternalStatuses()
.. |Document-GetDocumentPackage| replace:: GetDocumentPackage()
.. |Document-Delete| replace:: Delete()
.. |Document-Move| replace:: Move()
.. |Document-MarkAsRead| replace:: MarkAsRead()
.. |Document-AssignToResolutionRoute| replace:: AssignToResolutionRoute()
.. |Document-RemoveFromResolutionRoute| replace:: RemoveFromResolutionRoute()

.. |Document-CreateReplySendTask2| replace:: CreateReplySendTask2()
.. |Document-SendReceiptsAsync| replace:: SendReceiptsAsync()
.. |Document-Approve| replace:: Approve()
.. |Document-Disapprove| replace:: Disapprove()
.. |Document-CreateOutDocumentSignTask| replace:: CreateOutDocumentSignTask()
.. |Document-CreateResolutionRequestTask| replace:: CreateResolutionRequestTask()
.. |Document-CreateCustomDataPatchTask| replace:: CreateCustomDataPatchTask()



.. _Document-GetSenderSignature:
.. method:: Document.GetSenderSignature()

  Возвращает :doc:`представление подписи <Signature>` титула отправителя



.. _Document-GetRecipientSignature:
.. method:: Document.GetRecipientSignature()

  Возвращает :doc:`представление подписи <Signature>` титула получателя


.. _Document-GetDynamicContent:
.. method:: Document.GetDynamicContent(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает :doc:`упрощённое представление контента <DynamicContent>` титула документа со стороны *DocflowSide*.
  Если запрашиваемого титула у документа нет, то результатом будет :doc:`пустым <Descriptions/Empty_Com_Object>`.
  Если для данного документа не существует схемы, в которой можно представить контент документа, то так же результатом будет :doc:`пустым <Descriptions/Empty_Com_Object>`


.. _Document-GetBase64Content:
.. method:: Document.GetBase64Content(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает контент титула документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetBase64ContentAsync:
.. method:: Document.GetBase64ContentAsync(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает контент титула документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetBase64Signature:
.. method:: Document.GetBase64Signature(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, подпись титула которой будет представлена. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает подпись с меткой времени к титулу документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetBase64OriginalSignature:
.. method:: Document.GetBase64OriginalSignature(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, подпись титула которой будет представлена. :doc:`Возможные значения <Enums/DocflowSide>`

  Возвращает оригинальную подпись (обычно без метки времени) титула документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-SaveContent:
.. method:: Document.SaveContent(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет записан контент

  Сохраняет титул отправителя на диск в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан



.. _Document-SaveBuyerContent:
.. method:: Document.SaveBuyerContent(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет записан контент

  Сохраняет титул получателя документа в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан. Если титул отсутсвует, то ничего не произойдёт



.. _Document-SaveAllContent:
.. method:: Document.SaveAllContent(DirectoryPath, WithProtocol=false)

  :DirectoryPath: ``Строка`` Путь до директории, в которой будут сохранены файлы
  :WithProtocol:  ``Булево`` Признак необходимости сохранения протокола передачи документа

  Сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию



.. _Document-SaveAllContentAsync:
.. method:: Document.SaveAllContentAsync(DirectoryPath, WithProtocol=false)

  :DirectoryPath: ``Строка`` Путь до директории, в которой будут сохранены файлы
  :WithProtocol:  ``Булево`` Признак необходимости сохранения протокола передачи документа

  Асинхронно сохраняет все файлы, относящиеся к документу (в т.ч. электронные подписи), в указанную директорию



.. _Document-SaveAllContentZip:
.. method:: Document.SaveAllContentZip(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет сохранён архив

  Формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан



.. _Document-SaveAllContentZipAsync:
.. method:: Document.SaveAllContentZipAsync(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет сохранён архив

  Асинхронно формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанный файл. Если файла не существует, то он будет создан, иначе перезаписан



.. _Document-GetPrintForm:
.. method:: Document.GetPrintForm(FilePath, Timeout=30)

  :FilePath: ``Строка`` Путь до файла, в который будет сохранена печатная форма
  :Timeout:  ``Беззнаковое целое число`` Таймаут за который необходимо получить печатную форму в секундах

  Получает печатную форму документа в формате ``.pdf`` и сохраняет её в указанный файл. Если расширение файла отличается от ``.pdf``, то такой файл будет создан

  .. versionadded:: 3.0.10



.. _Document-GetAnyComment:
.. method:: Document.GetAnyComment(CommentType)

  :CommentType: ``строка`` Тип комментария. :doc:`Возможные значения <Enums/CommentType>`

  Возвращает строку с комментарием определённого типа, связанным с документом

  .. versionadded:: 5.20.3



.. _Document-GetExternalStatuses:
.. method:: Document.GetExternalStatuses()

  Возвращает :doc:`коллекцию <Collection>` :doc:`внешних статусов <ExternalStatus>` документа

  .. versionadded:: 5.32.0


.. _Document-GetDocumentPackage:
.. method:: Document.GetDocumentPackage()

  Возвращает :doc:`пакет документов <DocumentPackage>`, в котором находится документ

  .. versionadded:: 5.3.0

  .. note:: понятие пакета в терминах компоненты и в терминах `HTTP-API <http://api-docs.diadoc.ru/ru/latest/index.html>`_ или Веб-интерфейса разные.
    В данном случае в пакете будут содержаться только документы с одинаковым :doc:`MessageId <Descriptions/MessageId>`


.. _Document-Delete:
.. method:: Document.Delete()

  Помечает документ как удаленный



.. _Document-Move:
.. method:: Document.Move(DepartmentId)

  :DepartmentId: ``Строка`` Идентификатор подразделения

  Перемещает документ в указанное подразделение



.. _Document-MarkAsRead:
.. method:: Document.MarkAsRead()

  Помечает, что документ как прочитанный


.. _Document-AssignToResolutionRoute:
.. method:: Document.AssignToResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при постановке документа на маршрут

  Ставит документ на маршрут согласования. Получить доступные маршруты согласования можно методом :meth:`Organization.GetResolutionRoutes`



.. _Document-RemoveFromResolutionRoute:
.. method:: Document.RemoveFromResolutionRoute(RouteId[, Comment])

  :RouteId: ``строка`` Идентификатор маршрута
  :Comment: ``строка`` Комментарий, который будет добавлен при снятии документа с маршрута

  Снимает документ с маршрута согласования


.. _Document-CreateReplySendTask2:
.. method:: Document.CreateReplySendTask2(ReplyType="AcceptDocument")

  :ReplyType: ``строка`` Тип ответа. :doc:`Возможные значения <Enums/ReplyType>`

  Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask2>`

    .. versionadded:: 5.27.0


.. _Document-SendReceiptsAsync:
.. method:: Document.SendReceiptsAsync()

  Отправляет извещения о получении документа, необходимые для завершения документооборота. Возвращает объект :doc:`AsyncResult` с типом результата ``Булево``



.. _Document-Approve:
.. method:: Document.Approve([Comment])

  :Comment: ``Строка`` Комментарий, который будет указан при согласовании

  Согласует документ



.. _Document-Disapprove:
.. method:: Document.Disapprove([Comment])

  :Comment: ``Строка`` Комментарий, который будет указан при отказе согласования

  Отказывает в согласовании документа



.. _Document-CreateOutDocumentSignTask:
.. method:: Document.CreateOutDocumentSignTask()

  Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

  .. versionadded:: 5.6.0



.. _Document-CreateResolutionRequestTask:
.. method:: Document.CreateResolutionRequestTask()

  Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`



.. _Document-CreateCustomDataPatchTask:
.. method:: Document.CreateCustomDataPatchTask()

  Создает :doc:`задание на редактирование коллекции CustomData <CustomDataPatchTask>`



.. rubric:: Дополнительная информация

.. |Document-Inheritable| replace:: типов документов
.. _Document-Inheritable:

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


.. method:: Document.GetComment()

  Возвращает строку с комментарием к документу, заданным при отправке

  .. deprecated:: 5.20.3
    Используйте :meth:`GetAnyComment` с типом ``AttachmentComment``


.. method:: Document.SetOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Присваивает документу дополнительный идентификатор из учётной системы

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: Document.ReSetOneSDocumentId()

  Сбрасывает дополнительный идентификатор учётной системы у документа в Диадоке

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: Document.AddSubordinateOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Добавляет документу дополнительный идентификатор из учётной системы как подчинённый. Обычно используется чтобы обозначить связь документов друг с другом

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: Document.RemoveSubordinateOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Удаляет дополнительный подчинённый идентификатор

  .. deprecated:: 5.29.9
    Используйте :meth:`Organization.CreateDataTask`



.. method:: Document.CreateReplySendTask(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. :doc:`Возможные значения <./Enums/ReplyType>`

  Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask>`

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. method:: Document.SendRevocationRequest([Comment])

  :Comment: ``строка`` комментарий к запросу аннулирования

  Запрашивает аннулирование документа

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. method:: Document.AcceptRevocationRequest()

  Принимает запрос аннулирования

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. method:: Document.RejectRevocationRequest()

  Отказывает в аннулировании

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`
