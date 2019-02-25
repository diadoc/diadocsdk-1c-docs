Как работать с шаблонами
========================

Шаблон - документ, отправленный без подписи.
Шаблоны полезны, если необходимо до отправки показать документ контрагенту.
Из шаблона можно создать обычный :doc:`документ <Document>`


Как отправить шаблон документа
------------------------------

Для отправки шаблона документа необходимо
    -  находиться в контексте :doc:`организации <Organization>`
    -  вызвать метод :doc:`CreateTemplateSendTask <CreateTemplateSendTask>`
    -  заполнить :doc:`полученный объект <TemplateSendTask>`
    -  вызвать метод :doc:`Send <Send-(TemplateSendTask)>`

Можно отправлять как однотитульные документы, так и двухтитульные документы - для этого у :doc:`шаблона на отправку <TemplateToSend>` есть методы :doc:`LoadSellerTitleFromFile <LoadSellerTitleFromFile>` и :doc:`LoadBuyerTitleFromFile <LoadBuyerTitleFromFile>`

Сами титулы при этом компонента не готовит - подготовкой контента пользователь занимается самостоятельно.


Пример отправки шаблона двух титулов УПД СЧФДОП
   ::

            Функция ОтправитьШаблонУПДСЧФДОП(BoxId_ОтправителяШаблона,
                                             BoxId_ПолучателяШаблона,
                                             BoxId_ОтправителяДокумента,
                                             BoxId_ПолучателяДокумента,
                                             ПутьДоФайлаТитулаПродавца,
                                             ПутьДоФайлаТитулаПокупателя)

                Отправитель = dd_Connection.GetOrganizationById(BoxId_ОтправителяШаблона);
              
                TemplateSendTask = Organization.CreateTemplateSendTask();
                TemplateSendTask.ToBoxId          = BoxId_ПолучателяШаблона;
                TemplateSendTask.MessageFromBoxId = BoxId_ОтправителяДокумента;
                TemplateSendTask.MessageToBoxId   = BoxId_ПолучателяДокумента;
                
                TemplateToSend = dd_TemplateSendTask.AddTemplate("UniversalTransferDocument");
                TemplateToSend.Function = "InvoiceAndBasic";
                TemplateToSend.LoadSellerTitleFromFile(ПутьДоФайлаТитулаПродавца);
                TemplateToSend.LoadBuyerTitleFromFile(ПутьДоФайлаТитулаПокупателя);
              
                Возврат TemplateSendTask.Send();

            КонецФункции



Как получить документы, созданные из отправленного шаблона
----------------------------------------------------------


После отправки шаблона, вернётся объект :doc:`Template <Template>`, в котором можно удет узнать ID отправленного шаблона. Зная этот идентификатор, можно запросить шаблон повторно, и если из шаблона был создан документ, то в соответствующей коллекции будет указаны ID таких документов. Далее можно вызвать метод :doc:`GetDocumentById <GetDocumentById>`:

   ::
   
            Функция ПолучитьШаблонныеДокументы(Organization, CounterAgent)

                // Для простоты рассмотрим случай, когда отправитель шаблона является получателем документа
                SendedTemplate = ОтправитьШаблонУПДСЧФДОП(Organization.Id, CounterAgent.Id, CounterAgent.Id, Organization.Id, "C:\sellertitle.xml", "C:\buyertitle.xml");
                TemplateId = SendedTemplate.TemplateId;
                
                //
                //Прошло некоторое время, чтобы контрагент успел обработать шаблон
                //
                
                RefreshedTemplate = Organization.GetTemplate(TemplateId);
                FirstTemplateSellerTitle = RefreshedTemplate.Entities.GetItem(0);
                ИдентификаторыДокументовСозданныхИзШаблона = FirstTemplateSellerTitle.CreatedDocumentIds;
                
                Возврат ИдентификаторыДокументовСозданныхИзШаблона;

            КонецФункции


.. toctree::
   :name: Auto
   :hidden:
   
   TemplateSendTask <TemplateSendTask>
   TemplateToSend <TemplateToSend>
   TransformTemplateTask <TransformTemplateTask>
   Template <Template>
   DocumentTransformation <DocumentTransformation>
   Entity <Entity>
