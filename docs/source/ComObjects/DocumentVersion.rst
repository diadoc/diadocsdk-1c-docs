DocumentVersion
===============

Описание версий документа


.. rubric:: Свойства

:Version:
  **Строка, чтение** - строковой идентификатор версии, уникальный в рамках функции документа

:SupportsContentPatching:
  **Булево, чтение** - поддерживается патчинг

:SupportsEncrypting:
  **Булево, чтение** - поддерживается отправка зашифрованных документов

:Titles:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentTitle <DocumentTitle>` **, чтение** - описания титулов документа

:IsActual:
  **Булево, чтение** - версия актуальна

:Workflows:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentWorkflow <DocumentWorkflow>` **, чтение** - виды документооборота
