SetExtendedSignerDetailsTask
============================

Задача для добавления или обновления данных подписанта в базе Диадок

.. rubric:: Свойства

:IsSeller:
  **Булево, чтение/запись** - признак того, является ли подписант подписантом титула продавца или подписантом титула покупателя

  .. deprecated:: 5.19.0
    Используйте *DocumentTitleType*

:ForCorrection:
  **Булево, чтение/запись** - признак того, является ли подписант подписантом корректировки

  .. deprecated:: 5.19.0
    Используйте *DocumentTitleType*

:ExtendedSignerDetailsToPost:
  :doc:`ExtendedSignerDetailsToPost <ExtendedSignerDetailsToPost>` **, чтение** - данные подписанта

:DocumentTitleType:
  **Строка, чтение/запись** - тип титула документа. |SetExtendedSignerDetailsTask-TitleType|_


.. rubric:: Методы

+--------------------------------------+
| |SetExtendedSignerDetailsTask-Send|_ |
+--------------------------------------+

.. |SetExtendedSignerDetailsTask-Send| replace:: Send()



.. _SetExtendedSignerDetailsTask-Send:
.. method:: SetExtendedSignerDetailsTask.Send()

  Отправляет данные подписанта на сервер Диадок

.. rubric:: Дополнительная информация

.. |SetExtendedSignerDetailsTask-TitleType| replace:: Возможные значения
.. _SetExtendedSignerDetailsTask-TitleType:

============================ =====================================================
Значение *DocumentTitleType* Описание
============================ =====================================================
UtdSeller                    титул продавца УПД
UtdBuyer                     титул покупателя УПД
UcdSeller                    титул продавца УКД
UcdBuyer                     титул покупателя УКД
TovTorg551Seller             титул продавца Торг-12 в формате 551-го приказа ФНС
TovTorg551Buyer              титул покупателя Торг-12 в формате 551-го приказа ФНС
AccCert552Seller             титул продавца акта в формате 552-го приказа ФНС
AccCert552Buyer              титул покупателя акта в формате 552-го приказа ФНС
Utd820Buyer                  титул покупателя УПД 820
Torg2Buyer                   титул покупателя Торг-2 приказа 423
Torg2AdditionalInfo          титул дополнительных сведений Торг-2 приказа 423
============================ =====================================================
