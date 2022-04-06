PowerOfAttorneyToAttach
=======================

Информация об МЧД, которая будет использоваться в одной Task'е

.. versionadded:: 5.37.0


.. rubric:: Свойства

:PowerOfAttorney:
    :doc:`PowerOfAttorney` **, чтение/запись** - реквизиты МЧД. Может быть :doc:`пустым <Descriptions/EmptyVariant>`.
    Если задано, то **UseDefault** присваивается ``False``

:UseDefault:
    **Булево, чтение/запись** - использовать МЧД по-умолчанию.
    Если устанавливается занчение ``True``, то **PowerOfAttorney** становится :doc:`пустым <Descriptions/EmptyVariant>`


Если поле **PowerOfAttorney** :doc:`пустое <./Descriptions/EmptyVariant>` и ``UseDefault == False``, то МЧД использоваться не будет