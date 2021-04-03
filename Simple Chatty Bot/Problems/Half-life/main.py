initial_q = int(input())
final_q = int(input())

half_life = 12
half_life_period = 0


while initial_q >= final_q:
    initial_q = initial_q / 2
    half_life_period += 1

num_of_days = half_life * half_life_period
print(num_of_days)
