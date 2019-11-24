#region Example 1
"""

a,b=0,1
while a<10:
    print(a)
    a,b=b,a+b
   
""" 
#endregion
#region Example 2
"""
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

"""
#endregion
#region Example 3
"""
import requests
request = requests.get('http://api.open-notify.org')
#print(request.text)
print(request.status_code)

request2 = requests.get('http://api.open-notify.org/fake-endpoint')
print(request2.status_code)

"""
#endregion
#region Example 4 APIs
import requests
people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)

people_json = people.json()
print(people_json)

#To print the number of people in space
print("Number of people in space:",people_json['number'])
#To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])
    
#endregion