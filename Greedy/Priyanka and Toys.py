'''Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?'''

def toys(w):
    w.sort()
    toys = w[0]+4
    container = 1
    for i in range(len(w)):
        if(w[i]>toys):
            toys=w[i]+4
            container+=1
    return container