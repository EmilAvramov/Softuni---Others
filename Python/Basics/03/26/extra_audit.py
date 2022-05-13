expected_sum = int(input())
object_price = str(input())

cc_counter = 0
cs_counter = 0
total_counter = 1
cc_sum = 0
cs_sum = 0

while object_price != "End":
    float_object_price = int(object_price)
    if total_counter % 2 == 0:
        if float_object_price > 10:
            cc_sum += float_object_price
            total_counter += 1
            cc_counter += 1
            print(f'Product sold!')
        else:
            print("Error in transaction!")
            total_counter += 1
    else:
        if float_object_price <= 100:
            cs_sum += float_object_price
            total_counter += 1
            cs_counter += 1
            print(f'Product sold!')
        else:
            print("Error in transaction!")
            total_counter += 1
    if (cc_sum + cs_sum) >= expected_sum:
        if cc_counter == 0:
            cc_counter = 1
        if cs_counter == 0:
            cs_counter = 1
        print(f'Average CS: {cs_sum / cs_counter:.2f}', end='\n')
        print(f'Average CC: {cc_sum / cc_counter:.2f}')
        break
    object_price = str(input())

if (cc_sum + cs_sum) < expected_sum:
    print(f'Failed to collect required money for charity.')
