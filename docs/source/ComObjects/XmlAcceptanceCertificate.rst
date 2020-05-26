XmlAcceptanceCertificate
========================

Документ *Формализованный акт о выполнении работ*.
Является производным объектом от :doc:`Document <Document>`


.. rubric:: Свойства

:Total:
  **Число, чтение** - cумма по документу

:Vat:
  **Число, чтение** - cумма НДС по документу

:Grounds:
  **Строка, чтение** - основание документа

:Status:
  **Строка, чтение** - текущий статус документа в Диадоке. :doc:`Возможные значения <Enums/BilateralStatus>`


.. rubric:: Методы

+-------------------------------------------------+----------------------------------------+---------------------------------------------+
| |XmlAcceptanceCertificate-GetRejectionComment|_ | |XmlAcceptanceCertificate-GetContent|_ | |XmlAcceptanceCertificate-GetBuyerContent|_ |
+-------------------------------------------------+----------------------------------------+---------------------------------------------+

.. |XmlAcceptanceCertificate-GetRejectionComment| replace:: GetRejectionComment()
.. |XmlAcceptanceCertificate-GetContent| replace:: GetContent()
.. |XmlAcceptanceCertificate-GetBuyerContent| replace:: GetBuyerContent()


.. _XmlAcceptanceCertificate-GetRejectionComment:
.. method:: XmlAcceptanceCertificate.GetRejectionComment()

  Возвращает строку с комментарием, добавленным при отказе в подписи

  .. deprecated:: 5.20.3
    Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``



.. _XmlAcceptanceCertificate-GetContent:
.. method:: XmlAcceptanceCertificate.GetContent()

  Возвращает :doc:`представление контента титула продавца <AcceptanceCertificateSellerContent>` документа

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`



.. _XmlAcceptanceCertificate-GetBuyerContent:
.. method:: XmlAcceptanceCertificate.GetBuyerContent()

  Возвращает :doc:`представление контента титула покупателя <AcceptanceCertificateBuyerContent>` документа

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.GetDynamicContent`
