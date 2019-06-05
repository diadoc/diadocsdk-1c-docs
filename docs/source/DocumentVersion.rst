DocumentVersion
===============

Объект, описывающий версию документа


Свойства объекта
----------------

    - **Version** (строка, чтение) - строковой идентификатор версии, уникальный в рамках функции документа
    - **SupportsContentPatching** (булево, чтение) - поддерживается патчинг
    - **SupportsEncrypting** (булево, чтение) - поддерживается отправка зашифрованных документов
    - **Titles** (:doc:`коллекция <Collection>` объектов :doc:`DocumentTitle <DocumentTitle>`) - описания титулов документа
    - **IsActual** (булево, чтение) - версия актуальна
    - **Workflows** (:doc:`коллекция <Collection>` объектов :doc:`DocumentWorkflow <DocumentWorkflow>`) - виды документооборота

Методы
------

Отсутствуют


.. toctree::
   :name: Auto
   :hidden:

   DocumentTitle <DocumentTitle>
   DocumentWorkflow <DocumentWorkflow>
