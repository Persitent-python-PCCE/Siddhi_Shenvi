def create_hero(name, *powers, **stats):
    print(f"Hero: {name}")
    print(f"Powers: {', '.join(powers)}")
    print("Stats:")
    
    for key, value in stats.items():
        print(f"{key}: {value}")
        
    rating = sum(stats.values()) / len(stats)
    tier = " -> S-Tier" if rating >= 90 else ""
    
    print(f"Overall rating: {rating:.1f}{tier} *")

create_hero("Spider-Man", "wall-crawl", "spider-sense", strength=85, agility=95, intelligence=92)