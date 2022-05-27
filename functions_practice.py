def hello():
    print("hey!")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(packed_lunch):
    if(len(packed_lunch) > 0):
        print(f"First I eat {packed_lunch[0]}. Next I eat {packed_lunch[1]} & {packed_lunch[2]}.")  
    else:
        print("My lunchbox is empty!")

hello()
lunch = pack("apple", "sandwich", "milk")
print(lunch)
nolunch = []
eat_lunch(lunch)
eat_lunch(nolunch)