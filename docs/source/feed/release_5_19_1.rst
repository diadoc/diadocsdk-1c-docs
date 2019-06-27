Релиз 5.19.1
============

.. feed-entry::
   :date: 2017-11-20

- CustomData - коллекция "ключ-значение" для объекта Document:
    
    - свойство Document.CustomData - коллекция объектов CustomDataItem содержащих записи "ключ-значение"

    - метод Document.CreateCustomDataPatchTask - создает объект CustomDataPatchTask, позволяющий редактировать коллекцию Document.CustomData

- В объект Ucd добавлены свойства OriginalInvoiceNumber, OriginalInvoiceDate, OriginalInvoiceRevisionNumber, OriginalInvoiceRevisionDate

- Исправлены ошибки:
    - исправлена ошибка в алгоритме определения КЭП - свойство PersonalCertificate.IsQualifiedElectronicSignature возвращает ложное значение в случае, если сертификат юр. лица и в ОГРН(1.2.643.100.1) нет нолей
    - теперь кидается исключение в случае если задано неверное значение в свойстве AcquireCounteragentTask.CounteragentBoxId и вызвана отправка методом AcquireCounteragentTask.Send или AcquireCounteragentTask.SendAsync, ранее это приводило к неверному обращению к памяти
    - COM-компонента: при попытке получения содержимого документов в формате 551 и 552-го приказа методами GetContent, GetBuyerContent возвращался неверный контент



`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_