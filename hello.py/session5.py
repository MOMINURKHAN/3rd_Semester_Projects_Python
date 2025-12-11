#task1-- make a dict with 3 people and their favourite number

favourite_num = {
    'Alex' :'Green',
    'Abu' :'Yellow',
    'Isham' : 'Red',
}

#task 2
print("\ntask 2")
for (person,colour) in favourite_num.items():
    print(f"Person : {person} - Colour : {colour}")

#task3 - add one more with '=' assignment
favourite_num['Maxii'] = 'Brown'

#task4- change one existing's favourite color
favourite_num['Abu'] = 'black'

#task 5 - deleting one from the dict
del favourite_num['Abu']

#task 6 - loop and print only names(key)
print("\ntask -6")
for key in favourite_num.keys():
    print(key)

#task 7 - same same just this time values 
print("\ntask 7")
for value in favourite_num.values():
    print(value)

#task 8 - add a list as value of a new key
favourite_num['Smith'] = ['black','gray','green']

#task 9 - same as task 2 i think
print("\ntask - 9")
for (person,colour) in favourite_num.items():
    print(f"Person : {person} - Colour : {colour}")

#task 10 - quite tough compared to above one's - Add new information for each person: their country and major.
#Now each person should have a small nested dictionary (person : {info}).

favourite_num['Abu'] = {
    'colour' : 'Green',
    'country':'Saudi Arabia',
    'Major' : 'Oil Technology', # but not sure the subject exist or not heheh
}
favourite_num['Alex'] = {
    'colour' : 'black',
    'country':'United Kingdom',
    'Major' : 'Banking and Economics',
}
favourite_num['Isham'] = {
    'colour' : 'Brown',
    'country':'Qatar',
    'Major' : 'Electric and Electronic',
}
favourite_num['Maxii'] = {
    'colour' : 'White',
    'country':'Australia',
    'Major' : 'Ocean Science',
}
favourite_num['Smith'] = {
    'colour' : 'Sky-blue',
    'country':'Belgium',
    'Major' : 'Softwaer Engineering',
}
#task 11 - loop through dict and print formatted senten containing name,country,major - (colour was not mentioned there i just notice  )
print("\ntask 11- loop and format sentence : ")
for (person,dictionary) in favourite_num.items():
    print(f"{person} is from {dictionary['country']} studying {dictionary['Major']} ")

#task12 - adding one more student with all the info and sort name alphabetically

favourite_num['Nerob_vai'] = {
    'colour' : 'brownish',
    'country':'Bangladesh',
    'Major' : 'Military Technology',
}

favourite_num = dict(sorted(favourite_num.items() ,key=lambda x:x[0] ))
print("\nAfter sorted Task 12")
for i,(name,dictionary) in enumerate(favourite_num.items(),1):
    print(f" Index : {i} Name : {name}  Information : {dictionary}")