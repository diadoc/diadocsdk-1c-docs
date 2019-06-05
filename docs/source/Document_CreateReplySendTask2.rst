CreateReplySendTask2
====================

Метод объектов :doc:`Document <Document>` и :doc:`DocumentPackage <DocumentPackage>`


**Синтаксис**

CreateReplySendTask2(<Type>)


**Параметры**

    -  <Type> (строка) - тип ответного действия. В случае, если тип не указан, по умолчанию будет выполняться действие "AcceptDocument".

Параметр **Type** может принимать одно из следующих значений:

-  "AcceptDocument" - подписание документов
-  "RejectDocument" - отказ в подписи документов
-  "CorrectionRequest" - запроc на уточнение документов "счет-фактура" и "исправление счета-фактуры"
-  "RevocationRequest" - запроc на аннулирование документов
-  "AcceptRevocation" - принятие аннулирования документов
-  "RejectRevocation" - отказ от аннулирования документов


**Возвращаемое значение**

:doc:`ReplySendTask2 <ReplySendTask2>`


**Описание**

Формирует задание для ответного действия с документом.
