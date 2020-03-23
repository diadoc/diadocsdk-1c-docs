Document
========

Объект является базовым объектом для всех |Document-Inheritable|_ .
Обладает базовым набором свойств и методов, которые также работают для всех производных типов документов.


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа

  .. depracetad:: 5.21.0
    Используйте тройку **TypeNamedId**, **DocumentFunction**, **Version**

:TypeNamedId:
  **Строка, чтение** - строковый идентификатор типа документа

  .. versionadded:: 5.21.0

:DocumentFunction:
  **Строка, чтение** - функция документа

  .. versionadded:: 5.21.0

:Version:
  **Строка, чтение** - информация о версии XSD схемы, в соотвествии с которой сформирован документ

  .. versionadded:: 5.21.0

:Organization:
  :doc:`Organization <Organization>` **, чтение** - организация, которая отправила исходящий документ, либо получила входящий документ

:OrganizationId:
  **Строка, чтение** - идентификатор организации, которой принадлежит документ

:Counteragent:
  :doc:`Counteragent <Counteragent>` **, чтение** - контрагент документа

:DocumentId:
  **Строка, чтение** - идентификатор документа

:OneSDocumentId:
  **Строка, чтение** - дополнительный идентификатор документа

:PackageId:
  **Строка, чтение** - идентификатор пакета

:Direction:
  **Строка, чтение** - направление документа. |Document-Direction|_

:Department:
  :doc:`Department <Department>` **, чтение** - подразделение организации, к которому привязан документ

:FromDepartment:
  :doc:`Department <Department>` **, чтение** - подразделение организации, из которого был отправлен документ

  .. versionadded:: 3.0.8

:ToDepartment:
  :doc:`Department <Department>` **, чтение** - подразделение организации, в которое был отправлен документ

  .. versionadded:: 3.0.8

:Timestamp:
  **Дата и время, чтение** - дата и время отправки документа (в текущем часовом поясе)

:TimestampSeconds:
  **Число, чтение** - дата и время отправки документа в секундах

:DocumentDate:
  **Дата, чтение** - дата документа

:DocumentNumber:
  **Строка, чтение** - номер документа

:Title:
  **Строка, чтение** - название документа, например, ``Счет-фактура №123 от 20.02.18``

:FileName:
  **Строка, чтение** - имя файла документа, с которым он загружался в Диадок

:PathURL:
  **Строка, чтение** - URL документа, по которому он доступен в web-интерфейсе

:InitialDocumentIds:
  :doc:`Коллекция  <Collection>` **строк, чтение** - коллекция идентификаторов документов, на который ссылается данный документ (т.е. документы, которые по отношению к данному документы являются "родительскими"

:SubordinateDocumentIds:
  :doc:`Коллекция <Collection>` **строк, чтение** - коллекция идентификаторов документов, которые ссылаются на данный документ (т.е. документы, которые по отношению к данному документу являются "дочерними")

:CustomDocumentId:
  **Строка, чтение** - идентификатор документа, определяемый внешней системой

:RouteId:
  **Строка, чтение** - идентификатор маршрута согласования, на котором находится документ

:WorkflowId:
  **Целое число, чтение** - идентификатор типа документооборота

:Status:
  **Строка, чтение** - текущий статус документа в Диадоке. Перечень возможных значений зависит от типа документа и описан в спецификации соответствующего производного объекта

:ResolutionStatus:
  :doc:`ResolutionStatus <ResolutionStatus>` **, чтение** - текущий статус запрошенного согласования или подписи документа

:Resolutions:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Resolution <Resolution>` **, чтение** - история резолюций документа: согласований, подписаний, аннулирований

:ResolutionRequests:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ResolutionRequest <ResolutionRequest>` **, чтение** - история запросов резолюций документа: запросов согласований, запросов подписаний, запросов аннулирований

:ResolutionRequestDenials:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ResolutionRequestDenial <ResolutionRequestDenial>` **, чтение** - коллекция объектов отказов по резолюциям

:RevocationStatus:
  **Строка, чтение** - статус аннулирования документа. |Document-RevocationStatus|_

:SenderSignatureStatus:
  **Строка, чтение** - статус проверки ЭЦП отправителя. |Document-SenderSignatureStatus|_

:RecipientResponseStatus:
  **Строка, чтение** - отвечает за состояние ответного действия со стороны получателя документа. |Document-RecipientResponseStatus|_

:RoamingNotificationStatus:
  **Строка, чтение** - статус передачи документа через роуминг. |Document-RoamingNotificationStatus|_

  .. versionadded:: 5.3.1

:RoamingNotificationStatusDescription:
  **Строка, чтение** - описание статуса передачи документа через роуминг

  .. versionadded:: 5.3.1

:CustomData:
  :doc:`Коллекция <Collection>` **объектов** :doc:`CustomDataItem <CustomDataItem>` **, чтение** - коллекция элементов "ключ-значение"

:Metadata:
  :doc:`Коллекция <Collection>` **объектов** :doc:`MetadataItem <MetadataItem>` **, чтение** - коллекция метаданных

:RecipientReceiptMetadata:
  :doc:`RecipientReceiptMetadata <RecipientReceiptMetadata>` **, чтение** - метаданные извещения о получении документа получателем

:ConfirmationMetadata:
  :doc:`ConfirmationMetadata <ConfirmationMetadata>` **, чтение** - метаданные подтверждения оператором отправки/получения документа или служебного документа

:AmendmentRequestMetadata:
  :doc:`AmendmentRequestMetadata <AmendmentRequestMetadata>` **, чтение** - метаданные уведомления об уточнении

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

:IsRead:
  **Булево, чтение** - флаг, показывающий, что документ был прочитан сотрудником организации

:IsEncryptedContent:
  **Булево, чтение** - флаг, показывающий, что содержимое документа зашифровано

  .. versionadded:: 5.3.0


.. rubric:: Методы

+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-SaveContent|_                | |Document-GetComment|_                      | |Document-GetDocumentPackage|_          |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-SaveBuyerContent|_           | |Document-GetAnyComment|_                   | |Document-CreateReplySendTask|_         |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-SaveAllContent|_             | |Document-Move|_                            | |Document-CreateReplySendTask2|_        |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-SaveAllContentAsync|_        | |Document-Delete|_                          | |Document-CreateOutDocumentSignTask|_   |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-SaveAllContentZip|_          | |Document-MarkAsRead|_                      | |Document-CreateResolutionRequestTask|_ |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-SaveAllContentZipAsync|_     | |Document-SendRevocationRequest|_           | |Document-CreateCustomDataPatchTask|_   |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetDynamicContent|_          | |Document-AcceptRevocationRequest|_         | |Document-AssignToResolutionRoute|_     |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetBase64Content|_           | |Document-RejectRevocationRequest|_         | |Document-RemoveFromResolutionRoute|_   |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetBase64ContentAsync|_      | |Document-AddSubordinateOneSDocumentId|_    | |Document-SetOneSDocumentId|_           |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetBase64Signature|_         | |Document-RemoveSubordinateOneSDocumentId|_ | |Document-ReSetOneSDocumentId|_         |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetBase64OriginalSignature|_ | |Document-GetPrintForm|_                    |                                         |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetSenderSignature|_         | |Document-Approve|_                         |                                         |
+----------------------------------------+---------------------------------------------+-----------------------------------------+
| |Document-GetRecipientSignature|_      | |Document-Disapprove|_                      |                                         |
+----------------------------------------+---------------------------------------------+-----------------------------------------+


.. |Document-SaveContent| replace:: SaveContent()
.. |Document-SaveBuyerContent| replace:: SaveBuyerContent()
.. |Document-SaveAllContent| replace:: SaveAllContent()
.. |Document-SaveAllContentAsync| replace:: SaveAllContentAsync()
.. |Document-SaveAllContentZip| replace:: SaveAllContentZip()
.. |Document-SaveAllContentZipAsync| replace:: SaveAllContentZipAsync()
.. |Document-GetDynamicContent| replace:: GetDynamicContent()
.. |Document-GetBase64Content| replace:: GetBase64Content()
.. |Document-GetBase64ContentAsync| replace:: GetBase64ContentAsync()
.. |Document-GetBase64Signature| replace:: GetBase64Signature()
.. |Document-GetBase64OriginalSignature| replace:: GetBaseOriginal64Signature()
.. |Document-GetSenderSignature| replace:: GetSenderSignature()
.. |Document-GetRecipientSignature| replace:: GetRecipientSignature()
.. |Document-GetComment| replace:: GetComment()
.. |Document-GetAnyComment| replace:: GetAnyComment()
.. |Document-Move| replace:: Move()
.. |Document-Delete| replace:: Delete()
.. |Document-Approve| replace:: Approve()
.. |Document-Disapprove| replace:: Disapprove()
.. |Document-SetOneSDocumentId| replace:: SetOneSDocumentId()
.. |Document-ReSetOneSDocumentId| replace:: ReSetOneSDocumentId()
.. |Document-AddSubordinateOneSDocumentId| replace:: AddSubordinateOneSDocumentId()
.. |Document-RemoveSubordinateOneSDocumentId| replace:: RemoveSubordinateOneSDocumentId()
.. |Document-CreateResolutionRequestTask| replace:: CreateResolutionRequestTask()
.. |Document-GetPrintForm| replace:: GetPrintForm()
.. |Document-GetDocumentPackage| replace:: GetDocumentPackage()
.. |Document-CreateReplySendTask| replace:: CreateReplySendTask()
.. |Document-CreateReplySendTask2| replace:: CreateReplySendTask2()
.. |Document-CreateOutDocumentSignTask| replace:: CreateOutDocumentSignTask()
.. |Document-MarkAsRead| replace:: MarkAsRead()
.. |Document-CreateCustomDataPatchTask| replace:: CreateCustomDataPatchTask()
.. |Document-AssignToResolutionRoute| replace:: AssignToResolutionRoute()
.. |Document-RemoveFromResolutionRoute| replace:: RemoveFromResolutionRoute()
.. |Document-SendRevocationRequest| replace:: SendRevocationRequest()
.. |Document-AcceptRevocationRequest| replace:: AcceptRevocationRequest()
.. |Document-RejectRevocationRequest| replace:: RejectRevocationRequest()

.. _Document-SaveContent:
.. method:: Document.SaveContent(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет записан контент

  Сохраняет титул отправителя на диск



.. _Document-SaveBuyerContent:
.. method:: Document.SaveBuyerContent(FilePath)

  :FilePath: ``Строка`` Путь до файла, в который будет записан контент

  Сохраняет титул получателя документа в указанный файл. Если  титул отсутсвует, то ничего не произойдёт



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
.. method:: Document.SaveAllContentZip(DirectoryPath)

  :DirectoryPath: ``Строка`` Путь до директории, в которой будет сохранён архив

  Формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанную директорию



.. _Document-SaveAllContentZipAsync:
.. method:: Document.SaveAllContentZipAsync(DirectoryPath)

  :DirectoryPath: ``Строка`` Путь до директории, в которой будет сохранён архив

  Асинхронно формирует архив, содержащий все файлы, относящиеся к документу (в т.ч. электронные подписи), и сохраняет его в указанную директорию



.. _Document-GetDynamicContent:
.. method:: Document.GetDynamicContent(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. |Document-DocflowSide|_

  Возвращает :doc:`представление контента титула документа <DynamicContent>` со стороны *WorkflowSide*.
  Если запрашиваемого титула у документа нет, то результатом будет ``Undefined`` / ``Неопределено``.
  Если для данного документа не существует схемы, в которой можно представить контент документа, то так же результатом будет ``Undefined`` / ``Неопределено``



.. _Document-GetBase64Content:
.. method:: Document.GetBase64Content(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. |Document-DocflowSide|_

  Возвращает контент титула документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetBase64ContentAsync:
.. method:: Document.GetBase64ContentAsync(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, чей титул будет представлен. |Document-DocflowSide|_

  Возвращает контент титула документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetBase64Signature:
.. method:: Document.GetBase64Signature(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, подпись титула которой будет представлена. |Document-DocflowSide|_

  Возвращает подпись с меткой времени к титулу документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetBase64OriginalSignature:
.. method:: Document.GetBase64OriginalSignature(DocflowSide)

  :DocflowSide: ``Строка`` Сторона документооборота, подпись титула которой будет представлена. |Document-DocflowSide|_

  Возвращает оригинальную подпись (обычно без метки времени) титула документа со стороны *DocflowSide* в виде Base64 строки



.. _Document-GetSenderSignature:
.. method:: Document.GetSenderSignature()

  Возвращает :doc:`представление подписи <Signature>` титула отправителя



.. _Document-GetRecipientSignature:
.. method:: Document.GetRecipientSignature()

  Возвращает :doc:`представление подписи <Signature>` титула получателя



.. _Document-GetComment:
.. method:: Document.GetComment()

  Возвращает строку с комментарием к документу, заданным при отправке

  .. deprecated:: 5.20.3
    Используйте :meth:`GetAnyComment` с типом ``AttachmentComment``



.. _Document-GetAnyComment:
.. method:: Document.GetAnyComment(CommentType)

  :CommentType: ``строка`` Тип комментария

  Возвращает строку с комментарием определённого типа, связанным с документом

  ========================== ==================================
  Значение *CommentType*     Описание
  ========================== ==================================
  AttachmentComment          комментарий к документу
  RecipientAttachmentComment комментарий к титулу покупателя
  SignatureRejectionComment  комментарий к отказу в подписи
  AmendmentComment           комментарий к запросу на уточнение
  ========================== ==================================

  .. versionadded:: 5.20.3



.. _Document-Move:
.. method:: Document.Move(DepartmentId)

  :DepartmentId: ``Строка`` Идентификатор подразделения

  Перемещает документ в указанное подразделение. Идентификатор головного подразделения всегда ``00000000-0000-0000-0000-000000000000``



.. _Document-Delete:
.. method:: Document.Delete()

  Помечает документ как удаленный



.. _Document-Approve:
.. method:: Document.Approve([Comment])

  :Comment: ``Строка`` Комментарий, который будет указан при согласовании

  Согласует документ



.. _Document-Disapprove:
.. method:: Document.Disapprove([Comment])

  :Comment: ``Строка`` Комментарий, который будет указан при отказе согласования

  Отказывает в согласовании документа



.. _Document-SetOneSDocumentId:
.. method:: Document.SetOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Присваивает документу дополнительный идентификатор из учётной системы




.. _Document-ReSetOneSDocumentId:
.. method:: Document.ReSetOneSDocumentId()

  Сбрасывает дополнительный идентификатор учётной системы у документа в Диадоке



.. _Document-AddSubordinateOneSDocumentId:
.. method:: Document.AddSubordinateOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Добавляет документу дополнительный идентификатор из учётной системы как подчинённый. Обычно используется чтобы обозначить связь документов друг с другом




.. _Document-RemoveSubordinateOneSDocumentId:
.. method:: Document.RemoveSubordinateOneSDocumentId(ID)

  :ID: ``Строка`` Любая строка, идентифицирующая документ в учётной системе

  Удаляет дополнительный подчинённый идентификатор



.. _Document-CreateResolutionRequestTask:
.. method:: Document.CreateResolutionRequestTask()

  Создает :doc:`задание для отправки запроса согласования <ResolutionRequestTask>`



.. _Document-GetPrintForm:
.. method:: Document.GetPrintForm(FilePath[, Timeout])

  :FilePath: ``Строка`` Путь до файла, в который будет сохранена печатная форма
  :Timeout:  ``Беззнаковое целое число`` Таймаут за который необходимо получить печатную форму

  Получает печатную форму документа в формате ``.pdf`` и сохраняет её в указанный файл. Если расширение файла отличается от ``.pdf``, то такой файл будет создан/
  Совершается 5 попыток сгенерировать печатную форму. Если за 5 попыток она не получена или, если превышен таймаут, то будет сгенерировано исключение

  .. versionadded:: 3.0.10



.. _Document-GetDocumentPackage:
.. method:: Document.GetDocumentPackage()

  Возвращает :doc:`пакет документов <DocumentPackage>`, в котором находится документ

  .. versionadded:: 5.3.0

  .. note:: понятие пакета в терминах компоненты и в терминах `HTTP-API <http://api-docs.diadoc.ru/ru/latest/index.html>`_ или Веб-интерфейса разные.
    В данном случае в пакете будут содержаться только те документы, у которых LetterId/MessageId (первая половина DocumentId) совпадает со значением в исходном документе.
    Не стоит ожидать, что если документы связаны в пакет в веб интерфейсе, то все они вернутся в этом методе.



.. _Document-CreateReplySendTask:
.. method:: Document.CreateReplySendTask(ReplyType="AcceptDocument")

  :ReplyType: ``Строка`` Тип ответа. |Document-ReplyType|_

  Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask>`

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. _Document-CreateReplySendTask2:
.. method:: Document.CreateReplySendTask2(ReplyType="AcceptDocument")

  :ReplyType: ``строка`` Тип ответа. |Document-ReplyType|_

  Создает :doc:`задание на выполнение ответного действия с документом <ReplySendTask2>`

    .. versionadded:: 5.27.0



.. _Document-CreateOutDocumentSignTask:
.. method:: Document.CreateOutDocumentSignTask()

  Создает :doc:`задание на подписание и отправку исходящего документа с отложенной отправкой <OutDocumentSignTask>`

  .. versionadded:: 5.6.0



.. _Document-MarkAsRead:
.. method:: Document.MarkAsRead()

  Помечает, что документ как прочитанный



.. _Document-CreateCustomDataPatchTask:
.. method:: Document.CreateCustomDataPatchTask()

  Создает :doc:`задание на редактирование коллекции CustomData <CustomDataPatchTask>`



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


.. _Document-SendRevocationRequest:
.. method:: Document.SendRevocationRequest([Comment])

  :Comment: ``строка`` комментарий к запросу аннулирования

  Запрашивает аннулирование документа

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. _Document-AcceptRevocationRequest:
.. method:: Document.AcceptRevocationRequest()

  Принимает запрос аннулирования

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. _Document-RejectRevocationRequest:
.. method:: Document.RejectRevocationRequest()

  Отказывает в аннулировании

  .. versionadded:: 3.0.3

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. rubric:: Дополнительная информация


.. |Document-DocflowSide| replace:: Возможные значения
.. _Document-DocflowSide:

======================= =================
Значение *DocflowSide*  Описание
======================= =================
Seller                  Титул отправителя
Buyer                   Титул получателя
======================= =================


.. |Document-ReplyType| replace:: Возможные значения
.. _Document-ReplyType:

==================== =================================
Значение *ReplyType* Описание
==================== =================================
AcceptDocument       подписание документа
RejectDocument       отказ в подписи документа
CorrectionRequest    запроc на уточнение документа
RevocationRequest    запроc на аннулирование документа
AcceptRevocation     принятие аннулирования документа
RejectRevocation     отказ от аннулирования документа
==================== =================================


.. |Document-Direction| replace:: Возможные значения
.. _Document-Direction:

==================== ===================
Значение *Direction* Описание
==================== ===================
Inbound              входящий документ
Outbound             исходящий документ
Internal             внутренний документ
==================== ===================


.. |Document-RevocationStatus| replace:: Возможные значения
.. _Document-RevocationStatus:

=========================== =====================================================================
Значение *RevocationStatus* Описание
=========================== =====================================================================
RevocationStatusNone        документ не аннулирован, и не было предложений об аннулировании
RevocationIsRequestedByMe   отправлено исходящее предложение об аннулировании документа
RequestsMyRevocation        получено входящее предложение об аннулировании документа
RevocationAccepted          документ аннулирован
RevocationRejected          получен или отправлен отказ от предложения об аннулировании документа
UnknownRevocationStatus     неизвестный статус аннулирования документа
=========================== =====================================================================


.. |Document-RoamingNotificationStatus| replace:: Возможные значения
.. _Document-RoamingNotificationStatus:

==================================== =====================================================
Значение *RoamingNotificationStatus* Описание
==================================== =====================================================
RoamingNotificationStatusNone        документ не доставлялся в роуминг
RoamingNotificationStatusSuccess     документ с подтверждением успешной доставки в роуминг
RoamingNotificationStatusError       документ с ошибкой доставки в роуминг
UnknownRoamingNotificationStatus     неизвестный роуминговый статус документа
==================================== =====================================================


.. |Document-SenderSignatureStatus| replace:: Возможные значения
.. _Document-SenderSignatureStatus:

================================ =========================================
Значение *SenderSignatureStatus* Описание
================================ =========================================
WaitingForSenderSignature        ожидается подпись отправителя
SenderSignatureUnchecked         подпись отправителя еще не проверена
SenderSignatureCheckedAndValid   подпись отправителя проверена и валидна
SenderSignatureCheckedAndInvalid подпись отправителя проверена и невалидна
UnknownSenderSignatureStatus     неизвестный статус проверки подписи
================================ =========================================


.. |Document-RecipientResponseStatus| replace:: Возможные значения
.. _Document-RecipientResponseStatus:

==================================== ==================================================
Значение *RecipientResponseStatus*   Описание
==================================== ==================================================
RecipientResponseStatusUnknown       неизвестный статус ответного действия
RecipientResponseStatusNotAcceptable ответного действия не требуется
WaitingForRecipientSignature         ожидается ответное действие получателя
WithRecipientSignature               получатель подписал документ (ответный титул)
RecipientSignatureRequestRejected    получатель отказал в подписи
InvalidRecipientSignature            получатель подписал документ некорректной подписью
==================================== ==================================================



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
:doc:`BaseDocument`                       документ произвольного типа
========================================= ======================================================
