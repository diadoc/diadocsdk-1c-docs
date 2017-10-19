Act552BuyerContent
==================

Объект предназначен для работы с содержанием ответного титула документов типа "Акт в
формате 552-го приказа ФНС"

Свойства
--------

- **Signers** (коллекция :doc:`Collection <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - данные подписантов

- **DocumentCreator** (строка, чтение/запись) - cоставитель файла информации продавца

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла

- **OperationType** (строка, чтение/запись) - вид операции

- **OperationContent** (строка, чтение/запись) - содержание операции

- **AcceptanceDate** (дата, чтение/запись) - дата приемки результатов работ

- **CreatedThingAcceptDate** (дата, чтение/запись) - дата получения вещи, изготовленной  по договору подряда

- **CreatedThingInfo** (строка, чтение/запись) - сведения о получении

- **AdditionalInfoId** (объект :doc:`AdditionalInfoId <AdditionalInfoId>`) - информационное поле документа

Методы
------

-  :doc:`AddSigner <AddSigner-(Act552BuyerContent)>` - добавляет новый элемент в список подписантов

.. toctree::
   :name: Auto
   :hidden:

    AddSigner-(Act552BuyerContent)