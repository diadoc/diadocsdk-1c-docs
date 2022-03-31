EventContent
============

`Содержание факта хозяйственной жизни - сведения о факте согласования <https://normativ.kontur.ru/document?moduleId=1&documentId=273231&rangeId=230530>`_


.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`

.. rubric:: Свойства

:CostChangeInfo:
    **Строка, чтение/запись** - иные сведения об изменении стоимости

:TransferDocDetails:
    **Строка, чтение/запись** - реквизиты передаточных документов, к которым относится корректировка

:OperationContent:
    **Строка, чтение/запись** - содержание операции

:NotificationDate:
    **Дата, чтение/запись** - дата направления на согласование

:CorrectionBases:
    :doc:`Коллекция <Collection>` **объектов** :doc:`CorrectionBase` **, чтение** - основание корректировки


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddCorrectionBase() <EventContent.AddCorrectionBase>`


.. method:: ﻿EventContent.AddCorrectionBase()

    Добавляет :doc:`новый элемент <CorrectionBase>` в коллекцию *CorrectionBases* и возвращает его