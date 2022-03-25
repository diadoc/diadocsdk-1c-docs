AcquireCounteragentTask
=======================

Объект предназначен для отправки приглашения контрагента к партнерству


.. rubric:: Свойства

:CounteragentBoxId:
    **Строка, чтение/запись** - идентификатор организации-контрагента

:Inn:
    **Строка, чтение/запись** - ИНН организации-контрагента

:Message:
    **Строка, чтение/запись** - текст комментария к операции

:FileName:
    **Строка, чтение/запись** - имя файла с приглашением

:SignatureRequested:
    **Булево, чтение/запись** - запрос подписи контрагента

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

    .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tabs:: Все актуальные

        * :meth:`Send() <AcquireCounteragentTask.Send>`

        * :meth:`SendAsync() <AcquireCounteragentTask.SendAsync>`


.. method:: AcquireCounteragentTask.Send()

    Отправляет приглашение контрагента к партнерству


.. method:: AcquireCounteragentTask.SendAsync()

    Асинхронно отправляет приглашение контрагента к партнерству. Возвращает :doc:`AsyncResult`
