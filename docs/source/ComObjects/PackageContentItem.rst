PackageContentItem
==================

Пара *документ-контент*

.. versionadded:: 5.3.0



.. rubric:: Свойства

:Document:
  :doc:`Document <Document>` **, чтение** - документ, с которым связан хранимый в паре контент

:Content:
  :doc:`DynamicContent <DynamicContent>` **или** :doc:`BaseContent <BaseContent>` **, чтение** - представление контента.


.. note:: Если :doc:`PackageContentItem <PackageContentItem>` запрашивается из :doc:`ReplySendTask2 <ReplySendTask2>` с типом **AcceptDocument** для двухтитульного документа, то **Content** будет объектом :doc:`DynamicContent <DynamicContent>`.
  В противном случае **Content** будет объектом, производным от :doc:`BaseContent <BaseContent>`



.. rubric:: Методы

+-------------------------------------------+---------------------------------------------+
| |PackageContentItem-LoadContentFromFile|_ | |PackageContentItem-LoadContentFromBase64|_ |
+-------------------------------------------+---------------------------------------------+

.. |PackageContentItem-LoadContentFromFile| replace:: LoadContentFromFile()
.. |PackageContentItem-LoadContentFromBase64| replace:: LoadContentFromBase64()



.. _PackageContentItem-LoadContentFromFile:
.. method:: PackageContentItem.LoadContentFromFile(FilePath)

  :FilePath: ``строка`` путь до файла контента

  Загружает контент ответа из файла. Этот контент будет подписан



.. _PackageContentItem-LoadContentFromBase64:
.. method:: PackageContentItem.LoadContentFromBase64(Base64)

  :Base64: ``строка`` base64 представление контента

  Загружает контент ответа из Base64 строки. Этот контент будет подписан



.. rubric:: Дополнительная информация

.. |PackageContentItem-ContentType| replace:: Возможные типы BaseContent'а
.. _PackageContentItem-ContentType:

============================================================================ ====================================================================================================
Тип *Content*                                                                Описание
============================================================================ ====================================================================================================
:doc:`AcceptanceContent <AcceptanceContent>`                                 Подписание однотитульного документа или запроса аннулирования
:doc:`FormalizedRejectionContent <FormalizedRejectionContent>`               Отказ от подписания документа или запроса аннулирования
:doc:`CorrectionRequestContent <CorrectionRequestContent>`                   Запрос корректировки документа
============================================================================ ====================================================================================================
