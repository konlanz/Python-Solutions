from http.client import HTTPConnection  
conn = HTTPConnection("radio.modernghana.com")  
conn.request("GET", "/station/mellowfm")    
result = conn.getresponse()  
# retrieves the entire contents.    
contents = result.read()   
print(contents)  
