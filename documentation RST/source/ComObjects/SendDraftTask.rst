SendDraftTask
=============

Задание для отправки черновика сообщения


.. rubric:: Свойства

:Signer:
    :doc:`Signer` **, чтение** - данные подписанта

:ExtendedSigners:
    :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - данные подписанта для УПД, Торг-12 @551, Акта @552

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

    .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`SendAsync() <SendDraftTask.SendAsync>`
        * :meth:`AddExtendedSigner() <SendDraftTask.AddExtendedSigner>`

.. method:: SendDraftTask.SendAsync()

    Асинхронно превращает черновики в документы. Возвращает :doc:`AsyncResult` c :doc:`коллекцией <Collection>` :doc:`отправленных документов <Document>` в качестве результата


.. method:: SendDraftTask.AddExtendedSigner()

    Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию **ExtendedSigners** и возвращает его