CounteragentItem
================

Информации об организации, полученной по её ИНН.
Элемент коллекции, возвращаемой методом :meth:`Organization.GetCounteragentListByInnList`


.. rubric:: Свойства

:Inn:
    **Строка, чтение** - ИНН контрагента

:Counteragent:
    :doc:`Counteragent` **, чтение** - представление данных о контрагенте. Если информации об организации не найдено, то будет :doc:`пустым <Descriptions/Empty_Com_Object>`