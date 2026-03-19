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
