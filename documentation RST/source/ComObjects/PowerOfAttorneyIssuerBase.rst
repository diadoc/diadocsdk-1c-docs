PowerOfAttorneyIssuerBase
=========================

Базовый интерфейс для разных :ref:`видов доверителей <PowerOfAttorneyIssuerBase-Inheritable>` в МЧД


.. rubric:: Свойства

:Type:
    **Строка, чтение** - тип доверителя. :doc:`Возможные значения <./Enums/IssuerType>`


.. rubric:: Объекты, наследующие текущий интерфейс

.. _PowerOfAttorneyIssuerBase-Inheritable:


====================================== ===========================================
Наследники                             Описание
====================================== ===========================================
:doc:`PowerOfAttorneyForeignEntity`    Доверитель - иностранная организация
:doc:`PowerOfAttorneyIndividualEntity` Доверитель - индивидуальный предприниматель
:doc:`PowerOfAttorneyLegalEntity`      Доверитель - юридическое лицо
:doc:`PowerOfAttorneyPhysicalEntity`   Доверитель - физическое лицо
====================================== ===========================================