CustomDataPatchTask
===================

Задача редактирования коллекции :doc:`Document`.CustomData - тэгов документа


.. rubric:: Свойства

:Items:
    :doc:`Коллекция <Collection>` **объектов** :doc:`CustomDataPatchItem` **, чтение** - коллекция изменений тэгов


.. rubric:: Методы


.. method:: CustomDataPatchTask.AddItem()

    Добавляет :doc:`новый элемент <CustomDataPatchItem>` в коллекцию **Items** и возвращает его


.. method:: CustomDataPatchTask.Send()

    Применяет изменения


.. method:: CustomDataPatchTask.SendAsync()

    Асинхронно применяет изменения. Результатом в :doc:`асинхронном результате <AsyncResult>` будет булево значение
