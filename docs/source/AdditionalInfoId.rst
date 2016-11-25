AdditionalInfoId
================

Объект предназначен для работы с информационным полем документа.


Свойства объекта
----------------

- **InfoFileId** (строка, чтение/запись, обязательно для заполнения, строка длиной не более 36 символов) - идентификатор файла информационного поля

- **StructedAdditionalInfos** (:doc:`коллекция <Collection>` объектов :doc:`StructedAdditionalInfo <StructedAdditionalInfo>`, чтение/запись) - дополнительные сведения


Методы объекта
--------------

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo-(AdditionalInfoId)>` - добавляет строку дополнительных сведений


.. toctree::
   :name: Auto
   :hidden:

   AddStructedAdditionalInfo <AddStructedAdditionalInfo-(AdditionalInfoId)>