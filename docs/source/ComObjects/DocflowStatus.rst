DocflowStatus
=============

Текстовое представление статуса документа, как в веб-интерфейсе Диадок

:PrimaryStatus:
  :doc:`StatusModel` **, чтение** - основная компонента статуса

:SecondaryStatus:
  :doc:`StatusModel` **, чтение** - второстепенная компонента статуса


.. warning:: Не используйте эту структуру для построения логики обработки документов в своих интеграционных решениях.
Тексты статусов пополняются новыми значениями и могут меняться.
Для оценки состояния документооборота используйте поля **SenderSignatureStatus**, **RecipientResponseStatus**, **ProxySignatureStatus**, **RoamingNotificationStatus**, **RevocationStatus**, **ResolutionStatus** объекта :doc:`документа <./DocumentBase>`
