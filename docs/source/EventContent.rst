EventContent
============

Содержание события

Свойства объекта
----------------

- **CostChangeInfo** (строка, чтение/запись) - иные сведения об изменении стоимости

- **TransferDocDetails** (строка, чтение/запись) - реквизиты передаточных документов, к которым относится корректировка

- **OperationContent** (строка, чтение/запись) - содержание операции

- **NotificationDate** (дата, чтение/запись) - дата направления на согласование

- **CorrectionBases** (:doc:`коллекция <Collection>` объектов :doc:`CorrectionBase <CorrectionBase>`, чтение) - основание корректировки


Методы
------

- :doc:`AddCorrectionBase <AddCorrectionBase>` - добавляет основание корректировки в коллекцию оснований

.. toctree::
   :name: Auto
   :hidden:
   
   CorrectionBase <CorrectionBase>
   AddCorrectionBase <AddCorrectionBase>