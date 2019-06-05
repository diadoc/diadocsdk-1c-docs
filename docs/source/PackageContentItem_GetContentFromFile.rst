GetContentFromFile
==================

Метод объекта :doc:`PackageContentItem <PackageContentItem>`


**Синтаксис**

AddDocument(<Path>)


**Параметры**

    -  <Path> (строка, обязательный) - путь до файла с контентом


**Возвращаемое значение**

Отсутствует


**Описание**

Добавляет контент ответного действия с диска.

В объекте :doc:`PackageContentItem <PackageContentItem>`, из которого вызван метод, поле **Content** станет пустым.

При выполнении ответного действия объектом :doc:`ReplySendTask2 <ReplySendTask2>` загруженный контент будет подписан
