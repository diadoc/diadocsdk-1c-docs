Содержание документа
====================

Объект BaseContent является базовым объектом для всех типов контентов документов. Он обладает базовым набором свойств и методов, которые также
работают для всех производных типов контентов. 


Свойства объекта
----------------

- **Type** (строка, чтение ) - тип контента

У базового объекта нет доступных методов.


Производные объекты 
------------------------------------

Следующие объекты являются производными от BaseContent:

.. toctree::
   :name: ContentsChild
   :maxdepth: 1
   :caption: Производные объекты
   :hidden:

   AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>
   AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>
   AcceptanceContent <AcceptanceContent>
   BasicDocumentContent <BasicDocumentContent>
   ContractContent <ContractContent>
   CorrectionRequestContent <CorrectionRequestContent>
   FormalizedRejectionContent <FormalizedRejectionContent>
   InvoiceContent <InvoiceContent>
   InvoiceCorrectionContent <InvoiceCorrectionContent>
   NonformilizedContent <NonformilizedContent>
   OutDocumentSignTaskContent <OutDocumentSignTaskContent>
   PackageContent <PackageContent>
   RejectionContent <RejectionContent>
   RevocationRequestContent <RevocationRequestContent>
   SentPackageContent <SentPackageContent>
   Torg12BuyerContent <Torg12BuyerContent>
   Torg12SellerContent <Torg12SellerContent>
   XmlDocumentContent <XmlDocumentContent>
   UtdSellerContent <UtdSellerContent>
   
-  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя документа «акт о выполнении работ в формате ФНС»
-  :doc:`AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>` - титул исполнителя документа «акт о выполнении работ в формате ФНС»
-  :doc:`AcceptanceContent <AcceptanceContent>` - метаданные для подписания документа
-  :doc:`BasicDocumentContent <BasicDocumentContent>` - содержание акта о выполнении работ в неформализованном виде, ТОРГ-12 в неформализованном виде или счета на оплату
-  :doc:`ContractContent <ContractContent>` - метаданные договора
-  :doc:`CorrectionRequestContent <CorrectionRequestContent>` - метаданные запроса на коррекцию
-  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - метаданные формализованного отказа в подписании документа
-  :doc:`InvoiceContent <InvoiceContent>` - содержание документов «счет-фактура» и «исправление счета-фактуры»
-  :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>` - содержание документов «корректировочный счет-фактура» и «исправление корректировочного счета-фактуры»
-  :doc:`NonformilizedContent <NonformilizedContent>` - содержание неформализованного документа, реестра сертификатов, акта сверки, детализации, протокола согласования цены.
-  :doc:`OutDocumentSignTaskContent <OutDocumentSignTaskContent>` - содержание запроса на подписание и отправку исходящего документа с отложенной отправкой
-  :doc:`PackageContent <PackageContent>` - содержание пакета документов
-  :doc:`RejectionContent <RejectionContent>` - метаданные неформализованного отказа в подписании документа
-  :doc:`RevocationRequestContent <RevocationRequestContent>` - метаданные запроса на аннулирование документа
-  :doc:`SentPackageContent <SentPackageContent>` - содержание пакета документов на отправку
-  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - содержание титула покупателя документа «ТОРГ-12 в формате ФНС»
-  :doc:`Torg12SellerContent <Torg12SellerContent>` - содержание титула продавца документа типа «ТОРГ-12 в формате ФНС»
-  :doc:`XmlDocumentContent <XmlDocumentContent>` - содержание формализованных документов титул исполнителя документа «акт о выполнении работ в формате ФНС», титул продавца документа типа «ТОРГ-12 в формате ФНС»
   , «счет-фактура», «исправление счета-фактуры», «корректировочный счет-фактура» или «исправление корректировочного счета-фактуры» в формате XML
-  :doc:`UtdSellerContent <UtdSellerContent>` - содержание титула продавца универсального передаточного документа
   