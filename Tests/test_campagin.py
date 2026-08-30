from Models.Campaign_Simulator_Final import calculate_campaign


result = calculate_campaign(
    budget=10000,
    impressions=100000,
    ctr=5,
    registration_rate=20,
    lead_rate=30,
    customer_rate=20
)

assert result["clicks"] == 5000
assert result["registrations"] == 1000
assert result["leads"] == 300
assert result["customers"] == 60

print("All campaign calculation tests passed!")
