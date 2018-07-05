SendDraftTask
=============

Объект предназначен для отправки черновика сообщения.

Свойства
--------

- **Signer** (:doc:`Signer <Signer>`, чтение) - данные подписанта

Методы
------

-  :doc:`AddExtendedSigner <AddExtendedSigner-(SendDraftTask)>` - добавляет новый элемент в список подписантов исходящего титула продавца УПД с отложенной отправкой.

-  :doc:`SendAsync <SendAsync-(SendDraftTask)>` - инициирует асинхронную операцию отправки черновика по его уникальному идентификатору

.. toctree::
   :name: Auto
   :hidden:

    AddExtendedSigner <AddExtendedSigner-(SendDraftTask)>
    SendAsync <SendAsync-(SendDraftTask)>