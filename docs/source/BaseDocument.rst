BaseDocument
============

Объект предназначен для работы с "любыми типами" документов и является производным объектом от :doc:`Document <Document>`.

Свойства объекта
----------------

Нет.

Методы объекта
--------------

-  :doc:`GetContent <GetContent-(BaseDocument)>` - возвращает объект титула продавца
-  :doc:`GetBuyerContent <GetBuyerContent-(BaseDocument)>` - возвращает объект титула покупателя
-  :doc:`SendReceiptsAsync <SendReceiptsAsync-(BaseDocument)>` - формирует и подписывает документы по регламентному документообороту СЧФ/УПД

.. toctree::
   :name: Auto
   :hidden:

   GetContent <GetContent-(BaseDocument)>
   GetBuyerContent <GetBuyerContent-(BaseDocument)>
   SendReceiptsAsync <SendReceiptsAsync-(BaseDocument)>