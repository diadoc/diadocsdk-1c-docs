GetCounteragentListByInnList
============================

Метод объекта :doc:`Organization <Organization>`

**Синтаксис**


GetCounteragentListByInnList(<InnList>)

**Параметры**


-  <InnList> (Строка, обязательный) - список ИНН контрагентов,
   разделенные запятой

**Возвращаемое значение**


Объект :doc:`AsyncResult <AsyncResult>`.

**Описание**


Инициирует асинхронную операция получения списка контрагентов по списку
ИНН. Результатом асинхронной операции является объект Collection -
коллекция объектов типа CounteragentItem .
