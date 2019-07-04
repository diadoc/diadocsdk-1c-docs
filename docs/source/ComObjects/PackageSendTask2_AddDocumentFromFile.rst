AddDocumentFromFile
===================

Метод объекта :doc:`PackageSendTask2 <PackageSendTask2>`


.. rubric:: Синтаксис

AddDocumentFromFile(TitleName, Function, Version, Path)


.. rubric:: Параметры

:TitleName: (строкай) - название типа документа
:Function: (строка) - функция документа
:Version: (строка) - версия документа
:Path: (строка) - путь до файла с контентом


.. rubric:: Возвращаемое значение

:doc:`CustomDocumentToSend <CustomDocumentToSend>`


.. rubric:: Описание

Добавляет в задание на отправку документ указанного типа, загружая его контент из файла.

У полученного объекта :doc:`CustomDocumentToSend <CustomDocumentToSend>` поле **Content** будет пусто


.. seealso:: :doc:`GetDocumentTypes <GetDocumentTypes>`