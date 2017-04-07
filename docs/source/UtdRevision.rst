UtdRevision
===========

Объект предназначен для работы с исправлением универсального передаточного документа и является производным объектом от :doc:`Document <Document>`.


Свойства объекта
----------------

- **Function** (строка, чтение) - функция универсального передаточного документа

- **Grounds** (строка, чтение) - основание документа

- **Currency** (число, чтение) - код валюты

- **Total** (число, чтение) - cумма по документу

- **Vat** (число, чтение) - cумма НДС по документу

- **ConfirmationDate** (дата и время, чтение) - дата и время подтверждения оператора передачи документа

- **OriginalDocumentDate** (дата, чтение) - дата первоначального документа

- **OriginalDocumentNumber** (строка, чтение) - номер первоначального документа


Значения свойства **Function**

- СЧФ
- ДОП
- СЧФДОП


Методы объекта
--------------

-  :doc:`GetContent <GetContent-(UtdRevision)>` - возвращает объект титула продавца УПД
-  :doc:`GetBuyerContent <GetBuyerContent-(UtdRevision)>` - возвращает объект титула покупателя УПД
-  :doc:`SendReceiptsAsync <SendReceiptsAsync-(UtdRevision)>` - формирует и подписывает документы по регламентному документообороту УПД

.. toctree::
   :name: Auto
   :hidden:

   GetContent <GetContent-(UtdRevision)>
   GetBuyerContent <GetBuyerContent-(UtdRevision)>