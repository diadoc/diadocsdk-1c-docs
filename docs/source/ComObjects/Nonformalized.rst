Nonformalized
=============

Документам *Неформализованный*.
Является производным объектом от :doc:`Document`


.. rubric:: Свойства

:Status:
  **Строка, чтение** - статус документа. :doc:`Воможные значения <./Enums/NonfomalizedDocumentStatus>`


.. rubric:: Методы

+--------------------------------------+
| |Nonformalized-GetRejectionComment|_ |
+--------------------------------------+

.. |Nonformalized-GetRejectionComment| replace:: GetRejectionComment()



.. _Nonformalized-GetRejectionComment:
.. method:: Nonformalized.GetRejectionComment()

  Возвращает комментарий к отказу в подписании

  .. deprecated:: 5.20.3
    Используйте Используйте :meth:`Document.GetAnyComment` с типом ``SignatureRejectionComment``
