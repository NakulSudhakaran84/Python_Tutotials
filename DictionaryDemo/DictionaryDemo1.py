emp={"QA":"Nakul","Dev":"Akash","DevOps":"John","Security":90,50:"Python"}
print(emp)
print(type(emp))

print(emp["QA"])
print(emp.get("Dev"))

emp={"QA":["Nakul","Rahul","David"],"Dev":"Akash","DevOps":"John","Security":90,50:"Python"}
print(emp["QA"][1])

emp1=emp["QA"]
print(emp1)

emp={"QA":"Nakul","Dev":{"frontend":"Rajeev","backend":"Neha"}}
print(emp.get("Dev").get("frontend"))
print(emp["Dev"]["backend"])

emp["Manager"]="XYZ"
print(emp)

emp["Manager"]="Satya"
print(emp)

emp.pop("QA")
print(emp)

emp.popitem()
print(emp)