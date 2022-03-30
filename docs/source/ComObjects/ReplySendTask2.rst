ReplySendTask2
==============

Задание для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:ContentItems:
    :doc:`Коллекция <Collection>` **объектов** :doc:`PackageContentItem` **, чтение** - коллекция пар *документ-контент*, для которых создаётся ответное действие

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

    .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные
    
        * :meth:`Send() <ReplySendTask2.Send>`
        * :meth:`SendAsync() <ReplySendTask2.SendAsync>`


.. method:: ReplySendTask2.Send()

    Применяет ответные действия


.. method:: ReplySendTask2.SendAsync()

    Применяет ответные действия асинхронно. Возвращает :doc:`AsyncResult` с булевым типом результата