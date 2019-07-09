DocumentTypeDescription
=======================

Описание типа документа


.. rubric:: Свойства

:Name:
  **Строка, чтение** - уникальный строковой идентификатор типа

:Title:
  **Строка, чтение** - заголовок типа

:SupportedDocflows:
  :doc:`Коллекция <Collection>` **строк, чтение** - поддерживаемые типы документооборота. |DocumentTypeDescription-SupportedDocflows|_

:RequiresFnsRegistration:
  **Булево, чтение** - для работы требуется заявление участника ЭДО

:Functions:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentFunction <DocumentFunction>` **, чтение** - описания функций документа



.. rubric:: Дополнительная информация

.. |DocumentTypeDescription-SupportedDocflows| replace:: Возможные значения

.. _DocumentTypeDescription-SupportedDocflows:

============================ ==========================
Значение *SupportedDocflows* Описание
============================ ==========================
External                     внешний документооборот
Internal                     внутренний документооборот
============================ ==========================
