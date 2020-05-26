TovTorgBuyerContent
====================

Содержание титула покупателя документа *ТОРГ-12* в формате приказа `ММВ-7-10/551@ <https://normativ.kontur.ru/document?moduleId=1&documentId=265102>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``TovTorgBuyerTitle``

:DocumentCreator:
  **Строка, чтение/запись** - составитель файла обмена (информации покупателя)

:DocumentCreatorBase:
  **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла обмена

:OperationCode:
  **Строка, чтение/запись** - вид операции

:OperationContent:
  **Строка, чтение/запись** - содержание операции

:AcceptanceDate:
  **Дата, чтение/запись** - дата принятия товаров (результатов выполненных работ) или имущественных прав (подтверждения факта оказания услуг)

:Employee:
  :doc:`Employee` **, чтение** - работник организации покупателя

:OtherIssuer:
  :doc:`OtherIssuer` **, чтение** - иное лицо

:AdditionalInfo:
  :doc:`AdditionalInfoId` **, чтение** - информационное поле документа

:Signers:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - подписанты документа


.. rubric:: Методы

+----------------------------------+
| |TovTorgBuyerContent-AddSigner|_ |
+----------------------------------+

.. |TovTorgBuyerContent-AddSigner| replace:: AddSigner()



.. _TovTorgBuyerContent-AddSigner:
.. method:: TovTorgBuyerContent.AddSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его
