Релиз 5.26.0
============

.. feed-entry::
   :date: 2019-02-05

- Добавлена поддержка ставки НДС "20/120"
- Добавлена возможность постановки/снятия документов с маршрута согласования:
    - у объекта :doc:`Organization <Organization>` появился метод :doc:`GetResolutionRoutes() <GetResolutionRoutes>`
    - появился объект :doc:`маршрута согласования <Route>`
    - у объекта :doc:`Document <Document>` появилось поле RouteId
    - у объектов :doc:`Document <Document>` и :doc:`DocumentPackage <DocumentPackage>` появились методы :doc:`AssignToResolutionRoute(RouteId[, Comment]) <AssignToResolutionRoute>` и :doc:`RemoveFromResolutionRoute(RouteId[, Comment]) <RemoveFromResolutionRoute>`

- Методы :doc:`ReplySendTask.ValidateContent() <ValidateContent-(ReplySendTask)>` и :doc:`SendTask.ValidateContent() <ValidateContent-(SendTask)>` всегда в результате содержат оповещение, что метод устарел
- Асинхронные методы часто теряли описание ошибки, возвращая "Unknown exception"


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_