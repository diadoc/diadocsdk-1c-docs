ContractToSend
==============

Неформализованный *Договор* на отправку.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
  Используйте :doc:`CustomDocumentToSend`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``Contract``

:FileName:
  **Строка, чтение/запись** - имя файла вложения

:DocumentDate:
  **Дата, чтение/запись** - дата документа

:DocumentNumber:
  **Строка, чтение/запись** - номер документа

:Price:
  **Строка, чтение/запись** - сумма договора

  .. versionadded:: 5.22.2

:ContractType:
  **Строка, чтение/запись** - тип договора

:Content:
  `VARIANT <https://docs.microsoft.com/en-us/windows/win32/winauto/variant-structure>`_ : `VT_EMPTY <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-oaut/3fe7db9f-5803-4dc4-9d14-5425d3f5461f>`_ **, чтение** - представление контента. Всегда пустое
