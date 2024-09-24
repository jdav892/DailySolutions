def up_array(arr):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    
    num_str = ''.join(map(str, arr))
    num = int(num_str) + 1
    new_num_str = str(num)
   
    return [int(digit) for digit in new_num_str.zfill(len(arr))]