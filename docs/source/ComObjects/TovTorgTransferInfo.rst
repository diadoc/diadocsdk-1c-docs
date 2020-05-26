TovTorgTransferInfo
===================

Сведения о факте передачи (об отпуске груза)

.. rubric:: Свойства

:OperationInfo:
  **Строка, чтение/запись** - содержание операции

:TransferDate:
  **Дата, чтение/запись** - дата отгрузки

:Attachment:
  **Строка, чтение/запись** - приложение, сертификаты и прочее

:Waybills:
  :doc:`Коллекция <Collection>` **объектов** :doc:`Waybill ` **, чтение** - транспортны накладные

:Employee:
  :doc:`Employee` **, чтение** - работник организации продавца

:OtherIssuer:
  :doc:`OtherIssuer` **, чтение** - иное лицо

:StructedAdditionalInfos:
  :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAditionalInfo` **, чтение** - информационные поля документа



.. rubric:: Методы

+-----------------------------------+--------------------------------------------------+
| |TovTorgTransferInfo-AddWaybill|_ | |TovTorgTransferInfo-AddStructedAdditionalInfo|_ |
+-----------------------------------+--------------------------------------------------+

.. |TovTorgTransferInfo-AddWaybill| replace:: AddWaybill()
.. |TovTorgTransferInfo-AddStructedAdditionalInfo| replace:: AddStructedAdditionalInfo()



.. _TovTorgTransferInfo-AddWaybill:
.. method:: TovTorgTransferInfo.AddWaybill()

  Добавляет :doc:`новый элемент <Waybill>` в коллекцию *Waybills* и возвращает его



.. _TovTorgTransferInfo-AddStructedAdditionalInfo:
.. method:: TovTorgTransferInfo.AddStructedAdditionalInfo()

  Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию *StructedAdditionalInfos* и возвращает его
