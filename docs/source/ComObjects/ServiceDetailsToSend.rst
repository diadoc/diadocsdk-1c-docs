ServiceDetailsToSend
====================

Документ на отправку *Детализация*.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
  Используйте :doc:`CustomDocumentToSend`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``ServiceDetails``

:FileName:
  **Строка, чтение/запись** - имя файла вложения

:DocumentDate:
  **Дата, чтение/запись** - дата документа

:DocumentNumber:
  **Строка, чтение/запись** - номер документа

:Content:
  `VARIANT <https://docs.microsoft.com/en-us/windows/win32/winauto/variant-structure>`_ : `VT_EMPTY <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-oaut/3fe7db9f-5803-4dc4-9d14-5425d3f5461f>`_ **, чтение** - представление контента. Всегда пустое
