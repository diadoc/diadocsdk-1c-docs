DynamicContent
==============

Объект предназначен для представления содержания документа.

Используется:

    - в :doc:`CustomDocumentToSend.Content <CustomDocumentToSend>`, если тот создан через объект :doc:`PackageSendTask2 <PackageSendTask2>`
    - в :doc:`PackageContentItem.Content <PackageContentItem>`, полученным через объект  :doc:`ReplySendTask2 <ReplySendTask2>` с типом "AcceptDocument"
    - как результат выполнения методов :doc:`Document.GetDynamicContent() <Document_GetDynamicContent>` и :doc:`Document.GetDynamicBuyerContent() <Document_GetDynamicBuyerContent>`


Свойства объекта
----------------

Объект реализует интерфейс IDispatch и не имеет фиксированного набора полей и методов.
Набор полей напрямую зависит от информации о контенте, которую может предоставить Диадок.
Получить описание полей можно методом :doc:`Organization.SaveUserDataXSD <SaveUserDataXSD>`

Каждое поле объекта является или строкой, или :doc:`DynamicContent'ом <DynamicContent>`, или :doc:`коллекцией <Collection>`


Как работать с коллекциями
--------------------------

Если есть такая организация контента:

::

    DynamicContent.ВладелецКоллекции.Коллекция

Тогда для добавления элемента в коллекцию необходимо вызвать

::
    
    // Если коллекция состоит из COM-объектов
    // ЭлементКоллекции будет обектом типа DynamicContent
    ЭлементКоллекции = DynamicContent.ВладелецКоллекции.AddКоллекция();
    
    // или,
    // если коллекция состоит из строк
    DynamicContent.ВладелецКоллекции.AddКоллекция("Значение");
    
Имя метода, с помощью которого можно добавить элемент зависит от названия коллекции и формируется как "Add" + <название коллекции>