ReconciliationActToSend
=======================

Документ на отправку *Акт сверки*.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`CustomDocumentToSend`, создаваемый в :doc:`PackageSendTask2`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``ReconciliationAct``

:FileName:
    **Строка, чтение/запись** - имя файла вложения

:DocumentDate:
    **Дата, чтение/запись** - дата документа

:DocumentNumber:
    **Строка, чтение/запись** - номер документа

:Content:
    :doc:`Descriptions/Empty_Com_Object` **, чтение** - представление контента. Всегда пустое