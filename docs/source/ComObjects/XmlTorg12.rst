XmlTorg12
=========

Документ *формализованный ТОРГ-12*.
Является производным объектом от :doc:`Document`


.. rubric:: Свойства объекта

:Total:
  **Число, чтение** - cумма по документу

:Vat:
  **Число, чтение** - cумма НДС по документу

:Grounds:
  **Строка, чтение** - основание документа

:Status:
  **Строка, чтение** - текущий статус документа в Диадоке. :doc:`Возможные значения <./Enums/BilateralStatus>`


.. rubric:: Методы

+----------------------------------+-------------------------+------------------------------+
| |XmlTorg12-GetRejectionComment|_ | |XmlTorg12-GetContent|_ | |XmlTorg12-GetBuyerContent|_ |
+----------------------------------+-------------------------+------------------------------+

.. |XmlTorg12-GetRejectionComment| replace:: GetRejectionComment()
.. |XmlTorg12-GetContent| replace:: GetContent()
.. |XmlTorg12-GetBuyerContent| replace:: GetBuyerContent()


.. _XmlTorg12-GetRejectionComment:
.. method:: XmlTorg12.GetRejectionComment()

  Возвращает строку с комментарием, добавленным при отказе в подписи

  .. deprecated:: 5.20.3
    Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``



.. _XmlTorg12-GetContent:
.. method:: XmlTorg12.GetContent()

  Возвращает :doc:`представление контента титула продавца <Torg12SellerContent>` документа

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`



.. _XmlTorg12-GetBuyerContent:
.. method:: XmlTorg12.GetBuyerContent()

  Возвращает :doc:`представление контента титула покупателя <Torg12BuyerContent>` документа

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`
