SendDraftAsync
==============

Метод объекта :doc:`Organization <Organization>`.

**Синтаксис**


SendDraftAsync(<MessageId>)

**Параметры**


-  <MessageId> (Строка, обязательный) Уникальный идентификатор
   черновика.

**Возвращаемое значение**


:doc:`AsyncResult <AsyncResult>`.

**Описание**


Инициирует асинхронную операцию отправки черновика по его уникальному
идентификатору. Результатом асинхронной операции является коллекция
:doc:`Collection <Collection>` объектов, производных от
:doc:`Document <Document>`.
