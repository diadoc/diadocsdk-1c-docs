AcceptanceCertificateSellerContent
==================================

Содержание титула продавца *Акта о выполнении работ* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83259>`_ .
Является производным объектом от :doc:`BaseContent`

.. deprecated:: 5.27.0
    Используйте :doc:`DynamicContent`

.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificateContent``

:Date:
    **Дата, чтение/запись** - дата акта

:Number:
    **Строка, чтение/запись** - номер акта

:Title:
    **Строка, чтение/запись** - заголовок акта

:SignatureDate:
    **Дата, чтение/запись** - дата подписи акта исполнителем

:Seller:
    :doc:`OrganizationInfo` **, чтение** - исполнитель (организация, выполнившая работы либо оказавшая услуги)

:Items:
    :doc:`Коллекция <Collection>` **объектов** :doc:`AcceptanceCertificateItem` **, чтение** - табличная часть акта выполненных работ

:Official:
    :doc:`Official` **, чтение** - лицо, подписывающее со стороны исполнителя

:Attorney:
    :doc:`Attorney` **, чтение** - сведения о доверенности подписывающего со стороны исполнителя

:Signer:
    :doc:`Signer` **, чтение** - подписант

:AdditionalInfo:
    **Строка, чтение/запись** - дополнительные сведения


.. rubric:: Методы

.. tabs::

    .. tab:: Все актуальные

        * :meth:`AddItem() <AcceptanceCertificateSellerContent.AddItem>`

    .. tab:: Устаревшие

        .. csv-table::
            :header: "Метод", "Рекомендуемая альтернатива", "Когда устарел", "Когда удалён"

            :meth:`SaveExternalCodes() <AcceptanceCertificateSellerContent.SaveExternalCodes>`, :meth:`DataTask.SetData`, :doc:`../History/release_info/5_5_0`,

        .. method:: AcceptanceCertificateSellerContent.SaveExternalCodes()

            Сохраняет на сервере Диадока список внешних идентификаторов акта выполненных работ


.. method:: AcceptanceCertificateSellerContent.AddItem()

    Добавляет :doc:`новый элемент <AcceptanceCertificateItem>` в коллекцию *Items* и возвращает его
