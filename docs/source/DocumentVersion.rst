DocumentVersion
================

Описывает версию документа.

Свойства объекта
----------------

- **Version** (строка, чтение) - строковой идентификатор версии, уникальный в рамках функции документа

- **SupportsContentPatching** (булево, чтение) - поддерживается патчинг

- **SupportsEncrypting** (булево, чтение) - поддерживается отправка зашифрованных документов    

- **Titles** (коллекция :doc:`Collection <Collection>` объектов :doc:`DocumentTitle <DocumentTitle>`) - описания титулов документа

- **IsActual** (булево, чтение) - версия актуальна

- **Workflows** (коллекция :doc:`Collection <Collection>` объектов :doc:`DocumentWorkflow <DocumentWorkflow>`) - виды документооборота

Методы отсутствуют


.. toctree::
   :name: Auto
   :hidden:

   DocumentTitle <DocumentTitle>
   DocumentWorkflow <DocumentWorkflow>
