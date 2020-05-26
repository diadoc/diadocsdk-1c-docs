ExtendedInvoiceItem
===================

`Сведения об отгруженных товарах (о выполненных работах, оказанных услугах), переданных имущественных правах <https://normativ.kontur.ru/document?moduleId=1&documentId=271958&rangeId=230537>`_


.. rubric:: Свойства

:Product:
  **Cтрока, чтение/запись** - наименование товара

:UnitCode:
  **Cтрока, чтение/запись** - код единицы измерения товара

:UnitName:
  **Cтрока, чтение/запись** - наименование единицы измерения товара

:Quantity:
  **Число, чтение/запись** - количество единиц товара

:Price:
  **Число, чтение/запись** - цена за единицу товара без НДС

:Excise:
  **Строка, чтение/запись** - акциз

:TaxRate:
  **Строка, чтение/запись** - ставка НДС. :doc:`Возможные значения <Enums/TaxRate>`

:SubtotalWithVatExcluded:
  **Число, чтение/запись** - сумма без учета НДС

:Vat:
  **Число, чтение/запись** - сумма НДС

:Subtotal:
  **Число, чтение/записья** - сумма всего

:ItemMark:
  **Строка, чтение/запись** - признак товар-работа-услуга. :doc:`Возможные значения <Enums/ItemMark>`

:AdditionalProperty:
  **Строка, чтение/запись** - дополнительная информация о признаке

:VendorCode:
  **Строка, чтение/запись** - характеристика/код/артикул/сорт товара

:ToRelease:
  **Число, чтение/запись** - количество товара, которое надлежит отпустить

:AccountDebit:
  **Строка, чтение/запись** - корреспондирующие счета: дебет

:AccountCredit:
  **Строка, чтение/запись** - корреспондирующие счета: кредит

:CustomDeclarations:
  :doc:`Коллекция <Collection>` **объектов** :doc:`CustomDeclaration <CustomDeclaration>` **, чтение** - номера таможенных деклараций

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` **, чтение** - информационное поле документа


.. rubric:: Методы

+---------------------------------------------+--------------------------------------------------+
| |ExtendedInvoiceItem-AddCustomDeclaration|_ | |ExtendedInvoiceItem-AddStructedAdditionalInfo|_ |
+---------------------------------------------+--------------------------------------------------+

.. |ExtendedInvoiceItem-AddCustomDeclaration| replace:: AddCustomDeclaration()
.. |ExtendedInvoiceItem-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()




.. _ExtendedInvoiceItem-AddCustomDeclaration:
.. method:: ExtendedInvoiceItem.AddCustomDeclaration()

  Добавляет :doc:`новый элемент <CustomDeclaration>` в коллекцию *CustomDeclarations* и возвращает его



.. _ExtendedInvoiceItem-AddStructedAdditionalInfo:
.. method:: ExtendedInvoiceItem.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его



.. note:: Числа рекомендуется записывать строкой в виде XML представления типа `decimal <http://www.w3.org/TR/xmlschema-2/#decimal>`_.
          В 1С такое представление можно получить с помощью функции глобального контекста XMLСтрока/XMLString
