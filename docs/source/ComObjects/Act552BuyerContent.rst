Act552BuyerContent
==================

Объект предназначен для работы с содержанием титула покупателя формализованного документа "Акт о выполнении работ" в формате приказа `ММВ-7-10/552@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265283>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства
--------

- **Type** (строка, чтение) - тип документа (возвращает строку "XmlAcceptanceCertificate552BuyerTitle")

- **Signers** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - данные подписантов

- **DocumentCreator** (строка, чтение/запись) - cоставитель файла информации продавца

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла

- **OperationType** (строка, чтение/запись) - вид операции

- **OperationContent** (строка, чтение/запись) - содержание операции

- **AcceptanceDate** (дата, чтение/запись) - дата приемки результатов работ

- **CreatedThingAcceptDate** (дата, чтение/запись) - дата получения вещи, изготовленной  по договору подряда

- **CreatedThingInfo** (строка, чтение/запись) - сведения о получении

- **AdditionalInfoId** (:doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа


Методы
------


-  :doc:`AddSigner <AddSigner-(Act552BuyerContent)>` - добавляет новый элемент в список подписантов

.. toctree::
   :name: Auto
   :hidden:

   AddSigner-(Act552BuyerContent)