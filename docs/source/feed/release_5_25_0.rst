Релиз 5.25.0
============

.. feed-entry::
   :date: 2018-11-23

- Добавлена поддержка ставки НДС "20/120"
- Добавлен метод удаления черновика Organization.RecycleDraft
- Исправлены ошибки:
    - при выполнение ответного действия "AcceptDocument" для документа (Document.CreateReplySendTask): если в структуре документа Диадок АПИ у титула отправителя есть дочерние элементы типа Attachment это приводило к тому, что ReplySendTask.Content возвращал объект типа AcceptanceContent для любых типов документов
    - при вызове метода OutDocumentSignTask.Send или OutDocumentSignTask.SendAsync в Диадок АПИ не отправлялись данные подписанта типа ExtendedSigner
    - исправлена совместимость с Windows XP
    - При получении некоторых документов возникала ошибка "vector<T> too long"


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_