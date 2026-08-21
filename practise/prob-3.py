goblin  = {"Queens", "Manhattan", "Brooklyn", "Bronx"}
octopus = {"Manhattan", "Brooklyn", "Harlem"}
vulture = {"Manhattan", "Bronx", "Harlem"}

# Contested by all three 
contested = goblin & octopus & vulture

# Controlled by exactly one 
goblin_only = goblin - octopus - vulture
octopus_only = octopus - goblin - vulture
vulture_only = vulture - goblin - octopus
controlled = goblin_only | octopus_only | vulture_only

# Distinct neighborhoods 
distinct_neigbr = len(goblin | octopus | vulture)

print(f"Contested by all three: {contested}")
print(f"Controlled by exactly one: {controlled}")
print(f"Distinct neighborhoods: {distinct_neigbr}")