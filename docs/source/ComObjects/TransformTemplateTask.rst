TransformTemplateTask
=====================

Объект предназначенный для создания документов на основе шаблонов


Свойства
--------

-  **TemplateId** (строка, чтение/запись)
-  **DocumentTransformations** (:doc:`коллекция <Collection>` объектов :doc:`DocumentTransformation <DocumentTransformation>`, чтение)


Методы
------

-  :doc:`AddDocumentTransformation <AddDocumentTransformation>` - добавляет документ для трансформации
-  :doc:`Send <Send-(TransformTemplateTask)>` - создаёт документы на основе шаблонов документов, указанных в **DocumentTransformations**


.. toctree::
   :name: Auto
   :hidden:
   
   DocumentTransformation <DocumentTransformation>
   AddDocumentTransformation <AddDocumentTransformation>
   Send <Send-(TransformTemplateTask)>