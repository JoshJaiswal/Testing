python orchestration/functions/run_pipeline.py --input tests/fixtures/deal-intake-sample-structured.pdf --type nda --no-blob
INFO:__main__:[Pipeline] Starting — file=deal-intake-sample-structured.pdf, type=nda
INFO:normalization.pdf_handler:[PDF Handler] Processing: tests\fixtures\deal-intake-sample-structured.pdf
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to core-deal-intake-analyzer
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] In progress... (10s)
INFO:normalization.pdf_handler:[CU] In progress... (14s)
INFO:normalization.pdf_handler:[CU] In progress... (18s)
INFO:normalization.pdf_handler:[CU] Completed in 21.1s
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to nda-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (4s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] Completed in 10.9s
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
    "deliverables": [
      ". Configure Content Understanding custom task \\` deal-intake-doc\\` for extracting deal facts from transcripts/notes.",
      "Integrate extracted JSON output into Contoso's internal workflow tool (REST webhook).",
      "Provide dashboards for intake volume, missing-field rate, and confidence distribution.",
      "Knowledge transfer session + admin guide."
    ],
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
  "risks": "- Governing law preference not confirmed\n- Liability cap language to be proposed",
  "missingFields": [
    "parties.client.signatories",
    "parties.vendor.signatories",
    "dates.expirationDate",
    "dates.executionDate",
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
      "canonicalPath": "scope.deliverables",
      "value": "['. Configure Content Understanding custom task \\\\` deal-intake-doc\\\\` for extracting deal facts from transcripts/notes.', \"Integrate extracted JSON output into Contoso's internal workflow tool (REST webhook).\", 'Provide dashboards for intake volume, missing-field rate, and confidence distribution.', 'Knowledge transfer session + admin guide.']",
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
      "value": "- Governing law preference not confirmed\n- Liability cap language to be proposed",
      "sourceDocumentId": "",
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
ntake-sample-structured.pdf --type auto --no-blob --output tests/output/canonical-result.json
INFO:__main__:[Pipeline] Starting — file=deal-intake-sample-structured.pdf, type=auto
INFO:normalization.pdf_handler:[PDF Handler] Processing: tests\fixtures\deal-intake-sample-structured.pdf
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to core-deal-intake-analyzer
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] In progress... (9s)
INFO:normalization.pdf_handler:[CU] In progress... (13s)
INFO:normalization.pdf_handler:[CU] In progress... (16s)
INFO:normalization.pdf_handler:[CU] In progress... (19s)
INFO:normalization.pdf_handler:[CU] Completed in 22.3s
INFO:normalization.pdf_handler:[CU] deal_intake done — _source=deal_intake, confidence=0.0
INFO:normalization.pdf_handler:[PDF Handler] Detected type: both
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to nda-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] Completed in 9.2s
INFO:normalization.pdf_handler:[CU] nda done — _source=nda, confidence=0.837
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to sow-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
 3 result(s) from handler
 3 result(s) from handler
WARNING:orchestration.functions.map_to_canonical:[Mapper] No mapping found for source 'sow' analyzer 'sow-analyzer-extractor' — passing through raw
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'legal.governingLaw' — chose 'deal_intake' over ['nda']
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed             python orchestration/functions/run_pipeline.py --input tests/fixtures/deal-intake-sample-structured.pdf --type auto --no-blob --output tests/output/canonical-result.json
INFO:__main__:[Pipeline] Starting — file=deal-intake-sample-structured.pdf, type=auto
INFO:normalization.pdf_handler:[PDF Handler] Processing: tests\fixtures\deal-intake-sample-structured.pdf
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to core-deal-intake-analyzer-02
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[PDF Handler] Detected type: both
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to nda-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] Completed in 9.3s
INFO:normalization.pdf_handler:[CU] nda done — _source=nda, confidence=0.843
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to sow-analyzer-extractor-02
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] In progress... (9s)
INFO:normalization.pdf_handler:[CU] In progress... (12s)
INFO:normalization.pdf_handler:[CU] In progress... (15s)
INFO:normalization.pdf_handler:[CU] Completed in 18.3s
INFO:normalization.pdf_handler:[CU] sow done — _source=sow, confidence=0.681
INFO:__main__:[Pipeline] Extraction complete — 3 result(s) from handler
WARNING:orchestration.functions.map_to_canonical:[Mapper] No mapping found for source 'sow' analyzer 'sow-analyzer-extractor-02' — passing through raw
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'legal.governingLaw' — chose 'deal_intake' over ['nda']
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed
INFO:__main__:[Pipeline] Output saved to tests/output/canonical-result.json
PS C:\Users\DZ975HB\Documents\contract-intelligence-platform> python orchestration/functions/run_pipeline.py --input tests/fixtures/deal-intake-sample-structured.pdf --type auto --no-blob --output tests/output/canonical-result.json
INFO:__main__:[Pipeline] Starting — file=deal-intake-sample-structured.pdf, type=auto
INFO:normalization.pdf_handler:[PDF Handler] Processing: tests\fixtures\deal-intake-sample-structured.pdf
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to core-deal-intake-analyzer-02       
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] In progress... (9s)
INFO:normalization.pdf_handler:[CU] In progress... (12s)
INFO:normalization.pdf_handler:[CU] In progress... (16s)
INFO:normalization.pdf_handler:[CU] In progress... (19s)
INFO:normalization.pdf_handler:[CU] Completed in 22.0s
INFO:normalization.pdf_handler:[CU] deal_intake done — _source=deal_intake, confidence=0.814
INFO:normalization.pdf_handler:[PDF Handler] Detected type: both
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to nda-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] Completed in 9.3s
INFO:normalization.pdf_handler:[CU] nda done — _source=nda, confidence=0.848
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to sow-analyzer-extractor-02
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (6s)
INFO:normalization.pdf_handler:[CU] In progress... (10s)
ctor-02' — passing through raw
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'legal.governingLaw' — chose 'deal_intake' over ['nda']
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed             python orchestration/functions/run_pipeline.py --input tests/fixtures/deal-intake-sample-structured.pdf --type auto --no-blob --output tests/output/canonical-result.json\DZ975HB\Documents\contract-intelligence-platform>
INFO:__main__:[Pipeline] Starting — file=deal-intake-sample-structured.pdf, type=auto
INFO:normalization.pdf_handler:[PDF Handler] Processing: tests\fixtures\deal-intake-sample-structured.pdf
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to core-deal-intake-analyzer-02
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] In progress... (10s)
INFO:normalization.pdf_handler:[CU] In progress... (13s)
INFO:normalization.pdf_handler:[CU] In progress... (17s)
INFO:normalization.pdf_handler:[CU] In progress... (20s)
INFO:normalization.pdf_handler:[CU] Completed in 23.4s
INFO:normalization.pdf_handler:[CU] deal_intake done — _source=deal_intake, confidence=0.811
INFO:normalization.pdf_handler:[PDF Handler] Detected type: both
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to nda-analyzer-extractor
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (3s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] Completed in 9.9s
INFO:normalization.pdf_handler:[CU] nda done — _source=nda, confidence=0.84
INFO:normalization.pdf_handler:[CU] Submitted tests\fixtures\deal-intake-sample-structured.pdf to sow-analyzer-extractor-02
INFO:normalization.pdf_handler:[CU] In progress... (0s)
INFO:normalization.pdf_handler:[CU] In progress... (4s)
INFO:normalization.pdf_handler:[CU] In progress... (7s)
INFO:normalization.pdf_handler:[CU] In progress... (10s)
INFO:normalization.pdf_handler:[CU] In progress... (14s)
INFO:normalization.pdf_handler:[CU] Completed in 17.3s
INFO:normalization.pdf_handler:[CU] sow done — _source=sow, confidence=0.69
INFO:__main__:[Pipeline] Extraction complete — 3 result(s) from handler
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'parties.client.name' — chose 'deal_intake' over ['nda', 'sow']
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'commercials.paymentTerms' — chose 'deal_intake' over ['sow']
INFO:orchestration.functions.merge_engine:[Merge] Conflict on 'legal.governingLaw' — chose 'deal_intake' over ['nda', 'sow']
INFO:__main__:[Pipeline] Merge complete
INFO:__main__:[Pipeline] Schema validation passed
INFO:__main__:[Pipeline] Output saved to tests/output/canonical-result.json
