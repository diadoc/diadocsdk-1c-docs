ReceiptGenerationProcess
========================

Процесс автоматического формирования технологических документов в ящике

.. rubric:: Свойства

:IsRun:
  **Булево, чтение** - процесс запущен

:Errors:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ReceiptError <ReceiptError>` - информация об ошибках, возникших во время работы процесса


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
