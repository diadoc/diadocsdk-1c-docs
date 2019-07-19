TransformTemplateTask
=====================

Задания для создания документов на основе шаблонов


.. rubric:: Свойства

:TemplateId:
  **Строка, чтение/запись** - идентификатор шаблона пакета документов

:DocumentTransformations:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentTransformation <DocumentTransformation>` **, чтение** - информация об идентификаторах документа


.. rubric:: Методы

+----------------------------------------------------+-------------------------------+
| |TransformTemplateTask-AddDocumentTransformation|_ | |TransformTemplateTask-Send|_ |
+----------------------------------------------------+-------------------------------+

.. |TransformTemplateTask-AddDocumentTransformation| replace:: AddDocumentTransformation()
.. |TransformTemplateTask-Send| replace:: Send()



.. _TransformTemplateTask-AddDocumentTransformation:
.. method:: TransformTemplateTask.AddDocumentTransformation([EntityId])

  :EntityId: ``строка`` идентификтаор сущности документа в шаблоне, который будет превращён в документ

  Добавляет :doc:`новый элемент <DocumentTransformation>` в коллекцию *DocumentTransformations* и возвращает его



.. _TransformTemplateTask-Send:
.. method:: TransformTemplateTask.Send()

  Превращает отмеченные сущности шаблона в документы. Возвращает :doc:`DocumentPackage`
