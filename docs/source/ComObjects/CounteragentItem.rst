CounteragentItem
================

Информации об организации, полученной по её ИНН.
Элемент коллекции, возвращаемой методом :meth:`Organization.GetCounteragentListByInnList`


.. rubric:: Свойства

:Inn:
    **Строка, чтение** - ИНН контрагента

:Counteragent:
    :doc:`Counteragent` **, чтение** - представление данных о контрагенте. Если для ИНН не найдено ни одного ящика в Диадок, то в поле будет лежать :doc:`./Descriptions/EmptyVariant`