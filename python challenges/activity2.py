print("enter a number (numerater): ")
numn = int(input())
print("enter a number (dinominator): ")
numd = int(input())

if numn%numd==0:
    print("\n" +str(numn)+ " is devisible by " +str(numd))
else:
    print("\n" +str(numn)+ " is not devisible by " +str(numd))
    