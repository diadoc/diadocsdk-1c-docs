Регламентный документооборот по электронным счетам фактурам
===========================================================

Для удобства работы :doc:`Organization <Organization>` содержит механизм автоматизированного формирования и отправки всех технологических документов, которые требует `регламент документооборота ЭСФ <http://api-docs.diadoc.ru/ru/latest/docflows/InvoiceDocflow.html#id4>`_. Этот механизм инкапсулирован в объекте :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>`.

:doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>` имеет методы Start, Stop, предназначенные для запуска и остановки процесса, соответственно. Процесс формирования технологических документов работает в фоновом потоке и не вносит задержек в работу интерфейса. Пример:


::

    ReceiptGenerationProcess = Organization.GetReceiptGenerationProcess();
    ReceiptGenerationProcess.Start();
