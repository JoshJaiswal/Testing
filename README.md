
=== RAW FIELDS FROM None ===
 dealName: Contoso x Fabrikam — NDA + SOW
 customerLegalName: Contoso India Pvt. Ltd.
 vendorLegalName: Fabrikam Solutions Pvt. Ltd.
 participants: [{'type': 'object', 'valueObject': {'name': {'type': 'string', 'valueString': 'Anita Rao'}, 'role': {'type': 'string', 'valueString': 'Director, Procurement'}, 'company': {'type': 'string', 'valueString': 'Contoso'}}}, {'type': 'object', 'valueObject': {'name': {'type': 'string', 'valueString': 'Riya lyer'}, 'role': {'type': 'string', 'valueString': 'Account Executive'}, 'company': {'type': 'string', 'valueString': 'Fabrikam'}}}, {'type': 'object', 'valueObject': {'name': {'type': 'string', 'valueString': 'Legal (TBD)'}, 'role': {'type': 'string', 'valueString': 'Contracts counsel'}, 'company': {'type': 'string'}}}]
 requestedDocuments: [{'type': 'object', 'valueObject': {'docType': {'type': 'string', 'valueString': 'NDA'}, 'notes': {'type': 'string', 'valueString': 'Mutual NDA preferred; Contoso will review vendor template but may require their template.'}}}, {'type': 'object', 'valueObject': {'docType': {'type': 'string', 'valueString': 'SOW)'}, 'notes': {'type': 'string', 'valueString': 'Required for pilot delivery and support.'}}}]
 requestedDocumentTypes: NDA+SOW
 ndaRequired: yes
 ndaType: mutual
 confidentialityTermYears: 3
 governingLaw: Tamil Nadu / India
 sowObjective: Deploy a pilot for extracting key fields from procurement documents and generating structured outputs for downstream systems.
 inScope: [{'type': 'object', 'valueObject': {'item': {'type': 'string', 'valueString': '. Configure Content Understanding custom task \\` deal-intake-doc\\` for extracting deal facts from transcripts/notes.'}}}, {'type': 'object', 'valueObject': {'item': {'type': 'string', 'valueString': "Integrate extracted JSON output into Contoso's internal workflow tool (REST webhook)."}}}, {'type': 'object', 'valueObject': {'item': {'type': 'string', 'valueString': 'Provide dashboards for intake volume, missing-field rate, and confidence distribution.'}}}, {'type': 'object', 'valueObject': {'item': {'type': 'string', 'valueString': 'Knowledge transfer session + admin guide.'}}}]
 outOfScope: [{'type': 'object', 'valueObject': {'item': {'type': 'string', 'valueString': 'Full contract lifecycle management replacement'}}}, {'type': 'object', 'valueObject': {'item': {'type': 'string', 'valueString': 'Data warehouse buildout'}}}]
 pricingModel: hybrid
 currency: INR
 securityRequirements: Encryption at rest and in transit; audit logs; role-based access
 dataResidency: India
 liabilityCap: Proposed cap at fees paid in last 12 months
 ipOwnership: Customer retains ownership of customer data; vendor retains platform IP; customer wants a license to outputs.
 openQuestionsText: - Who will sign (authorized signatory) on both sides?
- Final governing law / venue requirement
- Whether subcontractors will access data
- Support SLA expectations during pilot
- Any third-party pen-test requirements
 nextSteps: [{'type': 'object', 'valueObject': {'owner': {'type': 'string', 'valueString': 'Riya'}, 'action': {'type': 'string', 'valueString': 'Fabrikam to share NDA template today'}, 'dueDate': {'type': 'date', 'valueDate': '2026-03-13'}}}, {'type': 'object', 'valueObject': {'owner': {'type': 'string', 'valueString': 'Anita;'}, 'action': {'type': 'string', 'valueString': 'Contoso to confirm template preference'}, 'dueDate': {'type': 'date', 'valueDate': '2026-03-15'}}}, {'type': 'object', 'valueObject': {'owner': {'type': 'string', 'valueString': 'Legal-TBD;'}, 'action': {'type': 'string', 'valueString': 'Fabrikam legal to propose liability cap language'}, 'dueDate': {'type': 'date', 'valueDate': '2026-03-16'}}}, {'type': 'object', 'valueObject': {'owner': {'type': 'string', 'valueString': 'Naveen;'}, 'action': {'type': 'string', 'valueString': 'Solutions team to send pilot plan & architecture overview'}, 'dueDate': {'type': 'date', 'valueDate': '2026-03-17'}}}]
 executiveSummary: Contoso is evaluating Fabrikam for implementing a document automation workflow, requiring an NDA followed by a SOW for a 12-week pilot. The deal involves mutual NDA preference and a hybrid pricing model with fixed-fee and usage-based options.     
 ndaReadiness: An NDA can be drafted now, pending template preference confirmation from Contoso.
 sowReadiness: A SOW can be drafted now, pending pilot plan and architecture overview from the solutions team.
 ndaKeyPoints: - Mutual NDA preferred
- Contoso to review vendor template
- NDA execution targeted for 2026-03-18
 sowOutline: - Objective: Deploy pilot for document automation
- In-scope deliverables: Configure tasks, integrate JSON output, provide dashboards
- Out of scope: Full contract lifecycle management replacement
- Timeline: 12-week pilot with weekly status calls
 setupFee: 1800000
 billingFrequency: oneTime
 invoicingTerms: 50% on kickoff, 50% on completion
 invoiceTriggers: [{'type': 'object', 'valueObject': {'trigger': {'type': 'string', 'valueString': 'kickoff,'}}}, {'type': 'object', 'valueObject': {'trigger': {'type': 'string', 'valueString': 'completion'}}}]
 invoiceSplit: 50% 50%
 extractedConflicts: - Governing law preference not finalized
- Liability cap language to be proposed
- Support SLA expectations during pilot not defined

=== RAW FIELDS FROM None ===
 disclosingParty: Contoso India Pvt. Ltd.
 receivingParty: Fabrikam Solutions Pvt. Ltd.
 mutualOrUnilateral: mutual
 exclusionsFromConfidentialInfo: Standard (public info, independently developed, required disclosure)
 confidentialityTermYears: 3
 intellectualPropertyOwnership: Customer retains ownership of customer data; vendor retains platform IP; customer wants a license to outputs.
 liabilityLimitations: Proposed cap at fees paid in last 12 months
 dataSecurityRequirements: Encryption at rest and in transit; audit logs; role-based access
 dataResidencyRequirements: India preferred
 personalDataProcessing: yes
 governingLaw: Prefer Tamil Nadu / India
 parties: PARTY::Contoso India Pvt. Ltd. | ROLE::disclosing | SIGNERS::<Authorized Signatory>^^<Title>^^<Place>^^<YYYY-MM-DD> ;; PARTY::Fabrikam Solutions Pvt. Ltd. | ROLE::receiving | SIGNERS::<Authorized Signatory>^^<Title>^^<Place>^^<YYYY-MM-DD>
 missingRequiredClauses: effectiveDate, definitionOfConfidentialInfo, permittedUse, permittedDisclosures, requiredDisclosureProtocol, returnOrDestructionObligations, survivalClauses, confidentialitySurvivalTrigger, noLicenseGranted, injunctiveRelief, assignmentClause, noticeProcedure, amendmentClause, terminationNoticeDays, publicityOrTrademarkRestriction, arbitrationSeat, arbitrationLanguage, arbitrationRulesOrStatute, arbitratorAppointment, disputeResolutionMechanism, jurisdiction
 unknownClauses: Open questions / missing info
 ndaSummary: Contoso and Fabrikam are negotiating a mutual NDA to explore a document automation workflow project, with a confidentiality term of 3 years and a liability cap discussion ongoing.
 ndaRiskAssessment: Potential risks include undefined effective date, missing clauses on permitted use and disclosures, and open questions regarding signatories and governing law.
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed
{
  "parties": {
    "client": {
      "name": "",
      "signatories": []
    },
    "vendor": {
      "name": "",
      "signatories": []
    }
  },
  "dates": {
    "effectiveDate": "",
    "expirationDate": "",
    "executionDate": ""
  },
  "scope": {
    "description": "",
    "deliverables": [],
    "milestones": []
  },
  "confidentiality": {
    "term": "",
    "obligations": [],
    "exceptions": []
  },
  "commercials": {
    "totalValue": "",
    "paymentTerms": "",
    "currency": ""
  },
  "legal": {
    "governingLaw": "Prefer Tamil Nadu / India",
    "jurisdiction": "",
    "disputeResolution": ""
  },
  "risks": [],
  "missingFields": [
    "parties.client.name",
    "parties.client.signatories",
    "parties.vendor.name",
    "parties.vendor.signatories",
    "dates.effectiveDate",
    "dates.expirationDate",
    "dates.executionDate",
    "scope.description",
    "scope.deliverables",
    "scope.milestones",
    "confidentiality.term",
    "confidentiality.obligations",
    "confidentiality.exceptions",
    "commercials.totalValue",
    "commercials.paymentTerms",
    "commercials.currency",
    "legal.jurisdiction",
    "legal.disputeResolution",
    "risks",
    "missingFields",
    "conflicts",
    "provenance",
    "review.status",
    "review.reviewReason",
    "review.reviewedBy",
    "review.reviewedAt"
  ],
  "conflicts": [],
  "provenance": [
    {
      "canonicalPath": "legal.governingLaw",
      "value": "Prefer Tamil Nadu / India",
      "sourceDocumentId": "",
      "sourceField": "nda",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.99
    }
  ],
  "review": {
    "status": "needs_review",
    "reviewReason": [
      "Critical fields missing: ['parties.client.name', 'parties.vendor.name', 'dates.effectiveDate']"
    ],
    "reviewedBy": "",
    "reviewedAt": ""
  }
}
