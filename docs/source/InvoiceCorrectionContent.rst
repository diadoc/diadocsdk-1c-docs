InvoiceCorrectionContent
========================

Объект предназначен для работы с содержанием документов "корректировочный счет-фактура" и "исправление корректировочного счета-фактуры".
Является производным объектом от :doc:`BaseContent <BaseContent>`.


.. rubric:: Свойства

:Type: (строка, чтение) - тип документа (возвращает строку "InvoiceCorrectionContent")
:InvoiceVersion: (строка, чтение/запись) - версия формата корректировочного счета-фактуры
:OriginalInvoices: (:doc:`коллекция <Collection>` объектов :doc:`OriginalInvoice <OriginalInvoice>`, чтение) - данные об счет-фактурах, на основании которых был выставлен корректировочный счет-фактура
:InvoiceCorrectionDate: (дата, чтение/запись) - дата КСФ
:InvoiceCorrectionNumber: (строка, чтение/запись, длина не более 256 символов) - номер КСФ
:InvoiceCorrectionRevisionDate: (дата, чтение/запись) - дата исправления КСФ
:InvoiceCorrectionRevisionNumber: (строка, чтение/запись, длина не более 3 символов) - номер исправления КСФ
:Currency: (строка, чтение/запись, обязательно для заполнения. Числовая строка длиной 3 символа. Код должен содержаться в общероссийском классификаторе валют.) - код валюты
:Seller: (:doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения) - данные продавца
:Buyer: (:doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения) - данные покупателя
:Signer: (:doc:`Signer <Signer>`, чтение, обязательно для заполнения) - данные подписанта документа
:Items: (:doc:`коллекция <Collection>` объектов :doc:`InvoiceCorrectionItem <InvoiceCorrectionItem>`, чтение, обязательно для заполнения) - табличная часть корректировочного счета-фактуры
:TotalsInc: (:doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - итоговая сумма к увеличению
:TotalsDec: (:doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, чтение) - итоговая сумма к уменьшению
:StructedAdditionalInfos: (:doc:`коллекция <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`, чтение) - дополнительные сведения


.. rubric:: Методы

* :doc:`AddItem <AddItem-(InvoiceCorrectionContent)>` - добавляет строку в табличную часть корректировочного счета-фактуры
* :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo-(InvoiceCorrectionContent)>` - добавляет строку дополнительных сведений
* :doc:`AddOriginalInvoice <AddOriginalInvoice>` - добавляет строку c данными о счет-фактуре, на основании которого был выставлен корректировочный счет-фактура


.. rubric:: Дополнительная информация

+--------------------------------+
|Значения свойства InvoiceVersion|
+--------------------------------+
|5.01                            |
+--------------------------------+
|5.02                            |
+--------------------------------+