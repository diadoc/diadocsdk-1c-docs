Регламентный документооборот по электронным счетам фактурам
===========================================================

Для удобства работы :doc:`объект организации <Organization>` содержит механизм автоматизированного формирования и отправки всех технологических документов, которые требует `регламент документооборота ЭСФ <http://api-docs.diadoc.ru/ru/latest/docflows/InvoiceDocflow.html#id4>`_.
Этот механизм инкапсулирован в объекте :doc:`ReceiptGenerationProcess <ReceiptGenerationProcess>`, иногда называемый ``Магией``.

Объект имеет методы :func:`ReceiptGenerationProcess.Start`, :func:`ReceiptGenerationProcess.Stop`, предназначенные для запуска и остановки процесса, соответственно.
Процесс формирования технологических документов работает в фоновом потоке и не вносит задержек в работу интерфейса.


.. code-block:: c#

    ReceiptGenerationProcess = Organization.GetReceiptGenerationProcess();
    ReceiptGenerationProcess.Start();



Также у отдельных типов документов есть методы для формирования технологических документов по конкретному документу:

  * :func:`BaseDocument.SendReceiptsAsync`
  * :func:`Invoice.SendReceiptsAsync`
  * :func:`InvoiceCorrection.SendReceiptsAsync`
  * :func:`InvoiceRevision.SendReceiptsAsync`
  * :func:`InvoiceCorrectionRevision.SendReceiptsAsync`
  * :func:`Ucd.SendReceiptsAsync`
  * :func:`UcdRevision.SendReceiptsAsync`
  * :func:`Utd.SendReceiptsAsync`
  * :func:`UtdRevision.SendReceiptsAsync`


.. note:: Метод формирует только технологические документы. Если документ необходимо подписать (сформировать титул покупателя), то необходимо использовать объект :doc:`ReplySendTask2 <ReplySendTask2>`

.. seealso:: :doc:`HowTo_reply_document`
