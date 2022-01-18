AttachedPowerOfAttorney
=======================

Представления данных об МЧД, прикреплённой к какой-либо из сущностей внутри документа

.. versionadded:: 5.37.0


.. rubric:: Свойства

:PowerOfAttorneyInfo:
  :doc:`PowerOfAttorneyInfo` **, чтение** - реквизиты МЧД

:Date:
  **Дата, чтение** - дата и время последнего изменения статуса прикреплённой МЧД

:Affiliation:
  **Строка, чтение** - информация о том, к какой сущности относится МЧД. :doc:`Возможные значения <./Enums/PowerOfAttorneyAffiliation>`

:Status:
  :doc:`PowerOfAttorneyStatus` **, чтение** - результат проверки МЧД. Если проверка ещё не завершилась, поле будет :doc:`пустым <Descriptions/Empty_Com_Object>`
