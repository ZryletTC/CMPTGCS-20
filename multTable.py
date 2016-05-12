from __future__ import print_function

def multTable(row,col):
    if type(row)!=int or type(col)!=int:
        return "Please input integers!"
    if row<1 or col<1:
        return "Row and column values must be greater than or equal to 1!"

    
    for i in range(row+1):
        for j in range(col+1):
            if i ==0:
                if j==0:
                    print("   |", end='')
                else:
                    print("{:^3d}|".format(j), end='')
            else:
                if j==0:
                    print("{:^3d}|".format(i), end='')
                else:
                    print("{:3d}|".format(i*j), end='')
        print("\n"+"---+"*(col+1))
