DocumentToSend
==============

Базовый объект для :ref:`всех документов на отправку <DocumentToSendBase-Inheritable>`


.. versionadded:: 5.5.0


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа на отправку

:NeedReceipt:
    **Булево, чтение/запись** - запросить у контрагента извещение о получении документа. Настройка сработает, если документооборот документа позволяет это сделать

:NeedRecipientSignature:
    **Булево, чтение/запись** - запросить у контрагента подпись по документу. Настройка сработает, если документооборот документа позволяет это сделать

:Content:
    :doc:`./Descriptions/AnyVariant` **, чтение** - представление содержимого документа. Тип контента для каждого :ref:`наследника <DocumentToSendBase-Inheritable>` этого интерфейса свой

:Comment:
    **Строка, чтение/запись** - комментарий, добавляемый к документу при отправке

:CustomDocumentId:
    **Строка, чтение/запись** - дополнительный идентификатор документа


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        .. csv-table::
            :header: Добавление связанных документов, Служебные
            
            :meth:`AddInitialDocument() <DocumentToSend.AddInitialDocument>`, :meth:`SaveContent() <DocumentToSend.SaveContent>`
            :meth:`AddSubordinateDocument() <DocumentToSend.AddSubordinateDocument>`,
            :meth:`AddInitialDocumentFromPackage() <DocumentToSend.AddInitialDocumentFromPackage>`,
            :meth:`AddSubordinateDocumentFromPackage() <DocumentToSend.AddSubordinateDocumentFromPackage>`,

    .. tab:: Добавление связанных документов

        * :meth:`AddInitialDocument() <DocumentToSend.AddInitialDocument>`
        * :meth:`AddSubordinateDocument() <DocumentToSend.AddSubordinateDocument>`
        * :meth:`AddInitialDocumentFromPackage() <DocumentToSend.AddInitialDocumentFromPackage>`
        * :meth:`AddSubordinateDocumentFromPackage() <DocumentToSend.AddSubordinateDocumentFromPackage>`

    .. tab:: Служебные

        * :meth:`SaveContent() <DocumentToSend.SaveContent>`


.. method:: DocumentToSend.AddInitialDocument(DocumentID)

    :DocumentID: **Строка** - идентификатор документа в Диадок

    Добавляет идентификатор документа в коллекцию "родительских" документов


.. method:: DocumentToSend.AddSubordinateDocument(DocumentID)

    :DocumentID: **Строка** - идентификатор документа в Диадок

    Добавляет идентификатор документа в коллекцию подчиненных документов


.. method:: DocumentToSend.AddInitialDocumentFromPackage(CustomDocumentID)

    :CustomDocumentID: **Строка** - идентификатор документа, определяемый внешней системой. Может быть взят у любого документа отправляемого пакета

    Добавляет идентификатор документа из пакета на отправку в коллекцию "родительских" документов


.. method:: DocumentToSend.AddSubordinateDocumentFromPackage(CustomDocumentID)

    :CustomDocumentID: **Строка** - идентификатор документа, определяемый внешней системой. Может быть взят у любого документа отправляемого пакета

    Добавляет идентификатор документа из пакета на отправку в коллекцию подчиненных документов


.. method:: DocumentToSend.SaveContent(BoxId, FilePath)

    :BoxId: **Строка** - идентификатор ящика контрагента, которому должен быть отправлен документ
    :FilePath: **Строка** - путь до файла

    Если контент документа загружался из файла или Base64, то сохранит их контент в указанный файл.
    Если контент заполнялся через заполнение представление контента контента, то сначала произойдёт попытка генерации контента по данным в этом представлении.

    .. versionadded:: 5.29.9


.. rubric:: Дополнительная информация

.. _DocumentToSendBase-Inheritable:

================================================ =======================================================
Объекты, наследующие интерфейс DocumentToSend    Описание
================================================ =======================================================
:doc:`CustomDocumentToSend`                      Документ произвольного типа
:doc:`ActToSend` (устарел)                       Акт о выполнении работ в неформализованном виде
:doc:`CertificateRegistryToSend` (устарел)       Реестр сертификатов
:doc:`ContractToSend` (устарел)                  Договор
:doc:`InvoiceToSend` (устарел)                   Счет-фактура в формате приказа ММВ-7-6/93@
:doc:`InvoiceCorrectionToSend` (устарел)         Корректировочный счет-фактура
:doc:`InvoiceRevisionToSend` (устарел)           Исправление счета-фактуры в формате приказа ММВ-7-6/93@
:doc:`InvoiceCorrectionRevisionToSend` (устарел) Исправление корректировочного счета-фактуры
:doc:`NonformalizedDocumentToSend` (устарел)     Неформализованный документ
:doc:`PriceListAgreementToSend` (устарел)        Протокол согласования цены
:doc:`NonformalizedProformaToSend` (устарел)     Счет на оплату
:doc:`ReconciliationActToSend` (устарел)         Акт сверки
:doc:`ServiceDetailsToSend` (устарел)            Детализация
:doc:`Torg12ToSend` (устарел)                    ТОРГ-12 в неформализованном виде
:doc:`XmlActToSend` (устарел)                    Акт о выполнении работ в формате приказа ММВ-7-6/172@
:doc:`XmlTorg12ToSend` (устарел)                 ТОРГ-12 в формате приказа ММВ-7-6/172@
:doc:`UtdToSend` (устарел)                       Универсальный передаточный документ
:doc:`UcdToSend` (устарел)                       Универсальный корректировочный документ
:doc:`TovTorgToSend` (устарел)                   ТОРГ-12 в формате приказа ММВ-7-10/551@
:doc:`XmlAct552ToSend` (устарел)                 Акт в формате приказа ММВ-7-10/552@
================================================ =======================================================
