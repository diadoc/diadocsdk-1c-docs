ReplySendTask
=============

.. deprecated:: 5.27.0
    Используйте :doc:`ReplySendTask2`

Задание для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:Content:
  :doc:`BaseContent` **, чтение** - содержимое ответного действия. |ReplySendTask-CreationContext|_

:PowerOfAttorneyToAttach:
  :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

  .. versionadded:: 5.37.0


.. rubric:: Методы

+-----------------------+----------------------------+----------------------------------+
| |ReplySendTask-Send|_ | |ReplySendTask-SendAsync|_ | |ReplySendTask-ValidateContent|_ |
+-----------------------+----------------------------+----------------------------------+


.. |ReplySendTask-Send| replace:: Send()
.. |ReplySendTask-SendAsync| replace:: SendAsync()
.. |ReplySendTask-ValidateContent| replace:: ValidateContent()

.. _ReplySendTask-Send:
.. method:: ReplySendTask.Send()

  Применяет ответные действия



.. _ReplySendTask-SendAsync:
.. method:: ReplySendTask.SendAsync()

  Применяет ответные действия асинхронно. Возвращает :doc:`AsyncResult` с булевым типом результата



.. _ReplySendTask-ValidateContent:
.. method:: ReplySendTask.ValidateContent()

  Валидирует ответные действия и возвращает :doc:`коллекцию <Collection>` :doc:`ошибок <ValidationError>`.

  .. deprecated:: 5.18.0
    Проверку контента рекомендуется проводить самостоятельно

  .. versionchanged:: 5.26.0
    Возвращаемая коллекция всегда содержит элемент, говорящий, что метод устарел

  .. versionchanged:: 5.29.0
    Коллекция всегда пустая. Валидации не происходит. Метод оставлен для совместимости



.. rubric:: Дополнительная информация

.. |ReplySendTask-CreationContext| replace:: Возможные типы
.. _ReplySendTask-CreationContext:

+------------------------------------------------------------------+----------------------------------------+
|Контекст создания ReplySendTask'а                                 |Тип контента                            |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`DocumentPackage.CreateReplySendTask`                       |:doc:`PackageContent`                   |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``AcceptDocument``   |:doc:`Torg12BuyerContent`               |
|                                                                  |:doc:`TovTorgBuyerContent`              |
|                                                                  |:doc:`AcceptanceCertificateBuyerContent`|
|                                                                  |:doc:`Act552BuyerContent`               |
|                                                                  |:doc:`UtdBuyerContent`                  |
|                                                                  |:doc:`AcceptanceContent`                |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``RejectDocument``   |:doc:`FormalizedRejectionContent`       |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``CorrectionRequest``|:doc:`CorrectionRequestContent`         |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``AcceptRevocation`` |:doc:`AcceptanceContent`                |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``RejectRevocation`` |:doc:`FormalizedRejectionContent`       |
+------------------------------------------------------------------+----------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``RevocationRequest``|:doc:`RevocationRequestContent`         |
+------------------------------------------------------------------+----------------------------------------+
