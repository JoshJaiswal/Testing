=== RAW FIELDS FROM None ===
 dealName: Contoso x Fabrikam — NDA+SOW
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
 executiveSummary: Contoso is evaluating Fabrikam for implementing a document automation workflow, requiring an NDA followed by a SOW for a 12-week pilot. The deal involves mutual NDA preference and hybrid pricing model with fixed-fee pilot and usage-based scale option.      
 ndaReadiness: An NDA can be drafted now, pending template preference confirmation from Contoso.
 sowReadiness: A SOW can be drafted now, pending support SLA expectations during the pilot.
 ndaKeyPoints: - Mutual NDA preferred
- Contoso to review vendor template
- NDA execution targeted for 2026-03-18
 sowOutline: - Objective: Deploy pilot for document automation
- In-scope deliverables: Configure task, integrate JSON output, provide dashboards
- Out of scope: Full contract lifecycle management replacement       
- Timeline: 12-week pilot with mid-pilot checkpoint
 setupFee: 1800000
 billingFrequency: oneTime
 invoicingTerms: 50% on kickoff, 50% on completion
 invoiceTriggers: [{'type': 'object', 'valueObject': {'trigger': {'type': 'string', 'valueString': 'kickoff,'}}}, {'type': 'object', 'valueObject': {'trigger': {'type': 'string', 'valueString': 'completion'}}}]
 invoiceSplit: 50% 50%
 extractedConflicts: - Governing law preference not finalized        
- Liability cap language to be proposed
- Support SLA expectations during pilot not defined
 ndaTargetExecutionDate: 2026-03-13

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
 parties: PARTY::Contoso India Pvt. Ltd. | ROLE::disclosing | SIGNERS::<unknown>^^<unknown>^^<unknown>^^<unknown> || PARTY::Fabrikam Solutions Pvt. Ltd. | ROLE::receiving | SIGNERS::<unknown>^^<unknown>^^<unknown>^^<unknown>
 missingRequiredClauses: effectiveDate, definitionOfConfidentialInfo, permittedUse, permittedDisclosures, requiredDisclosureProtocol, returnOrDestructionObligations, survivalClauses, confidentialitySurvivalTrigger, noLicenseGranted, injunctiveRelief, assignmentClause, noticeProcedure, amendmentClause, terminationNoticeDays, publicityOrTrademarkRestriction, arbitrationSeat, arbitrationLanguage, arbitrationRulesOrStatute, arbitratorAppointment, disputeResolutionMechanism, jurisdiction
 unknownClauses: Open questions / missing info
 ndaSummary: Contoso and Fabrikam are negotiating a mutual NDA to explore a document automation workflow. The NDA will have a confidentiality term of 3 years, with standard exceptions and a proposed liability cap at fees paid in the last 12 months.
 ndaRiskAssessment: The NDA lacks specific clauses on permitted use, disclosure protocols, and injunctive relief, which may pose risks. Additionally, the governing law and authorized signatories are yet to be confirmed.
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'legal.governingLaw' — chose 'deal_intake' over ['nda']
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed
{
  "parties": {
    "client": {
      "name": "Contoso India Pvt. Ltd.",
      "signatories": []
    },
    "vendor": {
      "name": "Fabrikam Solutions Pvt. Ltd.",
      "signatories": []
    }
  },
  "dates": {
    "effectiveDate": "2026-03-13",
    "expirationDate": "",
    "executionDate": ""
  },
  "scope": {
    "description": "Deploy a pilot for extracting key fields from procurement documents and generating structured outputs for downstream systems.",
    "deliverables": [],
    "milestones": []
  },
  "confidentiality": {
    "term": 3,
    "obligations": [],
    "exceptions": "Standard (public info, independently developed, required disclosure)"
  },
  "commercials": {
    "totalValue": 1800000,
    "paymentTerms": "50% on kickoff, 50% on completion",
    "currency": "INR"
  },
  "legal": {
    "governingLaw": "Tamil Nadu / India",
    "jurisdiction": "India preferred",
    "disputeResolution": ""
  },
  "risks": "- Governing law preference not finalized\n- Liability cap language to be proposed\n- Support SLA expectations during pilot not defined",
  "missingFields": [
    "parties.client.signatories",
    "parties.vendor.signatories",
    "dates.expirationDate",
    "dates.executionDate",
    "scope.deliverables",
    "scope.milestones",
    "confidentiality.obligations",
    "legal.disputeResolution",
    "missingFields",
    "conflicts",
    "provenance",
    "review.status",
    "review.reviewReason",
    "review.reviewedBy",
    "review.reviewedAt"
  ],
  "conflicts": [
    {
      "field": "legal.governingLaw",
      "chosen": "Tamil Nadu / India",
      "chosenSource": "deal_intake",
      "alternatives": [
        {
          "value": "Prefer Tamil Nadu / India",
          "source": "nda"
        }
      ]
    }
  ],
  "provenance": [
    {
      "canonicalPath": "parties.client.name",
      "value": "Contoso India Pvt. Ltd.",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "parties.vendor.name",
      "value": "Fabrikam Solutions Pvt. Ltd.",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "dates.effectiveDate",
      "value": "2026-03-13",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "scope.description",
      "value": "Deploy a pilot for extracting key fields from procurement documents and generating structured outputs for downstream systems.",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "confidentiality.term",
      "value": "3",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "confidentiality.exceptions",
      "value": "Standard (public info, independently developed, required disclosure)",
      "sourceDocumentId": "",
      "sourceField": "nda",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.833
    },
    {
      "canonicalPath": "commercials.totalValue",
      "value": "1800000",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "commercials.paymentTerms",
      "value": "50% on kickoff, 50% on completion",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "commercials.currency",
      "value": "INR",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "legal.governingLaw",
      "value": "Tamil Nadu / India",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "legal.jurisdiction",
      "value": "India preferred",
      "sourceDocumentId": "",
      "sourceField": "nda",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.833
    },
    {
      "canonicalPath": "risks",
      "value": "- Governing law preference not finalized\n- Liability cap language to be proposed\n- Support SLA expectations during pilot not defined",
      "sourceDocumentId": "",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    }
  ],
  "review": {
    "status": "needs_review",
    "reviewReason": [
  }             python orchestration/functions/run_pipeline.py --input tests/fixtures/deal-intake-sample-structured.pdf --type nda --no-blobnce-platform>
INFO:__main__:[Pipeline] Starting — file=deal-intake-sample-structured.pdf, type=nda
INFO:normalization.pdf_handler:[PDF Handler] Processing: tests\fixtures\deal-intake-sample-structured.pdf
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to core-deal-intake-analyzer
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (4s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] In progress... (10s)
INFO:normalization.pdf_handler:[CU] In progress... (14s)
INFO:normalization.pdf_handler:[CU] In progress... (17s)
INFO:normalization.pdf_handler:[CU] In progress... (21s)
INFO:normalization.pdf_handler:[CU] Completed in 24.9s
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to nda-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (4s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] Completed in 10.6s
INFO:__main__:[Pipeline] Extraction complete — 2 result(s) from handler

=== RAW FIELDS FROM None ===

=== RAW FIELDS FROM None ===
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'legal.governingLaw' — chose 'deal_intake' over ['nda']
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed
{
  "parties": {
    "client": {
      "name": "Contoso India Pvt. Ltd.",
      "signatories": []
    },
    "vendor": {
      "name": "Fabrikam Solutions Pvt. Ltd.",
      "signatories": []
    }
  },
  "dates": {
    "effectiveDate": "2026-03-13",
    "expirationDate": "",
    "executionDate": ""
  },
  "scope": {
    "description": "Deploy a pilot for extracting key fields from procurement documents and generating structured outputs for downstream systems.",
    "deliverables": [],
    "milestones": []
  },
  "confidentiality": {
    "term": 3,
    "obligations": [],
    "exceptions": "Standard (public info, independently developed, required disclosure)"
  },
  "commercials": {
    "totalValue": 1800000,
    "paymentTerms": "50% on kickoff, 50% on completion",
    "currency": "INR"
  },
  "legal": {
    "governingLaw": "Tamil Nadu / India",
    "jurisdiction": "India preferred",
    "disputeResolution": ""
  },
  "risks": "- Governing law preference not finalized\n- Liability cap language to be proposed\n- Support SLA expectations during pilot not confirmed",
  "missingFields": [
    "parties.client.signatories",
    "parties.vendor.signatories",
    "dates.expirationDate",
    "dates.executionDate",
    "scope.deliverables",
    "scope.milestones",
    "confidentiality.obligations",
    "legal.disputeResolution",
    "missingFields",
    "conflicts",
    "provenance",
    "review.status",
    "review.reviewReason",
    "review.reviewedBy",
    "review.reviewedAt"
  ],
  "conflicts": [
    {
      "field": "legal.governingLaw",
      "chosen": "Tamil Nadu / India",
      "chosenSource": "deal_intake",
      "alternatives": [
        {
          "value": "Prefer Tamil Nadu / India",
          "source": "nda"
        }
      ]
    }
  ],
  "provenance": [
    {
      "canonicalPath": "parties.client.name",
      "value": "Contoso India Pvt. Ltd.",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "parties.vendor.name",
      "value": "Fabrikam Solutions Pvt. Ltd.",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "dates.effectiveDate",
      "value": "2026-03-13",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "scope.description",
      "value": "Deploy a pilot for extracting key fields from procurement documents and generating structured outputs for downstream systems.",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "confidentiality.term",
      "value": "3",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "confidentiality.exceptions",
      "value": "Standard (public info, independently developed, required disclosure)",
      "sourceDocumentId": "",
      "sourceField": "nda",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.833
    },
    {
      "canonicalPath": "commercials.totalValue",
      "value": "1800000",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "commercials.paymentTerms",
      "value": "50% on kickoff, 50% on completion",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "commercials.currency",
      "value": "INR",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "legal.governingLaw",
      "value": "Tamil Nadu / India",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    },
    {
      "canonicalPath": "legal.jurisdiction",
      "value": "India preferred",
      "sourceDocumentId": "",
      "sourceField": "nda",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.833
    },
    {
      "canonicalPath": "risks",
      "value": "- Governing law preference not finalized\n- Liability cap language to be proposed\n- Support SLA expectations during pilot not confirmed",
      "sourceDocumentId": "",
      "sourceField": "deal_intake",
      "sourceFamily": "cu_analyzer",
      "confidence": 0.0
    }
  ],
  "review": {
    "status": "needs_review",
    "reviewReason": [
      "1 field conflict(s) found"
    ],
    "reviewedBy": "",
    "reviewedAt": ""
  }
}
