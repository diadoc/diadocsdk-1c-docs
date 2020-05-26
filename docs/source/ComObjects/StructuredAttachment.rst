StructuredAttachment
====================

Информация о структурированных данных в отправляемом сообщении, описывающий тот или иной документ, который представлен в виде печатной формы


.. rubric:: Свойства

:Document:
  :doc:`Document` **, чтение** - документ, к которому приложены структурированные данные

:FileName:
  **Строка, чтение** - имя файла со структурированными данными



.. rubric:: Методы

+-------------------------------------+
| |StructuredAttachment-SaveContent|_ |
+-------------------------------------+

.. |StructuredAttachment-SaveContent| replace:: SaveContent()



.. _StructuredAttachment-SaveContent:
.. method:: StructuredAttachment.SaveContent(DirectoryPath)

  :DirectoryPath: ``строка`` путь до директории

  Сохраняет структурированные данные в указанную директорию
