SetExtendedSignerDetailsTask
============================

Задача для добавления или обновления данных подписанта в базе Диадок

.. rubric:: Свойства

:IsSeller:
  **Булево, чтение/запись** - признак того, является ли подписант подписантом титула продавца или подписантом титула покупателя

  .. deprecated:: 5.19.0
    Используйте *DocumentTitleType*

:ForCorrection:
  **Булево, чтение/запись** - признак того, является ли подписант подписантом корректировки

  .. deprecated:: 5.19.0
    Используйте *DocumentTitleType*

:ExtendedSignerDetailsToPost:
  :doc:`ExtendedSignerDetailsToPost` **, чтение** - данные подписанта

:DocumentTitleType:
  **Строка, чтение/запись** - тип титула документа. :doc:`Возможные значения <./Enums/SignerTitleType>`


.. rubric:: Методы

+--------------------------------------+
| |SetExtendedSignerDetailsTask-Send|_ |
+--------------------------------------+

.. |SetExtendedSignerDetailsTask-Send| replace:: Send()



.. _SetExtendedSignerDetailsTask-Send:
.. method:: SetExtendedSignerDetailsTask.Send()

  Отправляет данные подписанта на сервер Диадок
