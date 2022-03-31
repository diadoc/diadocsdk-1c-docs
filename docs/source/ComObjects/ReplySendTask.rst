ReplySendTask
=============

.. deprecated:: 5.27.0
    Используйте :doc:`ReplySendTask2`

Задание для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:Content:
    :doc:`BaseContent` **, чтение** - содержимое ответного действия. :ref:`Возможные типы <ReplySendTask-Content>`

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

  .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`Send() <ReplySendTask.Send>`
        * :meth:`SendAsync() <ReplySendTask.SendAsync>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

            :meth:`ValidateContent() <ReplySendTask.ValidateContent>`, , :doc:`../History/release_info/5_18_0`,


        .. method:: ReplySendTask.ValidateContent()

            Валидирует ответные действия и возвращает :doc:`коллекцию <Collection>` :doc:`ошибок <ValidationError>`.


.. method:: ReplySendTask.Send()

  Применяет ответные действия


.. method:: ReplySendTask.SendAsync()

  Применяет ответные действия асинхронно. Возвращает :doc:`AsyncResult` с булевым типом результата


.. rubric:: Дополнительная информация

.. _ReplySendTask-Content:

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
