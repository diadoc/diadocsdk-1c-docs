CloudSignTask
=============

Задание на подписание документов Контур.Сертификатом

.. versionadded:: 5.2.0

.. deprecated:: 5.26.0
    На данный момент вопрос дальнейшей поддержки работы с Контур.Сертификатами не решён
    


.. rubric:: Методы

+-----------------------------+-----------------------+--------------------------+
| |CloudSignTask-AddContent|_ | |CloudSignTask-Sign|_ | |CloudSignTask-Confirm|_ |
+-----------------------------+-----------------------+--------------------------+

.. |CloudSignTask-AddContent| replace:: AddContent()
.. |CloudSignTask-Sign| replace:: Sign()
.. |CloudSignTask-Confirm| replace:: Confirm()


.. _CloudSignTask-AddContent:
.. method:: CloudSignTask.AddContent(Content, CounteragentId)

  :Content: ``BaseContent`` контент, который будет в последствии подписан. Должен быть одним из наследников :doc:`BaseContent`
  :CounteragentId: ``строка`` идентификатор контрагента, с которым идёт документооборот

  Добавляет содержимое документа в список заданий на подписание



.. _CloudSignTask-Sign:
.. method:: CloudSignTask.Sign()

  Передает на сервер запрос на подписание документов, добавленных в список и инициирует отправку СМС с кодом подтверждения на телефон пользователя



.. _CloudSignTask-Confirm:
.. method:: CloudSignTask.Confirm(SMSCode)

  :SMSCode: ``строка`` код подтверждения операции

  Подтвержает использование Контур.Сертификата для подписания набора документов



.. seealso:: :doc:`../HowTo/HowTo_cloud_certificate`
