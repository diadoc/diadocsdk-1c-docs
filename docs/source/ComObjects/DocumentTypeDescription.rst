DocumentTypeDescription
=======================

Описание типа документа


.. rubric:: Свойства

:Name:
  **Строка, чтение** - уникальный строковой идентификатор типа

:Title:
  **Строка, чтение** - заголовок типа

:SupportedDocflows:
  :doc:`Коллекция <Collection>` **строк, чтение** - поддерживаемые типы документооборота. :doc:`Возможные значения <Enums/Docflow>`

:RequiresFnsRegistration:
  **Булево, чтение** - для работы требуется заявление участника ЭДО

:Functions:
  :doc:`Коллекция <Collection>` **объектов** :doc:`DocumentFunction <DocumentFunction>` **, чтение** - описания функций документа
