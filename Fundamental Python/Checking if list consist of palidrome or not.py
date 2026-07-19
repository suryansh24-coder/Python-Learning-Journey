# WAP to check if the list consist of palidrome or not :-
# list is same form starting and ending :-
list1=[1,2,3,4,5,4,3,2,1]
list2 =[1,2,5,7,8,9]
copy_list1 = list1.copy()
copy_list2 = list2.copy()
copy_list1.reverse()
copy_list2.reverse()


if(list1==copy_list1) :
    print("List 01 is a palidromic list !")
else :
    print("It's not a paldromic series !")
    
if(list2==copy_list2) :
    print("List 2 is also a paldromic list !")
else :
    print("It is not a palidromic series!")   
    
# for case of letters :-

list1=["a","b","c","d","e","d","c","b","a"]
list2 =["a","b","c","D"]
copy_list1 = list1.copy()
copy_list2 = list2.copy()
copy_list1.reverse()
copy_list2.reverse()


if(list1==copy_list1) :
    print("List 01 is a palidromic list !")
else :
    print("It's not a paldromic series !")
    
if(list2==copy_list2) :
    print("List 2 is also a paldromic list !")
else :
    print("It is not a palidromic series!") 