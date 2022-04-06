TovTorgTransferInfo
===================

Сведения о факте передачи (об отпуске груза)

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`

.. rubric:: Свойства

:OperationInfo:
    **Строка, чтение/запись** - содержание операции

:TransferDate:
    **Дата, чтение/запись** - дата отгрузки

:Attachment:
    **Строка, чтение/запись** - приложение, сертификаты и прочее

:Waybills:
    :doc:`Коллекция <Collection>` **объектов** :doc:`Waybill` **, чтение** - транспортны накладные

:Employee:
    :doc:`Employee` **, чтение** - работник организации продавца

:OtherIssuer:
    :doc:`OtherIssuer` **, чтение** - иное лицо

:StructedAdditionalInfos:
    :doc:`Коллекция <Collection>` **объектов** :doc:`StructedAdditionalInfo` **, чтение** - информационные поля документа



.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddWaybill() <TovTorgTransferInfo.AddWaybill>`
        * :meth:`AddStructedAdditionalInfo() <TovTorgTransferInfo.AddStructedAdditionalInfo>`


.. method:: TovTorgTransferInfo.AddWaybill()

  Добавляет :doc:`новый элемент <Waybill>` в коллекцию **Waybills** и возвращает его


.. method:: TovTorgTransferInfo.AddStructedAdditionalInfo()

    Добавляет :doc:`новый элемент <StructedAdditionalInfo>` в коллекцию **StructedAdditionalInfos** и возвращает его