Релиз 5.15.0
============

.. feed-entry::
   :date: 2017-03-15

- Асинхронная отправка извещений о получении конкретного УПД. У объекта документа УПД :doc:`Utd <Utd>` появился метод :doc:`SendReceiptsAsync <SendReceiptsAsync-(Utd)>`

- Метод :doc:`CanSendInvoice <CanSendInvoice>` объекта :doc:`Organization <Organization>` - позволяет узнать, был ли переданный сертификат зарегистрирован в ФНС в качестве сертификата, используемого для подписания электронных счетов-фактур, отправляемых участником ЭДО, которому принадлежит ящик boxId

- В объекте :doc:`Counteragent <Counteragent>` появилось свойство **LastEventTimestampTicks** - метка времени последнего события из истории взаимодействия с данным контрагентом

- В объекте :doc:`UserPermissions <UserPermissions>` появилось свойство **JobTitle** - должность сотрудника

- В объекте базового документа :doc:`Document <Document>` появилось свойство **PackageId** - идентификатор пакета

- Полная поддержка исправительных УПД

- Исправлена работа :doc:`CreateReplySendTask <CreateReplySendTask-(Document)>` для старых типов документов с УПД-содержимым

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_