Torg12BuyerContent
==================

Объект предназначен для работы с содержанием титула покупателя формализованного документа "ТОРГ-12" в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа (возвращает строку "XmlTorg12BuyerTitle")

- **ShipmentReceiptDate** (дата, чтение/запись) - дата получения груза

- **Attorney** (:doc:`Attorney <Attorney>`, чтение) - сведения о доверенности

- **Receiver** (:doc:`Official <Official>`, чтение) - лицо, получившее груз

- **Accepter** (:doc:`Official <Official>`, чтение) - лицо, принявшее груз

- **Signer** (:doc:`Signer <Signer>`, чтение) - подписант

- **AdditionalInfo** (строка, чтение/запись) - дополнительные сведения


Методы отсутствуют
