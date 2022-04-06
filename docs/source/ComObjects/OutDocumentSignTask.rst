OutDocumentSignTask
===================

Задания на подписание и отправку исходящего документа с отложенной отправкой

.. versionadded:: 5.6.0

.. rubric:: Свойства

:Signer:
    :doc:`Signer` **, чтение/запись** - данные подписанта документа

:Content:
    :doc:`Descriptions/EmptyVariant` **, чтение** - содержимое запроса

:PowerOfAttorneyToAttach:
    :doc:`PowerOfAttorneyToAttach` **, чтение** - данные об МЧД, которая будет использоваться при подписании

    .. versionadded:: 5.37.0



.. rubric:: Методы


.. method:: OutDocumentSignTask.AddExtendedSigner()

    Добавляет :doc:`подписанта <ExtendedSigner>` для документов УПД, УКД, Торг12 @551, Акт @552 и возвращает его в качестве результата


.. method:: OutDocumentSignTask.AddEncryptCertificate(Certificate)

    :Certificate: :doc:`PersonalCertificate` сертификат КЭП

    Добавляет :doc:`сертификат <PersonalCertificate>` для шифрования контента


.. method:: OutDocumentSignTask.Send()

    Подписывает и отправляет исходящий документ с отложенной отправкой


.. method:: OutDocumentSignTask.SendAsync()

    Подписывает и отправляет исходящий документ с отложенной отправкой. Возвращает :doc:`AsyncResult` с булевым типом результата