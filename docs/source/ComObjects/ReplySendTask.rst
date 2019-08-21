ReplySendTask
=============

.. deprecated:: 5.27.0
    Используйте :doc:`ReplySendTask2 <ReplySendTask2>`

Задание для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:Content:
  :doc:`BaseContent <BaseContent>` **, чтение** - содержимое ответного действия. |ReplySendTask-CreationContext|_


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
  Возвращаемая коллекция всегда содержит элемент с информацией о нежелательном использовании этого метода и только его

  .. deprecated:: 5.18.0
    Проверку контента рекомендуется проводить самостоятельно


.. rubric:: Дополнительная информация

.. |ReplySendTask-CreationContext| replace:: Возможные типы
.. _ReplySendTask-CreationContext:

+------------------------------------------------------------------+----------------------------------------------------------------------------+
|Контекст создания ReplySendTask'а                                 |Тип контента                                                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`DocumentPackage.CreateReplySendTask`                       |:doc:`PackageContent <PackageContent>`                                      |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``AcceptDocument``   |:doc:`Torg12BuyerContent <Torg12BuyerContent>`                              |
|                                                                  |:doc:`TovTorgBuyerContent <TovTorgBuyerContent>`                            |
|                                                                  |:doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>`|
|                                                                  |:doc:`Act552BuyerContent <Act552BuyerContent>`                              |
|                                                                  |:doc:`UtdBuyerContent <UtdBuyerContent>`                                    |
|                                                                  |:doc:`AcceptanceContent <AcceptanceContent>`                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``RejectDocument``   |:doc:`FormalizedRejectionContent <FormalizedRejectionContent>`              |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``CorrectionRequest``|:doc:`CorrectionRequestContent <CorrectionRequestContent>`                  |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``AcceptRevocation`` |:doc:`AcceptanceContent <AcceptanceContent>`                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``RejectRevocation`` |:doc:`FormalizedRejectionContent <FormalizedRejectionContent>`              |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
|:meth:`Document.CreateReplySendTask` с типом ``RevocationRequest``|:doc:`RevocationRequestContent <RevocationRequestContent>`                  |
+------------------------------------------------------------------+----------------------------------------------------------------------------+
