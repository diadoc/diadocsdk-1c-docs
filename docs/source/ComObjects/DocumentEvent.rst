DocumentEvent
=============

Информации о событии, произошедшем с документом



.. rubric:: Свойства

:CounteragentId:
  **Строка, чтение** - идентификатор контрагента

:EventId:
  **Строка, чтение** - идентификатор события

:DocumentType:
  **Строка, чтение** - тип документа

:DocumentId:
  **Строка, чтение** - идентификатор документа

:DocumentDirection:
  **Строка, чтение** - направление документа. |DocumentEvent-Direction|_

:EventType:
  **Строка, чтение** - тип события. |DocumentEvent-EventType|_

:Timestamp:
  **Дата и время, чтение** - дата и время события в текущем часовом поясе



.. rubric:: Методы

+------------------------------+---------------------------------+--------------------------------------+
| |DocumentEvent-GetDocument|_ | |DocumentEvent-GetFileContent|_ | |DocumentEvent-GetSignatureContent|_ |
+------------------------------+---------------------------------+--------------------------------------+

.. |DocumentEvent-GetDocument| replace:: GetDocument()
.. |DocumentEvent-GetFileContent| replace:: GetFileContent()
.. |DocumentEvent-GetSignatureContent| replace:: GetSignatureContent()



.. _DocumentEvent-GetDocument:
.. method:: DocumentEvent.GetDocument()

  Возвращает :doc:`документ <Document>`, связанный с событием



.. _DocumentEvent-GetFileContent:
.. method:: DocumentEvent.GetFileContent(FilePath)

  :FilePath: ``строка`` путь до файла, в который будет сохранён контент

  Сохраняет содержимое документа на диск и возвращает *строку* с именем документа в Диадок



.. _DocumentEvent-GetSignatureContent:
.. method:: DocumentEvent.GetSignatureContent(FilePath)

  :FilePath: ``строка`` путь до файла, в который будет сохранён контент подписи

  Сохраняет контент подписи документа на диск и возвращает *строку* с именем документа в Диадок



.. rubric:: Дополнительная информация

.. |DocumentEvent-EventType| replace:: Возможные значения
.. _DocumentEvent-EventType:

==================== ========================================
Значение *EventType* Описание
==================== ========================================
New                  новый документооборот
Accept               подписание документа
Confirmation         Извещение о получении документа
CorrectionRequest    уведомление об уточнении счета-фактуры
Reject               отказ в формировании запрошенной подписи
Resolution           согласование документа
ResolutionRequest    запрос на согласование документа
MetaModify           событие не изменяющее статус документа
UnsupportedEventType неподдерживаемый тип события
==================== ========================================


.. |DocumentEvent-Direction| replace:: Возможные значения
.. _DocumentEvent-Direction:

==================== ===================
Значение *Direction* Описание
==================== ===================
Inbound              входящий документ
Outbound             исходящий документ
Internal             внутренний документ
==================== ===================
