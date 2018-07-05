SetExtendedSignerDetailsTask
============================

Объект предназначен для добавления или обновления данных подписанта в базе Диадок.

Свойства
--------

-  **IsSeller** (булево, чтение/запись) - признак того, является ли подписант подписантом титула продавца или подписантом титула покупателя

-  **ForCorrection** (булево, чтение/запись) - признак того, является ли подписант подписантом корректировки

-  **ExtendedSignerDetailsToPost** (:doc:`ExtendedSignerDetailsToPost <ExtendedSignerDetailsToPost>`, чтение/запись) - данные подписанта

-  **DocumentTitleType** (строка, чтение/запись) - тип титула документа


Свойство **DocumentTitleType** может принимать следующие значения:

- UtdSeller - титул продавца УПД

- UtdBuyer - титул покупателя УПД

- UcdSeller - титул продавца УКД

- UcdBuyer - титул покупателя УКД

- TovTorg551Seller - титул продавца торг-12 в формате 551-го приказа ФНС

- TovTorg551Buyer - титул покупателя торг-12 в формате 551-го приказа ФНС

- AccCert552Seller - титул продавца акта в формате 552-го приказа ФНС

- AccCert552Buyer - титул покупателя акта в формате 552-го приказа ФНС

Методы
------

-  :doc:`Send <Send-(SetExtendedSignerDetailsTask)>` - отправляет данные подписанта на сервер Диадок


.. toctree::
   :name: Auto
   :hidden:

   Send <Send-(SetExtendedSignerDetailsTask)>
