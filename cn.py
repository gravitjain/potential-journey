import re
def findClass(x):
    global c
    if re.match('''^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$''',x):
                    m=str()
                    i=0
                    while(x[i]!="."):
                        m=m+x[i]
                        i=i+1
                    m=int(m)
                    if(m>=0 and m<=127):
                        print("Given IP Address is of class A")
                        c="A"
                    elif(m>=128 and m<=191):
                        print("Given IP Address is of class B")
                        c="B"
                    elif(m>=192 and m<=223):
                        print("Given IP Address is of class C")
                        c="C"
                    elif(m>=224 and m<=239):
                        print("Given IP Address is of class D")
                        c="D"
                    elif(m>=240 and m<=255):
                        print("Given IP Address is of class E")
                        c="E"
                    seperateip(n)  
                    firstlast()
    else:
        print("Enter a proper IP Address")


def seperatedmf(x):
    global dm1f,dm2f,dm3f,dm4f
    a=(x.split("."))
    dm1f=a[0]
    dm2f=a[1]
    dm3f=a[2]
    dm4f=a[3]

def seperatedml(x):
    global dm1,dm2,dm3,dm4,dm1l,dm2l,dm3l,dm4l
    a=(x.split("."))
    dm1l=a[0]
    dm2l=a[1]
    dm3l=a[2]
    dm4l=a[3]

        
def firstlast():
    if(c=="A"):
        default_maskf="255.0.0.0"
        default_maskl="0.255.255.255"
        seperatedmf(default_maskf)
        seperatedml(default_maskl)
        a1=int(int(ip1) & int(dm1f))
        a2=int(int(ip2) & int(dm2f))
        a3=int(int(ip3) & int(dm3f))
        a4=int(int(ip4) & int(dm4f))
        a5=int(int(ip1) | int(dm1l))
        a6=int(int(ip2) | int(dm2l))
        a7=int(int(ip3) | int(dm3l))
        a8=int(int(ip4) | int(dm4l))
        print("First IP:"+ str(a1)+"."+str(a2)+"."+str(a3)+"."+str(a4))
        print("Last IP:"+ str(a5)+"."+str(a6)+"."+str(a7)+"."+str(a8))
        
        
    elif(c=="B"):
        default_maskf="255.255.0.0"
        default_maskl="0.0.255.255"
        seperatedmf(default_maskf)
        seperatedml(default_maskl)
        a1=int(int(ip1) & int(dm1f))
        a2=int(int(ip2) & int(dm2f))
        a3=int(int(ip3) & int(dm3f))
        a4=int(int(ip4) & int(dm4f))
        a5=int(int(ip1) | int(dm1l))
        a6=int(int(ip2) | int(dm2l))
        a7=int(int(ip3) | int(dm3l))
        a8=int(int(ip4) | int(dm4l))
        print("First IP:"+ str(a1)+"."+str(a2)+"."+str(a3)+"."+str(a4))
        print("Last IP:"+ str(a5)+"."+str(a6)+"."+str(a7)+"."+str(a8))
    elif(c=="C"):
        default_maskf="255.255.255.0"
        default_maskl="0.0.0.255"
        seperatedmf(default_maskf)
        seperatedml(default_maskl)
        a1=int(int(ip1) & int(dm1f))
        a2=int(int(ip2) & int(dm2f))
        a3=int(int(ip3) & int(dm3f))
        a4=int(int(ip4) & int(dm4f))
        a5=int(int(ip1) | int(dm1l))
        a6=int(int(ip2) | int(dm2l))
        a7=int(int(ip3) | int(dm3l))
        a8=int(int(ip4) | int(dm4l))
        print("First IP:"+ str(a1)+"."+str(a2)+"."+str(a3)+"."+str(a4))
        print("Last IP:"+ str(a5)+"."+str(a6)+"."+str(a7)+"."+str(a8))
    subnet()

def seperateip(x):
    global ip1,ip2,ip3,ip4,ip1b,ip2b,ip3b,ip4b
    a=(x.split("."))
    ip1=a[0]
    ip2=a[1]
    ip3=a[2]
    ip4=a[3]
    #ip1b=decimalToBinary(int(ip1))
    #ip2b=decimalToBinary(int(ip2))
    #ip3b=decimalToBinary(int(ip3))
    #ip4b=decimalToBinary(int(ip4))
    #print(ip1)
    #print(ip2)
    #print(ip3)
    #print(ip4)
def rec(x):
        global ans
        i=0
        y=0
        b=0
        while(i!=x):
            b=2**(7-i)
            y=y+b
            i=i+1
        ans=int(y)
def rec1(x):
        global ans1
        i=0
        y=0
        b=0
        while(i!=x):
            b=2**(7-i)
            y=y+b
            i=i+1
        ans1=int(y)     
def rec2(x):
        global ans2
        i=0
        y=0
        b=0
        while(i!=x):
            b=2**(7-i)
            y=y+b
            i=i+1
        ans2=int(y)   
def subnet():
    if(c=="A"):
        net_id=ip1
        host_id=ip2+"."+ip3+"."+ip4
        host_power=24
        print("Net-Id= "+ net_id)
        print("Host-Id= "+host_id)
        print()
        print("Enter Subnet-ID: ")
        s=int(input())
        total_subnets=2**s
        total_devices=2**(host_power-s)
        print()
        print("Total Subnets= "+ str(total_subnets))
        print("Total Devices= "+str(total_devices))
        if(s<=8):
            rec(s)  
            print("Subnet Mask= "+str(net_id)+"."+str(ans)+"."+str("0")+"."+str("0"))
        elif(s>8 and s<=16):
            rec(s)       
            g=s-8
            rec1(g)
            print("Subnet Mask= "+str(net_id)+"."+str(ans)+"."+str(ans1)+"."+str("0"))
        elif(n>16):
            rec(n)       
            g=n-8
            rec1(g)
            f=n-16
            rec2(f)
            print(ans)
            print(ans1)
            print("Subnet Mask= "+str(net_id)+"."+str(ans)+"."+str(ans1)+"."+str(ans2))
        
    if(c=="B"):
        net_id=ip1+"."+ip2
        host_id=ip3+"."+ip4
        host_power=16
        print("Net-Id= "+net_id)
        print("Host-Id= "+host_id)
        print()
        print("Enter Subnet-ID: ")
        s=int(input())
        total_subnets=2**s
        total_devices=2**(host_power-s)
        print()
        print("Total Subnets= "+ str(total_subnets))
        print("Total Devices= "+str(total_devices))
        if(s<=8):
            rec(s)  
            print("Subnet Mask= "+str(net_id)+"."+str(ans)+"."+str("0"))
        elif(n>8 and n<16):
            rec(n)       
            g=n-8
            rec1(g)
            print(ans)
            print(ans1)
            print("Subnet Mask= "+str(net_id)+"."+str(ans)+"."+str(ans1))
        
    if(c=="C"):
        net_id=ip1+"."+ip2+"."+ip3
        host_id=ip4
        host_power=8
        print("Net-Id= "+net_id)
        print("Host-Id= "+host_id)
        print()
        print("Enter Subnet-ID: ")
        s=int(input())
        total_subnets=2**s
        total_devices=2**(host_power-s)
        print()
        print("Total Subnets= "+ str(total_subnets))
        print("Total Devices= "+str(total_devices))
        rec(n)  
        print("Subnet Mask= "+str(net_id)+"."+str(ans))
   
print("Enter IP Address: ")    
n=str(input())
findClass(n)    
 


    
    
    








