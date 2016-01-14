ResolutionRequestTask
=====================

Объект предназначен для отправки запроса на согласование.

Свойства
--------

-  InitialDocumentId (строка, чтение) - идентификатор документа, для
   которого формируется запрос на согласование, если такой документ единственный
   (т.е. объект ResolutionRequestTask создан методом :doc:`CreateResolutionRequestTask <CreateResolutionRequestTask>`
   объекта :doc:`Document <Document>`)

-  InitialDocuments (:doc:`Коллекция <Collection>` объектов :doc:`Document <Document>`, чтение) - документы, для
   которых формируется запрос на согласование.
   
   -  если объект ResolutionRequestTask создан методом :doc:`CreateResolutionRequestTask <CreateResolutionRequestTask>`
      объекта :doc:`Document <Document>`, то **InitialDocuments** вернет единственный документ;

   -  если объект ResolutionRequestTask создан методом :doc:`CreateResolutionRequestTask <CreateResolutionRequestTask-(DocumentPackage)>`
      объекта :doc:`DocumentPackage <DocumentPackage>`, то **InitialDocuments** вернет все документы пакета, 
      для которого был создан запрос.

-  ResolutionRequestType (строка, чтение/запись) - тип запроса на
   согласование

-  Comment (строка, чтение/запись) - комментарий к запросу согласования

-  TargetDepartmentId (строка, чтение/запись) - идентификатор
   подразделения, в которое направлен запрос

-  TargetUserId (строка, чтение/запись) - идентификатор пользователя,
   которому направлен запрос

Свойство ResolutionRequestType принимает одно из следующих значений:

-  ApprovementRequest - запрос на согласование документа

-  SignatureRequest - запрос на подпись документа

Методы
------

-  :doc:`Send <Send-(ResolutionRequestTask)>` - отправить запрос на
   согласование на сервер Диадок

.. toctree::
   :name: Auto
   :hidden:

   Send <Send-(ResolutionRequestTask)>
