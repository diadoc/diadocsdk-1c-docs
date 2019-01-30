ReplySendTask
=============

Объект предназначен для выполнения ответного действия с документом или с пакетом документов.


Свойства
--------

-  Content (:doc:`BaseContent <BaseContent>`, чтение) - содержимое задания. Зависит от объекта, из которого был создан ReplySendTask и от типа дейтсвия:

   - если ReplySendTask был создан методом :doc:`CreateReplySendTask <CreateReplySendTask-(DocumentPackage)>` объекта :doc:`DocumentPackage <DocumentPackage>`, то Content будет являться объектом типа :doc:`PackageContent <PackageContent>`.

   - если ReplySendTask был создан методом :doc:`CreateReplySendTask <CreateReplySendTask-(Document)>` объекта :doc:`Document <Document>`, то Content в зависимости от выбранного типа действия будет являться объектом:

     -  для действия "AcceptDocument":

        - :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для документа "ТОРГ-12 в формате 172 приказа ФНС"
        - :doc:`TovTorgBuyerContent <TovTorgBuyerContent>` - титул покупателя для документа "ТОРГ-12 в формате 551 приказа ФНС"
        - :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для документа "акт о выполнении работ в 172 формате ФНС"
        - :doc:`Act552BuyerContent <Act552BuyerContent>` - титул покупателя для документа "акт о выполнении работ в 552 формате ФНС"
        - :doc:`UtdBuyerContent <UtdBuyerContent>` - титул покупателя для универсального передаточного документа
        - :doc:`AcceptanceContent <AcceptanceContent>` - для других документов

     -  для действия типа "RejectDocument":

        - :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - формализованный отказ в подписи. Для любых документов

     -  для действия типа "CorrectionRequest":

        - :doc:`CorrectionRequestContent <CorrectionRequestContent>` - для любых документов


Методы
------

-  :doc:`Send <Send-(ReplySendTask)>` - отправить титул покупателя на сервер Диадок

.. toctree::
   :name: Auto
   :hidden:

   Send <Send-(ReplySendTask)>