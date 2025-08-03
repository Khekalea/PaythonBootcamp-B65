value = input("Enter any value: ")
 
print("Original:", value)
print("Type:", type(value))
 
 
try:
    int_val = int(value)
    print("Integer:", int_val)
except:
    print("Can't convert to int")
 
try:
    float_val = float(value)
    print("Float:", float_val)
except:
    print("Can't convert to float")
 
 
bool_val = bool(value)
print("Boolean:", bool_val)