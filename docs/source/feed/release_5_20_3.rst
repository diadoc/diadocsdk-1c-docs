Релиз 5.20.3
=============

.. feed-entry::
   :date: 2018-02-06

- добавлен универсальный метод получения комментариев - :doc:`GetAnyComment <GetAnyComment>`

- в :doc:`Utd <Utd>` и :doc:`Ucd <Ucd>` появились признаки **Revised** (было ли исправление данного документа) и **Corrected** (была ли корректировка данного документа)

- методы используемые для получения контрагентов (:doc:`GetCounteragentById <GetCounteragentById>`, :doc:`GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>`) теперь используют /V2/GetCounteragent АПИ Диадок

- метод :doc:`AcquireCounteragent <AcquireCounteragent>` стал блокирующим, теперь ожидается завершение асинхронного вызова со стороны АПИ Диадок - генерирует исключения в случае получения ошибочных кодов состояния со стороны АПИ Диадок

- свойство **AdressText** объекта :doc:`AddressInfo <AddressInfo>` для  :doc:`XmlTorg12 <XmlTorg12>` и :doc:`XmlAcceptanceCertificate <XmlAcceptanceCertificate>`, предтавляет строку иностранного адреса или неструктурированного российского адреса.

- улучшена совместимость COM-компоненты с Microsoft VB6 и Microsoft VBA (Microsoft Office)

- :doc:`Исправлены ошибки <Bugs_5_20>`


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_