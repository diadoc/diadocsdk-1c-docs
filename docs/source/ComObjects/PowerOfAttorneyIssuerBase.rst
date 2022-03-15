PowerOfAttorneyIssuerBase
=========================

Базовый интерфейс для разных |PowerOfAttorneyIssuerBase-Inheritable|_ в МЧД


.. rubric:: Свойства

:Type:
  **Строка, чтение** - тип доверителя. :doc:`Возможные значения <./Enums/IssuerType>`


.. rubric:: Производные объекты

.. |PowerOfAttorneyIssuerBase-Inheritable| replace:: видов доверителей
.. _PowerOfAttorneyIssuerBase-Inheritable:


====================================== ===========================================
Наследники                             Описание
====================================== ===========================================
:doc:`PowerOfAttorneyForeignEntity`    Доверитель - иностранная организация
:doc:`PowerOfAttorneyIndividualEntity` Доверитель - индивидуальный предприниматель
:doc:`PowerOfAttorneyLegalEntity`      Доверитель - юридическое лицо
:doc:`PowerOfAttorneyPhysicalEntity`   Доверитель - физическое лицо
====================================== ===========================================
