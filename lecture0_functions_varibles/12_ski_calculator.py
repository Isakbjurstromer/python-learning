def total_time(runs, avg_time):
    return runs*avg_time

name = input("Name:").title()
runs = int(input("Number of runs:"))
avg_time = float(input("Average time per run in s:"))

print(f"{name}, completed {runs} runs.")

total_s = total_time(runs, avg_time)

print(f"Totall skiing time: {total_s}s")