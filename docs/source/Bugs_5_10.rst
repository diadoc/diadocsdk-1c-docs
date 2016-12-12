Ошибки, исправленные в версии 5.10
==================================

v5.10.1 - 07.12.2016
-----------------------

- Исправлена ошибка связанная с получением подписи :doc:`GetRecipientSignature <GetRecipientSignature>` для УПД.

v5.10.2 - 08.12.2016
-----------------------

- Исправлена валидация актов при вызове :doc:`ValidateContent <ValidateContent-(SendTask)>` в случае отрицательного количества позиций. 
- Исправлена валидация точности поля **Quantity** :doc:`ExtendedInvoiceItem <ExtendedInvoiceItem>`.

v5.10.3 - 12.12.2016
-----------------------

- Валидация акта :doc:`ValidateContent <ValidateContent-(SendTask)>` теперь допускает 5 знаков после запятой для количества - поле **Quantity** :doc:`AcceptanceCertificateItem <AcceptanceCertificateItem>`.
- Исправлено возвращаемое значение :doc:`GetExtendedSignerDetails <GetExtendedSignerDetails>` на :doc:`ExtendedSignerDetails <ExtendedSignerDetails>`.