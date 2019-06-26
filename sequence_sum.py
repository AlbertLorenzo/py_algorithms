def sequence_sum(begin_number, end_number, step):
    num_list = list()
    for x in range(begin_number, end_number + 1, step):
        num_list.append(x)
    return sum(num_list)

# def sequence_sum(begin_number, end_number, step):
#     return sum(range(begin_number, end_number + 1, step))    

print(sequence_sum(2, 6, 2))