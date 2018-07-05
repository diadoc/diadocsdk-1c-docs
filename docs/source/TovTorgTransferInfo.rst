TovTorgTransferInfo
===================

Сведения о факте передачи (об отпуске груза)

Свойства объекта
----------------


- **OperationInfo** (строка, чтение/запись) - содержание операции

- **TransferDate** (дата, чтение/запись) - дата отгрузки

- **Attachment** (строка, чтение/запись) - приложение, сертификаты и прочее

- **Waybills** (:doc:`коллекция <Collection>` объектов :doc:`Waybill <Waybill>`) - транспортны накладные

- **Employee** (:doc:`Employee <Employee>`) - работник организации продавца

- **OtherIssuer** (:doc:`OtherIssuer <OtherIssuer>`) - иное лицо

- **StructedAdditionalInfos** (:doc:`коллекция <Collection>` объектов :doc:`StructedAditionalInfo <StructedAdditionalInfo>`) - информационные поля документа

Методы объекта
--------------

-  :doc:`AddWaybill <AddWaybill-(TovTorgTransferInfo)>` - добавляет новый элемент в список транспортных накладных

-  :doc:`AddStructedAdditionalInfo <AddStructedAdditionalInfo-(TovTorgTransferInfo)>` - добавляет новый элемент в список дополнительных сведений


.. toctree::
   :name: Auto
   :hidden:

   AddWaybill <AddWaybill-(TovTorgTransferInfo)>
   AddStructedAdditionalInfo <AddStructedAdditionalInfo-(TovTorgTransferInfo)>
