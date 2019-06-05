AcquireCounteragentTask
=======================

Объект предназначен для отправки приглашения контрагента к партнерству

Свойства
--------

- **CounteragentBoxId** (строка, чтение/запись) - идентификатор организации-контрагента
- **Inn** (строка, чтение/запись) - ИНН организации-контрагента
- **Message** (строка, чтение/запись) - текст комментария к операции
- **FileName** (строка, чтение/запись) - имя файла с приглашением
- **SignatureRequested** (булево, чтение/запись) - запрос подписи контрагента

Методы
------

-  :doc:`Send <Send-(AcquireCounteragentTask)>` - отправляет приглашение контрагента к партнерству
-  :doc:`SendAsync <SendAsync-(AcquireCounteragentTask)>` - инициирует асинхронную отправку приглашения контрагента к партнерству


.. toctree::
   :name: Auto
   :hidden:

   Send <Send-(AcquireCounteragentTask)>
   SendAsync <SendAsync-(AcquireCounteragentTask)>
