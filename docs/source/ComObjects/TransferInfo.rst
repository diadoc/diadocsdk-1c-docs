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

+---------------------------------+----------------------------+
| |TransferInfo-AddTransferBase|_ | |TransferInfo-AddWaybill|_ |
+---------------------------------+----------------------------+

.. |TransferInfo-AddTransferBase| replace:: AddTransferBase()
.. |TransferInfo-AddWaybill| replace:: AddWaybill()



.. _TransferInfo-AddTransferBase:
.. method:: TransferInfo.AddTransferBase()

  Добавляет :doc:`новый элемент <TransferBase>` в коллекцию *TransferBases* и возвращает его



.. _TransferInfo-AddWaybill:
.. method:: TransferInfo.AddWaybill()

  Добавляет :doc:`новый элемент <Waybill>` в коллекцию *Waybills* и возвращает его
