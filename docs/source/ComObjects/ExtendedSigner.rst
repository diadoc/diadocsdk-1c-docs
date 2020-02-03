ExtendedSigner
==============

Информации о лице, подписавшем документ

.. deprecated:: 5.27.0
  Используется только в "старых" контентах документов, производных от :doc:`BaseContent`.
  Внутри :doc:`DynamicContent`  поле `ExtendedSigner` имеет тип :doc:`DynamicContent`


.. rubric:: Свойства

:BoxId:
  **Строка, чтение/запись** - идентификатор ящика организации, которую представляет подписант

:CertificateThumbprint:
  **Строка, чтение/запись** - отпечаток сертификата подписанта

:SignerDetails:
  :doc:`ExtendedSignerDetails <ExtendedSignerDetails>` **, чтение** - информация о подписанте


.. note:: Должны быть заполнены либо *BoxId* + *CertificateThumbprint*, либо *SignerDetails*


.. seealso:: :meth:`Organization.CreateSetExtendedSignerDetailsTask`
