Nonformalized
=============

Документам *Неформализованный*.
Является производным объектом от :doc:`Document <Document>`


.. rubric:: Свойства

:Status:
  **Строка, чтение** - статус документа. |Nonformalized-Status|_


.. rubric:: Методы

+--------------------------------------+
| |Nonformalized-GetRejectionComment|_ |
+--------------------------------------+

.. |Nonformalized-GetRejectionComment| replace:: GetRejectionComment()



.. _Nonformalized-GetRejectionComment:
.. method:: Nonformalized.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``



.. rubric:: Дополнительная информация

.. |Nonformalized-Status| replace:: Возможные значения
.. _Nonformalized-Status:

========================================= ======================================================================================================
Значения *Status*                         Описание
========================================= ======================================================================================================
UnknownNonformalizedDocumentStatus        неизвестное состояние документа
OutboundNoRecipientSignatureRequest       документ исходящий, без запроса ответной подписи
OutboundWaitingForRecipientSignature      документ исходящий, ответная подпись, либо отказ от ее формирования еще не получены
OutboundWithRecipientSignature            документ исходящий, ответная подпись получена
OutboundRecipientSignatureRequestRejected документ исходящий, получен отказ от формирования ответной подписи
OutboundWaitingForSenderSignature         документ исходящий, документ не отправлен, поскольку не подписан отправителем
OutboundInvalidSenderSignature            документ исходящий, документ не отправлен, поскольку подпись отправителя не является корректной
InboundNoRecipientSignatureRequest        документ входящий, без запроса ответной подписи
InboundWaitingForRecipientSignature       документ входящий, ответная подпись либо отказ от ее формирования еще не отправлены
InboundWithRecipientSignature             документ входящий, ответная подпись поставлена
InboundRecipientSignatureRequestRejected  документ входящий, отправлен отказ от формирования ответной подписи
InboundInvalidRecipientSignature          документ входящий, документооборот не завершен, поскольку подпись отправителя не является корректной
InternalNoRecipientSignatureRequest       документ внутренний, документ без запроса ответной подписи
InternalWaitingForRecipientSignature      документ внутренний, ответная подпись
InternalWithRecipientSignature            документ внутренний, ответная подпись поставлена
InternalRecipientSignatureRequestRejected документ внутренний, отправлен отказ от формирования ответной подписи
InternalWaitingForSenderSignature         документ внутренний, документ не отправлен, поскольку не подписан отправителем
InternalInvalidSenderSignature            документ внутренний, документ не отправлен, поскольку подпись отправителя не является корректной
InternalInvalidRecipientSignature         документ внутренний, документооборот не завершен, поскольку подпись отправителя не является корректной
========================================= ======================================================================================================
