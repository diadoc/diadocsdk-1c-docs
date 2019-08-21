Contract
========

Неформализованный *Договор*.
Является производным объектом от :doc:`Document <Document>`


.. rubric:: Свойства

:Price:
  **Строка, чтение** - цена, указанная в договоре

:ContractType:
  **Строка, чтение** - тип договора


.. rubric:: Методы

+---------------------------------+--------------------+--------------------+
| |Contract-GetRejectionComment|_ | |Contract-Accept|_ | |Contract-Reject|_ |
+---------------------------------+--------------------+--------------------+

.. |Contract-GetRejectionComment| replace:: GetRejectionComment()
.. |Contract-Accept| replace:: Accept()
.. |Contract-Reject| replace:: Reject()



.. _Contract-GetRejectionComment:
.. method:: Contract.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``



.. _Contract-Accept:
.. method:: Contract.Accept()

  Подписывает документы

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`



.. _Contract-Reject:
.. method:: Contract.Reject([Comment])

  :Comment: ``строка`` комментарий к отказу подписании

  Отказывает в подписании документа

  .. deprecated:: 5.27.0
    Используйте :meth:`Document.CreateReplySendTask2`
