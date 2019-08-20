Регламентный документооборот по электронным счетам фактурам
===========================================================

Для удобства работы :doc:`объект организации <../ComObjects/Organization>` содержит механизм автоматизированного формирования и отправки всех технологических документов, которые требует `регламент документооборота ЭСФ <http://api-docs.diadoc.ru/ru/latest/docflows/InvoiceDocflow.html#id4>`_.
Этот механизм инкапсулирован в объекте :doc:`ReceiptGenerationProcess <../ComObjects/ReceiptGenerationProcess>`, иногда называемый ``Магией``.

Объект имеет методы :meth:`ReceiptGenerationProcess.Start`, :meth:`ReceiptGenerationProcess.Stop`, предназначенные для запуска и остановки процесса, соответственно.
Процесс формирования технологических документов работает в фоновом потоке и не вносит задержек в работу интерфейса.


.. code-block:: c#

    ReceiptGenerationProcess = Organization.GetReceiptGenerationProcess();
    ReceiptGenerationProcess.Start();



Также у отдельных типов документов есть методы для формирования технологических документов по конкретному документу:

  * :meth:`BaseDocument.SendReceiptsAsync`
  * :meth:`Invoice.SendReceiptsAsync`
  * :meth:`InvoiceCorrection.SendReceiptsAsync`
  * :meth:`InvoiceRevision.SendReceiptsAsync`
  * :meth:`InvoiceCorrectionRevision.SendReceiptsAsync`
  * :meth:`Ucd.SendReceiptsAsync`
  * :meth:`UcdRevision.SendReceiptsAsync`
  * :meth:`Utd.SendReceiptsAsync`
  * :meth:`UtdRevision.SendReceiptsAsync`


.. note:: Метод формирует только технологические документы. Если документ необходимо подписать (сформировать титул покупателя), то необходимо использовать объект :doc:`ReplySendTask2 <../ComObjects/ReplySendTask2>`

.. seealso:: :doc:`HowTo_reply_document`
