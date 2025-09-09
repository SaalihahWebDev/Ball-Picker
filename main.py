machine1={"Red":4,"White":0}
machine2={"Red":3,"White":1}
machine3={"Red":0,"Blue":4}
def check_probality(machine,color):
    total=sum(machine.values())
    count=machine.get(color,0)
    probality=count/total
    if probality==1:
        return "Certain"
    elif probality==0.75:
        return "Likely"
    elif probality==0.25:
        return "Unlikely"
    else:
        return "Impossible"
print("Machine 1,Red:",check_probality(machine1,"Red"))
print("Machine 2,Red:",check_probality(machine2,"Red"))
print("Machine 2,White:",check_probality(machine2,"White"))
print("Machine 3,Red:",check_probality(machine3,"Red"))