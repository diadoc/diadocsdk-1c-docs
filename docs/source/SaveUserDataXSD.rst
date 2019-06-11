SaveUserDataXSD
===============

Метод объекта :doc:`Organization <Organization>`


.. rubric:: Синтаксис

SaveUserDataXSD(TitleName, Function, Version, Side, Path)


.. rubric:: Параметры

:TitleName: (строка) - название типа документа
:Function: (строка) - функция документа
:Version: (строка) - версия документа
:Side: (строка) - участник документооброта
:Path: (строка) - полное имя файла, в который нужно сохранить описание контента


.. rubric:: Возвращаемое значение

Отсутствует


.. rubric:: Описание

Сохраняет описание контента, которое можно использвоать для заполнения :doc:`DynamicContent <DynamicContent>`


.. rubric:: Дополнительная информация

+-----------------------+
|Значение параметра Side|
+-----------------------+
|Seller                 |
+-----------------------+
|Buyer                  |
+-----------------------+


.. seealso:: :doc:`GetDocumentTypes <GetDocumentTypes>`