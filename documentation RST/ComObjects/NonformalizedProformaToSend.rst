NonformalizedProformaToSend
===========================

Документ на отправку *Счет на оплату*.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`CustomDocumentToSend`

.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``NonformalizedProforma``

:FileName:
    **Строка, чтение/запись** - имя файла вложения

:DocumentDate:
    **Дата, чтение/запись** - дата документа

:DocumentNumber:
    **Строка, чтение/запись** - номер документа

:Total:
    **Число, чтение/запись** - сумма с учетом НДС

:Vat:
    **Число, чтение/запись** - сумма НДС

:Grounds:
    **Строка, чтение/запись** - основание документа

:Content:
    :doc:`./Descriptions/EmptyVariant` **, чтение** - представление контента