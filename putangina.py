import numpy as np

n = 999999999999999999999999
num_list = list(int(num) for num in input("Enter the list items separated by space :").strip().split())[:n]

print("User list: ", num_list)

print("mean:", np.mean(num_list))
print('median:', np.median(num_list))
print("modus:", np.mode(num_list))
print('75th percentile', np.percentile(num_list, 72))
print('50th percentile sama kaya median:', np.percentile(num_list, 50))
print('25th percentile:', np.percentile(num_list, 25))
print('standart deviation:', np.std(num_list))
print('variance:', np.var(num_list))