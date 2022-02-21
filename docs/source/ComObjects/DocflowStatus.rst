DocflowStatus
=============

Текстовое представление статуса документа, как в веб-интерфейсе Диадок

:PrimaryStatus:
  :doc:`StatusModel` **, чтение** - основная компонента статуса

:SecondaryStatus:
  :doc:`StatusModel` **, чтение** - второстепенная компонента статуса

:PowerOfAttorneyStatus:
  :doc:`PowerOfAttorneyStatus` **, чтение** - Сводный статус всех МЧД, использованных при подписании сущностей документа



.. warning:: Не используйте поля **PrimaryStatus** и **SecondaryStatus** для построения логики обработки документов в интеграционных решениях.

  Тексты статусов пополняются новыми значениями и могут меняться.

  Для оценки состояния документооборота используйте поля **SenderSignatureStatus**, **RecipientResponseStatus**, **ProxySignatureStatus**, **RoamingNotificationStatus**, **RevocationStatus**, **ResolutionStatus** объекта :doc:`документа <./DocumentBase>`
