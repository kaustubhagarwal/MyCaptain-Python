#Task 3
#Program to return the length of the longest string 

def relong(l):
    long=0
    for i in range(len(l)):
        if(len(l[i])>long):
            long=len(l[i])
    return long

if __name__=="__main__":
    li=input("Enter your space-separated strings ")
    le=li.split(" ")
    z=relong(le)
    print(str(z)+" is the length of the longest string you have given as input")