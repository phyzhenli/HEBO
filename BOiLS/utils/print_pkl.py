import pickle


# with open('/home/zli/Desktop/HEBO/BOiLS/utils/zli/BOiLS/results/BO/fpga-6_seq-20_ref-resyn2_act-extended/BOiLS_std_init-20_obj-both_acq-ei_ard_kernel-ssk_yosys/log2/0/playground/log2/seq_to_func_dic.pkl', 'rb') as f:
#     data = pickle.load(f)

# print('== total number: ', len(data))

# for key, value in data.items():
#     print(key, value[0], value[1], value[0]+value[1])

with open('/home/zli/Desktop/HEBO/BOiLS/utils/zli/BOiLS/results/refs/resyn2/fpga-6/log2/refs.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)