DocumentToSend
==============

Базовый объект для всех документов на отправку

.. versionadded:: 5.5.0


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа на отправку

:NeedReceipt:
  **Булево, чтение/запись** - флаг принудительного запроса извещения о получении по документу


.. rubric:: Методы

+------------------------------------------+-----------------------------------------------------+-------------------------------+
| |DocumentToSend-AddInitialDocument|_     | |DocumentToSend-AddInitialDocumentFromPackage|_     | |DocumentToSend-SaveContent|_ |
+------------------------------------------+-----------------------------------------------------+-------------------------------+
| |DocumentToSend-AddSubordinateDocument|_ | |DocumentToSend-AddSubordinateDocumentFromPackage|_ |                               |
+------------------------------------------+-----------------------------------------------------+-------------------------------+

.. |DocumentToSend-AddInitialDocument| replace:: AddInitialDocument()
.. |DocumentToSend-AddSubordinateDocument| replace:: AddSubordinateDocument()
.. |DocumentToSend-AddInitialDocumentFromPackage| replace:: AddInitialDocumentFromPackage()
.. |DocumentToSend-AddSubordinateDocumentFromPackage| replace:: AddSubordinateDocumentFromPackage()
.. |DocumentToSend-SaveContent| replace:: SaveContent()



.. _DocumentToSend-AddInitialDocument:
.. method:: DocumentToSend.AddInitialDocument(DocumentID)

  :DocumentID: ``строка`` идентификатор документа в Диадок

  Добавляет идентификатор документа в коллекцию "родительских" документов



.. _DocumentToSend-AddSubordinateDocument:
.. method:: DocumentToSend.AddSubordinateDocument(DocumentID)

  :DocumentID: ``строка`` идентификатор документа в Диадок

  Добавляет идентификатор документа в коллекцию подчиненных документов



.. _DocumentToSend-AddInitialDocumentFromPackage:
.. method:: DocumentToSend.AddInitialDocumentFromPackage(CustomDocumentID)

  :CustomDocumentID: ``строка`` идентификатор документа, определяемый внешней системой. Может быть взят у любого документа отправляемого пакета

  Добавляет идентификатор документа из пакета на отправку в коллекцию "родительских" документов



.. _DocumentToSend-AddSubordinateDocumentFromPackage:
.. method:: DocumentToSend.AddSubordinateDocumentFromPackage(CustomDocumentID)

  :CustomDocumentID: ``строка`` идентификатор документа, определяемый внешней системой. Может быть взят у любого документа отправляемого пакета

  Добавляет идентификатор документа из пакета на отправку в коллекцию подчиненных документов


.. _DocumentToSend-SaveContent:
.. method:: DocumentToSend.SaveContent(BoxId, FileName)

  :BoxId: ``строка`` идентификатор ящика контрагента, которому должен быть отправлен документ
  :FileName: ``строка`` полной имя файла, в который необходимо сохранить содержание документа

  Генерирует содержание отправляемого документа и сохраняет его на диск

  .. versionadded:: 5.29.9



.. rubric:: Дополнительная информация

* Если значение *NeedReceipt* == ``FALSE``, то ИоП запрашивает только по документам, чей :doc:`документооборот <../HowTo/HowTo_invoice_docflow>` это предполагает

====================================== =======================================================
Объекты, производные от DocumentToSend Описание
====================================== =======================================================
:doc:`ActToSend`                       Акт о выполнении работ в неформализованном виде
:doc:`CertificateRegistryToSend`       Реестр сертификатов
:doc:`ContractToSend`                  Договор
:doc:`InvoiceToSend`                   Счет-фактура в формате приказа ММВ-7-6/93@
:doc:`InvoiceCorrectionToSend`         Корректировочный счет-фактура
:doc:`InvoiceRevisionToSend`           Исправление счета-фактуры в формате приказа ММВ-7-6/93@
:doc:`InvoiceCorrectionRevisionToSend` Исправление корректировочного счета-фактуры
:doc:`NonformalizedDocumentToSend`     Неформализованный документ
:doc:`PriceListAgreementToSend`        Протокол согласования цены
:doc:`NonformalizedProformaToSend`     Счет на оплату
:doc:`ReconciliationActToSend`         Акт сверки
:doc:`ServiceDetailsToSend`            Детализация
:doc:`Torg12ToSend`                    ТОРГ-12 в неформализованном виде
:doc:`XmlActToSend`                    Акт о выполнении работ в формате приказа ММВ-7-6/172@
:doc:`XmlTorg12ToSend`                 ТОРГ-12 в формате приказа ММВ-7-6/172@
:doc:`UtdToSend`                       Универсальный передаточный документ
:doc:`UcdToSend`                       Универсальный корректировочный документ
:doc:`TovTorgToSend`                   ТОРГ-12 в формате приказа ММВ-7-10/551@
:doc:`XmlAct552ToSend`                 Акт в формате приказа ММВ-7-10/552@
:doc:`CustomDocumentToSend`            документ произвольного типа
====================================== =======================================================
