Act552WorkItem
===============

Сведения о произведенной работе для *Акта о выполнении работ* в формате приказа `ММВ-7-10/552@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265283>`_

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`

.. rubric:: Свойства

:Name:
    **Строка, чтение/запись** - наименование

:Description:
    **Строка, чтение/запись** - описание работы

:UnitCode:
    **Строка, чтение/запись** - код единицы измерения

:UnitName:
    **Строка, чтение/запись** - наименование единицы измерения

:Price:
    **Число, чтение/запись** - цена

:Quantity:
    **Число, чтение/запись** - количество

:SubtotalWithVatExcluded:
    **Число, чтение/запись** - сумма без учета НДС

:Vat:
    **Число, чтение/запись** - сумма НДС

:Subtotal:
    **Число, чтение/запись** - сумма с учетом НДС

:StructedAdditionalInfos:
    :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение** - информационное поле сведений о работе (услуге)

:TaxRate:
    **Строка, чтение/запись** - ставка налога. :doc:`Возможные значения <./Enums/TaxRate>`

:ItemAccountDebit:
    **Строка, чтение/запись** - корреспондирующие счета: дебет

:ItemAccountCredit:
    **Строка, чтение/запись** - корреспондирующие счета: кредит


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddStructedAdditionalInfo() <Act552WorkItem.AddStructedAdditionalInfo>`

.. method:: Act552WorkItem.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию **StructedAdditionalInfos** и возвращает его
