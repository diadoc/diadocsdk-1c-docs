PackageContentItem
==================

Элемент объекта :doc:`PackageContent <PackageContent>`, хранящий в себе пару "документ-контент"

Свойства объекта
----------------


    - **Document** (:doc:`Document <Document>`, чтение) - документ, с которым связан хранимый в паре контент
    - **Content** (:doc:`BaseContent <BaseContent>`, чтение) - контент. Может быть одним из следующих объектов:
       -  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа "ТОРГ-12 в формате ФНС"
       -  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа "акт о выполнении работ в формате ФНС"
       -  :doc:`UtdBuyerContent <UtdBuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа УПД
       -  :doc:`AcceptanceContent <AcceptanceContent>` - для действия типа "AcceptDocument" других документов
       -  :doc:`RejectionContent <RejectionContent>` - для действия типа "RejectDocument", применяемого к неформализованному документу
       -  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - для действия типа "RejectDocument", применяемого к формализованному документу


Методы
------

Отсутствуют


Дополнительная информация
-------------------------

1. Если :doc:`PackageContent <PackageContent>` запрашивается из :doc:`ReplySendTask2 <ReplySendTask2>`, то **Content** будет объектом :doc:`DynamicContent <DynamicContent>`

2. Если :doc:`PackageContent <PackageContent>` запрашивается из :doc:`ReplySendTask2 <ReplySendTask2>`, то у объекта есть методы :doc:`GetContentFromFile <PackageContentItem_GetContentFromFile>` и :doc:`GetContentFromString <PackageContentItem_GetContentFromString>`