ContractToSend
==============

Неформализованный *Договор* на отправку.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`CustomDocumentToSend`, создаваемый в :doc:`PackageSendTask2`


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
    :doc:`Descriptions/Empty_Com_Object` **, чтение** - представление контента