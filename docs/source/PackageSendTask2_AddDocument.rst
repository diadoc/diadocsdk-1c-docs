AddDocument
===========

    Метод объекта :doc:`PackageSendTask2 <PackageSendTask2>`


**Синтаксис**

AddDocument(<TitleName>, <Function>, <Version>)


**Параметры**

    -  <TitleName> (строка, обязательный) - название типа документа
    -  <Function> (строка, обязательный) - функция документа
    -  <Version> (строка, обязательный) - версия документа


**Возвращаемое значение**

:doc:`CustomDocumentToSend <CustomDocumentToSend>`


**Описание**

Добавляет в задание на отправку документ указанного типа.
Доступные значения названия, функции и версии документа можно получить методом :doc:`GetDocumentTypes <GetDocumentTypes>`

.. toctree::
   :name: Auto
   :hidden:

   CustomDocumentToSend <CustomDocumentToSend>
