UtdBuyerContent
================

Содержание титула покупателя *Универсального передаточного документа* в формате приказа `ММВ-7-15/155@ <https://normativ.kontur.ru/document?moduleId=1&documentId=271958>`_
или *универсального корректировочного документа* в формате приказа `ММВ-7-15/189@ <https://normativ.kontur.ru/document?moduleId=1&documentId=273231>`_.
Является производным объектом от :doc:`BaseContent`


.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``UniversalTransferDocumentBuyerTitle``

:Creator:
  **Строка, чтение/запись** - составитель файла обмена счета-фактуры (информации покупателя)

:CreatorBase:
  **Строка, чтение/запись** - основание, по которому экономический субъект является составителем файла обмена счета-фактуры

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

:AdditionalInfoId:
  :doc:`AdditionalInfoId` **, чтение** - информационное поле документа

:Signers:
  :doc:`Коллекция <Collection>` **объектов** :doc:`ExtendedSigner` **, чтение** - подписанты документа


.. rubric:: Методы

.. method:: UtdBuyerContent.AddSigner()

  Добавляет :doc:`новый элемент <ExtendedSigner>` в коллекцию *Signers* и возвращает его
