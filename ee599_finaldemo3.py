import random
from datetime import datetime
import math

global rand_num

def random_gen(min,max):
    rand_num = random.randint(min,max)
    return rand_num


def jacobi(a,b):
    try:
        if a==1:
            return 1
        elif a%2==0:
            return (jacobi(a/2,b)) * (pow(-1, (((b*b)-1)/8)))
        else:
            return (jacobi(b%a,a)) * (pow(-1, (a-1)*(b-a)/4))
    except RecursionError:
        return 99


def finding_primes(digits):

    min = int("1"+("0"*(digits-1)))
    max = int("9"*digits)
    flag1 = True
    prime_num = None

    # randomly generated odd numbers
    random_nums = [random.randint(min,max) for x in range(100) ]
    odds = [x for x in random_nums if x%2==1]
    i_r=0
    
    while flag1:
        
        b= odds[i_r]
        i_r+=1
        #print(b)

        checks = 100
        true_vals = 0
        randomval_a = [random.randint(2,b-1) for x in range(100)]
        i=0
        while checks > 0:
            jacobi_res = jacobi(randomval_a[i],b)
            if math.gcd(randomval_a[i],b) == 1 and jacobi_res in [-1,1]:
                true_vals+=1
            checks -= 1
            i+=1
        
        #print("true_vals: ",true_vals)
        if true_vals >= 100:
            prime_num = b
            #print(prime_num)
            flag1 = False
    
    return prime_num

#print(finding_primes(2))

def finding_d(p, q, size):
    t=(p-1)*(q-1)
    while True:
        d=finding_primes(size)
        #print(d)
        if math.gcd(d, t) == 1:
            return d     


def solution_ab(a,b,c):
    flag = True
    y=0
    while flag:
        if (c- (b*y))%a == 0:
            x=(c- (b*y))/a
            return x,y
        else:
            y+=1
#solution_ab(a,b,c)  


def finding_e(p,q,size):
    n=p*q
    t=(p-1)*(q-1)
    flag1 = True

    while flag1:
        flag2 = True
        d = finding_d(p,q, size)

        xim1= t
        xi=d 
        xip1=None
        a=None
        b=None
        log_n_ct = 0
        
        while flag2:
            xip1 = xim1%xi
            xim1 = xi
            xi = xip1
            log_n_ct+=1
            if xi==1:
                a,b= solution_ab(t,d,xi)
            elif xi == 0:
                flag2 = False
        #print("e:", b)
        #print("log count:",log_n_ct, math.log(n,2))
        if log_n_ct >= int(math.log(n,2)):
            flag1= False
            return b,d
#size=3
#print("e,d: ",finding_e(p,q,size))


def compute_keys(size):
    p = finding_primes(size)
    q = p
    while q==p:
        q = finding_primes(size)
    
    e, d = finding_e(p, q, size+1)
    print(f"p: {p} \nq: {q} \n--------- \nn:{p*q} \nd: {d} \ne: {e}")

compute_keys(2)