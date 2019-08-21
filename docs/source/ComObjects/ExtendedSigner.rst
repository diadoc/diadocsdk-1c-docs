ExtendedSigner
==============

Информации о лице, подписавшем документ


.. rubric:: Свойства

:BoxId:
  **Строка, чтение/запись** - идентификатор ящика организации, которую представляет подписант

:CertificateThumbprint:
  **Строка, чтение/запись** - отпечаток сертификата подписанта

:SignerDetails:
  :doc:`ExtendedSignerDetails <ExtendedSignerDetails>` **, чтение** - информация о подписанте


.. note:: Должны быть заполнены либо *BoxId* + *CertificateThumbprint*, либо *SignerDetails*


.. seealso:: :meth:`Organization.CreateSetExtendedSignerDetailsTask`
