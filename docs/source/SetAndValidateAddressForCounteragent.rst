SetAndValidateAddressForCounteragent 
====================================

Метод объекта :doc:`Organization <Organization>`


.. rubric:: Синтаксис

SetAndValidateAddressForCounteragent(key1S, addressTypeKey, isForeign, zipCode, regionCode, territory, city, locality, street, building, block, apartment)


.. rubric:: Параметры

:key1S: (строка, обязательный) - идентификатор адресной информации
:addressTypeKey: (строка, обязательный) - тип адресной информации
:isForeign: (булево, обязательный) - признак того, что адрес является иностранным (за пределами РФ)
:zipCode: (строка, чтение/запись) - индекс
:regionCode: (строка, чтение/запись) - код региона РФ
:territory: (строка, чтение/запись) - район
:city: (строка, чтение/запись) - город
:locality: (строка, чтение/запись) - населенный пункт
:street: (строка, чтение/запись) - улица
:building: (строка, чтение/запись) - дом
:block: (строка, чтение/запись) - корпус
:apartment: (строка, чтение/запись) - квартира


..rubric:: Возвращаемое значение

:doc:`Коллекция <Collection>` объектов :doc:`ValidationError <ValidationError>` - результаты валидации


.. rubric:: Описание

Валидирует и загружает адресную информацию в хранилище по ключу <key1S> и типу <addressTypeKey>