Релиз 5.26.3
============

.. feed-entry::
   :date: 2019-03-29
   
- Добавлен метод TestConnection2 для проверки связи с сервером Диадок
- В объект UserPermissions добавлены поля CanManageCounteragents, IsBlocked, BlockReason
- Обновлены типы ResolutionRequest
- Исправлены ошибки:
    - при выполнении метода GetDocumentEventList возникала ошибка "##100[Ошибка сервера Диадок]code:400, HTTP error: Could not parse messageId query param:."
    - GetDocumentEventList получал пустую коллекцию событий по документам, если в ящике было создано много черновиков подряд


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_