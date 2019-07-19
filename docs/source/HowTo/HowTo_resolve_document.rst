Как работать с согласованием и передачей на подпись
===================================================


Как запрашивать согласование и передавать на подпись документ
-------------------------------------------------------------

Для отправки документа на подпись или согласование предназначен объект :doc:`../ComObjects/ResolutionRequestTask`, который можно создать методами :func:`Document.CreateResolutionRequestTask` и :func:`DocumentPackage.CreateResolutionRequestTask`


.. code-block:: c#

    Процедура ОтправитьДокументНаПодписьВПодразделение(ИдентификаторДокумента, ИдентификаторПодразделения)

        Document = Organization.GetDocumentById(ИдентификаторДокумента)

        ResolutionRequestTask = Document.CreateResolutionRequestTask();

        // ResolutionRequestType определяет будет ли это запрос на согласование или передача на подпись
        // В данном случае - передача на подпись
        ResolutionRequestTask.ResolutionRequestType = "SignatureRequest";
        ResolutionRequestTask.TargetDepartmentId    = ИдентификаторПодразделения;

        ResolutionRequestTask.Send();

    КонецПроцедуры


Подтверждение и отказ в соласовании или подписи
-----------------------------------------------

Для принятия резолюции используйте методы :func:`Document.Approve` и :func:`DpcumentPackage.Approve`

Для отказа в резолюции - :func:`Document.Disapprove` и :func:`DpcumentPackage.Disapprove`
