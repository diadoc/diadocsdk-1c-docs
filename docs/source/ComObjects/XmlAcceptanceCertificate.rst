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
  **Строка, чтение** - текущий статус документа в Диадоке. |XmlAcceptanceCertificate-Status|_


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



.. rubric:: Дополнительная информация

.. |XmlAcceptanceCertificate-Status| replace:: Возможные значения
.. _XmlAcceptanceCertificate-Status:

========================================= ======================================================================================================
Значение *Status*                         Описание
========================================= ======================================================================================================
UnknownBilateralDocumentStatus            неизвестное состояние документа
OutboundWaitingForRecipientSignature      документ исходящий, ответная подпись, либо отказ от ее формирования еще не получены
OutboundWithRecipientSignature            документ исходящий, ответная подпись получена
OutboundRecipientSignatureRequestRejected документ исходящий, получен отказ от формирования ответной подписи
OutboundWaitingForSenderSignature         документ исходящий, документ не отправлен, поскольку не подписан отправителем
OutboundInvalidSenderSignature            документ исходящий, документ не отправлен, поскольку подпись отправителя не является корректной
InboundWaitingForRecipientSignature       документ входящий, ответная подпись, либо отказ от ее формирования еще не отправлены
InboundWithRecipientSignature             документ входящий, ответная подпись поставлена
InboundRecipientSignatureRequestRejected  документ входящий, отправлен отказ от формирования ответной подписи
InboundInvalidRecipientSignature          документ входящий, документооборот не завершен, поскольку подпись отправителя не является корректной
InternalWaitingForRecipientSignature      документ внутренний, ответная подпись отсутствует
InternalWithRecipientSignature            документ внутренний, ответная подпись поставлена
InternalRecipientSignatureRequestRejected документ внутренний, отправлен отказ от формирования ответной подписи
InternalWaitingForSenderSignature         документ внутренний, документ не отправлен, поскольку не подписан отправителем
InternalInvalidSenderSignature            документ внутренний, документ не отправлен, поскольку подпись отправителя не является корректной
InternalInvalidRecipientSignature         документ внутренний, документооборот не завершен, поскольку подпись отправителя не является корректной
========================================= ======================================================================================================
