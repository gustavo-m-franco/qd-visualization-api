### QuaDev Visualization Service
Consuming: azure-cognitiveservices-vision-computervision
source myenv/bin/activate


## Use case
Service will receive an image with code in it and possibly another image with an exercise statement referrred to the code, and will capture the code and the statement and send them to chat gpt for a response.
Also the service could receive the statement in text and only need the OCR to capture the code fromt the image.


curl.exe -H "Ocp-Apim-Subscription-Key: <subscriptionKey>" -H "Content-Type: application/json" "https://<endpoint>/computervision/imageanalysis:analyze?features=caption,read&model-version=latest&language=en&api-version=2023-02-01-preview" -d "{'url':'https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png'}"

Image examples:
# code: https://global.discourse-cdn.com/business7/uploads/codewithmosh/original/1X/38220fb4a5b574ee5341b68f3a5a00452472b4c4.png
# table: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM0qp4O3V-zsnfkvAvTTQDs-27ZE8sVR5mvJO-1IjsqhtDs1MugcKYeTwmE4ICU-uz-28&usqp=CAU 
# person sitting in front of a computer: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMYTkXomgV45DFsmAMEw9LZYLGptflBmdbmA&usqp=CAU
# html table: https://www.simplilearn.com/ice9/free_resources_article_thumb/defining_html_tables-html_tables.PNG


##Dependencies
These are managed through `requirements.txt`, which contains the dependencies used in the code (Live dependencies). On another side, dependencies related to the development environment are installed using `requirements-dev.txt`.

