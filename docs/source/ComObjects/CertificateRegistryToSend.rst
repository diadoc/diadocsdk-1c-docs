CertificateRegistryToSend
=========================

*Реестр сертификатов*  на отправку.

Наследует интерфейс :doc:`DocumentToSend`

.. versionadded:: 5.5.0

.. deprecated:: 5.27.0
    Используйте :doc:`CustomDocumentToSend`, создаваемый в :doc:`PackageSendTask2`


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``CertificateRegistry``

:FileName:
    **Строка, чтение/запись** - имя файла вложения

:DocumentDate:
    **Дата, чтение/запись** - дата документа

:DocumentNumber:
  **Строка, чтение/запись** - номер документа

:Content:
    :doc:`./Descriptions/EmptyVariant` **, чтение** - представление контента