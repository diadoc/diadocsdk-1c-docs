AdditionalInfoId
================

Объект предназначен для работы с информационным полем документа


.. rubric:: Свойства

:InfoFileId:
  **Строка, чтение/запись** - идентификатор файла информационного поля

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo <StructedAdditionalInfo>` **, чтение** - дополнительные сведения


.. rubric:: Методы

+----------------------------------+
|:func:`.AddStructedAdditionalInfo`|
+----------------------------------+

.. function:: ﻿AdditionalInfoId.AddStructedAdditionalInfo()
  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
