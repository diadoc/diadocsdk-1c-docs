Релиз 5.22.1
=============

.. feed-entry::
   :date: 2018-08-09

- В объект :doc:`UserPermissions <UserPermissions>` добавлено индикатор права пользователя на создание документов CanCreateDocuments.
- Улучшена стабильность

- исправлены ошибки:
    - Метод :doc:`SaveAllContent <SaveAllContent>` не сохранял печатную форму документа с типом "Дополнительное соглашение"
    - Неверное сериализовалось поле Total объекта :doc:`InvoiceTotalsDiff <InvoiceTotalsDiff>`, что приводило к непринятию Диадоком такого документа
    - В контенте :doc:`работы <Act552WorkItem>` с неуказанной ставкой НДС, если сумма НДС не указана, то ставка будет "Без НДС"; если сумма заполнена нулевым значением - ставка будет 0%;

`История изменений <http://diadocsdk-1c.readthedocs.io/ru/dev/History.html>`_

`Релиз <http://diadocsdk-1c.readthedocs.io/ru/dev/Downloads.html>`_