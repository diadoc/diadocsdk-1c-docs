DynamicContent
==============

Представление контента документа

Используется:

    * в :doc:`CustomDocumentToSend.Content <CustomDocumentToSend>`, если тот создан через объект :doc:`PackageSendTask2`
    * в :doc:`PackageContentItem.Content <PackageContentItem>`, полученным через объект  :doc:`ReplySendTask2` с типом ``AcceptDocument``
    * как результат выполнения метода :meth:`Document.GetDynamicContent`



.. rubric:: Свойства

Не имеет фиксированного набора свойств.
Набор полей можно понять или из XSD, получаемой методами :meth:`Organization.SaveUserDataXSD`, :meth:`Organization.GetBase64UserDataXSD`, или, используя объект :doc:`Reflector`

Представление контента документа имеет рекурсивную структуру:

- полями :doc:`DynamicContent`'а могут являться:

    - строки
    - объекты интерфейса :doc:`IValueCollection <Collection>`
    - объекты :doc:`DynamicContent`

- объекты :doc:`IValueCollection <Collection>` могут содержать:

    - строки
    - объекты :doc:`DynamicContent`



.. rubric:: Общие правила формирования структуры :doc:`DynamicContent`'а

- Элементы сложного типа будут представлены как :doc:`DynamicContent`

    - ``<xs:element name="ComplexElementName"> <xs:complexType>....``
    - ``<xs:element name="ComplexElementName" type="ComlexElementType">``

- Элементы простого (встроенного) типа (числа, строки, даты) будут представлены как строки

    - ``<xs:attribute name="SimpleElementName" type="string50">`` ( ``<xs:simpleType name="string50"> <xs:restriction base="xs:string">`` )
    - ``<xs:attribute name="SimpleElementName"><xs:simpleType><xs:restriction base="xs:decimal">...``

- Повторяющиеся элементы (``maxOccurs= "unbounded"``, ``maxOccurs > 1`` или повторяющиеся по умолчанию для описанного типа элемента) будут добавлены как :doc:`IValueCollection <Collection>`

- Имя поля COM-объекта, соответствующее элементу XSD-схемы будет совпадать с именем элемента в XSD-схеме

- Если у повторяющегося элемента XSD-схемы не указано имя, то будет применено имя ``items``

- Если тип элемента наследуется от другого типа, то наследник будет иметь все свойства родителя

    - ``<xs:complexType name="ChildType"><xs:extension base="ParentType">...``



.. rubric:: Как работать с коллекциями

1. Чтобы добавить элемент в :doc:`коллекцию <Collection>`, необходимо вызвать метод объекта, в котором эта :doc:`коллекция <Collection>` лежит. Назовём этот объект ``ВладелецКоллекции``
2. Имя метода для добавления элемента - ``"Add" + <Имя поля с коллекцией>``
3. Если :doc:`коллекция <Collection>` хранит в себе повторяющиеся строки (а не :doc:`DynamicContent`), то метод нужно вызвать с одним параметром - добавляемой в коллекцию строкой. Возвращаемого значения у метода не будет
4. Если коллекция хранит не строки, то метод нужно вызвать без параметров. Метод вернёт добавленный в коллекцию элемент



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


.. warning::
  При использовании динамического контента ориентироваться на описание **старых версий контента** (например, :doc:`UtdSellerContent`) **нельзя** - отличается как набор полей, так и допустимые для них значения.


.. rubric:: Устаревшие Методы

+--------------------------------------+-------------------------------+
| |DynamicContent-GetPropertiesNames|_ | |DynamicContent-HasProperty|_ |
+--------------------------------------+-------------------------------+

.. |DynamicContent-GetPropertiesNames| replace:: GetPropertiesNames()
.. |DynamicContent-HasProperty| replace:: HasProperty()


.. _DynamicContent-GetPropertiesNames:
.. method:: DynamicContent.GetPropertiesNames()

  Возвращает :doc:`коллекцию <Collection>` строк - имён свойств контента

  .. versionadded:: 5.28.3

  .. deprecated:: 5.28.7
    Используйте :doc:`Reflector`


.. _DynamicContent-HasProperty:
.. method:: DynamicContent.HasProperty(PropertyName)

  :PropertyName: ``строка`` - имя свойства

  Возвращает булевое значение наличия у объекта свойства с заданным именем

  .. versionadded:: 5.28.3

  .. deprecated:: 5.28.7
    Используйте :doc:`Reflector`


.. seealso:: :doc:`../HowTo/HowTo_reflect_object`
