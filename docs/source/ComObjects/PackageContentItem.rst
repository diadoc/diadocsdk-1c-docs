PackageContentItem
==================

Пара *документ-контент*

.. versionadded:: 5.3.0


.. rubric:: Свойства

:Document:
    :doc:`Document` **, чтение** - документ, с которым связан хранимый в паре контент

:Content:
    :doc:`DynamicContent` **или** :doc:`BaseContent` **, чтение** - представление контента.


.. note:: Если :doc:`PackageContentItem <PackageContentItem>` запрашивается из :doc:`ReplySendTask2 <ReplySendTask2>` с типом **AcceptDocument** для двухтитульного документа, то **Content** будет объектом :doc:`DynamicContent <DynamicContent>`.
    В противном случае **Content** будет объектом, производным от :doc:`BaseContent`


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`LoadContentFromFile() <PackageContentItem.LoadContentFromFile>`
        * :meth:`LoadContentFromBase64() <PackageContentItem.LoadContentFromBase64>`


.. method:: PackageContentItem.LoadContentFromFile(FilePath)

    :FilePath: ``строка`` путь до файла контента

    Загружает контент ответа из файла. Этот контент будет подписан


.. method:: PackageContentItem.LoadContentFromBase64(Base64)

    :Base64: ``строка`` base64 представление контента

    Загружает контент ответа из Base64 строки. Этот контент будет подписан