GetCounteragentListByInnList
============================

Метод объекта :doc:`Organization <Organization>`


**Синтаксис**

GetCounteragentListByInnList(<InnList>)


**Параметры**

-  <InnList> (Строка, обязательный) - список ИНН контрагентов, разделенные запятой


**Возвращаемое значение**

:doc:`AsyncResult <AsyncResult>`.


**Описание**

Инициирует асинхронную операция получения списка ящиков в Диадок по списку ИНН. Результатом асинхронной операции является :doc:`коллекция <Collection>` объектов :doc:`CounteragentItem <CounteragentItem>`.
