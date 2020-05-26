Torg12SellerContent
===================

Содержание документа *ТОРГ-12* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlTorg12Content``

:Date:
  **Дата, чтение/запись** - дата документа

:Number:
  **Строка, чтение/запись** - номер документа

:WaybillDate:
  **Дата, чтение/запись** - дата транспортной накладной

:WaybillNumber:
  **Строка, чтение/запись** - номер транспортной накладной

:OperationCode:
  **Строка, чтение/запись** - код вида операции

:GroundName:
  **Строка, чтение/запись** - наименование документа-основания

:GroundDate:
  **Дата, чтение/запись** - дата документа-основания

:GroundNumber:
  **Строка, чтение/запись** - номер документа-основания

:Seller:
  :doc:`OrganizationInfo` **, чтение** - данные продавца

:Buyer:
  :doc:`OrganizationInfo` **, чтение** - данные покупателя

:Shipper:
  :doc:`OrganizationInfo` **, чтение** - данные грузоотправителя

:ShipperDepartment:
  **Строка, чтение/запись** - структурное подразделение грузоотправителя

:ShipperOkdp:
  **Строка, чтение/запись** - код основного вида деятельности по ОКДП грузоотправителя

:Consignee:
  :doc:`OrganizationInfo` **, чтение** - данные грузополучателя

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Torg12Item` **, чтение** - табличная часть Торг-12

:Totals:
  :doc:`Torg12Totals` **, чтение** - итоги по накладной

:Commons:
  :doc:`Torg12Commons` **, чтение** - общие сведения по накладной

:AttachmentSheetsQuantity:
  **Число, чтение/запись** - приложение, количество листов

:SupplyAllowedBy:
  :doc:`Official` **, чтение** - отпуск груза разрешил

:ChiefAccountant:
  :doc:`Official` **, чтение** - главный бухгалтер

:SupplyPerformedBy:
  :doc:`Official` **, чтение** - отпуск груза произвел

:SupplyDate:
  **Дата, чтение/запись** - дата отпуска груза

:Signer:
  :doc:`Signer` **, чтение** - подписант

:AdditionalInfo:
  **Строка, чтение/запись** - дополнительные сведения


.. rubric:: Методы

+--------------------------------+------------------------------------------+
| |Torg12SellerContent-AddItem|_ | |Torg12SellerContent-SaveExternalCodes|_ |
+--------------------------------+------------------------------------------+

.. |Torg12SellerContent-AddItem| replace:: AddItem()
.. |Torg12SellerContent-SaveExternalCodes| replace:: SaveExternalCodes()



.. _Torg12SellerContent-AddItem:
.. method:: Torg12SellerContent.AddItem()

  Добавляет :doc:`новый элемент <Torg12Item>` в коллекцию *Items* и возвращает его



.. _Torg12SellerContent-SaveExternalCodes:
.. method:: Torg12SellerContent.SaveExternalCodes()

  Сохраняет на сервере Диадока список внешних идентификаторов товаров накладной

  .. deprecated:: 5.5.0
    Используйте :meth:`Organization.SetData`

  .. versionchanged:: 5.29.7
    Метод перестал что-либо делать. Оставлен для совместимости
