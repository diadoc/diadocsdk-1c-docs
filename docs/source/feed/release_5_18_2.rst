Релиз 5.18.2
============

.. feed-entry::
   :date: 2017-07-18

    - Свойство **EncryptedDocumentsAllowed** у объекта :doc:`Organization` -  для организации разрешена отправка зашифрованных документов
    - Теперь файлы подписи получаемые в результате выполнения метода :doc:`SaveAllContent` сохраняются с расширением .sgn


Исправлены ошибки:
    - в результате вызова методов :doc:`SaveAllContent` и :doc:`SaveAllContentAsync` печатная форма скачивалась без расширения
    - в объекте :doc:`Document` получаемом в результате вызова :doc:`SendTask.Send` или :doc:`SendTask.SendAsync` не заполнялось поле OneSDocumentId
    - ошибка при вызове :doc:`CreateReplySendTask("RejectDocument")>` для NonformalizedAcceptanceCertificate, CertificateRegistry, PriceListAgreement, ReconciliationAct, NonformalizedTorg12, Contract, Nonformalized
    - ошибка в COM-компоненте - исключение при чтении свойства **AmendmentRequested**
    - :doc:`SendDraftTask.SendAsync` не создавался объект результата выполнения задачи
    - :doc:`DocumentsTask.GetDocuments` - если в результате поиска не было найдено документов, возвращалась не пустая коллекция, а неопределенное значение
    - при подписи документа дважды запрашивался ПИН закрытого ключа
    - :doc:`SendTask` - допускалось создание объекта для некорректного типа документа

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_