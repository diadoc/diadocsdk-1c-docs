CreateReplySendTask 
===================

Метод объекта :doc:`DocumentPackage <DocumentPackage>`.

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


Формирует задание для ответного действия с пакетом документов. В данном случае 
содержимым объекта :doc:`ReplySendTask <ReplySendTask>` (свойство **Content**) будет объект :doc:`PackageContent <PackageContent>`, 
который будет включать в себя набор контентов для каждого документа из пакета. Они будут связаны в пары "документ-контент" в 
объекте :doc:`PackageContentItem <PackageContentItem>`. При этом контент будет являться объектом, производным от 
:doc:`BaseContent <BaseContent>` и соответствующим типу выполняемого действия:

-  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа «ТОРГ-12 в формате ФНС»

-  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для действия типа "AcceptDocument" 
   документа «акт о выполнении работ в формате ФНС»

-  :doc:`AcceptanceContent <AcceptanceContent>` - для действия типа "AcceptDocument" других документов

-  :doc:`RejectionContent <RejectionContent>` - для действия типа "RejectDocument", применяемого к неформализованному документу

-  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - для действия типа "RejectDocument", применяемого 
   к формализованному документу