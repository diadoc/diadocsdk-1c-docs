PackageSendTask
===============

Задание для отправки сообщения с пакетом документов на сервер Диадок

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`PackageSendTask2 <PackageSendTask2>`


.. rubric:: Свойства

:Content:
  :doc:`SentPackageContent <SentPackageContent>` **, чтение** - содержание пакета документов

:OperationId:
  **Строка, чтение/запись** - уникальный идентификатор операции

:CounterAgentId:
  **Строка, чтение/запись** - идентификатор контрагента

:FromDepartmentId:
  **Строка, чтение/запись** - идентификатор подразделения отправителя

:ToDepartmentId:
  **Строка, чтение/запись** - идентификатор подразделения получателя

:IsDraft:
  **Булево, чтение/запись** - признак того, что сообщение является черновиком

:IsInternal:
  **Булево, чтение/запись** - признак того, что сообщение является внутренним, то есть сообщением между подразделениями организации

:LockPackage:
  **Булево, чтение/запись** - признак того, что пакет после отправки должен быть нередактируемым

:DelaySend:
  **Булево, чтение/запись** - признак того, что сообщение будет сохранено без отправки

:DocumentsToSend:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentToSend <DocumentToSend>` **, чтение** - документы на отправку, добавленные в пакет

:ProxyBoxId:
  **Строка, чтение/запись** - идентификатор ящика, промежуточного получателя

:ProxyDepartmentId:
  **Строка, чтение/запись** -  идентификатор подразделения, в ящике промежуточного получателя

:UseShelf:
  **Булево, чтение/запись** - отправлять документы частями, а не за один запрос. Рекомендуется использовать для больших документов

:SaveContentPath:
  **Строка, чтение/запись** - путь к папке, для сохранения сгенерированного содержимого


.. rubric:: Методы

+--------------------------------+----------------------------------------+-------------------------------------------+
| |PackageSendTask-AddDocument|_ | |PackageSendTask-AddDocumentFromFile|_ | |PackageSendTask-AddDocumentFromFileRaw|_ |
+--------------------------------+----------------------------------------+-------------------------------------------+
| |PackageSendTask-Send|_        | |PackageSendTask-SendAsync|_           | |PackageSendTask-AddEncryptCertificate|_  |
+--------------------------------+----------------------------------------+-------------------------------------------+

.. |PackageSendTask-AddDocument| replace:: AddDocument()
.. |PackageSendTask-AddDocumentFromFile| replace:: AddDocumentFromFile()
.. |PackageSendTask-AddDocumentFromFileRaw| replace:: AddDocumentFromFileRaw()
.. |PackageSendTask-Send| replace:: Send()
.. |PackageSendTask-SendAsync| replace:: SendAsync()
.. |PackageSendTask-AddEncryptCertificate| replace:: AddEncryptCertificate()



.. _PackageSendTask-AddDocument:
.. method:: PackageSendTask.AddDocument(FormalizedDocumentType)

  :FormalizedDocumentType: ``строка`` тип документа. |PackageSendTask-FormalizedDocumentType|_

  Добавляет :doc:`новый элемент <DocumentToSend>` в коллекцию *DocumentsToSend* и возвращает его



.. _PackageSendTask-AddDocumentFromFile:
.. method:: PackageSendTask.AddDocumentFromFile(FormalizedDocumentType, FilePath)

  :FormalizedDocumentType: ``строка`` тип документа. |PackageSendTask-FormalizedDocumentType|_
  :FilePath: ``строка`` путь до файла контента

  Добавляет :doc:`новый элемент <DocumentToSend>` в коллекцию *DocumentsToSend*, загружая контент из файла, и возвращает его.
  Контент будет разобран и получен в виде объектной модели, если это возможно. При отправке он будет перегенерирован



.. _PackageSendTask-AddDocumentFromFileRaw:
.. method:: PackageSendTask.AddDocumentFromFileRaw(DocumentType, FilePath)

  :DocumentType: ``строка`` тип документа. |PackageSendTask-DocumentType|_
  :FilePath: ``строка`` путь до файла контента

  Добавляет :doc:`новый элемент <DocumentToSend>` в коллекцию *DocumentsToSend*, загружая контент из файла, и возвращает его.
  Разбора контента и представления в виде объектной модели не происходит. При отправке перегенерации контента не произойдёт



.. _PackageSendTask-Send:
.. method:: PackageSendTask.Send()

  Отправляет пакет документов в Диадок и возвращает :doc:`отправленные документы <DocumentPackage>`.
  Если отправка пакета с заполненным *OperationId* завершилась успехом, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового пакета, а в результате выполнения метода вернется ранее отправленный пакет



.. _PackageSendTask-SendAsync:
.. method:: PackageSendTask.SendAsync()

  Асинхронно отправляет пакет документов в Диадок и возвращает :doc:`AsyncResult` с :doc:`отправленными документами <DocumentPackage>` в качестве результата.
  Если отправка пакета с заполненным *OperationId* завершилась успехом, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового пакета, а в результате выполнения метода вернется ранее отправленный пакет



.. _PackageSendTask-AddEncryptCertificate:
.. method:: PackageSendTask.AddEncryptCertificate(Certificate)

  :Certificate: :doc:`PersonalCertificate` сертификат КЭП

  Добавляет :doc:`сертификат <PersonalCertificate>` для шифрования контента



.. rubric:: Дополнительная информация

.. |PackageSendTask-FormalizedDocumentType| replace:: Возможные значения
.. _PackageSendTask-FormalizedDocumentType:

========================================================== ==================================================================== ======================================
Значение *FormalizedDocumentType*                          Описание                                                             Тип *DocumentToSend*
========================================================== ==================================================================== ======================================
Invoice                                                    счет-фактура в формате 93 приказа ФНС                                :doc:`InvoiceToSend`
InvoiceCorrection                                          корректировочный счет-фактура в формате 93 приказа ФНС               :doc:`InvoiceCorrectionToSend`
InvoiceRevision                                            исправительный счет-фактура в формате 93 приказа ФНС                 :doc:`InvoiceRevisionToSend`
InvoiceCorrectionRevision                                  исправление корректировочного счета-фактуры в формате 93 приказа ФНС :doc:`InvoiceCorrectionRevisionToSend`
XmlAcceptanceCertificate                                   акт о выполнении работ в формате 172 приказа ФНС                     :doc:`XmlActToSend`
XmlTorg12                                                  ТОРГ-12 в формате 172 приказа ФНС                                    :doc:`XmlTorg12ToSend`
UniversalTransferDocument                                  УПД в формате 155 приказа ФНС                                        :doc:`UtdToSend`
UniversalTransferDocumentRevision                          исправление УПД в формате 155 приказа ФНС                            :doc:`UtdToSend`
UniversalCorrectionDocument                                УКД в формате 189 приказа ФНС                                        :doc:`UcdToSend`
UniversalCorrectionDocumentRevision                        исправление УКД в формате 189 приказа ФНС                            :doc:`UcdToSend`
UtdTorg12                                                  ТОРГ-12 в формате 155 приказа ФНС                                    :doc:`UtdToSend`
UtdAcceptanceCertificate                                   акт о выполнении работ в формате 155 приказа ФНС                     :doc:`UtdToSend`
UtdInvoice                                                 счет-фактура в формате 155 приказа ФНС                               :doc:`UtdToSend`
UcdInvoiceCorrection                                       корректировка счета-фактуры в формате 189 приказа ФНС                :doc:`UtdToSend`
TovTorg                                                    Торг-12 в формате 551-го приказа ФНС                                 :doc:`TovTorgToSend`
XmlAcceptanceCertificate552                                акт в формате 552-го приказа ФНС                                     :doc:`XmlAct552ToSend`
один из :doc:`DocumentVersion.Version <DocumentVersion>`   произвольный формализованный документ                                :doc:`CustomDocumentToSend`
Document (для :meth:`PackageSendTask.AddDocumentFromFile`) произвольный формализованный документ                                :doc:`CustomDocumentToSend`
========================================================== ==================================================================== ======================================


.. |PackageSendTask-DocumentType| replace:: Возможные значения
.. _PackageSendTask-DocumentType:

========================================================== ==================================================================== ======================================
Значение *DocumentType*                                    Описание                                                             Тип *DocumentToSend*
========================================================== ==================================================================== ======================================
Invoice                                                    счет-фактура в формате 93 приказа ФНС                                :doc:`InvoiceToSend`
InvoiceCorrection                                          корректировочный счет-фактура в формате 93 приказа ФНС               :doc:`InvoiceCorrectionToSend`
InvoiceRevision                                            исправительный счет-фактура в формате 93 приказа ФНС                 :doc:`InvoiceRevisionToSend`
InvoiceCorrectionRevision                                  исправление корректировочного счета-фактуры в формате 93 приказа ФНС :doc:`InvoiceCorrectionRevisionToSend`
XmlAcceptanceCertificate                                   акт о выполнении работ в формате 172 приказа ФНС                     :doc:`XmlActToSend`
XmlTorg12                                                  ТОРГ-12 в формате 172 приказа ФНС                                    :doc:`XmlTorg12ToSend`
UniversalTransferDocument                                  УПД в формате 155 приказа ФНС                                        :doc:`UtdToSend`
UniversalTransferDocumentRevision                          исправление УПД в формате 155 приказа ФНС                            :doc:`UtdToSend`
UniversalCorrectionDocument                                УКД в формате 189 приказа ФНС                                        :doc:`UcdToSend`
UniversalCorrectionDocumentRevision                        исправление УКД в формате 189 приказа ФНС                            :doc:`UcdToSend`
UtdTorg12                                                  ТОРГ-12 в формате 155 приказа ФНС                                    :doc:`UtdToSend`
UtdAcceptanceCertificate                                   акт о выполнении работ в формате 155 приказа ФНС                     :doc:`UtdToSend`
UtdInvoice                                                 счет-фактура в формате 155 приказа ФНС                               :doc:`UtdToSend`
UcdInvoiceCorrection                                       корректировка счета-фактуры в формате 189 приказа ФНС                :doc:`UtdToSend`
TovTorg                                                    Торг-12 в формате 551-го приказа ФНС                                 :doc:`TovTorgToSend`
XmlAcceptanceCertificate552                                акт в формате 552-го приказа ФНС                                     :doc:`XmlAct552ToSend`
один из :doc:`DocumentVersion.Version <DocumentVersion>`   произвольный формализованный документ                                :doc:`CustomDocumentToSend`
Document                                                   произвольный формализованный документ                                :doc:`CustomDocumentToSend`
Contract                                                   договор                                                              :doc:`ContractToSend`
CertificateRegistry                                        реестр сертификатов                                                  :doc:`CertificateRegistryToSend`
PriceListAgreement                                         протокол согласования цены                                           :doc:`PriceListAgreementToSend`
ReconciliationAct                                          акт сверки                                                           :doc:`ReconciliationActToSend`
ServiceDetails                                             детализация                                                          :doc:`ServiceDetailsToSend`
Nonformalized                                              произволный неформализованный документ                               :doc:`NonformalizedDocumentToSend`
NonformalizedProforma                                      неформализованный счёт на оплату                                     :doc:`NonformalizedProformaToSend`
AcceptanceCertificate                                      неформализованный акт                                                :doc:`ActToSend`
Torg12                                                     неформализованный Торг-12                                            :doc:`Torg12ToSend`
========================================================== ==================================================================== ======================================


.. seealso:: :doc:`../HowTo/HowTo_post_document`
