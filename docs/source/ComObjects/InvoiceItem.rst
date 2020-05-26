InvoiceItem
===========

`Сведения о товаре (работе, услуге) <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=230599>`_

.. rubric:: Свойства


:Product:
  **Строка, чтение/запись** - наименование товара (описание выполненных работ, оказанных услуг), имущественного права

:UnitCode:
  **Строка, чтение/запись** - код единицы измерения

:Quantity:
  **Число, чтение/запись** - количество (объем)

:Price:
  **Число, чтение/запись** - цена (тариф) за единицу измерения (без НДС)

:TaxRate:
  **Строка, чтение/запись** - налоговая ставка. :doc:`Возможные значения <Enums/TaxRate>`

:Excise:
  **Строка, чтение/запись** - акциз

:TotalWithVatExcluded:
  **Строка, чтение/запись** - стоимость товаров (работ, услуг), имущественных прав без налога - всего

:Vat:
  **Число, чтение/запись**- Сумма налога, предъявляемая покупателю

:Total:
  **Число, чтение/запись** - стоимость товаров (работ, услуг), имущественных прав с налогом - всего

:CountriesOfOrigin:
  **Строка, чтение/запись** - цифровой код страны происхождения товара

:CustomsDeclarationNumbers:
  **Строка, чтение/запись** - номер таможенной декларации. В случае несколькимх ТД они перечисляются через запятую

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение/запись** - Информационное поле строки

  .. versionadded:: 5.0.0


.. rubric:: Методы

+------------------------------------------+
| |InvoiceItem-AddStructedAdditionalInfo|_ |
+------------------------------------------+

.. |InvoiceItem-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()


.. _InvoiceItem-AddStructedAdditionalInfo:
.. method:: InvoiceItem.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
