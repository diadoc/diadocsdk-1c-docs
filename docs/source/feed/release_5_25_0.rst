Релиз 5.25.0
============

.. feed-entry::
   :date: 2018-11-23

- Добавлена поддержка ставки НДС "20/120"
- Добавлен метод удаления черновика :doc:`Organization.RecycleDraft <RecycleDraft>`
- Исправлены ошибки:
    - при выполнение ответного действия "AcceptDocument" для документа (:doc:`Document.CreateReplySendTask <CreateReplySendTask-(Document)>`): если в структуре документа Диадок АПИ у титула отправителя есть дочерние элементы типа Attachment это приводило к тому, что :doc:`ReplySendTask.Content <ReplySendTask>` возвращал объект типа :doc:`AcceptanceContent <AcceptanceContent>` для любых типов документов
    - при вызове метода :doc:`OutDocumentSignTask.Send <OutDocumentSignTask>` или :doc:`OutDocumentSignTask.SendAsync <OutDocumentSignTask>` в Диадок АПИ не отправлялись данные подписанта типа :doc:`ExtendedSigner <ExtendedSigner>`
    - исправлена совместимость с Windows XP


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_