target=[("Falcon", 34.05, -118.24), 
        ("Ghost", 99.9, 12.0), 
        ("Condor", 40.71, -74.00)]

invalid_points = [
    item for item in target
    if not (-90 <= item[1] <= 90) or not (-180 <= item[2] <= 180)
]

valid_targets = [
    (name, lat, lon) for name, lat, lon in target
    if -90 <= lat <= 90 and -180 <= lon <= 180
]

valid_targets.sort(key=lambda x: x[1], reverse=True)

print(f"INVALID: {invalid_points}")
print("Briefing (N->S):")
for name, lat, lon in valid_targets:
    print(f"{name} ->Lat:{lat}, Lon:{lon}")

#Tuples can't be modified, so they protect your coordinate data from accidental changes.




