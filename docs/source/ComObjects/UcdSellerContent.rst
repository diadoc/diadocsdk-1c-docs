UcdSellerContent
================

Содержание документа *Универсальный корректировочный документ* в формате приказа `ММВ-7-15/189@ <https://normativ.kontur.ru/document?moduleId=1&documentId=273231>`_.
Является производным объектом от :doc:`BaseContent <BaseContent>`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``UniversalCorrectionDocument``

:Function:
  **Строка, чтение/запись** - функция документа. |UcdSellerContent-Function|_

:Name:
  **Строка, чтение/запись** - наименование первичного документа, определенное организацией

:Date:
  **Дата, чтение/запись** - дата УКД

:Number:
  **Строка, чтение/запись** - номер УКД

:Invoices:
  :doc:`Коллекция <Collection>` **объектов** :doc:`InvoiceForCorrectionInfo <InvoiceForCorrectionInfo>` **, чтение** - счет-фактура (первичный документ), к которому составлен УКД

:Seller:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - данные продавца. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для продавца должен быть указан адрес

:Buyer:
  :doc:`ExtendedOrganizationInfo <ExtendedOrganizationInfo>` **, чтение** - данные покупателя. В случае УКД с функцией "КСЧФ" и "КСЧФДИС" для покупателя должен быть указан адрес

:Signers:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner <ExtendedSigner>` **, чтение** - подписанты документа. Для документа должен быть указан по крайней мере один подписант.

:EventContent:
  :doc:`EventContent <EventContent>` **, чтение** - содержание события

:InvoiceCorrectionTable:
  :doc:`InvoiceCorrectionTable <InvoiceCorrectionTable>` **, чтение** - сведения таблицы корректировочного счета-фактуры

:Currency:
  **Строка, чтение/запись** - код валюты по Общероссийскому классификатору валют

:CurrencyRate:
  **Строка, чтение/запись** - курс валюты

:RevisionDate:
  **Дата, чтение/запись** - дата исправления

:RevisionNumber:
  **Строка, чтение/запись** - номер исправления

:AdditionalInfoId:
  :doc:`AdditionalInfoId <AdditionalInfoId>` **, чтение** - информационное поле документа

:Creator:
  **Строка, чтение/запись** - составитель файла обмена счета-фактуры (информации продавца)

:CreatorBase:
  **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

:GovernmentContractInfo:
  **Строка, чтение/запись** - идентификатор государственного контракта


.. rubric:: Методы

+-------------------------------+--------------------------------+
| |UcdSellerContent-AddSigner|_ | |UcdSellerContent-AddInvoice|_ |
+-------------------------------+--------------------------------+

.. |UcdSellerContent-AddSigner| replace:: AddSigner()
.. |UcdSellerContent-AddInvoice| replace:: AddInvoice()



.. _UcdSellerContent-AddSigner:
.. method:: UcdSellerContent.AddSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его



.. _UcdSellerContent-AddInvoice:
.. method:: UcdSellerContent.AddInvoice()

  Добавляет :doc:`новый элемент <InvoiceForCorrectionInfo>` в коллекцию *Invoices* и возвращает его



.. rubric:: Дополнительная информация

.. |UcdSellerContent-Function| replace:: Возможные значения
.. _UcdSellerContent-Function:

=================== ========
Значение *Function* Описание
=================== ========
Invoice             КСЧФ
Basic               ДИС
InvoiceAndBasic     КСЧФДИС
=================== ========
