AddDocumentFromString
=====================

    Метод объекта :doc:`PackageSendTask2 <PackageSendTask2>`


**Синтаксис**

AddDocumentFromString(<TitleName>, <Function>, <Version>, <Content_string>, <Encoding>)


**Параметры**

    -  <TitleName> (строка, обязательный) - название типа документа
    -  <Function> (строка, обязательный) - функция документа
    -  <Version> (строка, обязательный) - версия документа
    -  <Content_string> (строка, обязательный) - контент документа в строковом представлении
    -  <Encoding> (целое беззнаковое число, обязательный) - кодовая страница, в которую необходимо перекодировать контент


**Возвращаемое значение**

:doc:`CustomDocumentToSend <CustomDocumentToSend>`


**Описание**

Добавляет в задание на отправку документ указанного типа, загружая его контент из строки

Доступные значения названия, функции и версии документа можно получить методом :doc:`GetDocumentTypes <GetDocumentTypes>`

У полученного объекта :doc:`CustomDocumentToSend <CustomDocumentToSend>` поле **Content** будет неопределено

.. toctree::
   :name: Auto
   :hidden:

   CustomDocumentToSend <CustomDocumentToSend>
