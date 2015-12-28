PackageContentItem
==================

Элемент объекта :doc:`PackageContent <PackageContent>`, хранящий в себе пару "документ-контент".

Свойства объекта
----------------


- **Document** (объект :doc:`Document <Document>`, чтение ) - документ, с которым связан хранимый в паре контент

- **Content** (объект :doc:`BaseContent <BaseContent>`, чтение) - контент. Может быть одним из следующих объектов:

   -  :doc:`Torg12BuyerContent <Torg12BuyerContent>` - титул покупателя для действия типа "AcceptDocument" документа «ТОРГ-12 в формате ФНС»

   -  :doc:`AcceptanceCertificateBuyerContent <AcceptanceCertificateBuyerContent>` - титул покупателя для действия типа "AcceptDocument" 
      документа «акт о выполнении работ в формате ФНС»

   -  :doc:`AcceptanceContent <AcceptanceContent>` - для действия типа "AcceptDocument" других документов

   -  :doc:`RejectionContent <RejectionContent>` - для действия типа "RejectDocument", применяемого к неформализованному документу

   -  :doc:`FormalizedRejectionContent <FormalizedRejectionContent>` - для действия типа "RejectDocument", применяемого 
      к формализованному документу


Методы отсутствуют
