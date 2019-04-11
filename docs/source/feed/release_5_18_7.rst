Релиз 5.18.7
============

.. feed-entry::
   :date: 2017-09-05

    - в объект :doc:`PersonalCertificate` добавлено поле **JobTitle** - должность
    - в COM-компоненте добавлена поддержка типа UcdInvoiceCorrection для объекта :doc:`PackageSendTask`

Исправлены ошибки:
    - исключение с описанием: "Unknown attachment type", при создании :doc:`CreateSendTask` для документов в формате 155-го приказа
    - метод :doc:`ValidateContent` теперь работает для документов в формате 155-го приказа

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_