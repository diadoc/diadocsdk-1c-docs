DynamicContent
==============

Объект предназначен для представления содержания документа

Используется:

    * в :doc:`CustomDocumentToSend.Content <CustomDocumentToSend>`, если тот создан через объект :doc:`PackageSendTask2 <PackageSendTask2>`
    * в :doc:`PackageContentItem.Content <PackageContentItem>`, полученным через объект  :doc:`ReplySendTask2 <ReplySendTask2>` с типом ``AcceptDocument``
    * как результат выполнения метода :func:`Document.GetDynamicContent`


.. rubric:: Свойства и методы

Объект реализует интерфейс `IDispatch <https://docs.microsoft.com/en-us/windows/desktop/api/oaidl/nn-oaidl-idispatch>`_ и не имеет фиксированного набора полей и методов.
Набор полей напрямую зависит от информации о контенте, которую может предоставить Диадок.
Получить описание полей можно методом :func:`Organization.SaveUserDataXSD`

Каждое поле объекта является или строкой, или :doc:`коллекцией <Collection>`, или :doc:`DynamicContent'ом <DynamicContent>`


.. rubric:: Как работать с коллекциями

Если есть такая организация контента:

    ``DynamicContent.ВладелецКоллекции.Коллекция``

Тогда для добавления элемента в коллекцию необходимо вызвать

.. code-block:: c#

    // Если коллекция состоит из COM-объектов
    // ЭлементКоллекции будет обектом типа DynamicContent
    НовыйЭлементКоллекции = DynamicContent.ВладелецКоллекции.AddКоллекция();

    // или,
    // если коллекция состоит из строк
    DynamicContent.ВладелецКоллекции.AddКоллекция("Значение");


Имя метода, с помощью которого можно добавить элемент зависит от названия коллекции и формируется как ``"Add" + <название коллекции>``
