DocumentsTask
=============

Объект предназначен для получения списка документов, отправленных из
выбранного ящика или пришедших в него.

Свойства объекта
----------------


- **FromSendDate** (дата и время, чтение/запись ) - дата отправки или получения документа, начальная дата интервала

- **ToSendDate** (дата и время, чтение/запись ) - дата отправки или получения документа, конечная дата интервала

- **FromDocumentDate** (дата и время, чтение/запись ) - дата документа, начальная дата интервала

- **ToDocumentDate** (дата и время, чтение/запись ) - дата документа, конечная дата интервала

- **Category** (строка, чтение/запись ) - категория типов документов

- **CounteragentId** (строка, чтение/запись ) - идентификатор контрагента, в адрес которого были отправлены или от которого были получены документы

- **DepartmentId** (строка, чтение/запись ) - идентификатор подразделения организации

- **RequireOneSDocumentId** (булево, чтение/запись ) - признак того, что необходимо загружать идентификаторы 1С

- **ExcludeSubdepartments** (булево, чтение/запись ) - признак того, что в выборку не нужно включать документы по подразделениям, которые являются дочерними по отношению к подразделению, идентификатор которого задан в параметре DepartmentId

- **Top100** (булево, чтение/запись ) - признак того, что нужно вернуть только первые сто документов


Методы объекта
--------------


-  :doc:`GetDocuments <GetDocuments>` - возвращает список документов в текущем ящике по заданному фильтру

-  :doc:`GetDocumentsAsync <GetDocumentsAsync>` - инициирует асинхронную операцию получения списка документов в текущем ящике по заданному фильтру


Использовать параметры FromSendDate/ToSendDate и
FromDocumentDate/ToDocumentDate одновременно нельзя. Фильтрация
производится либо по дате документа, либо по дате его передачи через
Диадок.


.. toctree::
   :name: Auto_1
   :hidden:

   GetDocuments <GetDocuments>
   GetDocumentsAsync <GetDocumentsAsync>

Правила формирования параметра **FilterCategory**
-----------------------------------------------------

Обязательный параметр <FilterCategory> задается строкой в формате
"ТИП\_ДОКУМЕНТА.ТИП\_ФИЛЬТРА". Первая часть строки задает тип документа
и может принимать одно из следующих значений:

-  Any – любой документ
-  Invoice – счет-фактура
-  InvoiceRevision – исправление счета-фактуры
-  InvoiceCorrection – корректировочный счет-фактура
-  InvoiceCorrectionRevision – исправление корректировочного
   счета-фактуры
-  AnyInvoiceDocumentType – любой вид счет-фактуры
-  Torg12 – неформализованная накладная ТОРГ-12
-  XmlTorg12 – накладная ТОРГ-12 в формате ФНС
-  AcceptanceCertificate – неформализованный акт о выполнении работ
-  XmlAcceptanceCertificate – акт о выполнении работ в формате ФНС
-  TrustConnectionRequest – запрос на инициацию канала обмена
   документами через Диадок
-  PriceListAgreement – протокол согласования цены
-  CertificateRegistry – реестр сертификатов
-  ReconciliationAct – акт сверки
-  Contract – договор
-  ProformaInvoice – счет на оплату
-  ServiceDetails – детализация

ТИП\_ФИЛЬТРА указывает дополнительную информацию для отбора документов
указанного типа. Набор возможных значений фильтра зависит от типа
выбираемого документа.



Отбор по статусу подписания документа
""""""""""""""""""""""""""""""""""""""

- Для всех типов документов применимы статусы
    - **Inbound** все входящие документы
    - **Outbound** все исходящие документы
    - **OutboundWaitingForSenderSignature** исходящие документы, требующие подписания и отправки
    - **OutboundInvalidSenderSignature** исходящие документы с невалидной подписью отправителя, требующие повторного подписания и отправки
- Для документов с типами Invoice, InvoiceRevision, InvoiceCorrection, InvoiceCorrectionRevision, AnyInvoiceDocumentType применимы следующие статусы
    - **OutboundNotFinished** Исходящий, документооборот не завершен
    - **OutboundFinished**  Исходящий, документооборот завершен
    - **InboundNotFinished** Входящий, документооборот не завершен
    - **InboundFinished** Входящий, документооборот завершен
- Для документов с типами Torg12, XmlTorg12, AcceptanceCertificate, XmlAcceptanceCertificate, Nonformalized, TrustConnectionRequest, PriceListAgreement, CertificateRegistry, ReconciliationAct, Contract применимы следующие статусы
    - **OutboundWaitingForRecipientSignature** исходящий документ в ожидании ответной подписи
    - **OutboundWithRecipientSignature** исходящий документ с ответной подписью
    - **OutboundRecipientSignatureRequestRejected** исходящий документ с отказом в ответной подписи
    - **InboundWaitingForRecipientSignature** входящий документ в ожидании ответной подписи
    - **InboundWithRecipientSignature** входящий документ с ответной подписью
    - **InboundRecipientSignatureRequestRejected** входящий документ с отказом в ответной подписи   
- Для документов с типами Nonformalized, PriceListAgreement, CertificateRegistry применимы следующие статусы
    - **OutboundNoRecipientSignatureRequest** исходящий документ без запроса ответной подписи
    - **InboundNoRecipientSignatureRequest** вхдящий документ без запроса ответной подписи

Отбор по статусу согласования документа
"""""""""""""""""""""""""""""""""""""""""

Для всех типов документы применимы следующие статусы:

- **OutboundWaitingForResolution** исходящий документ, переданный на согласование или подписание
- **OutboundApproved** согласованный исходящий документ
- **OutboundDisapproved** исходящий документ с отказом в согласовании
- **InboundWaitingForResolution** входящий документ, переданный на согласование или подписание
- **InboundApproved** согласованный входящий документ
- **InboundDisapproved** входящий документ с отказом в согласовании

Отбор по статусу аннулирования документа
"""""""""""""""""""""""""""""""""""""""""

Для всех типов документы применимы следующие статусы:

- **OutboundRevocationIsRequestedByMe** исходящий документ, по которому запрошено аннулирование у другой стороны
- **OutboundRequestsMyRevocation** исходящий документ, по которому другой стороной запрошено аннулирование
- **OutboundRevocationAccepted** исходящий аннулированный документ
- **OutboundRevocationRejected** исходящий документ, по которому получен отказ на запрос об аннулировании
- **InboundRevocationIsRequestedByMe** входящий документ, по которому запрошено аннулирование у другой стороны
- **InboundRequestsMyRevocation** входящий документ, по которому другой стороной запрошено аннулирование
- **InboundRevocationAccepted** входящий аннулированный документ
- **InboundRevocationRejected** входящий документ, по которому получен отказ на запрос об аннулировании




Пример использования
--------------------

Следующая процедура позволяет получить список всех входящих
формализованных торг-12, которые требуется подписать:

::

        Процедура ПолучитьСписокНеподписанныхТорг12(Organization)
            DocumentsTask = Organization.GetDocumentsTask();
            DocumentsTask.FromSendDate = НачалоГода(ТекущаяДата());
            DocumentsTask.ToSendDate = КонецГода(ТекущаяДата());
            DocumentsTask.Category = "XmlTorg12.InboundWaitingForRecipientSignature";

            DocumentList = DocumentsTask.GetDocuments();
            ц = 0;
            Пока ц < DocumentList.Count цикл
                Document = DocumentList.GetItem(ц);
                Сообщить("Не подписан торг-12 №"+Document.Number+" от "+Document.Date);
                ц = ц +1;
            КонецЦикла;
        КонецПроцедуры

.. toctree::
   :name: Auto_2
   :hidden:

   GetDocuments <GetDocuments>
   GetDocumentsAsync <GetDocumentsAsync>

