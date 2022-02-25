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

+-----------------------------------+----------------------------------+
| |ReceiptGenerationProcess-Start|_ | |ReceiptGenerationProcess-Stop|_ |
+-----------------------------------+----------------------------------+

.. |ReceiptGenerationProcess-Start| replace:: Start()
.. |ReceiptGenerationProcess-Stop| replace:: Stop()



.. _ReceiptGenerationProcess-Start:
.. method:: ReceiptGenerationProcess.Start()

  Запускает процесс формирования технологических документов



.. _ReceiptGenerationProcess-Stop:
.. method:: ReceiptGenerationProcess.Stop()

  Останавливает процесс формирования технологических документов


.. seealso:: :doc:`../HowTo/HowTo_invoice_docflow`
