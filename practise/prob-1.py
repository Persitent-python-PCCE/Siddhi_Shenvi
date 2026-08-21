name = "Neville"
signals = "gGhrGsgH"

def sorting_hat(student_name, signal_string):
    signals_upper = signal_string.upper()
    
    count_g = signals_upper.count('G')
    count_h = signals_upper.count('H')
    count_r = signals_upper.count('R')
    count_s = signals_upper.count('S')
    
    best_house = "Gryffindor"
    max_count = count_g
    
    if count_h > max_count:
        best_house = "Hufflepuff"
        max_count = count_h
        
    if count_r > max_count:
        best_house = "Ravenclaw"
        max_count = count_r
        
    if count_s > max_count:
        best_house = "Slytherin"
        max_count = count_s
        
    print(f"{student_name}, you belong in... {best_house}! ({max_count} signals)")

sorting_hat(name, signals)