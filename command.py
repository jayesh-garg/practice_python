import argparse

def fib(n):
    a,b =0,1
    for i in range(n):
        a,b=b,a+b
        print (a)
    return a
def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("num",help="it will print fibonacci series",type=int)
    parser.add_argument("-o","--output",help="to store series in file",action="store_true")
    args=parser.parse_args()
    result=fib(args.num)
    print ("the {}th fibonacci number is {}".format(args.num,result))
    if args.output:
        f=open("/home/jgarg/Documents/python/programs/fibonacci.txt","w")
        f.write(str(result))
if __name__ == '__main__':
    Main()

