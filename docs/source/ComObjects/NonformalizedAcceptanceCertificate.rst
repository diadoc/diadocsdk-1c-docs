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
  **Строка, чтение** - статус документа. |NonformalizedAcceptanceCertificate-Status|_


.. rubric:: Методы объекта

+-----------------------------------------------------------+
| |NonformalizedAcceptanceCertificate-GetRejectionComment|_ |
+-----------------------------------------------------------+

.. |NonformalizedAcceptanceCertificate-GetRejectionComment| replace:: GetRejectionComment()



.. _NonformalizedAcceptanceCertificate-GetRejectionComment:
.. method:: NonformalizedAcceptanceCertificate.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте Используйте :func:`Document.GetAnyComment` с типом ``SignatureRejectionComment``



.. rubric:: Дополнительная информация

.. |NonformalizedAcceptanceCertificate-Status| replace:: Возможные значения
.. _NonformalizedAcceptanceCertificate-Status:

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
