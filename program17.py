#DICTIONARY
'''
player={}
print(type(player))
'''


#WAYS TO CREATE DICT. IN PY.

#1.
'''
player2={45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul"}
print(player2)
'''

#2.
'''
player3=dict({45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul"})
print(player3)
'''

#DICT. CAN BE MIXED
'''
myInfo={"name":"Unknown",3:["Python","Java","CPP"]}
print(myInfo)
'''


#player={45:"Rohit",77:"Shubhman",18:"Virat",1:"KLRahul","next to bat":{96:"Shreyas",63:"SKY",8:"Jaddu"}}
#TO ACCESS VALUE 
'''
print(player)
print(player[18])
print(player["next to bat"])
print(player["next to bat"][63])
'''


#TO ADD
'''
player[100]="Virat Kohli"            #add key value at the end of dictionary
print(player)
'''


#METHODS

player={45:"Rohit",77:"Shubhman",18:"Virat",1:"KLRahul",96:"Shreyas",8:"Jaddu"}
print(player)
print("AFTER USING METHOD:")

#1.get()
'''
print(player.get(18))
'''


#2.items()
'''
print(player.items())
'''

#3.keys()
'''
print(player.keys())
'''

#4.values()
'''
print(player.values())
'''

#5. pop()
'''
player.pop(18)
print(player)
'''

#6. popitem()-----------------> pops last key:value pair
'''
player.popitem()
print(player)
'''

#7. clear()
'''
player.clear()
print(player)
'''

#8. copy()-------------> shallow copy
'''
dict1=player.copy()
print(dict1)
'''


#9. update()
'''
team={63:"SKY",33:"Hardik"}
player.update(team)
print(player)
'''

#10. setdefault()
'''
val=player.setdefault(18,"Kohli")
print(player)
print(val)
val1=player.setdefault(12,"Yuvraj")
print(player)
print(val1)
'''


#11. fromkey()

lang=["reactjs","flutter","springboot"]
teacher="Shashi"
print(player.fromkeys(lang,teacher))

















