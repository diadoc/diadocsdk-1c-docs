Как получить описание объекта
=============================

Для получения описания COM-объектов, создаваемых компонентой, используется объект :doc:`../ComObjects/Reflector`.
Он является независимой частью компоненты и создаётся как отдельный объект

С помощью :doc:`../ComObjects/Reflector`'а можно:
  * получить имя класса (имя реализуемого интерфейса) как оно описано в библиотеке типов
  * получить набор полей объекта
  * узнать, есть ли объекта указанное свойство
  * узнать тип значения у свойства


.. code-block:: c#

  //Создание Reflector'а
  Reflector = Новый ComОбъект("AddIn.Diadoc.Reflector");

  // Допустим, хотим посмотреть описание корневого объекта компоненты AddIn
  DiadocApi_ = Новый("AddIn.DiadocInvoiceAPI");
  DiadocApi  = DiadocApi_.CreateObject();

  ОписаниеОбъекта = Reflector.Describe(DiadocApi);

  ИмяИнтерфейса  = ОписаниеОбъекта.GetInterfaceName(); // "IDiadocApiInvoiceApi"
  ПоляОбъекта    = ОписаниеОбъекта.GetPropertiesNames(); // коллекция строк с именами полей объекта
  ЕстьЛиСвойство = ОписаниеОбъекта.HasProperty("ProxySettings"); // true
  ТипСвойства_1  = ОписаниеОбъекта.GetPropertyType("ProxySettings"); // "VT_PTR"
  ТипСвойства_2  = ОписаниеОбъекта.GetPropertyType("Свойство_которого_нет"); // ""
  ТипСвойства_3  = ОписаниеОбъекта.GetPropertyType("ApiClientId"); // "VT_BSTR"
