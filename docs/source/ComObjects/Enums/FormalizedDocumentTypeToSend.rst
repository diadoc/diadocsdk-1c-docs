FormalizedDocumentTypeToSend
============================


=========================================================== ==================================================================== =========================================
Значение                                                    Описание                                                             Тип *DocumentToSend*
=========================================================== ==================================================================== =========================================
Invoice                                                     счет-фактура в формате 93 приказа ФНС                                :doc:`../InvoiceToSend`
InvoiceCorrection                                           корректировочный счет-фактура в формате 93 приказа ФНС               :doc:`../InvoiceCorrectionToSend`
InvoiceRevision                                             исправительный счет-фактура в формате 93 приказа ФНС                 :doc:`../InvoiceRevisionToSend`
InvoiceCorrectionRevision                                   исправление корректировочного счета-фактуры в формате 93 приказа ФНС :doc:`../InvoiceCorrectionRevisionToSend`
XmlAcceptanceCertificate                                    акт о выполнении работ в формате 172 приказа ФНС                     :doc:`../XmlActToSend`
XmlTorg12                                                   ТОРГ-12 в формате 172 приказа ФНС                                    :doc:`../XmlTorg12ToSend`
UniversalTransferDocument                                   УПД в формате 155 приказа ФНС                                        :doc:`../UtdToSend`
UniversalTransferDocumentRevision                           исправление УПД в формате 155 приказа ФНС                            :doc:`../UtdToSend`
UniversalCorrectionDocument                                 УКД в формате 189 приказа ФНС                                        :doc:`../UcdToSend`
UniversalCorrectionDocumentRevision                         исправление УКД в формате 189 приказа ФНС                            :doc:`../UcdToSend`
UtdTorg12                                                   ТОРГ-12 в формате 155 приказа ФНС                                    :doc:`../UtdToSend`
UtdAcceptanceCertificate                                    акт о выполнении работ в формате 155 приказа ФНС                     :doc:`../UtdToSend`
UtdInvoice                                                  счет-фактура в формате 155 приказа ФНС                               :doc:`../UtdToSend`
UcdInvoiceCorrection                                        корректировка счета-фактуры в формате 189 приказа ФНС                :doc:`../UtdToSend`
TovTorg                                                     Торг-12 в формате 551-го приказа ФНС                                 :doc:`../TovTorgToSend`
XmlAcceptanceCertificate552                                 акт в формате 552-го приказа ФНС                                     :doc:`../XmlAct552ToSend`
один из :doc:`DocumentVersion.Version <../DocumentVersion>` произвольный формализованный документ                                :doc:`../CustomDocumentToSend`
Document (для :meth:`PackageSendTask.AddDocumentFromFile`)  произвольный формализованный документ                                :doc:`../CustomDocumentToSend`
=========================================================== ==================================================================== =========================================
