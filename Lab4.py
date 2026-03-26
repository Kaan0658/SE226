x = int(input("Please enter the number of tasks:"))
Dict = {}
ZeroDep = []
for a in range(x):
    TskName = input("Enter task name:")
    NumOfDep = int(input("Enter number of dependency:"))
    if NumOfDep == 0:
        ZeroDep.append(TskName)
    DepName = []
    for m in range(NumOfDep):
        DepName.append(input("Enter dependency:"))
    Dict[TskName] = DepName
print(Dict)
print(ZeroDep, 'dont have any dependency')

print("EXECUTION ORDER:")
for a in Dict:
    if not Dict[a]:
        print(Dict[a])
        for s in Dict:
            if a in Dict[s]:
                Dict[s].remove(a)
    del Dict[a]
