SetExtendedSignerDetailsTask
============================

Задача для добавления или обновления данных подписанта в базе Диадок

.. rubric:: Свойства


:ExtendedSignerDetailsToPost:
    :doc:`ExtendedSignerDetailsToPost` **, чтение** - данные подписанта

:DocumentTitleType:
    **Строка, чтение/запись** - тип титула документа. :doc:`Возможные значения <./Enums/DocumentTitleType>`.
    Получить значение для *DocumentTitleType* можно из объекта :doc:`DocumentTitle` в ответе метода :meth:`Organization.GetDocumentTypes`.
    Для *TitleType* == ``Absent`` и *TitleType* == ``UNKNOWN`` вызов невозможен.


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`Send() <SetExtendedSignerDetailsTask.Send>`


.. method:: SetExtendedSignerDetailsTask.Send()

    Отправляет данные подписанта на сервер Диадок