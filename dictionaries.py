# Building a dossier on a known threat
hacker_profile = {
    "alias": "Nightshade",
    "ip_address": "192.168.1.99",
    "threat_level": "Critical",
}

# If we want to know the threat level, we just ask for that specific key

print(hacker_profile["threat_level"])
# This outputs: Critical