PowerOfAttorneyToAttach
=======================

Информация об МЧД, которая будет использоваться в одной Task'е

.. versionadded:: 5.37.0


:PowerOfAttorney:
  :doc:`PowerOfAttorneyInfo` **, чтение/запись** - реквизиты МЧД. Может быть :doc:`пустым <Descriptions/Empty_Com_Object>`.
  Если задано, то **UseDefault** присваивается ``FALSE``

:UseDefault:
  **Булево, чтение/запись** - использовать МЧД по-умолчанию.
  Если устанавливается занчение ``TRUE``, то **PowerOfAttorney** становится :doc:`пустым <Descriptions/Empty_Com_Object>`
