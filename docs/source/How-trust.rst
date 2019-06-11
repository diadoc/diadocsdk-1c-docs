Как установить партнерские отношения
====================================


Для того, чтобы отправлять документы другой организации в Диадок, между вашей органиазцией и организацией контрагента должны быть установлены партнёрские отношения


Как найти контрагента
---------------------

Есть несколько способов найти контрагента:

# Поиск по ИНН-КПП контрагента

.. code-block:: c#

    ЯщикиКонтрагентов = Новый Массив;

    ИНН= СокрЛП(Контрагент.ИНН);
    КПП= СокрЛП(Контрагент.КПП);

    // Получаем список контрагентов с заданными ИНН/КПП
    CounteragentList = Organization.GetCounteragentListByInnKpp(ИНН, КПП);
    Для Ц = 0 по CounteragentList.count-1 Цикл
        ЯщикиКонтрагентов.Добавить(CounteragentList.GetItem(Ц));
    КонецЦикла;

# Поиск контрагентов по списку ИНН

.. code-block:: c#

    СтрокаИНН = "9667853716,9667853667";
    CounteragentList=   Organization.GetCounteragentListByInnList(СтрокаИНН);

    Если CounteragentList.IsCompleted Тогда
        РезультатЗапроса = CounteragentList.Result;
        Item = РезультатЗапроса.GetItem(0);
        Counteragent = Item.Counteragent;
    КонецЕсли;


Также можно получать объект :doc:`Counteragent <Counteragent>`, зная идентификатор ящика контрагента в диадок, - :doc:`Organization.GetCounteragentById <GetCounteragentById>`

Или фильтровать контрагентов по статусу - :doc:`Organization.GetCounteragentListByStatus <GetCounteragentListByStatus>`


Как пригласить контрагента к партнёрству
----------------------------------------

Для установления партнерских отношений между двумя организациями необходимо отправить запрос партнёрства с помощью метода :doc:`Counteragent.AcquireCounteragent <AcquireCounteragent>` или с помощью объекта :doc:`AcquireCounteragentTask <AcquireCounteragentTask>`

.. code-block:: c#

    Task = Organization.CreateAcquireCounteragentTask();
    Task.FileName           = "С:\Файл с приглашением.pdf";
    Task.CounteragentBoxId  = Counteragent.Id;
    Task.Message            = "Приглашаем к партнерству";
    Task.SignatureRequested = True;
    
    ИдентификаторКонтрагента = Task.Send();
    


Как принять приглашение от контрагента
--------------------------------------

Необходимо выполнить метод :doc:`Counteragent.AcquireCounteragent <AcquireCounteragent>`

.. code-block:: c#

    Counteragent = Organization.GetCounteragentById(CounteragentId);
    Counteragent.AcquireCounteragent("Принимаем партнёрство");


Как отказаться от партнёрства
-----------------------------

Необходимо выполнить метод :doc:`Counteragent.BreakWithCounteragent <BreakWithCounteragent>`

.. code-block:: c#

    Counteragent = Organization.GetCounteragentById(CounteragentId);
    Counteragent.BreakWithCounteragent("Отказываем в партнерстве");