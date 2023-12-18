import requests
responce = requests.get("https://api.github.com/repos/Satyam_V/Terraform-Projects/pulls")
print(responce)
print(type(responce))
complete_detail = (responce.json())
for element in range(len(complete_detail)):
    print(complete_detail[element]["user"]["login"])
