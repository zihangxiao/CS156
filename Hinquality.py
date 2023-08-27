from tqdm import tqdm
import numpy as np

all_c1 = 0
all_crand = 0
all_cmin = 0
number_iteration=100000
for y in tqdm(range(number_iteration), desc="Processing", unit="iteration"):
    coin_result = np.empty(1000)
    ten_time_coin_result = np.empty((10, 1000))
    
    for z in range(10):
        coin_result = np.random.randint(2, size=1000)
        ten_time_coin_result[z, :] = coin_result

    c1 = ten_time_coin_result[:, 0]
    c1_f_heads = np.count_nonzero(c1) / 10
    all_c1 += c1_f_heads

    # Random coins selected from 1000 coins
    index = np.random.randint(999)
    crand = ten_time_coin_result[:, index]
    crand_f_heads = np.count_nonzero(crand) / 10
    all_crand += crand_f_heads

    # Coin with minimum frequency of heads
    cmin_f_heads = np.min(np.count_nonzero(ten_time_coin_result, axis=0)) / 10
    all_cmin += cmin_f_heads

avg_c1 = all_c1 / number_iteration
avg_crand = all_crand / number_iteration
avg_cmin = all_cmin / number_iteration  # Move this line outside of the loop

# Print the averages
print("Average νc1:", avg_c1)
print("Average νcrand:", avg_crand)
print("Average νcmin:", avg_cmin)
