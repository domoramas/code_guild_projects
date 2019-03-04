#dictionaries practice
#1
def combine(a,b):
        return dict(zip(a,b))
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
# print(combine(fruits, prices))

#2
def average(d):
        total = 0
        for value in list(d.values()):
                total += value
        return round((total/(len(list(d.values())))),2)
# combined = {'apple': 1.2, 'banana': 3.3, 'pear': 2.1}
# print(average(combined))

#3
def unify(d):
        unify_dict ={}
        a_list = [ v for k,v in d.items() if 'a' in k]
        unify_dict["a"] = round((sum(a_list)/len(a_list)))
        b_list = [ v for k, v in d.items() if "b"in k]
        unify_dict["b"] = round((sum(b_list)/len(b_list)))
        c_list = [v for k, v in d.items() if "c" in k]
        unify_dict["c"] = round((sum(c_list)/len(c_list)))
        return unify_dict              
                        
d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
print(unify(d))