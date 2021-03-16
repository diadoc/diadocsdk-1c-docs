OutDocumentSignTask
===================

Задания на подписание и отправку исходящего документа с отложенной отправкой

.. versionadded:: 5.6.0

.. rubric:: Свойства

:Signer:
  :doc:`Signer` **, чтение/запись** - данные подписанта документа

:Content:
  `VARIANT <https://docs.microsoft.com/en-us/windows/win32/winauto/variant-structure>`_ : `VT_EMPTY <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-oaut/3fe7db9f-5803-4dc4-9d14-5425d3f5461f>`_ **, чтение** - содержимое запроса



.. rubric:: Методы

+----------------------------------------------+----------------------------------+
| |OutDocumentSignTask-AddExtendedSigner|_     | |OutDocumentSignTask-Send|_      |
+----------------------------------------------+----------------------------------+
| |OutDocumentSignTask-AddEncryptCertificate|_ | |OutDocumentSignTask-SendAsync|_ |
+----------------------------------------------+----------------------------------+

.. |OutDocumentSignTask-AddExtendedSigner| replace:: AddExtendedSigner()
.. |OutDocumentSignTask-AddEncryptCertificate| replace:: AddEncryptCertificate()
.. |OutDocumentSignTask-Send| replace:: Send()
.. |OutDocumentSignTask-SendAsync| replace:: SendAsync()


.. _OutDocumentSignTask-AddExtendedSigner:
.. method:: OutDocumentSignTask.AddExtendedSigner()

  Добавляет :doc:`подписанта <ExtendedSigner>` для документов УПД, УКД, Торг12 @551, Акт @552 и возвращает его в качестве результата



.. _OutDocumentSignTask-AddEncryptCertificate:
.. method:: OutDocumentSignTask.AddEncryptCertificate(Certificate)

  :Certificate: :doc:`PersonalCertificate` сертификат КЭП

  Добавляет :doc:`сертификат <PersonalCertificate>` для шифрования контента



.. _OutDocumentSignTask-Send:
.. method:: OutDocumentSignTask.Send()

  Подписывает и отправляет исходящий документ с отложенной отправкой



.. _OutDocumentSignTask-SendAsync:
.. method:: OutDocumentSignTask.SendAsync()

  Подписывает и отправляет исходящий документ с отложенной отправкой. Возвращает :doc:`AsyncResult` с булевым типом результата
