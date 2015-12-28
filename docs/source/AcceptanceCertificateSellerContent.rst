AcceptanceCertificateSellerContent
==================================

Объект предназначен для работы с содержанием документов типа «акт о
выполнении работ в формате ФНС» (титул исполнителя) и является производным объектом от :doc:`BaseContent <BaseContent>`.

Свойства объекта
----------------


- **Date** (дата, чтение/запись, обязательно для заполнения ) - дата акта

- **Number** (строка, чтение/запись, строка длиной не более 256 символов ) - номер акта

- **Title** (строка, чтение/запись, обязательно для заполнения. Строка длиной не более 2000 символов ) - заголовок акта

- **SignatureDate** (дата, чтение/запись, --- ) - дата подписи акта исполнителем

- **Seller** (объект :doc:`OrganizationInfo <OrganizationInfo>`, чтение, обязательно для заполнения ) - исполнитель (организация, выполнившая работы либо оказавшая услуги)

- **Items** (:doc:`Коллекция <Collection>` объектов :doc:`AcceptanceCertificateItem <AcceptanceCertificateItem>`, чтение, обязательно для заполнения ) - табличная часть акта выполненных работ

- **Official** (объект :doc:`Official <Official>`, чтение, обязательно для заполнения ) - лицо, подписывающее со стороны исполнителя

- **Attorney** (объект :doc:`Attorney <Attorney>`, чтение, --- ) - сведения о доверенности подписывающего со стороны исполнителя

- **Signer** (объект :doc:`Signer <Signer>`, чтение, обязательно для заполнения ) - подписант

- **AdditionalInfo** (строка, чтение/запись, строка длиной не более 2000 символов ) - дополнительные сведения

- **Type** (строка, чтение, --- ) - тип документа


Методы объекта
--------------


-  :doc:`AddItem <AddItem-(AcceptanceCertificateSellerContent)>` - добавляет строку в табличную часть Акта


.. toctree::
   :name: Auto
   :hidden:

   AddItem-(AcceptanceCertificateSellerContent) <AddItem-(AcceptanceCertificateSellerContent)>
   AcceptanceCertificateItem <AcceptanceCertificateItem>
