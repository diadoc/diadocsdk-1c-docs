Как установить партнерские отношения
====================================

Для того что бы две организации могли обмениваться документами, они
должны установить партнерские отношения в Диадоке.

Отправлять документы организации, с которой не установлены партнерские
отношения невозможно.

Для отражения сущности произвольной организации в Диадоке предназначен
:doc:`Counteragent <Counteragent>`.

﻿Как найти контрагента
---------------------------------

Найти контрагента в Диадоке возможно с помощью поиска по ИНН/КПП. С
помощью компоненты можно реализовать несколько способов поиска
контрагента.

-  Поиск по ИНН/КПП в синхронном режиме, для этого можно использовать
   метод :doc:`GetCounteragentListByInnKpp <GetCounteragentListByInnKpp>`

   ::

                   ЯщикиКонтрагентов = Новый Массив;

                   ИНН= СокрЛП(Контрагент.ИНН);
                   КПП= СокрЛП(Контрагент.КПП);

                   //Получаем список контрагентов с заданными ИНН/КПП
                   CounteragentList = Organization.GetCounteragentListByInnKpp(ИНН, КПП);
                   Для Ц = 0 по CounteragentList.count-1 Цикл
                     ЯщикиКонтрагентов.Добавить(CounteragentList.GetItem(Ц));
                   КонецЦикла;

-  Поиск по списку ИНН, для получения результата в асинхронном режиме,
   можно воспользоваться методом
   :doc:`GetCounteragentListByInnList <GetCounteragentListByInnList>`
   объекта :doc:`Organization <Organization>`

   ::

                   //Получаем результат асинхронной операции по строке содержащей список ИНН
                   CounteragentList=   Organization.GetCounteragentListByInnList(СтрокаИНН);

                   Если CounteragentList.IsCompleted Тогда
                     РезультатЗапроса = CounteragentList.Result;
                     Item = РезультатЗапроса.GetItem(0);
                     Counteragent = Item.Counteragent;
                   КонецЕсли;

Как установить партнерство
--------------------------------------

Для установления партнерства между организациями А и Б в Диадоке,
организация А должна отправить, а организация Б принять запрос на
установление партнерства.

Для отправки, принятия или отклонения запроса, а также для разрыва
партнерских отношений используются методы объекта
:doc:`Counteragent <Counteragent>`:

-  AcquireCounteragent – отправка запроса и подтверждение входящего
   запроса от контрагента.

   ::

                   //Находим контрагента по ИНН/КПП
                   CounteragentList = Organization.GetCounteragentListByInnKpp(ИНН, КПП);
                   Counteragent = CounteragentList.GetItem(0);
                   //Принимаем запрос или отправляем приглашение
                   Counteragent.AcquireCounteragent("Приглашаем к партнерству");

                   //Или если у нас имеется ID контрагента, получаем его по ID
                   Counteragent = Organization.GetCounteragentById(CounteragentId);
                   Counteragent.AcquireCounteragent("Приглашаем к партнерству");

-  BreakWithCounteragent – отклонение запроса и разрыв существующего
   партнерства.

   ::

                   //Находим контрагента по ИНН/КПП
                   CounteragentList = Organization.GetCounteragentListByInnKpp(ИНН, КПП);
                   Counteragent = CounteragentList.GetItem(0);
                   //Отклоняем запрос или разрываем взаимоотношения
                   Counteragent.BreakWithCounteragent("Отказываем в партнерстве");

                   //Или если у нас имеется ID контрагента, получаем его по ID
                   Counteragent = Organization.GetCounteragentById(CounteragentId);
                   Counteragent.BreakWithCounteragent("Отказываем в партнерстве");

Для получения списка контрагентов в зависимости от статуса партнерства
предназначен метод
:doc:`GetCounteragentListByStatus <GetCounteragentListByStatus>` объекта
:doc:`Organization <Organization>`.

Для получения объекта :doc:`Counteragent <Counteragent>` по идентификатору
ящика организации используется метод
:doc:`GetCounteragentById <GetCounteragentById>` объекта
:doc:`Organization <Organization>`.

Важно. Партнерство с контрагентом необходимо устанавливать для каждой
нашей организации.
