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

+----------------------------+---------------+---------------+
|:func:`.GetRejectionComment`|:func:`.Accept`|:func:`.Reject`|
+----------------------------+---------------+---------------+


.. function:: Contract.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте :func:`Document.GetAnyComment` с типом ``SignatureRejectionComment``


.. function:: Contract.Accept()

  Подписывает документы

  .. deprecated:: 5.27.0
    Используйте :func:`Document.CreateReplySendTask2`


.. function:: Contract.Reject([Comment])

  :Comment: ``строка`` комментарий к отказу подписании

  Отказывает в подписании документа

  .. deprecated:: 5.27.0
    Используйте :func:`Document.CreateReplySendTask2`
