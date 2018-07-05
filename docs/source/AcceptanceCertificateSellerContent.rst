AcceptanceCertificateSellerContent
==================================

Объект предназначен для работы с содержанием формализованного документа "Акт о выполнении работ" в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83259>`_ и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------

- **Type** (строка, чтение) - тип документа (возвращает строку "XmlAcceptanceCertificateContent")

- **Date** (дата, чтение/запись) - дата акта

- **Number** (строка, чтение/запись) - номер акта

- **Title** (строка, чтение/запись) - заголовок акта

- **SignatureDate** (дата, чтение/запись) - дата подписи акта исполнителем

- **Seller** (:doc:`OrganizationInfo <OrganizationInfo>`, чтение) - исполнитель (организация, выполнившая работы либо оказавшая услуги)

- **Items** (:doc:`коллекция <Collection>` объектов :doc:`AcceptanceCertificateItem <AcceptanceCertificateItem>`, чтение) - табличная часть акта выполненных работ

- **Official** (:doc:`Official <Official>`, чтение) - лицо, подписывающее со стороны исполнителя

- **Attorney** (:doc:`Attorney <Attorney>`, чтение) - сведения о доверенности подписывающего со стороны исполнителя

- **Signer** (:doc:`Signer <Signer>`, чтение) - подписант

- **AdditionalInfo** (строка, чтение/запись) - дополнительные сведения


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(AcceptanceCertificateSellerContent)>` - добавляет строку в табличную часть Акта


.. toctree::
   :name: Auto
   :hidden:

   AddItem-(AcceptanceCertificateSellerContent) <AddItem-(AcceptanceCertificateSellerContent)>
   AcceptanceCertificateItem <AcceptanceCertificateItem>
