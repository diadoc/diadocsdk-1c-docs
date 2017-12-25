DocumentTypeDescription
=======================

Описывает тип документов.

Свойства объекта
----------------

- **Name** (строка, чтение) - уникальный строковой идентификатор типа

- **Title** (строка, чтение) - заголовок типа

- **SupportedDocflows** (коллекция :doc:`Collection <Collection>` строк) - поддерживаемые типы документооборота

- **RequiresFnsRegistration** (булево, чтение) - для работы требуется заявление участника ЭДО

- **Functions** (коллекция :doc:`Collection <Collection>` объектов типа :doc:`DocumentFunction <DocumentFunction>`) - описания функций документа

Элементы коллекции **SupportedDocflows** могут принимать значения:

- External - внешний документооборот

- Internal - внутренний документооборот

Методы отсутствуют

.. toctree::
   :name: Auto
   :hidden:

   DocumentFunction <DocumentFunction>
