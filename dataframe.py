"""import pandas as pd
stud_data={
"rn":[101,102,103],
"name":["tina","mina","tika"],
"gender":["female","female","female"],
"course":["cf","eng","ds"],
"marks":[99,99,99],
}
df=pd.DataFrame(stud_data)
print("stud information data")
print(df)

print("\n stud info:")
print(df.info())

print("\n static summery:")
print(df.describe())"""


import pandas as pd
emp_data={
"employe.id":[101,102,103],
"name":["tina","mina","tika"],
"department":["it","hr","it"],
"salary":["5000","5000","5000"],
"experience":[9,9,9],
}
df=pd.DataFrame(emp_data)
print("emp information data")
print(df)

print("\n stud info:")
print(df.info())

print("\n static summery:")
print(df.describe())


import pandas as pd
car_data={
"car.id":[101,102,103],
"brandname":["maruti","honda","tata"],
"price":["900000","900000","900000"],
"fueltype":["cng","cng","cng"],
"mileage":["10km/1","10km/1","10km/1"],
}
df=pd.DataFrame(car_data)
print("emp information data")
print(df)

print("\n car info:")
print(df.info())

print("\n car summery:")
print(df.describe())



import pandas as pd
patient_data={
"patient.id":[101,102,103],
"name":["tina","mina","tika"],
"age":["12","12","12"],
"gender":["female","female","female"],
"diseasename":["dangue","korona","polyo"],
"doctor":["neha","meha","ekta"]
}
df=pd.DataFrame(emp_data)
print("patient information data")
print(df)

print("\n patient info:")
print(df.info())

print("\n static summery:")
print(df.describe())
