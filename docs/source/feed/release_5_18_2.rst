Релиз 5.18.2
============

.. feed-entry::
   :date: 2017-07-18

- Свойство **EncryptedDocumentsAllowed** у объекта Organization -  для организации разрешена отправка зашифрованных документов
- Теперь файлы подписи получаемые в результате выполнения метода SaveAllContent сохраняются с расширением .sgn


Исправлены ошибки:
    - в результате вызова методов SaveAllContent и SaveAllContentAsync печатная форма скачивалась без расширения
    - в объекте Document получаемом в результате вызова SendTask.Send или SendTask.SendAsync не заполнялось поле OneSDocumentId
    - ошибка при вызове CreateReplySendTask("RejectDocument") для NonformalizedAcceptanceCertificate, CertificateRegistry, PriceListAgreement, ReconciliationAct, NonformalizedTorg12, Contract, Nonformalized
    - ошибка в COM-компоненте - исключение при чтении свойства **AmendmentRequested**
    - SendDraftTask.SendAsync не создавался объект результата выполнения задачи
    - DocumentsTask.GetDocuments - если в результате поиска не было найдено документов, возвращалась не пустая коллекция, а неопределенное значение
    - при подписи документа дважды запрашивался ПИН закрытого ключа
    - SendTask - допускалось создание объекта для некорректного типа документа

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_
