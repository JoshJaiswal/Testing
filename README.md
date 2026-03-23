def build_appendix(canonical, styles):
    story = [
        PageBreak(),
        Paragraph("APPENDIX A — PIPELINE METADATA", styles["h1"]),
        HRFlowable(width="100%", thickness=0.5, color=YELLOW_ACCENT, spaceAfter=12),
        Paragraph("This appendix is generated automatically by the contract intelligence pipeline. It documents the AI extraction process for audit and review purposes and forms no part of the contractual terms above.", styles["body"]),
        Spacer(1, 12)
    ]
    
    missing = canonical.get("missingFields", [])
    if missing: 
        # Only show fields that are genuinely expected to be populated
        # Skip SOW-only fields when generating NDA and vice versa
        skip_always = {
            "parties.client.signatories",
            "parties.vendor.signatories",
            "dates.executionDate",
        }
        skip_sow_only = {
            "scope.sowReferenceId", "scope.locationAndTravel",
            "projectGovernance.acceptanceCriteria", "projectGovernance.acceptanceTimeline",
            "projectGovernance.changeControl", "projectGovernance.issueEscalation",
            "projectGovernance.governanceModel", "projectGovernance.keyPersonnel",
            "projectGovernance.dependencies", "projectGovernance.assumptions",
            "projectGovernance.constraints",
            "legal.warranties", "legal.indemnities", "legal.terminationForConvenience",
            "legal.terminationForCause", "legal.injunctiveRelief",
            "legal.licenseGrants", "legal.thirdPartySoftware",
            "legal.msaReference", "legal.serviceLevels",
            "commercials.expenses",
        }
        skip_nda_only = {
            "confidentiality.obligations",
        }

        # Filter to only genuinely missing important fields
        important_missing = [
            f for f in missing
            if f not in skip_always
            and f not in skip_sow_only
            and f not in skip_nda_only
        ]

        if important_missing:
            story.append(Paragraph("Missing Fields", styles["h2"]))
            story += section_rule(styles)
            story += bullet_list(important_missing, styles)
            story.append(Spacer(1, 12))
            
    story += conflict_table(canonical.get("conflicts", []), styles)
    story.append(Spacer(1, 8))
    story += provenance_table(canonical.get("provenance", []), styles)
    
    return story
