def launch(*stages, abort_threshold=5000):
    cumulative_mass = 0

    for i, mass in enumerate(stages, 1):
        cumulative_mass += mass
        
        print(f"Stage {i} armed -> cumulative {cumulative_mass} kg")

        if cumulative_mass > abort_threshold:
            print(
                f"[ABORT] at stage {i}: threshold {abort_threshold} kg exceeded."
            )
            return

    print(
        f"[SUCCESS] All {len(stages)} stages fired safely. Total mass: {cumulative_mass} kg"
    )

def launch(*stages, abort_threshold=5000):
    cumulative_mass = 0

    for i, mass in enumerate(stages, 1):
        cumulative_mass += mass
        
        print(f"Stage {i} armed -> cumulative {cumulative_mass} kg")
        
        if cumulative_mass > abort_threshold:
            print(
                f"[ABORT] at stage {i}: threshold {abort_threshold} kg exceeded."
            )
            return

    print(
        f"[SUCCESS] All {len(stages)} stages fired safely. Total mass: {cumulative_mass} kg"
    )

launch(1200, 1800, 2500, 900)  