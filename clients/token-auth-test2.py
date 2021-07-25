import requests

def client():
    token_h="Token 60c29ee4b168836d711fecbacce2bc9f158da617"
    # credentials={"username":"resttest","email":"test@rest.com","password1":"resttest1234","password2":"resttest1234"}
    # response=requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",data=credentials)
    heaaders={"Authorization":token_h}
    response=requests.get("http://127.0.0.1:8000/api/profiles/",headers=heaaders)

    print("Status Code :",response.status_code)
    response_data=response.json()
    print(response_data)

if __name__=="__main__":
    client() 