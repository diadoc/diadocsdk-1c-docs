CreateCloudSignTask
===================

Метод объекта :doc:`DiadocConnection <Connection>`

**Синтаксис**


CreateCloudSignTask(<Thumbprint>)

**Параметры**


-  **<Thumbprint>** (строка, обязательный) - отпечаток облачного сертификата пользователя.

Отпечаток облачной подписи можно получить из объекта :doc:`CloudCertificateInfo <CloudCertificateInfo>` :doc:`коллекции <Collection>`, возвращённой методом :doc:`DiadocConnection <Connection>`.:doc:`GetCloudCertificates() <GetCloudCertificates>`

**Возвращаемое значение**


:doc:`CloudSignTask <CloudSignTask>`.

**Описание**


Позволяет создать задание для подписания облачной подписью набора документов.
