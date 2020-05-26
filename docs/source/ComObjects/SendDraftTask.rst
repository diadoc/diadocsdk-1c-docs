SendDraftTask
=============

Задание для отправки черновика сообщения


.. rubric:: Свойства

:Signer:
  :doc:`Signer` **, чтение** - данные подписанта

:ExtendedSigners:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - данные подписанта для УПД, Торг-12 @551, Акта @552


.. rubric:: Методы

+----------------------------+------------------------------------+
| |SendDraftTask-SendAsync|_ | |SendDraftTask-AddExtendedSigner|_ |
+----------------------------+------------------------------------+

.. |SendDraftTask-SendAsync| replace:: SendAsync()
.. |SendDraftTask-AddExtendedSigner| replace:: AddExtendedSigner()


.. _SendDraftTask-SendAsync:
.. method:: SendDraftTask.SendAsync()

  Асинхронно превращает черновики в документы. Возвращает :doc:`AsyncResult` c :doc:`коллекцией <Collection>` :doc:`отправленных документов <Document>` в качестве результата



.. _SendDraftTask-AddExtendedSigner:
.. method:: SendDraftTask.AddExtendedSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *ExtendedSigners* и возвращает его
