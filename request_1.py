import requests
import json

saral_url = "http://saral.navgurukul.org/api/courses"
saral_api = requests.get(saral_url)

data = saral_api.json()

with open("data.json","w") as saral_data :
    json.dump(data,saral_data,indent=4)

serial_no = 1
for courses in data["availableCourses"]:
    print(serial_no ,".",courses["name"],courses["id"])
    serial_no += 1
course = int(input("enter the course number: "))
print(data["availableCourses"][course-1]["name"])



user_input_1=input("if you want to go next or previous n/p: ")
if user_input_1=="p":
    i=0
    while i<len(data["availableCourses"]):
        Courses = (data["availableCourses"][i]["name"])
        print(i+1," ",Courses,data["availableCourses"][i]["id"])
        i=i+1
    user_input = int(input("Enter your courses number "))
    print(data["availableCourses"][user_input-1]["name"])
    






saral_api_1 = ("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][course-1]["id"])+"/exercises")
saral_url_1=requests.get(saral_api_1)
data_1 = saral_url_1.json()
with open ("data_1.json","w") as saral_data_1 :
    json.dump(data_1,saral_data_1,indent=4)




    no=0
    for child in range(len(data_1["data"])):
        no+=1
        print("  ",no,data_1["data"][child]["name"])
        no=no+1
    # user_2=int(input("enter parent number"))

    user=input("if you want to go next or previous n/p: ")
    if user=="p":

        no=0
        for child in range(len(data_1["data"])):
            no+=1
            print("  ",no+1,data_1["data"][child]["name"])
            no=no+1


    user_1=int(input("enter parent number"))
    no_1=0
    if data_1["data"][user_1-1]["childExercises"]!=[] :
        for i in range(len(data_1["data"][user_1-1]["childExercises"])):
            print(data_1["data"][user_1-1]["childExercises"][i]["name"])
        no_1+=1
        
    user1=input("if you want to go next or previous n/p; ")

    if user1=="p":

        if data_1["data"][user_1-1]["childExercises"]!=[] :
            for i in range(len(data_1["data"][user_1-1]["childExercises"])):
                print(data_1["data"][user_1-1]["childExercises"][i]["name"])
            no_1+=1
        
        
        content=int(input("enter the number"))
        url=(data_1["data"][user_1-1]["childExercises"][content-1]["id"])
        url_1=(data_1["data"][user_1-1]["childExercises"][content-1]["slug"])

    
        
        
        
        saral_api_2=("http://saral.navgurukul.org/api/courses/"+str((data_1["data"][user_1-1]["childExercises"][content-1]["id"]))+"/exercise/getBySlug?slug="+(data_1["data"][user_1-1]["childExercises"][content-1]["slug"]))

        saral_data=requests.get(saral_api_2)

        saral_data2=saral_data.json()

        with open ("content.json","w") as f:
            json.dump(saral_data2,f,indent=4)
        print(saral_data2["content"])


    else:
        print(data_1["data"][user_1-1]["slug"])    

    


