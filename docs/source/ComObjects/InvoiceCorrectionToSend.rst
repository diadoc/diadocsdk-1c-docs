InvoiceCorrectionToSend
=======================

Документ на отправку *Корректировочный счет-фактура* в формате приказа `ММВ-7-6/93@ <https://normativ.kontur.ru/document?moduleId=1&documentId=249567&rangeId=83296>`_.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`CustomDocumentToSend`, создаваемый в :doc:`PackageSendTask2`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``InvoiceCorrection``


:Content:
    :doc:`InvoiceCorrectionContent` **, чтение** - содержимое документа