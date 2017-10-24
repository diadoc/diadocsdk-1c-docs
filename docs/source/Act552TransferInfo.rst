Act552TransferInfo
==================

Содержание факта хозяйственной жизни - сведения о передаче результатов работ (о предъявлении оказанных услуг) для документа типа 

Свойства
--------

- **OperationInfo** (строка, чтение/запись) - содержание операции

- **TransferDate** (дата, чтение/запись) - дата передачи результатов работ

- **CreatedThingTransferDate** (дата, чтение/запись) - дата передачи вещи, изготовленной по договору подряда

- **CreatedeThingInfo** (строка, чтение/запись) - сведения о передаче

- **StructedAdditionalInfos** (коллекция :doc:`Collection <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`) - информационное поле документа

Методы
------

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo-(Act552TransferInfo)>` - добавляет элемент в коллекцию информационных полей

.. toctree::
   :name: Auto
   :hidden:

    AddStructedAdditionalInfo <AddStructedAdditionalInfo-(Act552TransferInfo)>