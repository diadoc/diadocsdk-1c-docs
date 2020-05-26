NonformalizedTorg12
===================

Документ *ТОРГ-12* в произвольном формате.
Является производным объектом от :doc:`Document <Document>`


.. rubric:: Свойства

:Total:
  **Число, чтение** - cумма по документу

:Vat:
  **Число, чтение** - cумма НДС по документу

:Grounds:
  **Строка, чтение** - основание документа

:Status:
  **Строка, чтение** - статус документа. :doc:`Возможные значения <Enums/BilateralStatus>`


.. rubric:: Методы

+--------------------------------------------+
| |NonformalizedTorg12-GetRejectionComment|_ |
+--------------------------------------------+

.. |NonformalizedTorg12-GetRejectionComment| replace:: GetRejectionComment()


.. _NonformalizedTorg12-GetRejectionComment:
.. method:: NonformalizedTorg12.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``
