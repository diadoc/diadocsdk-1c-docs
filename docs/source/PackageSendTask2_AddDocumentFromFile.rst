AddDocumentFromFile
===================

    Метод объекта :doc:`PackageSendTask2 <PackageSendTask2>`


**Синтаксис**

AddDocumentFromFile(<TitleName>, <Function>, <Version>, <Path>)


**Параметры**

    -  <TitleName> (строка, обязательный) - название типа документа
    -  <Function> (строка, обязательный) - функция документа
    -  <Version> (строка, обязательный) - версия документа
    -  <Path> (строка, обязательный) - путь до файла с контентом


**Возвращаемое значение**

:doc:`CustomDocumentToSend <CustomDocumentToSend>`


**Описание**

Добавляет в задание на отправку документ указанного типа, загружая его контент из файла

Доступные значения названия, функции и версии документа можно получить методом :doc:`GetDocumentTypes <GetDocumentTypes>`

У полученного объекта :doc:`CustomDocumentToSend <CustomDocumentToSend>` поле **Content** будет неопределено

.. toctree::
   :name: Auto
   :hidden:

   CustomDocumentToSend <CustomDocumentToSend>
