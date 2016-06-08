OutDocumentSignTask
===================

Объект предназначен для подписания и отправки исходящего документа с отложенной отправкой.

Свойства
--------

- **Signer** (объект :doc:`Signer <Signer>`, чтение/запись) - данные подписанта документа

- **Content** (объект :doc:`OutDocumentSignTaskContent <OutDocumentSignTaskContent>`, чтение/запись) - содержимое запроса

Методы
------

-  :doc:`Send <Send-(OutDocumentSignTask)>` - подписывает и отправляет исходящий документ с отложенной отправкой

-  :doc:`SendAsync <SendAsync-(OutDocumentSignTask)>` - инициирует асинхронное подписание и отправку исходящего 
   документа с отложенной отправкой

.. toctree::
   :name: Auto
   :hidden:

   Send <Send-(OutDocumentSignTask)>
   SendAsync <SendAsync-(OutDocumentSignTask)>
