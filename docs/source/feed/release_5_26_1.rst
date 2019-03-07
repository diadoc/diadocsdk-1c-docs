Релиз 5.26.1
============

.. feed-entry::
   :date: 2019-03-07
   
- Внутренние улучшения
- Исправлены ошибки:
    - Неправильно возвращалась организация-получатель при обращении к полю Document.FromDepartment, что приводило к ошибке "Организация отсутствует"
    - В :doc:`Act552WorkItem <Act552WorkItem>` в :doc:`Act552SellerContent <Act552SellerContent>` неверно десериализовывалась ставка "БезНДС"
    - Cтавку НДС в :doc:`Act552WorkItem <Act552WorkItem>` в :doc:`XmlAct552ToSend <XmlAct552ToSend>`  невозможно было изменить, если не заполнена сумма НДС
    - Если ставка НДС в :doc:`Act552WorkItem <Act552WorkItem>` в :doc:`XmlAct552ToSend <XmlAct552ToSend>` не указывалась явно, то вместо значения по умолчанию "БезНДС" сериализовалось значение "18%"
    - Во многих объектах выставлялась неправильная дата по-умолчанию
    - В :doc:`TemplateToSend <TemplateToSend>` не сериализовалось поле CustomDocumentId
    - В COM для произвольных систем некоторые булевые поля могли возвращать неправильное значение


`История изменений <http://diadocsdk-1c.readthedocs.io/ru/latest/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/latest/Downloads.html>`_