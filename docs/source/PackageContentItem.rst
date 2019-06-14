PackageContentItem
==================

Элемент объекта :doc:`PackageContent <PackageContent>`, хранящий в себе пару "документ-контент"


.. rubric:: Свойства

:Document: (:doc:`Document <Document>`, чтение) - документ, с которым связан хранимый в паре контент
:Content: (:doc:`BaseContent <BaseContent>` или :doc:`DynamicContent <DynamicContent>`, чтение) - представление контента


.. rubric:: Методы

* :doc:`LoadContentFromFile <PackageContentItem_LoadContentFromFile>` - загружает контент ответа из файла
* :doc:`LoadContentFromBase64 <PackageContentItem_LoadContentFromBase64>` загружает контент ответа из Base64 строки


.. rubric:: Методы

Отсутствуют


.. rubric:: Дополнительная информация

* Если :doc:`PackageContent <PackageContent>` запрашивается из :doc:`ReplySendTask2 <ReplySendTask2>` с типом **AcceptDocument** для двухтитульного документа, то **Content** будет объектом :doc:`DynamicContent <DynamicContent>`.
  В противном случае **Content** будет объектом, производным от :doc:`BaseContent <BaseContent>`

============================================================================ ====================================================================================================
Тип BaseContent'а свойства Content                                           Описание
============================================================================ ====================================================================================================
:doc:`Torg12BuyerContent <Torg12BuyerContent>`                               Титул покупателя Торг-12 в формате 172 приказа ФНС
:doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` Титул покупателя акта выполненных работ в формате 172 приказа ФНС
:doc:`UtdBuyerContent <UtdBuyerContent>`                                     Титул покупателя для документа формата 155 приказа ФНС (УПД)
:doc:`AcceptanceContent <AcceptanceContent>`                                 Подписание однотитульного документа или запроса аннулирования
:doc:`FormalizedRejectionContent <FormalizedRejectionContent>`               Отказ от подписания документа или запроса аннулирования
:doc:`CorrectionRequestContent <CorrectionRequestContent>`                   Запрос корректировки документа
============================================================================ ====================================================================================================
