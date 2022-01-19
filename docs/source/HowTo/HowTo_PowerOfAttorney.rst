Работа с машиночитаемыми доверенностями (МЧД)
=============================================

При работе с МЧД могут потребоваться следующие данные:

* поле **NeedAttachPowerOfAttorney** объекта :doc:`Organization`
* поле **OwnerType** объекта :doc:`PersonalCertificate`
* объекты для представления данных об МЧД:

  * :doc:`PowerOfAttorneyInfo`
  * :doc:`PowerOfAttorenyParticipant`
  * :doc:`PowerOfAttorneyStatus`
  * :doc:`PowerOfAttorneyValidationInfo`
  * :doc:`PowerOfAttorneyRegistrationInfo`
  * :doc:`PowerOfAttorneyRegistrationResult`
  * :doc:`EmployeePowerOfAttorney`
  * :doc:`AttachedPowerOfAttorney`
  * :doc:`PowerOfAttorneyToAttach`



.. rubric:: Регистрация МЧД


Для регистрации МЧД существуют два метода:

  * :meth:`Organization.RegisterPowerOfAttorneyById`
  * :meth:`Organization.RegisterPowerOfAttorneyByContent`

Первый из этих методов может быть использован, если МЧД уже зарегистрирована в ФНС через какой-либо другой сервис (не Диадок).

Второй - если МЧД выпущена, или же как альтернатива первому методу.



.. rubric:: МЧД привязанные к сотруднику организации

Для получения МЧД, привязанных к текущему авторизованному сотруднику мпредназначен метод :meth:`Organization.GetMyPowersOfAttorney`

Если какую-то из полученных МЧД требуется установить как МЧД по умолчанию, то можно использовать :meth:`Organization.SetDefaultPowerOfAttorney`


.. code-block:: c#

  Процедура УстановитьМЧДПоУмолчанию()
    dd_EmployeePowerOfAttorney_Collection = dd_Organization.GetMyPowersOfAttorney(Истина);
    dd_EmployeePowerOfAttorney = dd_EmployeePowerOfAttorney_Collection.getItem(0);
    dd_PowerOfAttorneyInfo = dd_EmployeePowerOfAttorney.PowerOfAttorneyInfo;

    dd_Organization.SetDefaultPowerOfAttorney(dd_PowerOfAttorneyInfo);
  КонецПроцедуры


.. rubric:: Как использовать МЧД

МЧД необходимо прикладывать при подписании каких-либо сущностей.
В Task'ах, в которых может произойти подписание каких-либо сущностей добавлено поле **PowerOfAttorneyToAttach**. К таким Task'ам относятся:

  * :doc:`AcquireCounteragentTask` - для подписания документа-вложения, если он указан
  * :doc:`ReceiptGenerationProcess` - для подписания ИоПов
  * :doc:`OutDocumentSignTask` - для подписания титула отправляемого документа
  * :doc:`PackageSendTask` - для подписания отправляемых документов
  * :doc:`PackageSendTask2` - для подписания отправляемых документов
  * :doc:`ReplySendTask` - для любого из ответных действий по документам
  * :doc:`ReplySendTask2` - для любого из ответных действий по документам
  * :doc:`SendDraftTask` - для подписания отправляемых документов


.. code-block:: c#

  Процедура УказаниеМЧД_НаПримере_PackageSendTask2()
    dd_PST2 = dd_Organization.CreatePackageSendTask2();

    Если dd_Organization.NeedAttachPowerOfAttorney Тогда
      dd_PowerOfAttorneyToAttach = dd_PST2.PowerOfAttorneyToAttach;

      Если ХочуИспользоватьМЧДПоУмолчанию Тогда
        dd_PowerOfAttorneyToAttach.UseDefault = Истина;

      Иначе
        dd_EmployeePowerOfAttorney_Collection = dd_Organization.GetMyPowersOfAttorney(Истина);
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

    Если dd_Organization.NeedAttachPowerOfAttorney Тогда
      Если ХочуИспользоватьМЧДПоУмолчанию Тогда
        dd_AsyncResult = dd_DocumentBase.SendReceiptsWithPowerOfAttorney();

      Иначе
        dd_EmployeePowerOfAttorney_Collection = dd_Organization.GetMyPowersOfAttorney(Истина);
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

Для получения данных об МЧД, которые использовались для подписания сущностей документа был добавлен метод :meth:`DocumentBase.DocumentBase.GetPowersOfAttorney`
