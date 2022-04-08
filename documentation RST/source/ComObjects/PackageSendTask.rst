PackageSendTask
===============

Задание для отправки сообщения с пакетом документов на сервер Диадок

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`PackageSendTask2`


.. rubric:: Свойства

:OperationId:
    **Строка, чтение/запись** - уникальный идентификатор операции

:CounterAgentId:
    **Строка, чтение/запись** - идентификатор контрагента. **Не влияет** на заполнение контента

:FromDepartmentId:
    **Строка, чтение/запись** - идентификатор подразделения отправителя

:ToDepartmentId:
    **Строка, чтение/запись** - идентификатор подразделения получателя

:ProxyBoxId:
    **Строка, чтение/запись** - идентификатор ящика, промежуточного получателя

:ProxyDepartmentId:
    **Строка, чтение/запись** -  идентификатор подразделения, в ящике промежуточного получателя

:IsDraft:
    **Булево, чтение/запись** - признак того, что сообщение является черновиком

:IsInternal:
    **Булево, чтение/запись** - признак того, что сообщение является внутренним, то есть сообщением между подразделениями организации

:LockPackage:
    **Булево, чтение/запись** - признак того, что пакет после отправки должен быть нередактируемым

:DelaySend:
    **Булево, чтение/запись** - признак того, что сообщение будет сохранено без отправки

:DocumentsToSend:
    :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentToSend` **, чтение** - документы на отправку, добавленные в пакет

:SaveContentPath:
    **Строка, чтение/запись** - путь к папке, для сохранения сгенерированного содержимого

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

    .. versionadded:: 5.37.0


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddDocument() <PackageSendTask.AddDocument>`
        * :meth:`AddDocumentFromFile() <PackageSendTask.AddDocumentFromFile>`
        * :meth:`AddDocumentFromFileRaw() <PackageSendTask.AddDocumentFromFileRaw>`
        * :meth:`Send() <PackageSendTask.Send>`
        * :meth:`SendAsync() <PackageSendTask.SendAsync>`
        * :meth:`AddEncryptCertificate() <PackageSendTask.AddEncryptCertificate>`


.. method:: PackageSendTask.AddDocument(FormalizedDocumentType)

    :FormalizedDocumentType: **Строка** - тип документа. Может принимать одно из значений :doc:`перечисления <./Enums/FormalizedDocumentTypeToSend>`

    Добавляет :doc:`новый элемент <DocumentToSend>` в коллекцию **DocumentsToSend** и возвращает его

    Если в качестве типа передана версия документа, возвращает объект :doc:`LegacyDocumentToSend`


.. method:: PackageSendTask.AddDocumentFromFile(DocumentType, FilePath)

    :DocumentType: **Строка** - тип документа. Принимает значение из :doc:`перечисления <./Enums/FormalizedDocumentTypeToSend>` или :doc:`перечисления <./Enums/DocumentToSend>`
    :FilePath: **Строка** - путь до файла контента

    Добавляет :doc:`новый элемент <DocumentToSend>` в коллекцию **DocumentsToSend**, загружая контент из файла, и возвращает его.
    Контент будет разобран и получен в виде объектной модели, если это возможно. При отправке он будет перегенерирован


.. method:: PackageSendTask.AddDocumentFromFileRaw(DocumentType, FilePath)

    :DocumentType: **Строка** - тип документа. Принимает значение из :doc:`перечисления <./Enums/FormalizedDocumentTypeToSend>` или :doc:`перечисления <./Enums/DocumentToSend>`
    :FilePath: **Строка** - путь до файла контента

    Добавляет :doc:`новый элемент <DocumentToSend>` в коллекцию **DocumentsToSend**, загружая контент из файла, и возвращает его.
    Разбора контента и представления в виде объектной модели не происходит. При отправке перегенерации контента не произойдёт


.. method:: PackageSendTask.Send()

    Отправляет пакет документов в Диадок и возвращает :doc:`отправленные документы <DocumentPackage>`.
    Если отправка пакета с заполненным **OperationId** завершилась успехом, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового пакета, а в результате выполнения метода вернется ранее отправленный пакет


.. method:: PackageSendTask.SendAsync()

    Асинхронно отправляет пакет документов в Диадок и возвращает :doc:`AsyncResult` с :doc:`отправленными документами <DocumentPackage>` в качестве результата.
    Если отправка пакета с заполненным **OperationId** завершилась успехом, то все остальные попытки отправки с тем же идентификатором не будут приводить к отправке нового пакета, а в результате выполнения метода вернется ранее отправленный пакет


.. method:: PackageSendTask.AddEncryptCertificate(Certificate)

    :Certificate: :doc:`PersonalCertificate` сертификат КЭП

    Добавляет :doc:`сертификат <PersonalCertificate>` для шифрования контента


.. seealso:: :doc:`../HowTo/HowTo_post_document`