def reverse_lookup(data,target):

    results=[]

    for k,v in data.items():

        if v==target:

            results.append(k)

    return results

my_dict={"sandeep":"33","goverdhan":"60","dhynesh":"39" }

print(reverse_lookup(my_dict,"39"))

