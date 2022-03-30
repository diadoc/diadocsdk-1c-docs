Torg12BuyerContent
==================

Содержание титула покупателя документа *ТОРГ-12* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859>`_.
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``XmlTorg12BuyerTitle``

:ShipmentReceiptDate:
    **Дата, чтение/запись** - дата получения груза

:Attorney:
    :doc:`Attorney` **, чтение** - сведения о доверенности

:Receiver:
    :doc:`Official` **, чтение** - лицо, получившее груз

:Accepter:
    :doc:`Official` **, чтение** - лицо, принявшее груз

:Signer:
    :doc:`Signer` **, чтение** - подписант

:AdditionalInfo:
    **Строка, чтение/запись** - дополнительные сведения