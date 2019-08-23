DynamicContent
==============

Представление содержания документа

Используется:

    * в :doc:`CustomDocumentToSend.Content <CustomDocumentToSend>`, если тот создан через объект :doc:`PackageSendTask2 <PackageSendTask2>`
    * в :doc:`PackageContentItem.Content <PackageContentItem>`, полученным через объект  :doc:`ReplySendTask2 <ReplySendTask2>` с типом ``AcceptDocument``
    * как результат выполнения метода :meth:`Document.GetDynamicContent`


.. rubric:: Свойства

Не имеет фиксированного набора свойств.
Набор свойств можно получить методом :meth:`DynamicContent.GetPropertyNames` или можно ориентироваться на описание, полученное методами :meth:`Organization.SaveUserDataXSD`, :meth:`Organization.GetBase64UserDataXSD`

Каждое поле объекта является или строкой, или :doc:`коллекцией <Collection>`, или :doc:`DynamicContent'ом <DynamicContent>`


.. rubric:: Методы

+------------------------------------+-------------------------------+
| |DynamicContent-GetPropertyNames|_ | |DynamicContent-HasProperty|_ |
+------------------------------------+-------------------------------+

.. |DynamicContent-GetPropertyNames| replace:: GetPropertyNames()
.. |DynamicContent-HasProperty| replace:: HasProperty()


.. _DynamicContent-GetPropertyNames:
.. method:: DynamicContent.GetPropertyNames()

  Возвращает :doc:`коллекцию <Collection>` строк - имён свойств контента

  .. versionadded:: 5.28.3


.. _DynamicContent-HasProperty:
.. method:: DynamicContent.HasProperty(PropertyName)

  :PropertyName: ``строка`` - имя свойства

  Возвращает булевое значение наличия у объекта свойства с заданным именем

  .. versionadded:: 5.28.3



.. rubric:: Как работать с коллекциями

Если контент выглядит так:

    ``DynamicContent_ВладелецКоллекции.Коллекция``

Тогда для добавления элемента в коллекцию необходимо вызвать

.. code-block:: c#

    // Если коллекция состоит из сложных объектов
    НовыйЭлементКоллекции = DynamicContent_ВладелецКоллекции.AddКоллекция();

    // Если коллекция состоит из строк
    DynamicContent_ВладелецКоллекции.AddКоллекция("Значение");


Имя метода, с помощью которого можно добавить элемент зависит от названия коллекции и формируется как ``"Add" + <название коллекции>``. У коллекций, для которых в XSD не указано имя, используется имя ``items``

.. rubric:: Пример работы с динамическим контентом

.. code-block:: c#

  // Добавление нового элемента в коллекцию строк
  SendTask = Organization.CreatePackageSendTask2();
  DocumentToSend = SendTask.AddDocument("UniversalTransferDocument", "СЧФДОП", "utd820_05_01_01");
  DynamicContent = DocumentToSend.Content;
  Utd820_SellerContent = DynamicContent.UniversalTransferDocument;

  Signers = Utd820_SellerContent.Signers;
  NewSigner = Signers.AddItems();
  // Signers - Владелец коллекции с именем items. Имя будет items потому, что у узла choice нет имени и он повторяющийся
  // Описание в XSD:
  // <xs:element name="Signers">
  //   <xs:complexType>
  //     <xs:choice maxOccurs="unbounded">
  //       <xs:element name="SignerReference" type="SignerReference" />
  //       <xs:element name="SignerDetails" type="ExtendedSignerDetails_SellerTitle" />
  //     </xs:choice>
  //   </xs:complexType>
  // </xs:element>

  InvoiceTable = Utd820_SellerContent.Table;
  NewInvoiceTableItem = InvoiceTable.AddItem();
  // InvoiceTable - Владелец коллекции с именем Item
  // Описание в XSD:
  // <xs:complexType name="InvoiceTable">
  // <xs:sequence>
  //   <xs:element maxOccurs="unbounded" name="Item">

  ItemIdentificationNumbers = NewInvoiceTableItem.ItemIdentificationNumbers;
  NewItemIdentificationNumber = ItemIdentificationNumbers.AddItemIdentificationNumber();
  NewItemIdentificationNumber.AddUnit("Unit1")
  NewItemIdentificationNumber.TransPackageId = "SomeTransPackageId";
  // ItemIdentificationNumbers - Владелец коллекции с именем ItemIdentificationNumber
  // NewItemIdentificationNumber - владелец коллекции строк с именем Unit. В отличие от Signers, узел choice не повторяющийся
  // Описание в XSD:
  // <xs:element minOccurs="0" name="ItemIdentificationNumbers">
  //   <xs:complexType>
  //     <xs:sequence>
  //       <xs:element maxOccurs="**unbounded**" name="ItemIdentificationNumber">
  //         <xs:complexType>
  //           <xs:choice>
  //             <xs:element minOccurs="0" maxOccurs="unbounded" name="Unit" type="string255">
  //             </xs:element>
  //             <xs:element minOccurs="0" maxOccurs="unbounded" name="PackageId" type="string255">
  //             </xs:element>
  //           </xs:choice>
  //           <xs:attribute name="TransPackageId" type="string255" use="optional">
  //           </xs:attribute>
  //         </xs:complexType>
  //       </xs:element>
  //     </xs:sequence>
  //   </xs:complexType>
  // </xs:element>
