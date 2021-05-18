InvoiceTable
============

`Табличная часть счета-фактуры формата ММВ-7-15/155@ <https://normativ.kontur.ru/document?moduleId=1&documentId=271958&rangeId=230625>`_

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:TotalWithVatExcluded:
  **Число, чтение/запись** - сумма без учета НДС

:Vat:
  **Число, чтение/запись** - сумма НДС

:Total:
  **Число, чтение/запись** - сумма всего

:TotalNet:
  **Число, чтение/запись** - нетто всего

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedInvoiceItem` **, чтение** - информация о товарах

.. note:: Числа рекомендуется записывать строкой в виде XML представления типа `decimal <http://www.w3.org/TR/xmlschema-2/#decimal>`_ .
          В 1С такое представление можно получить с помощью функции глобального контекста XMLСтрока/XMLString


.. rubric:: Методы

+-------------------------+
| |InvoiceTable-AddItem|_ |
+-------------------------+

.. |InvoiceTable-AddItem| replace:: AddItem()



.. _InvoiceTable-AddItem:
.. method:: InvoiceTable.AddItem()

  Добавляет :doc:`новый элемент <ExtendedInvoiceItem>` в коллекцию *Items* и возвращает его
