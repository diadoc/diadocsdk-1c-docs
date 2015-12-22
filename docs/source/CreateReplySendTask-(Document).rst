CreateReplySendTask 
===================

Метод объекта :doc:`Document <Document>`.

**Синтаксис**


CreateReplySendTask(<Type>)

**Параметры**

-  <Type> (строка, обязательный) - тип ответного действия. В случае, если тип не указан, по умолчанию будет выполняться действие "AcceptDocument".


Параметр Type может принимать одно из следующих значений:

-  "AcceptDocument" - подписание документа

-  "RejectDocument" - отказ в подписи документа


**Возвращаемое значение**


Объект :doc:`ReplySendTask <ReplySendTask>`.

**Описание**


Формирует задание для ответного действия с документом. В данном случае 
содержимым объекта :doc:`ReplySendTask <ReplySendTask>` (свойство **Content**) будет объект, производный от 
:doc:`BaseContent <BaseContent>`, соответствующий типу выполняемого действия:

-  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа «ТОРГ-12 в формате ФНС»

-  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для действия типа "AcceptDocument" 
   документа «акт о выполнении работ в формате ФНС»

-  :doc:`AcceptanceContent <AcceptanceContent>` - для действия типа "AcceptDocument" других документов

-  :doc:`RejectionContent <RejectionContent>` - для действия типа "RejectDocument", применяемого к неформализованному документу

-  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - для действия типа "RejectDocument", применяемого 
   к формализованному документу

