SendDraftTask
=============

Объект предназначен для отправки черновика сообщения.


Свойства
--------

- **Signer** (:doc:`Signer <Signer>`, чтение) - данные подписанта
- **ExtendedSigners** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigners <ExtendedSigners>`, чтение) - данные подписанта для УПД, Торг-12 @551, Акта @552


Методы
------

-  :doc:`SendAsync <SendAsync-(SendDraftTask)>` - инициирует асинхронную операцию отправки черновика по его уникальному идентификатору
-  :doc:`AddExtendedSigner <AddExtendedSigner-(SendDraftTask)>` - добавляет новый элемент в список подписантов исходящего титула продавца УПД с отложенной отправкой.


.. toctree::
   :name: Auto
   :hidden:

    AddExtendedSigner <AddExtendedSigner-(SendDraftTask)>
    SendAsync <SendAsync-(SendDraftTask)>
    ExtendedSigner <ExtendedSigner>
    Signer <Signer>