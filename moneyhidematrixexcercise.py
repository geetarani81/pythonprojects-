# program for nested list (list inside a list ) and have a marix of 3 by 3 and want to hide any of them 
list1= [1,1,1]
list2= [1,1,1]
list3= [1,1,1]
print (f"{list1}\n,{list2}\n,{list3}")
final_list = [list1,list2,list3]
inputno = input("input any double digit no both have range from 0 to 2 ")
row =int(inputno[0])
coloum= int(inputno[1])
row_select = final_list[row-1]
row_select[coloum-1]='x'
print (f"{list1}\n,{list2}\n,{list3}")
