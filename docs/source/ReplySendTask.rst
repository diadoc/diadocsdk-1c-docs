ReplySendTask
=============

Объект предназначен для выполнения ответного действия с документом или с пакетом документов.

Свойства
--------

-  Content (объект :doc:`BaseContent <BaseContent>`, чтение) - содержимое задания. Зависит от объекта, из которого был создан ReplySendTask 
   и от типа дейтсвия:
  
   - если ReplySendTask был создан методом :doc:`CreateReplySendTask <CreateReplySendTask-(DocumentPackage)>` объекта :doc:`DocumentPackage <DocumentPackage>`, 
     то Content будет являться объектом типа :doc:`PackageContent <PackageContent>`.

   - если ReplySendTask был создан методом :doc:`CreateReplySendTask <CreateReplySendTask-(Document)>` объекта :doc:`Document <Document>`, 
     то Content в зависимости от выбранного типа действия будет являться объектом:

     -  для действия "AcceptDocument":

        - :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для документа «ТОРГ-12 в формате ФНС»
        - :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для документа 
          «акт о выполнении работ в формате ФНС»
        - :doc:`AcceptanceContent <AcceptanceContent>` - для других документов

     -  для действия типа "RejectDocument":

        - :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - для формализованных документов
        - :doc:`RejectionContent <RejectionContent>` - для неформализованных документов


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