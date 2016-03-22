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
   ContractContent <ContractContent>
   CorrectionRequestContent <CorrectionRequestContent>
   FormalizedRejectionContent <FormalizedRejectionContent>
   InvoiceContent <InvoiceContent>
   InvoiceCorrectionContent <InvoiceCorrectionContent>
   NonformilizedContent <NonformilizedContent>
   PackageContent <PackageContent>
   RejectionContent <RejectionContent>
   RevocationRequestContent <RevocationRequestContent>
   Torg12BuyerContent <Torg12BuyerContent>
   Torg12SellerContent <Torg12SellerContent>
   
-  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя документа «акт 
   о выполнении работ в формате ФНС»
-  :doc:`AcceptanceCertificateSellerContent <AcceptanceCertificateSellerContent>` - титул исполнителя документа «акт 
   о выполнении работ в формате ФНС»
-  :doc:`AcceptanceContent <AcceptanceContent>` - метаданные для подписания документа
-  :doc:`ContractContent <ContractContent>` - метаданные договора
-  :doc:`CorrectionRequestContent <CorrectionRequestContent>` - метаданные запроса на коррекцию
-  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - метаданные формализованного отказа в подписании документа
-  :doc:`InvoiceContent <InvoiceContent>` - содержание документов «счет-фактура» и «исправление счет-фактуры»
-  :doc:`InvoiceCorrectionContent <InvoiceCorrectionContent>` - содержание документов «корректировочный счет-фактура» и 
   «исправление корректировочного счета-фактуры»
-  :doc:`NonformilizedContent <NonformilizedContent>` - содержание неформализованного документа, реестра сертификатов, 
   акта сверки, детализации, протокола согласования цены.
-  :doc:`PackageContent <PackageContent>` - содержание пакета документов
-  :doc:`RejectionContent <RejectionContent>` - метаданные неформализованного отказа в подписании документа
-  :doc:`RevocationRequestContent <RevocationRequestContent>` - метаданные запроса на аннулирование документа
-  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - содержание титула покупателя документа «ТОРГ-12 в формате ФНС»
-  :doc:`Torg12SellerContent <Torg12SellerContent>` - содержание титула продавца документа типа «ТОРГ-12 в формате ФНС»
