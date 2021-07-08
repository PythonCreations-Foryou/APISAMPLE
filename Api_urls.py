import requests
import json


class RequestResponse :

    def __init__(self,base_url):

        self.base_url = base_url
              
    def Users(self,request):
        
         self.request = request
         url = self.base_url+self.request        
         self.response = requests.get(url)
         return json.loads(self.response.text)   
            

    def Create(self,request,json_data):

         self.request = request
         self.json_data = json_data
         url = self.base_url+self.request
         self.response = requests.post(url,json_data)
         return json.loads(self.response.text)
         
       
    def Delete(self,request):
         
         self.request = request
         url = self.base_url+self.request
         self.response = request.delete(url)
      
         

    def Update(self,request,json_data):

         self.request = request
         self.json_data = json_data
         url = self.base_url+self.request
         self.response = requests.put(url,json_data)
         return json.loads(self.response.text)

             
             
             
         
        
website = RequestResponse('https://reqres.in')

print(website.Users('/api/users/23'))

print(website.response)

