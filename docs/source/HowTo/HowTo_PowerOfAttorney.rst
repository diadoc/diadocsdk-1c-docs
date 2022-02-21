Работа с машиночитаемыми доверенностями (МЧД)
=============================================

Основные объекты для работы с МЧД:

* :doc:`../../ComObjects/PowerOfAttorney`
* :doc:`../../ComObjects/EmployeePowerOfAttorney`
* :doc:`../../ComObjects/AttachedPowerOfAttorney`



.. rubric:: Регистрация МЧД


Для регистрации МЧД существуют два метода:

  * :meth:`Organization.RegisterPowerOfAttorneyById`
  * :meth:`Organization.RegisterPowerOfAttorneyByContent`

Первый из этих методов может быть использован, если МЧД уже зарегистрирована в ФНС через какой-либо другой сервис (не Диадок).

Второй - если МЧД выпущена, или же как альтернатива первому методу.



.. rubric:: МЧД привязанные к сотруднику организации

Для получения МЧД, привязанных к текущему авторизованному сотруднику, предназначен метод :meth:`MyEmployee.GetPowersOfAttorney`

Если какую-то МЧД требуется установить как МЧД по умолчанию, то можно использовать :meth:`MyEmployee.SetDefaultPowerOfAttorney`


.. code-block:: c#

  Процедура УстановитьМЧДПоУмолчанию()
    dd_MyEmployee = dd_Organization.MyEmployee;
    dd_EmployeePowerOfAttorney_Collection = MyEmployee.GetMyPowersOfAttorney(Истина);
    dd_EmployeePowerOfAttorney = dd_EmployeePowerOfAttorney_Collection.getItem(0);
    dd_PowerOfAttorneyInfo = dd_EmployeePowerOfAttorney.PowerOfAttorneyInfo;

    dd_MyEmployee.SetDefaultPowerOfAttorney(dd_PowerOfAttorneyInfo);
  КонецПроцедуры


.. rubric:: Как использовать МЧД

МЧД необходимо прикладывать при подписании каких-либо сущностей.
В Task'ах, в которых может произойти подписание каких-либо сущностей добавлено поле **PowerOfAttorneyToAttach**. К таким Task'ам относятся:

  * :doc:`../ComObjects/AcquireCounteragentTask` - для подписания документа-вложения, если он указан
  * :doc:`../ComObjects/ReceiptGenerationProcess` - для подписания ИоПов
  * :doc:`../ComObjects/OutDocumentSignTask` - для подписания отправляемых документов
  * :doc:`../ComObjects/PackageSendTask` - для подписания отправляемых документов
  * :doc:`../ComObjects/PackageSendTask2` - для подписания отправляемых документов
  * :doc:`../ComObjects/ReplySendTask` - для любого из ответных действий по документам
  * :doc:`../ComObjects/ReplySendTask2` - для любого из ответных действий по документам
  * :doc:`../ComObjects/SendDraftTask` - для подписания отправляемых документов


.. code-block:: c#

  Процедура УказаниеМЧД_НаПримере_PackageSendTask2()
    dd_PST2 = dd_Organization.CreatePackageSendTask2();
    dd_MyEmployee = dd_Organization.MyEmployee;

    Если dd_MyEmployee.NeedAttachPowerOfAttorney Тогда
      dd_PowerOfAttorneyToAttach = dd_PST2.PowerOfAttorneyToAttach;

      Если ХочуИспользоватьМЧДПоУмолчанию Тогда
        dd_PowerOfAttorneyToAttach.UseDefault = Истина;

      Иначе
        dd_EmployeePowerOfAttorney_Collection = dd_MyEmployee.GetMyPowersOfAttorney(Истина);
        dd_EmployeePowerOfAttorney = dd_EmployeePowerOfAttorney_Collection.getItem(0);
        dd_PowerOfAttorneyInfo = dd_EmployeePowerOfAttorney.PowerOfAttorneyInfo;

        dd_PowerOfAttorneyToAttach.PowerOfAttorney = dd_PowerOfAttorneyInfo;
      КонецЕсли;

    КонецЕсли;

    // Код добавления и отправки документов не приведён

  КонецПроцедуры


Кроме того, МЧД можно указать для подписания ИоПов по конкретного документу:

.. code-block:: c#

  Процедура ПодписатьИоПыИспользуяМЧД(ИдентификаторДокумента)
    dd_DocumentBase = dd_Organization.GetDocumentById(ИдентификаторДокумента);
    dd_MyEmployee = dd_Organization.MyEmployee;

    Если dd_MyEmployee.NeedAttachPowerOfAttorney Тогда
      Если ХочуИспользоватьМЧДПоУмолчанию Тогда
        dd_AsyncResult = dd_DocumentBase.SendReceiptsWithPowerOfAttorney();

      Иначе
        dd_EmployeePowerOfAttorney_Collection = dd_MyEmployee.GetMyPowersOfAttorney(Истина);
        dd_EmployeePowerOfAttorney = dd_EmployeePowerOfAttorney_Collection.getItem(0);
        dd_PowerOfAttorneyInfo = dd_EmployeePowerOfAttorney.PowerOfAttorneyInfo;

        dd_AsyncResult = dd_DocumentBase.SendReceiptsWithPowerOfAttorney(dd_PowerOfAttorneyInfo);
      КонецЕсли;

    Иначе
      dd_AsyncResult = dd_DocumentBase.SendReceiptsAsync();

    КонецЕсли;

    // Код обработки dd_AsyncResult не приведён

  КонецПроцедуры



.. rubric:: Получение данных об МЧД

Для получения данных об :doc:`МЧД, которые использовались для подписания сущностей документа <../../ComObjects/AttachedPowerOfAttorney>`, используется метод :meth:`DocumentBase.GetPowersOfAttorney`
