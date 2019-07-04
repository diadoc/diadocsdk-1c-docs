OutDocumentSignTask
===================

Объект предназначен для подписания и отправки исходящего документа с отложенной отправкой.

Свойства
--------

- **Signer** (:doc:`Signer <Signer>`, чтение/запись) - данные подписанта документа. Используется для всех типов документов, кроме УПД. В случае, если производится подписание УПД, этот параметр игнорируется, вместо него используются подписанты, добавленные с помощью метода **AddExtendedSigner**.

- **Content** (:doc:`OutDocumentSignTaskContent <OutDocumentSignTaskContent>`, чтение/запись) - содержимое запроса

Методы
------

-  :doc:`AddExtendedSigner <AddExtendedSigner>` - добавляет подписант документа. Используется только с случае подписания УПД. В случае подписания других документов подписанты, добавленные с помощью этого метода, игнорируются, а в качестве подписанта используется подписант, указанный в поле **Signer**.

-  :doc:`Send <Send-(OutDocumentSignTask)>` - подписывает и отправляет исходящий документ с отложенной отправкой

-  :doc:`SendAsync <SendAsync-(OutDocumentSignTask)>` - инициирует асинхронное подписание и отправку исходящего 
   документа с отложенной отправкой

.. toctree::
   :name: Auto
   :hidden:

   AddExtendedSigner <AddExtendedSigner>
   Send <Send-(OutDocumentSignTask)>
   SendAsync <SendAsync-(OutDocumentSignTask)>
