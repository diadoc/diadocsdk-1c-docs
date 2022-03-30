SessionInfo
===========


Информация об авторизационной сессии

.. versionadded:: 5.37.0


.. rubric:: Свойства

:AuthenticationType:
    **Строка, чтение** - тип авторизации. :doc:`Возможные значения <./Enums/AuthenticationType>`


:Certificate:
    :doc:`PersonalCertificate` **, чтение** - информация о сертификате, использованном для авторизации. Может быть :doc:`пустым <Descriptions/Empty_Com_Object>`


:Login:
    **Строка, чтение** - логин, использованный для авторизации


:Token:
    **Строка, чтение** - полученный авторизационный токен