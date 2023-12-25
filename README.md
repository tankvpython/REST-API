# create a env using this command

- python -m venv myenv

# activate env on windows using this command
- myenv\Scripts\activate.ps1   

# before run allow permission this comand only run on  ubuntu and linux
- chmod +x restful.py 
- i have no ubuntu thats why i have call all rest request using python, i have also read this point on git file.
- we have run all the url in ubuntu or linux remove python form all url and run.

# get all post on console and termoinal using print statement
1) GET all posts and dump to console: 
- python .\restful.py get /posts


# dump all data in .json file
2) GET all posts and dump to JSON file:
- python .\restful.py get /posts  -o test.json

test.json is replace with your file name

# dump all data in .csv file
3) GET all posts and dump to CSV file:
- python ./restful.py get /posts -o test.csv


# get one post using post id and print in console
4) one post and dump to console:
- python ./restful.py get /posts/1 

# create new post on console
5) POST a new dummy post and dump response to console:
- python ./restful.py post /posts --data "{'title': 'Treesha Rocks!' , 'body': 'It really really rocks.' , 'userId': '1'}"   #this is not working.
- Invoke-RestMethod -Uri "https://jsonplaceholder.typicode.com/posts" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"title": "Treesha Rocks!", "body": "It really really rocks.", "userId": 1}'

# create new post and save on .json file
6) POST a new dummy post and write response to JSON file:
- python ./restful.py post /posts -d '{"title": "Treesha Rocks!" , "body": "It really really rocks." , "userId": "1"}' -o test.json  # this is not working 
- $response = Invoke-RestMethod -Method Post -Uri "https://jsonplaceholder.typicode.com/posts" -Headers @{"Content-Type"="application/json"} -Body '{"title": "Treesha Rocks!", "body": "It really really rocks.", "userId": 1}'

save data on reponce and after save in to ,json file using given command
- $response | ConvertTo-Json | Set-Content -Path "response.json"





