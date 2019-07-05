AcceptanceCertificateBuyerContent
=================================

Содержание титула покупателя *Акта о выполнении работ* в формате приказа `ММВ-7-6/172@ <https://normativ.kontur.ru/document?moduleId=1&documentId=261859&rangeId=83259>`_ .
Является производным объектом от :doc:`BaseContent <BaseContent>`

.. deprecated:: 5.27.0
  Используйте :doc:`DynamicContent`


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип документа. Константа ``XmlAcceptanceCertificateBuyerTitle``

:Complaints:
  **Строка, чтение/запись** - претензии

:SignatureDate:
  **Дата, чтение/запись** - дата подписи акта заказчиком

:Official:
  :doc:`Official <Official>` **, чтение** - лицо, подписывающее со стороны заказчика

:Attorney:
  :doc:`Attorney <Attorney>` **, чтение** - сведения о доверенности подписывающего со стороны закзачика

:Signer:
  :doc:`Signer <Signer>` **, чтение** - подписант

:AdditionalInfo:
  **Строка, чтение/запись** - дополнительные сведения
