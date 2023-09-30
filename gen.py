import random
heist = ["nrftw", "Road_rage", "Dirt_hiest", "under_surphaze", "gold_sharke", "99", "TS"]
type = ["loud","stealth"]
diff = ["normal", "hard", "very_hard", "overkill",]

random_heist = random.choice(heist)
random_type  = random.choice(type)
random_diff = random.choice(diff)
print (f"Your random heist is:", random_heist,"the type is ", random_type, "the diff is", random_diff)
