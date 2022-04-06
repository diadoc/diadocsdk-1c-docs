TransformTemplateTask
=====================

Задания для создания документов на основе шаблонов


.. rubric:: Свойства

:TemplateId:
    **Строка, чтение/запись** - идентификатор шаблона пакета документов

:DocumentTransformations:
    :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentTransformation` **, чтение** - информация об идентификаторах документа


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddDocumentTransformation() <TransformTemplateTask.AddDocumentTransformation>`
        * :meth:`Send() <TransformTemplateTask.Send>`


.. method:: TransformTemplateTask.AddDocumentTransformation([EntityId])

    :EntityId: ``строка`` идентификтаор сущности документа в шаблоне, который будет превращён в документ

    Добавляет :doc:`новый элемент <DocumentTransformation>` в коллекцию **DocumentTransformations** и возвращает его


.. method:: TransformTemplateTask.Send()

    Превращает отмеченные сущности шаблона в документы. Возвращает :doc:`DocumentPackage`