import requests

def client():
    token_h="Token c241a0a42005212927ce4b09f3b9058a4f9ec693"
    # credentials={"username":"hari","password":"hari"}
    # response=requests.post("http://127.0.0.1:8000/api/rest-auth/login/",data=credentials)
    heaaders={"Authorization":token_h}
    response=requests.get("http://127.0.0.1:8000/api/profiles/",headers=heaaders)

    print("Status Code :",response.status_code)
    response_data=response.json()
    print(response_data)

if __name__=="__main__":
    client() 