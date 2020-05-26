BaseDocument
============

Документ, для которого не удалось найти подходящего типа, встроенного в компоненту.
Является производным объектом от :doc:`Document`


.. rubric:: Методы объекта

+-----------------------------------+
| |BaseDocument-SendReceiptsAsync|_ |
+-----------------------------------+

.. |BaseDocument-SendReceiptsAsync| replace:: SendReceiptsAsync()

.. _BaseDocument-SendReceiptsAsync:
.. method:: BaseDocument.SendReceiptsAsync()

  Формирует и подписывает документы по регламентному документообороту СЧФ/УПД. Возвращает объект :doc:`AsyncResult` с типом результата ``Булево``
