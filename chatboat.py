import requests
import os 
from dotenv import load_dotenv,dotenv_values
import json
# we first load the enviroments valiables 
load_dotenv()


# then we are going to build the function of the chat bot 
def chat () :
    load_dotenv()
    
    # first we check if there are the api key which has been sent 
    apikey=os.getenv('CHATBOTAPI')
    if apikey==None :
        print (" no api has been provided")
    
    # when is provided 
    # we make the loop for seeing if there are any messages 
    while True :

      message=input (" you :")
      if message.lower()==["exit","quit"] :
         break 
      else :
         # we create the request or we send the api on the open router 
         response = requests.post(url="https://openrouter.ai/api/v1/chat/completions",
                                  headers={

                                    "Authorization":f"Bearer {apikey}",
                                    "HTTP-Referer":"http://localhost",
                                    "content-type":"application/json",
                                    "X-Title":"sam pray" 


                                    

                                  },

                                  #now we are going to writes the bod what is going to be sent on the 
                                  # api given 
                                  data=json.dumps({
                                     "model":"meta-llama/llama-3.3-70b-instruct:free",
                                     "messages":[
                                        {
                                           "role":"system","content":" you are the best analysist who can analyse the informations of the sensors and control systems "
                                           "and provide the engineering advices about the perfomances and other thinsg and you are name is FUNDABOT  the ai chat bot which helps the people to analyse thier systems either "
                                           "temperatures and other things in different senerios you must be supportive and all the things must be clear and consise ",


                                        },
                                        {
                                           'role':"user","content":message
                                        }

                                     ]
                                    
                                  })
                                  )
         
         
         print (f"  \nBot :{response.json()['choices'][0]['message']['content']}\n \n")

         

# now we can build the other things which return 
# test the violations 
# the declarations 
# wwe have to declare the messages and headers and the data where we are going to add them 
apikey= os.getenv("CHATBOTAPI")
header= {
   "Authorization":f"Bearer {apikey}",
   "HTTP-Referer":"http://localhost",
   "X-Title":"this is reasearch",
   "content-type":"application/json"

}
urls= "https://openrouter.ai/api/v1/chat/completions"

# anather things to declare is the messages to send 
# but messages will be in the loop where we will make the things for the btter timing and make it hard to replicates 
def violation() :
 
   while True :
      message= input (" you :\n")
      if message =="quit":
         print (" thanks for using our chat boat and we are very happy to hear again ")
         break
      else :
         response= requests.post (url=urls,headers=header,data=json.dumps({
            # in that what we put inside is the models and the messages to send 
            "model":"meta-llama/llama-3.3-70b-instruct:free",
            "messages":[{
               "role":"system","content":" detecting the violations and other humfull thinsg from the posts someone is going to post and then after "
               "you will respond if the message is hamfully and say it is bad or not and you will tell the user and suggest where he or can change what to do you are the fist world best violation detector and first "
               "you will say this content contains violations at this level and say it and this is the social media which where people who "
               "read the books share the ideas about what they have read so we dont want people to post somethings bad or hamful so state the amount of the halmufl and pacentages like 10 % or other things  "

            }, {
               "role":"user","content":message
            }
            ]


         }))
         print (response.json()["choices"][0]["message"]["content"])
