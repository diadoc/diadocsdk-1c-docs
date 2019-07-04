ReplySendTask
=============

.. deprecated:: 5.27.0
    Используйте :doc:`ReplySendTask2 <ReplySendTask2>`

Объект предназначен для выполнения ответного действия с документом или с пакетом документов


.. rubric:: Свойства

:Content: (:doc:`BaseContent <BaseContent>`, чтение) - содержимое ответного действия


.. rubric:: Методы

* :doc:`Send <Send-(ReplySendTask)>` - отправить титул покупателя на сервер Диадок


.. rubric:: Дополнительная информация

Тип свойства Content зависит от контекста создания объекта ReplySendTask

+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|Контекст создания                                                                             |Тип контента                                                                |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`DocumentPackage.CreateReplySendTask(Any Type) <CreateReplySendTask-(DocumentPackage)>`  |:doc:`PackageContent <PackageContent>`                                      |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`Document.CreateReplySendTask("AcceptDocument") <CreateReplySendTask-(Document)>`        |:doc:`Torg12BuyerContent <Torg12BuyerContent>`                              |
|                                                                                              |:doc:`TovTorgBuyerContent <TovTorgBuyerContent>`                            |
|                                                                                              |:doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>`|
|                                                                                              |:doc:`Act552BuyerContent <Act552BuyerContent>`                              |
|                                                                                              |:doc:`UtdBuyerContent <UtdBuyerContent>`                                    |
|                                                                                              |:doc:`AcceptanceContent <AcceptanceContent>`                                |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`Document.CreateReplySendTask("RejectDocument") <CreateReplySendTask-(Document)>`        |:doc:`FormalizedRejectionContent <FormalizedRejectionContent>`              |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`Document.CreateReplySendTask("CorrectionRequest") <CreateReplySendTask-(Document)>`     |:doc:`CorrectionRequestContent <CorrectionRequestContent>`                  |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`Document.CreateReplySendTask("AcceptRevocation") <CreateReplySendTask-(Document)>`      |:doc:`AcceptanceContent <AcceptanceContent>`                                |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`Document.CreateReplySendTask("RejectRevocation") <CreateReplySendTask-(Document)>`      |:doc:`FormalizedRejectionContent <FormalizedRejectionContent>`              |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
|:doc:`Document.CreateReplySendTask("RevocationRequest") <CreateReplySendTask-(Document)>`     |:doc:`RevocationRequestContent <RevocationRequestContent>`                  |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
