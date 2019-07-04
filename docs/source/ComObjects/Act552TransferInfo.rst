Act552TransferInfo
==================

Содержание факта хозяйственной жизни - сведения о передаче результатов работ (о предъявлении оказанных услуг) для документа типа

.. rubric:: Свойства

:OperationInfo:
  **Строка, чтение/запись** - содержание операции

:TransferDate:
  **Дата, чтение/запись** - дата передачи результатов работ

:CreatedThingTransferDate:
  **Дата, чтение/запись** - дата передачи вещи, изготовленной по договору подряда

:CreatedThingInfo:
  **Строка, чтение/запись** - сведения о передаче

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` **, чтение** - информационное поле документа



.. rubric:: Методы

+----------------------------------+
|:func:`.AddStructedAdditionalInfo`|
+----------------------------------+

.. function:: ﻿Act552TransferInfo.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию `StructedAdditionalInfos`
