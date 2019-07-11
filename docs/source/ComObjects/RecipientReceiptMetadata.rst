RecipientReceiptMetadata
========================

Метаданные извещения о получении документа

.. rubric:: Свойства

:ReceiptStatus:
  **Строка, чтение** - состояние ИОП на документ. |RecipientReceiptMetadata-ReceiptStatus|_

:ConfirmationMetadata:
  :doc:`ConfirmationMetadata <ConfirmationMetadata>` **, чтение** - метаданные подтверждения оператором даты отправки/получения документа


.. rubric:: Дополнительная информация


.. |RecipientReceiptMetadata-ReceiptStatus| replace:: Возможные значения
.. _RecipientReceiptMetadata-ReceiptStatus:

================================= ==================================================
Значение **ReceiptStatus**        Описание
================================= ==================================================
GeneralReceiptStatusNotAcceptable ИОП на документ не запрошен. Действий не требуется
HaveToCreateReceipt               нужно подписать ИОП на документ
WaitingForReceipt                 ожидание подписания ИОПа на документ
Finished                          ИОП подписано. Действий не требуется
================================= ==================================================
