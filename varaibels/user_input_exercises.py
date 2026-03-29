# is_adult = True 
# # print(type(is_adult))
# # print(is_adult)

# print(5 == 5)
# print("baba"=="baba")
# friends = [1, "Rolf", 5]
# aboard = [5, "Rolf", 1]
# print (set(friends) == set(aboard))
# print(friends[0] is aboard[2] )

# day_of_week = input("enter day: ").lower()
# today='monday'
# print(day_of_week==today)
# if day_of_week == today:
#     print("have a great start of week")
# elif day_of_week=='sunday':
#     print("one day late")
# else:
#     print("that not the right day")
    
# print("this is after")
# freinds = ["yuval", "moshe"]
# print("yuval" in freinds )
# num_1=input("enter number ")
# num_2=input("enter number ")

# num_3=["hi", "no", "yes"]
# num_4=["hi", "no", "yes"]
# result = num_3 is num_4
# another = num_4

# print (result)
# print (another is num_4)
# day_of_week = input("What day of the week is it today? ")
# if day_of_week.lower()== "monday":
#     print("today is monday")
# elif (day_of_week.lower() == "tuesday"):
#     print("today is tuesday")
# else:
#     print("not the right day")
# friends=["jen", "Bob","Rolf"]
# # print("jen" in friends)
# movies = {"narkos", "hamehasf", "dragonball", "narkos"}
# # user_movie = input("Enter a movie you have watched recently: ")
# # if user_movie in movies:
# #     print ("the movie is in")
# # else:
# #     print("the movie isnt")
# print (movies)

# movies = {"narkos", "hamehasf", "dragonball"}
# user_movie = input("Enter a movie you have watched recently: ")
# if user_movie in movies:
#     print("i have watche")
# else:
#     print("i havnt watch yet")
    
# num=3
# user_input = input("Enter Y if you would like to play: ")
# if user_input in ('y', 'Y'):
#     num_guess=int(input("enter number "))
#     if num_guess == num:
#         print("nc work!")
#     elif abs(num-num_guess)==1:
#         print("next to each other")
#     else:
#         print("maybe next timr")
    
# def process_data_guarded(data):
#     if not isinstance(data, list):
#         print("not a list")
#         print(f"the type of the data is: ", type(data))
#         return
#     if not data:
#         print("no data provide")
#     else:
#         print("processing ", len(data), "items")
#         print ("processed")
# process_data_guarded("ABC")
# process_data_guarded(10)
# def user_age_in_seconds():
#     age = int(input("Whats is your age: "))
#     age_seconds = age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is: {age_seconds}")

# user_age_in_seconds()
# def regular_user(first_name, second_name):
    
#     print(f"hello, {first_name} {second_name}")
# first_name="bob"
# second_name="marly"
# regular_user(first_name, second_name)

# def dividing (num1, num2):
#     if  num2 == 0 :
#         print("you fool")
#     elif num1 > num2:
#         resault=num1/num2
#         print(resault)
#     elif num2 > num1:
#         resault=num2/num1
#         print(resault)

# dividing(6 , 8)

# def numbers (num_list):
#     sum=0
    
#     for i in num_list:
#         sum+=i
#         lenth_num=len(num_list)
#     # print (f"the sum of the numbers is: {sum}")
#     # print (f"the count of the numbers: {lenth_num}")    
#     # print (f"the ave of the numbers: {sum/lenth_num}")  
#     final_tuple=(sum, lenth_num, sum/lenth_num)
#     print(final_tuple)  

# num_list=(1, 3, 5)
# numbers(num_list)
    
# def returning (list_num):
#     num_low=list_num[0]
#     num_high=list_num[0]
#     for i in list_num:
#         if num_low>i:
#             num_low=i
#         if i>num_high:
#             num_high=i
#     final_list=(num_low,num_high)
#     print(final_list)
# list_num=[0, 18, 32, 52, 3]
# returning(list_num)
            
# def zugi (num_list: list):
#     num_list.sort()
#     new_list=[]
#     for i in num_list:
#         if i%2==0:
#             new_list.append(i)
    
#     return(new_list)
# print(zugi(num_list=[1,2,8,0,1,4,7,9]))     

# def even_or_not(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")          
# even_or_not(3)
# def grades (grades_list: list):
#     correct_list=[]
#     for i in grades_list:
#         if i>60:
#             correct_list.append(i)
#     print (correct_list)
# grades(grades_list=[37,90,72,45,80])
# def num_list (numbers: list):
#     sum=0
#     ave=0
#     if not numbers:
#         return None
#     else:
#         for i in numbers:
#             sum+=i
#         ave= sum/len(numbers)
#         print(ave)
        
# num_list( numbers=[])

# def saf (number_list, num):
#     new_list=[]
#     for i in number_list:
#         if i > num:
#             new_list.append(i)
#     print(new_list)
# saf(number_list=[22,11,33,0,1,2,55], num=10)
# def reverse_fun (numbers_list:list, reverse:bool):
#     if reverse:
#         numbers_list.reverse()
#         print(numbers_list)
# reverse_fun(numbers_list=[1,2,3,4,5,6,7,8,9], reverse=True)
# def biggest_num (*numbers):
#     return max(numbers)
# print(biggest_num(1,5,10,2,33,100,5))
# def only_even (*numbers):
#     new_list=[]
#     for i in numbers:
#         if i%2==0:
#             new_list.append(i)
#     return new_list
# print(only_even(2,4,5,6,8,1,7,6,8,2,82))
# def mesudar(name:str, age:float):
#     print(f"your name is {name} you r {age} years old")
# mesudar(name="yuval", age=20)
# def peula (num_list:list, action:str):
#     if action.lower() =="min":
#         return min(num_list)
#     elif action.lower() =="max":
#         return max(num_list)
#     elif action.lower() =="sum":
#         return sum(num_list)
# print(peula(num_list=[4,5,9], action="sum"))

# def inter_fun():
#     num1=3
#     num2=4
#     def sum_num (num1:int, num2:int):
#         print(num1+num2)
#     sum_num(num1,num2)
# inter_fun()

# num1=3
# def mugdar ():
#     def inter (num1):
#         print(num1+3)
#     inter(num1)
# mugdar()

# def outer_fun():
#     counter=0
#     def inter_fun():
#         nonlocal counter
#         counter+=1
#         print(counter)
#     return inter_fun
# outer_fun()()


# def some_fun(some_list):
#     sum=0
#     for i in some_list:
#         sum=sum+i
#     print(sum)
# some_list=[3,1,4,7,72,5]
    
# def the_outer (some_list: list, some_fun:function):
#     some_fun(some_list)
# the_outer(some_list, some_fun)

# num=5
# def act_func(num):
#     multy=num*2
#     print(multy)
# def some_fun(num:int, act_func:function):
#     act_func(num)
# some_fun(num, act_func)


# top_list=[22,106,2,8,45,3,795,23]
# threshold=3
# if_reverse=True
# def some_func (top_list:list, threshold:int, if_reverse:bool):
#     new_list=[]
#     if if_reverse==True:
#         top_list.reverse()
#         for i in top_list:
#             if i>threshold:
#                 new_list.append(i)
#     print(new_list)
# some_func(top_list,threshold,if_reverse)              
        
    
# def un_limited(*args):
#     the_max=args[0]
#     the_sum=0
#     the_min=args[0]
#     for i in args:
#         if i>the_max:
#             the_max=i
#             the_sum+=i
#         else:
#             the_sum+=i
#         if i<the_min:
#             the_min=i
#             the_sum+=i
#         else:
#             the_sum+=i
#     some_tupl=(the_sum,the_min,the_max)
#     print(some_tupl)
# un_limited(1,2,3,7,4,5,6,9,4)


def some_fun(some_list):
    pare_tupl=[]
    not_pare_tupl=[]
    for i in some_list:
        if i%2 ==0:
            pare_tupl.append(i)
        else:
            not_pare_tupl.append(i) 
    pare_tupl_2=tuple(pare_tupl)
    not_pare_tupl_2=tuple(not_pare_tupl)
    print(pare_tupl_2)
    print(not_pare_tupl_2)
some_fun([2,4,5,7,9,1,22,33,55,11,44])   



