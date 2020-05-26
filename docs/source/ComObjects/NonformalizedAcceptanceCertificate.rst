NonformalizedAcceptanceCertificate
==================================

Документам *Акт о выполнении работ* в произвольном формате.
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


.. rubric:: Методы объекта

+-----------------------------------------------------------+
| |NonformalizedAcceptanceCertificate-GetRejectionComment|_ |
+-----------------------------------------------------------+

.. |NonformalizedAcceptanceCertificate-GetRejectionComment| replace:: GetRejectionComment()



.. _NonformalizedAcceptanceCertificate-GetRejectionComment:
.. method:: NonformalizedAcceptanceCertificate.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``
