ReplySendTask
=============

Объект предназначен для отправки титула покупателя документов «ТОРГ-12 в
формате ФНС» и «акт о выполнении работ в формате ФНС».

Свойства
--------

-  Content (объект
   :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>`,
   либо :doc:`Torg12BuyerContent <Torg12BuyerContent>`, чтение) - титула
   покупателя

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