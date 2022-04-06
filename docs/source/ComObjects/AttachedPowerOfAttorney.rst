AttachedPowerOfAttorney
=======================

Представления данных об МЧД, прикреплённой к какой-либо из сущностей внутри документа

.. versionadded:: 5.37.0


.. rubric:: Свойства

:PowerOfAttorney:
    :doc:`PowerOfAttorney` **, чтение** - реквизиты МЧД

:Date:
    **Дата, чтение** - дата и время в локальном часовом поясе появления МЧД в документе

:Affiliation:
    **Строка, чтение** - информация о том, к какой сущности относится МЧД. :doc:`Возможные значения <./Enums/PowerOfAttorneyAffiliation>`

:Status:
    :doc:`PowerOfAttorneyStatus` **, чтение** - результат проверки МЧД. Если проверка ещё не завершилась, поле будет содержать :doc:`./Descriptions/EmptyVariant`

:SignatureType:
    **Строка, чтение** - тип подписи, к которой относится МЧД. :doc:`Возможные значения <./Enums/SignatureType>`