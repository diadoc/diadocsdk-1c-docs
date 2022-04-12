Ссылки для скачивания
=====================

`Новости RSS <http://diadocsdk-1c.readthedocs.io/ru/latest/index.rss>`_


.. rubric:: Последняя версия компоненты :doc:`./History/release_info/5_37_4`

* `1С AddIn x86 <https://diadoc-api.kontur.ru/1c-addin/for_integrators/Diadoc_latest.zip>`_
* `1С AddIn x64 <https://diadoc-api.kontur.ru/1c-addin/for_integrators/Diadoc_latest_x64.zip>`_
* `COM x86 <https://diadoc-api.kontur.ru/1c-addin/for_integrators/DiadocCom_latest.zip>`_
* `COM x64 <https://diadoc-api.kontur.ru/1c-addin/for_integrators/DiadocCom_latest_x64.zip>`_


.. rubric:: Устаревшие методы и свойства объектов


.. warning:: В связи с изменениями в API Диадока после 1 октября 2021 года, методы, использующие старое представление контентов, перестанут работать и через некоторое время будут удалены из компоненты вместе с возвращаемыми ими объектами.
  Методы, которые будут затронуты:

  * :meth:`Organization.CreatePackageSendTask`
  * :meth:`DocumentBase.GetContent`
  * :meth:`DocumentBase.GetContentAsync`
  * :meth:`DocumentBase.GetBuyerContent`
  * :meth:`DocumentBase.CreateReplySendTask`
  * :meth:`DocumentPackage.CreateReplySendTask`


.. csv-table::
    :header: Метод или свойство,Рекомендуемая альтернатива, Когда устарел, Когда удалён

    :meth:`DiadocAPI.TestConnection`, :meth:`DiadocAPI.TestConnection2`, :doc:`History/release_info/5_26_3`,
    :meth:`DiadocAPI.GetVersion`, :meth:`DiadocAPI.GetFullVersion`, :doc:`History/release_info/5_29_04`,
    :meth:`DiadocAPI.CreateConnectionByCertificate`, :meth:`DiadocAPI.CreateConnectionByCertificate2`, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/Connection`.Login, :doc:`ComObjects/Connection`.SessionInfo.Login, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/Connection`.AuthenticateType, :doc:`ComObjects/Connection`.SessionInfo.AuthenticationType, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/Connection`.Certificate, :doc:`ComObjects/Connection`.SessionInfo.Certificate, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/Connection`.Token, :doc:`ComObjects/Connection`.SessionInfo.Token, :doc:`History/release_info/5_37_0`,
    :meth:`Connection.CreateCloudSignTask`, , :doc:`History/release_info/5_26_0`, :doc:`History/release_info/5_33_0`
    :meth:`Connection.GetCloudCertificates`, , :doc:`History/release_info/5_26_0`, :doc:`History/release_info/5_33_0`
    :doc:`ComObjects/Organization`.Id, :doc:`ComObjects/Organization`.Guid, :doc:`History/release_info/5_31_0`,
    :doc:`ComObjects/Organization`.EncryptedDocumentsAllowed, :meth:`Organization.GetFeatures`, :doc:`History/release_info/5_32_4`,
    :doc:`ComObjects/Organization`.AuthenticateType, :doc:`ComObjects/Organization`.MyEmployee.SessionInfo.AuthenticationType, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/Organization`.Login, :doc:`ComObjects/Organization`.MyEmployee.SessionInfo.Login, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/Organization`.Certificate, :doc:`ComObjects/Organization`.MyEmployee.SessionInfo.Certificate, :doc:`History/release_info/5_37_0`,
    :meth:`Organization.CreateSendTask`, :meth:`Organization.CreatePackageSendTask2`, :doc:`History/release_info/5_05_0`, :doc:`History/release_info/5_33_4`
    :meth:`Organization.CreateSendTaskFromFile`, :meth:`Organization.CreatePackageSendTask2`, :doc:`History/release_info/5_05_0`, :doc:`History/release_info/5_33_4`
    :meth:`Organization.CreateSendTaskFromFileRaw`, :meth:`Organization.CreatePackageSendTask2`, :doc:`History/release_info/5_05_0`, :doc:`History/release_info/5_33_4`
    :meth:`Organization.CreatePackageSendTask`, :meth:`Organization.CreatePackageSendTask2`, :doc:`History/release_info/5_27_0`,
    :meth:`Organization.SendDraftAsync`, :meth:`Organization.CreateSendDraftTask`, :doc:`History/release_info/5_18_0`, :doc:`History/release_info/5_36_8`
    :meth:`Organization.SetAndValidateAddressForCounteragent`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_05_0`,
    :meth:`Organization.GetSentDocuments`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_05_0`,
    :meth:`Organization.SetData`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_05_0`,
    :meth:`Organization.GetData`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_05_0`,
    :meth:`Organization.GetAddressForCounteragent`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_05_0`,
    :meth:`Organization.GetExtendedSignerDetails`, :meth:`MyEmployee.GetExtendedSignerDetails` или :meth:`AdminTools.GetExtendedSignerDetails`, :doc:`History/release_info/5_33_0`,
    :meth:`Organization.GetExtendedSignerDetails2`, :meth:`MyEmployee.GetExtendedSignerDetails` или :meth:`AdminTools.GetExtendedSignerDetails`, :doc:`History/release_info/5_33_0`,
    :meth:`Organization.SendFnsRegistrationMessage`, :meth:`MyEmployee.UpdateCertificateFNSRegistration` или :meth:`AdminTools.RegisterCertificateInFNS`, :doc:`History/release_info/5_37_0`,
    :meth:`Organization.GetUsers`, :meth:`Organization.GetEmployees`, :doc:`History/release_info/5_37_0`,
    :meth:`Organization.GetUserPermissions`, :doc:`ComObjects/Organization`.MyEmployee.EmployeeInfo.Permissions, :doc:`History/release_info/5_37_0`,
    :meth:`Organization.CanSendInvoice`, :meth:`MyEmployee.CanSendInvoice` или :meth:`AdminTools.CanSendInvoice`, :doc:`History/release_info/5_37_0`,
    :meth:`Organization.CreateSetExtendedSignerDetailsTask`, :meth:`MyEmployee.CreateSetExtendedSignerDetailsTask` или :meth:`AdminTools.CreateSetExtendedSignerDetailsTask`, :doc:`History/release_info/5_37_0`,
    :doc:`ComObjects/BoxInfo`.Id, :doc:`ComObjects/BoxInfo`.Guid, :doc:`History/release_info/5_31_0`,
    :doc:`ComObjects/Counteragent`.Id, :doc:`ComObjects/Counteragent`.Guid, :doc:`History/release_info/5_31_0`,
    :doc:`ComObjects/Counteragent`.OrganizationId, :doc:`ComObjects/Counteragent`.OrganizationGuid, :doc:`History/release_info/5_31_0`,
    :doc:`ComObjects/CustomDocumentToSend`.IsEncrypted, , :doc:`History/release_info/5_27_0`,
    :doc:`ComObjects/DocumentBase`.AttachmentVersion, :doc:`ComObjects/DocumentBase`.Version, :doc:`History/release_info/5_25_2`,
    :doc:`ComObjects/DocumentBase`.Type, :doc:`ComObjects/DocumentBase`.TypeNamedId, :doc:`History/release_info/5_25_2`,
    :doc:`ComObjects/DocumentBase`.OrganizationId, :doc:`ComObjects/DocumentBase`.OrganizationGuid, :doc:`History/release_info/5_31_0`,
    :doc:`ComObjects/DocumentBase`.TimestampSeconds, :doc:`ComObjects/DocumentBase`.Timestamp, :doc:`History/release_info/5_30_2`,
    :doc:`ComObjects/DocumentBase`.Status, :doc:`ComObjects/DocumentBase`.DocflowStatus или поля со статусами отдельных сущностей, :doc:`History/release_info/5_34_0`,
    :doc:`ComObjects/DocumentBase`.Resolutions, :meth:`DocumentBase.GetResolutions`, :doc:`History/release_info/5_34_0`,
    :doc:`ComObjects/DocumentBase`.ResolutionRequests, :meth:`DocumentBase.GetResolutionRequests`, :doc:`History/release_info/5_34_0`,
    :doc:`ComObjects/DocumentBase`.ResolutionRequestDenials, :meth:`DocumentBase.GetResolutionRequestDenials`, :doc:`History/release_info/5_34_0`,
    :doc:`ComObjects/DocumentBase`.HasCustomPrintForm, :meth:`DocumentBase.DetectCustomPrintForm`, :doc:`History/release_info/5_35_0`
    :meth:`DocumentBase.GetContent`, :meth:`DocumentBase.GetDynamicContent`, :doc:`History/release_info/5_28_0`,
    :meth:`DocumentBase.GetContentAsync`, , :doc:`History/release_info/5_28_0`,
    :meth:`DocumentBase.GetBuyerContent`, :meth:`DocumentBase.GetDynamicContent`, :doc:`History/release_info/5_28_0`,
    :meth:`DocumentBase.CreateReplySendTask`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`,
    :meth:`DocumentBase.Accept`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.Reject`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.RejectAsync`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.SendRevocationRequest`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.AcceptRevocationRequest`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.RejectRevocationRequest`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.SendCorrectionRequest`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.SendCorrectionRequestAsync`, :meth:`DocumentBase.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`, :doc:`History/release_info/5_37_0`
    :meth:`DocumentBase.GetComment`, :meth:`DocumentBase.GetAnyComment`, :doc:`History/release_info/5_20_3`,
    :meth:`DocumentBase.GetRejectionComment`, :meth:`DocumentBase.GetAnyComment`, :doc:`History/release_info/5_20_3`,
    :meth:`DocumentBase.GetAmendmentRequestedComment`, :meth:`DocumentBase.GetAnyComment`, :doc:`History/release_info/5_20_3`,
    :meth:`DocumentBase.SetOneSDocumentId`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_29_09`,
    :meth:`DocumentBase.ReSetOneSDocumentId`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_29_09`,
    :meth:`DocumentBase.AddSubordinateOneSDocumentId`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_29_09`,
    :meth:`DocumentBase.RemoveSubordinateOneSDocumentId`, :meth:`Organization.CreateDataTask`, :doc:`History/release_info/5_29_09`,
    :meth:`DocumentPackage.CreateReplySendTask`, :meth:`DocumentPackage.CreateReplySendTask2`, :doc:`History/release_info/5_27_0`,
    :doc:`ComObjects/Entity`.AttachmentVersion, , :doc:`History/release_info/5_25_2`,