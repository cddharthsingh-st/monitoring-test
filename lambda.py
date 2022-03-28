import requests

def hellowWorld1(event, context):
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    res = {
        "event": event,
        "output": response.json(),
        "context": context
    }
    print(res)
    return None

def secondLambda(event, context):
    lst = []
    for i in range(20):
        lst.append(i*i)
    print (lst)
    return None