filename = "assignment4.txt"

with open(filename, "r") as file:
    for line in (file):

    
#for line in lines:

        line = line.strip()
    
    

        if not all(bit in "01" for bit in line):
            print(f"Error: invalid binary number {line}")
            continue
    

   

        if len(line) != 8:
            print(f"Error: binary mumber {line} does not have 8 bits")
            continue
    
    
   
    
        decimal = int(line, 2)
        print(f"Binary: {line}, Decimal: {decimal}")    
