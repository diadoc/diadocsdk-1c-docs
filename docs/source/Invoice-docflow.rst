Регламентный документооборот по электронным счетам фактурам
===========================================================

Для удобства работы объект :doc:`Organization <Organization>` содержит
механизм автоматизированного формирования и отправки всех
технологических документов, которые требует `регламент документооборота
:doc:ЭСФ <#InvoiceDocflow>`. Этот механизм инкапсулирован в объекте
:doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>`.

Объект :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>` имеет
методы Start, Stop, предназначенные для запуска и остановки процесса,
соответственно. Процесс формирования технологических документов работает
в фоновом потоке и не вносит задержек в работу интерфейса. Пример:

::

        ReceiptGenerationProcess = Organization.GetReceiptGenerationProcess();
        ReceiptGenerationProcess.Start();
