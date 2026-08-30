# ======================================
# NEXORA ANALYTICS
# AI DIGITAL MARKETING CAMPAIGN SIMULATOR
# ======================================


def calculate_campaign(
    budget,
    impressions,
    ctr,
    registration_rate,
    lead_rate,
    customer_rate
):
    """Calculate campaign funnel and marketing KPIs."""

    clicks = int(impressions * ctr / 100)

    registrations = int(
        clicks * registration_rate / 100
    )

    leads = int(
        registrations * lead_rate / 100
    )

    customers = int(
        leads * customer_rate / 100
    )

    cpc = budget / clicks if clicks else 0
    cpl = budget / leads if leads else 0
    cac = budget / customers if customers else 0

    return {
        "impressions": impressions,
        "clicks": clicks,
        "registrations": registrations,
        "leads": leads,
        "customers": customers,
        "cpc": round(cpc, 2),
        "cpl": round(cpl, 2),
        "cac": round(cac, 2)
    }


def marketing_decision_engine(
    ctr,
    cpl,
    conversion_rate
):
    """Generate campaign optimization recommendations."""

    recommendations = []

    if ctr < 2:
        recommendations.append(
            "Improve ad creative and headline."
        )
    elif ctr < 5:
        recommendations.append(
            "Test new hooks and CTAs."
        )
    else:
        recommendations.append(
            "CTR is strong. Consider scaling."
        )

    if cpl > 500:
        recommendations.append(
            "Refine audience targeting to reduce CPL."
        )
    else:
        recommendations.append(
            "CPL is within the target range."
        )

    if conversion_rate < 2:
        recommendations.append(
            "Improve landing page and offer."
        )
    else:
        recommendations.append(
            "Conversion performance looks promising."
        )

    return recommendations
