Релиз 5.20.3
============

.. feed-entry::
   :date: 2018-02-06

- добавлен универсальный метод получения комментариев - GetAnyComment

- в Utd и Ucd появились признаки **Revised** (было ли исправление данного документа) и **Corrected** (была ли корректировка данного документа)

- методы используемые для получения контрагентов (GetCounteragentById, GetCounteragentListByInnKpp) теперь используют /V2/GetCounteragent АПИ Диадок

- метод AcquireCounteragent стал блокирующим, теперь ожидается завершение асинхронного вызова со стороны АПИ Диадок - генерирует исключения в случае получения ошибочных кодов состояния со стороны АПИ Диадок

- свойство **AdressText** объекта AddressInfo для  XmlTorg12 и XmlAcceptanceCertificate, предтавляет строку иностранного адреса или неструктурированного российского адреса.

- улучшена совместимость COM-компоненты с Microsoft VB6 и Microsoft VBA (Microsoft Office)

- Исправлены ошибки:
    - у документа на отправку ContractToSend не заполнялось свойство **FileName**, было невозможно отправить такой документ


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_