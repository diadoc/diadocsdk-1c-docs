XmlTorg12
=========

Документ *формализованный ТОРГ-12*.
Является производным объектом от :doc:`Document <Document>`


.. rubric:: Свойства объекта

:Total:
  **Число, чтение** - cумма по документу

:Vat:
  **Число, чтение** - cумма НДС по документу

:Grounds:
  **Строка, чтение** - основание документа

:Status:
  **Строка, чтение** - текущий статус документа в Диадоке. |XmlTorg12-Status|_


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
    Используйте :func:`Document.GetAnyComment` с типом ``SignatureRejectionComment``



.. _XmlTorg12-GetContent:
.. method:: XmlTorg12.GetContent()

  Возвращает :doc:`представление контента титула продавца <Torg12SellerContent>` документа

  .. deprecated:: 5.27.0
    Используйте :func:`Document.GetDynamicContent`



.. _XmlTorg12-GetBuyerContent:
.. method:: XmlTorg12.GetBuyerContent()

  Возвращает :doc:`представление контента титула покупателя <Torg12BuyerContent>` документа

  .. deprecated:: 5.27.0
    Используйте :func:`Document.GetDynamicContent`



.. rubric:: Дополнительная информация

.. |XmlTorg12-Status| replace:: Возможные значения
.. _XmlTorg12-Status:


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
