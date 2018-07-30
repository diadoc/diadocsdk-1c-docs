Релиз 5.21.10
=============

.. feed-entry::
   :date: 2018-07-31

- У объекта :doc:`Document <Document>` появился метод SaveBuyerContent для сохранения только ответного титула двухтитульного документа.

- исправлены ошибки:
	- Метод :doc:`Send <Send-(PackageSendTask)>` не возвращал в результат документы, отправленные с типом SupplementaryAgreement
	- При чтении контента акта @552 у :doc:`работы <Act552WorkItem>` с неуказанной ставкой НДС, поле TaxRate заполнялось "18%" вместо "БезНДС"
	- В Com-компоненте для произвольных систем пустая дата изменена на 01.01.0001 00:00:00, по аналогии с AddInCom
	- Метод :doc:`getDocumentEventList <GetDocumentEventList>` не возвращал события с типом "New" для документов, пришедших внутри патча к другому документу
	- Метод :doc:`getDocumentEventList <GetDocumentEventList>` неверно определял DocumentId у некоторых :doc:`событий <DocumentEvent>`
	- Метод :doc:`getDocumentEventList <GetDocumentEventList>` неверно определял тип события для сущности с Извещением о Получении документа получателем. Теперь для ИоП возвращается событие с типом Accept (было Confirmation)

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_