Релиз 5.26.0
============

.. feed-entry::
   :date: 2019-02-05

- Добавлена возможность постановки/снятия документов с маршрута согласования:
    - у объекта Organization появился метод GetResolutionRoutes
    - появился объект маршрута согласования
    - у объекта Document появилось поле RouteId
    - у объектов Document и DocumentPackage появились методы AssignToResolutionRoute и RemoveFromResolutionRoute

- Методы ReplySendTask.ValidateContent и SendTask.ValidateContent всегда в результате содержат оповещение, что метод устарел
- Асинхронные методы часто теряли описание ошибки, возвращая "Unknown exception"


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_