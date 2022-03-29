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
    **Строка, чтение** - направление документа. :doc:`Возможные значения <./Enums/DocumentDirection>`

:EventType:
    **Строка, чтение** - тип события. :doc:`Возможные значения <./Enums/EventType>`

:Timestamp:
    **Дата и время, чтение** - дата и время события в текущем часовом поясе



.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`GetDocument() <DocumentEvent.GetDocument>`

        * :meth:`GetFileContent() <DocumentEvent.GetFileContent>`

        * :meth:`GetSignatureContent() <DocumentEvent.GetSignatureContent>`


.. method:: DocumentEvent.GetDocument()

    Возвращает :doc:`документ <Document>`, связанный с событием


.. method:: DocumentEvent.GetFileContent(FilePath)

    :FilePath: ``строка`` путь до файла, в который будет сохранён контент

    Сохраняет содержимое документа на диск и возвращает *строку* с именем документа в Диадок


.. method:: DocumentEvent.GetSignatureContent(FilePath)

    :FilePath: ``строка`` путь до файла, в который будет сохранён контент подписи

    Сохраняет контент подписи документа на диск и возвращает *строку* с именем документа в Диадок