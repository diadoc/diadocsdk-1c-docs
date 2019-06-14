AddDocumentFromBase64
=====================

Метод объекта :doc:`PackageSendTask2 <PackageSendTask2>`


.. rubric:: Синтаксис

AddDocumentFromBase64(TitleName, Function, Version, Base64)


.. rubric:: Параметры

:TitleName: (строка) - название типа документа
:Function: (строка) - функция документа
:Version: (строка) - версия документа
:Base64: (строка) - контент документа в Base64


.. rubric:: Возвращаемое значение

:doc:`CustomDocumentToSend <CustomDocumentToSend>`


**Описание**

Добавляет в задание на отправку документ указанного типа, загружая его контент из Base64 строки

У полученного объекта :doc:`CustomDocumentToSend <CustomDocumentToSend>` поле **Content** будет пусто


.. seealso:: :doc:`GetDocumentTypes <GetDocumentTypes>`
