TransferInfo
============

Сведения о передаче

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:OperationInfo:
    **Строка, чтение/запись** - содержание операции

:OperationType:
    **Строка, чтение/запись** - вид операции

:TransferDate:
    **Дата, чтение/запись** - дата отгрузки

:TransferTextInfo:
    **Строка, чтение/запись** - сведения о транспортировке и грузе

:Carrier:
    :doc:`ExtendedOrganizationInfo` **, чтение** - перевозчик

:Employee:
    :doc:`Employee` **, чтение** - работник организации продавца

:OtherIssuer:
    :doc:`OtherIssuer` **, чтение** - иное лицо

:CreatedThingTransferDate:
    **Дата, чтение/запись** - дата передачи вещи, изготовленной по договору

:CreatedThingInfo:
    **Строка, чтение/запись** - сведения о передаче вещи, изготовленной по договору

:AdditionalInfoId:
    :doc:`AdditionalInfoId` **, чтение** - информационное поле документа

:TransferBases:
    :doc:`Коллекция <Collection>` **объектов** :doc:`TransferBase` **, чтение** - основание отгрузки

:Waybills:
    :doc:`Коллекция <Collection>` **объектов** :doc:`Waybill` **, чтение** - транспортная накладная


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddTransferBase() <TransferInfo.AddTransferBase>`
        * :meth:`AddWaybill() <TransferInfo.AddWaybill>`


.. method:: TransferInfo.AddTransferBase()

    Добавляет :doc:`новый элемент <TransferBase>` в коллекцию *TransferBases* и возвращает его


.. method:: TransferInfo.AddWaybill()

    Добавляет :doc:`новый элемент <Waybill>` в коллекцию *Waybills* и возвращает его