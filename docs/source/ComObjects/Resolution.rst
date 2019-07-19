Resolution
==========

Согласование документа


.. rubric:: Свойства

:Author:
  **Строка, чтение** - ФИО согласователя

:CreationDate:
  **Дата, чтение** - дата-время создания согласования

:Comment:
  **Строка, чтение** - комментарий к согласованию

:ResolutionType:
  **Строка, чтение** - тип действия по согласованию. |Resolution-Type|_

:TargetDepartment:
  :doc:`Department <Department>` **, чтение** - подразделение организации, в которое направлен запрос

:TargetUser:
  :doc:`OrganizationUser <OrganizationUser>` **, чтение** - пользователь, которому направлен запрос


.. rubric:: Дополнительная информация


.. |Resolution-Type| replace:: Возможные значения
.. _Resolution-Type:

============================= ======================================
Значение *ResolutionType*     Описание
============================= ======================================
SignatureRequest              запрос на подпись документа
SignatureApprove              подпись документа
SignatureDisapprove           отказ в подписи документа
ResolutionRequest             запрос согласования документа
ResolutionApprove             согласование документа
ResolutionDisapprove          отказ в согласовании документа
RevocationApprove             подтверждение аннулирования документа
RevocationDisapprove          отказ в аннулировании документа
RevocationRequest             запрос аннулирования документа
FormalizedSignatureDisapprove формализованный отказ в подписи
InvoiceCorrectionRequest      уведомление об уточнении счета-фактуры
============================= ======================================
