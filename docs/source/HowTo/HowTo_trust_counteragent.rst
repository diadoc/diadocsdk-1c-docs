Как установить партнерские отношения
====================================

Как найти контрагента
---------------------

Есть несколько способов найти контрагента:

.. rubric:: Поиск по ИНН-КПП контрагента

Необходимо использовать метод :func:`Organization.GetCounteragentListByInnKpp`

.. code-block:: c#

    ЯщикиКонтрагентов = Новый Массив;

    ИНН= СокрЛП(Контрагент.ИНН);
    КПП= СокрЛП(Контрагент.КПП);

    // Получаем список контрагентов с заданными ИНН/КПП
    CounteragentList = Organization.GetCounteragentListByInnKpp(ИНН, КПП);
    Для Ц = 0 по CounteragentList.count-1 Цикл
        ЯщикиКонтрагентов.Добавить(CounteragentList.GetItem(Ц));
    КонецЦикла;

.. rubric:: Поиск контрагентов по списку ИНН

Необходимо использовать метод :func:`Organization.GetCounteragentListByInnList`

.. code-block:: c#

    СтрокаИНН = "9667853716,9667853667";
    CounteragentList = Organization.GetCounteragentListByInnList(СтрокаИНН);

    Если CounteragentList.IsCompleted Тогда
        РезультатЗапроса = CounteragentList.Result;
        Item = РезультатЗапроса.GetItem(0);
        Counteragent = Item.Counteragent;
    КонецЕсли;

.. rubric:: Другие способы

* Зная идентификатор ящика контрагента в Диадок можно применить метод :func:`Organization.GetCounteragentById`

* Или отфильтровать контрагентов по статусу: :func:`Organization.GetCounteragentListByStatus`


Как пригласить контрагента к партнёрству
----------------------------------------

Необходимо отправить запрос партнёрства методом :func:`Counteragent.AcquireCounteragent` или использовать объект :doc:`AcquireCounteragentTask <../ComObjects/AcquireCounteragentTask>`:

.. code-block:: c#

    Task = Organization.CreateAcquireCounteragentTask();
    Task.FileName           = "С:\\Файл с приглашением.pdf";
    Task.CounteragentBoxId  = Counteragent.Id;
    Task.Message            = "Приглашаем к партнерству";
    Task.SignatureRequested = True;

    ИдентификаторКонтрагента = Task.Send();



Как принять приглашение от контрагента
--------------------------------------

Необходимо выполнить метод :func:`Counteragent.AcquireCounteragent`

.. code-block:: c#

    Counteragent = Organization.GetCounteragentById(CounteragentId);
    Counteragent.AcquireCounteragent("Принимаем партнёрство");


Как отказаться от партнёрства
-----------------------------

Необходимо выполнить метод :func:`Counteragent.BreakWithCounteragent`

.. code-block:: c#

    Counteragent = Organization.GetCounteragentById(CounteragentId);
    Counteragent.BreakWithCounteragent("Отказываем в партнерстве");
