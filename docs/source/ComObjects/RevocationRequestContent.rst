RevocationRequestContent
========================

Метаданные запроса аннулирования документа.
Является производным объектом от :doc:`BaseContent <BaseContent>`

.. versionadded:: 5.2.2

.. rubric:: Свойства

:Signer:
  :doc:`Signer <Signer>` **, чтение** - данные подписанта аннулирования

:Comment:
  **Строка, чтение/запись** - комментарий к аннулированию

:Type:
  **Строка, чтение** - тип контента. Константа ``RevocationRequest``
