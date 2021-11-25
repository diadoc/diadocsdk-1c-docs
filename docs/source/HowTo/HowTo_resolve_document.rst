Как работать с согласованием и передачей на подпись
===================================================


Как запрашивать согласование и передавать на подпись документ
-------------------------------------------------------------

Для отправки документа на подпись или согласование предназначен объект :doc:`../ComObjects/ResolutionRequestTask`, который можно создать методами :meth:`Document.CreateResolutionRequestTask` и :meth:`DocumentPackage.CreateResolutionRequestTask`


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


Подтверждение и отказ в согласовании или подписи
-----------------------------------------------

Для принятия резолюции используйте методы :meth:`Document.Approve` и :meth:`DocumentPackage.Approve`

Для отказа в резолюции - :meth:`Document.Disapprove` и :meth:`DocumentPackage.Disapprove`
