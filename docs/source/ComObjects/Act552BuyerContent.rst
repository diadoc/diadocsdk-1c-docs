Act552BuyerContent
==================

Cодержание титула покупателя *Акта о выполнении работ* в формате приказа `ММВ-7-10/552@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265283>`_ .
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`

.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificate552BuyerTitle``

:Signers:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - данные подписантов

:DocumentCreator:
  **Строка, чтение/запись** - cоставитель файла информации продавца

:DocumentCreatorBase:
  **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла

:perationType:
  **Строка, чтение/запись** - вид операции

:OperationContent:
  **Строка, чтение/запись** - содержание операции

:AcceptanceDate:
  **Дата, чтение/запись** - дата приемки результатов работ

:CreatedThingAcceptDate:
  **Дата, чтение/запись** - дата получения вещи, изготовленной  по договору подряда

:CreatedThingInfo:
  **Строка, чтение/запись** - сведения о получении

:AdditionalInfoId:
  :doc:`AdditionalInfoId` **, чтение** - информационное поле документа


.. rubric:: Методы

+---------------------------------+
| |Act552BuyerContent-AddSigner|_ |
+---------------------------------+

.. |Act552BuyerContent-AddSigner| replace:: AddSigner()

.. _Act552BuyerContent-AddSigner:
.. method:: Act552BuyerContent.AddSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его
