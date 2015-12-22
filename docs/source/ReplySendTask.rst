ReplySendTask
=============

Объект предназначен для выполнения ответного действия с документом или с пакетом документов.

Свойства
--------

-  Content (объект :doc:`BaseContent <BaseContent>`, чтение) - содержимое задания в зависимости от типа дейтсвия:

   -  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа «ТОРГ-12 в формате ФНС»

   -  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для действия типа "AcceptDocument" 
      документа «акт о выполнении работ в формате ФНС»

   -  :doc:`AcceptanceContent <AcceptanceContent>` - для действия типа "AcceptDocument" других документов

   -  :doc:`RejectionContent <RejectionContent>` - для действия типа "RejectDocument", применяемого к неформализованному документу

   -  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - для действия типа "RejectDocument", применяемого 
      к формализованному документу

   -  :doc:`PackageContent <PackageContent>` - для любых действий, применяемых к пакетам документов.

Методы
------

-  :doc:`ValidateContent <ValidateContent-(ReplySendTask)>` - проверить
   титул покупателя на корректность заполнения

-  :doc:`Send <Send-(ReplySendTask)>` - отправить титул покупателя на
   сервер Диадок

.. toctree::
   :name: Auto
   :hidden:

   ValidateContent <ValidateContent-(ReplySendTask)>
   Send <Send-(ReplySendTask)>