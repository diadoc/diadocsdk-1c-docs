TovTorgTable
============

`Сведения об ассортименте, количестве, стоимости и другой информации о товарных позициях <https://normativ.kontur.ru/document?moduleId=1&documentId=265102&rangeId=233872>`_

.. rubric:: Свойства

:Items:
  :doc:`Коллекция <Collection>` **объектов** :doc:`TovTorgItem` **, чтение** - информация о товарах

:TotalQuantity:
  **Число, чтение/запись** - количество мест всего по документу

:TotalGross:
  **Число, чтение/запись** - масса брутто всего по документу

:TotalNet:
  **Число, чтение/запись** - масса нетто всего по документу

:TotalWithVatExcluded:
  **Число, чтение/запись** - сумма без учета налога

:TotalVat:
  **Число, чтение/запись** - сумма НДС - всего по документу

:Total:
  **Число, чтение/запись** - сумма всего


.. rubric:: Методы

+-------------------------+
| |TovTorgTable-AddItem|_ |
+-------------------------+

.. |TovTorgTable-AddItem| replace:: AddItem()



.. _TovTorgTable-AddItem:
.. method:: TovTorgTable.AddItem()

  Добавляет :doc:`новый элемент <TovTorgItem>` в коллекцию *Items* и возвращает его
