import requests as rq 
import json



def get_data(url):
    try:
        print("***********")
        return rq.get(url).text
    except Exception as e:
        print("Unable to load url", e)
        
def load_json(data):
    if not data is None:
        j = json.loads(data) 
        
        fname = j["results"][0]["name"]["first"] 
        lname = j["results"][0]["name"]["last"] 
        
        return fname, lname 
    

def main():
    url = "https://randomuser.me/api"
    
    values = load_json(get_data(url))
    
    if not values is None:
        print("First Name: ", values[0])
        print("Last Name: ", values[1])


if __name__ == "__main__":
    main()