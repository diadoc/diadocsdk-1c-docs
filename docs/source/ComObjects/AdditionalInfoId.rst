AdditionalInfoId
================

Информационные поле документа


.. rubric:: Свойства

:InfoFileId:
  **Строка, чтение/запись** - идентификатор файла информационного поля

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение** - дополнительные сведения


.. rubric:: Методы

+-----------------------------------------------+
| |AdditionalInfoId-AddStructedAdditionalInfo|_ |
+-----------------------------------------------+

.. |AdditionalInfoId-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()



.. _AdditionalInfoId-AddStructedAdditionalInfo:
.. method:: AdditionalInfoId.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
