DocumentEvent
=============

Объект предназначен для получения информации о событии

Свойства
--------

-  CounteragentId (строка, чтение) - идентификатор контрагента
-  EventId (строка, чтение) - идентификатор события
-  DocumentType (строка, чтение) - тип документа
-  DocumentId (строка, чтение) - идентификатор документа
-  DocumentDirection (строка, чтение) - направление: входящий/исходящий
-  EventType (строка, чтение) - тип события
-  Timestamp (дата и время, чтение) - дата и время события (в текущем
   часовом поясе)

Свойство EventType принимает одно из следующих значений:

-  New - новый документооборот
-  Accept - согласование содержимого документа
-  Confirmation - подтверждение оператора электронного документооборота
-  CorrectionRequest - уведомление об уточнении счета-фактуры
-  Reject - отказ в формировании запрошенной подписи
-  Resolution - согласование документа

Методы объекта
--------------

-  :doc:`GetDocument <GetDocument>` - возвращает документ, связанный с
   событием
-  :doc:`GetFileContent <GetFileContent>` - сохраняет содержимое документа
   на диск
-  :doc:`GetSignatureContent <GetSignatureContent>` - сохраняет содержимое
   подписи документа на диск

.. toctree::
   :name: Auto
   :hidden:

   GetDocument <GetDocument>
   GetFileContent <GetFileContent>
   GetSignatureContent <GetSignatureContent>