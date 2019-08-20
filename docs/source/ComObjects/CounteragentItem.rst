CounteragentItem
================

Контрагент с ИНН.
Является результатом метода :meth:`Organization.GetCounteragentListByInnList`


.. rubric:: Свойства

:Inn:
  **Строка, чтение** - ИНН контрагента

:Counteragent:
  :doc:`Counteragent <Counteragent>` **, чтение** - представление данных о контрагенте

.. note:: В случае, если контрагент с заданным ИНН не найден в Диадок, свойство *Counteragent* принимает значение ``Неопределено``
