TovTorgBuyerContent
====================

Объект предназначен для работы с содержанием ответного титула документов типа "ТОРГ-12 в
формате 551-го приказа ФНС"

Свойства объекта
----------------

- **DocumentCreator** (строка, чтение/запись) - составитель файла обмена (информации покупателя)

- **DocumentCreatorBase** (строка, чтение/запись) - основание, по которому экономический субъект является составителем файла обмена

- **OperationCode** (строка, чтение/запись) - вид операции

- **OperationContent** (строка, чтение/запись) - содержание операции

- **AcceptanceDate** (дата, чтение/запись) - дата принятия товаров (результатов выполненных работ) или имущественных прав (подтверждения факта оказания услуг)

- **Employee** (объект :doc:`Employee <Employee>`, чтение) - работник организации покупателя

- **OtherIssuer** (объект :doc:`OtherIssuer <OtherIssuer>`, чтение) - иное лицо

- **AdditionalInfo** (объект :doc:`AdditionalInfoId <AdditionalInfoId>`, чтение) - информационное поле документа

- **ExtendedSigners** (:doc:`коллекция <Collection>` объектов :doc:`ExtendedSigner <ExtendedSigner>`, чтение) - подписанты документа. Для документа должен быть указан по крайней мере один подписант.

Методы объекта
--------------

-  :doc:`AddExtendedSigner <AddSigner-(TovTorgBuyerContent)>` - добавляет подписанта

.. toctree::
   :name: Auto
   :hidden:

   AddSigner <AddSigner-(TovTorgBuyerContent)>
