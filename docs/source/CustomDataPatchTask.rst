CustomDataPatchTask
===================

Объект предназначен для редактирования коллекции **CustomData** объекта :doc:`Document <Document>`


Свойства объекта
----------------

- **Items** (:doc:`коллекция <Collection>` объектов :doc:`CustomDataPatchItem <CustomDataPatchItem>`, чтение) - элементы для вставки/удаления

Методы
------

-  :doc:`AddItem <AddItem-(CustomDataPatchTask)>` - добавляет элемент в коллекцию **Items**

-  :doc:`Send <Send-(CustomDataPatchTask)>` - применяет изменнения описанные в коллекции **Items**

-  :doc:`SendAsync <SendAsync-(CustomDataPatchTask)>` - асинхронно применяет изменнения описанные в коллекции **Items**

.. toctree::
   :name: Auto
   :hidden:

   CustomDataPatchItem <CustomDataPatchItem>
   AddItem <AddItem-(CustomDataPatchTask)>
   Send <Send-(CustomDataPatchTask)>
   SendAsync <SendAsync-(CustomDataPatchTask)>