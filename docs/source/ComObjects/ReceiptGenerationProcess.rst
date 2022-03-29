ReceiptGenerationProcess
========================

Процесс автоматического формирования технологических документов в ящике

.. rubric:: Свойства

:IsRun:
    **Булево, чтение** - процесс запущен

:Errors:
    :doc:`Коллекция <Collection>` **объектов** :doc:`ReceiptError` - информация об ошибках, возникших во время работы процесса

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

    .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`Start() <ReceiptGenerationProcess.Start>`
        * :meth:`Stop() <ReceiptGenerationProcess.Stop>`

.. method:: ReceiptGenerationProcess.Start()

    Запускает процесс формирования технологических документов


.. method:: ReceiptGenerationProcess.Stop()

    Останавливает процесс формирования технологических документов


.. seealso:: :doc:`../HowTo/HowTo_invoice_docflow`