temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

new_temp = [t for t in temperatures if t > 28]

# через filter
# new_temp_using_filter = list(filter(lambda t: t > 28, temperatures))

print(new_temp)

print(max(new_temp))
print(min(new_temp))
print(sum(new_temp) / len(new_temp))
