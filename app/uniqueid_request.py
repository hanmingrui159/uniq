import requests
import argparse

# response = requests.post('http://httpbin.org/post', data={'key1':'value1'})
# print(response.request.url)
# print(response.request.body)
# print(response.request.headers)


def try_request_uuid4():
    response = requests.get('http://172.31.107.232:8105/uuid4',stream=True)
    x = response.content.decode("utf-8") 
    print(x)
    
def try_request_snowid():
    response = requests.get('http://k8s-dev-uniqueid-fc495960de-4417dc3c9d629f4b.elb.us-east-1.amazonaws.com:8105/snowid',stream=True)
    x = response.content.decode("utf-8") 
    print(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's go working!!!")
    parser.add_argument('code', type=int,
                    help='cmd code: 0->uuid4, 1->snowid')
    
    args = parser.parse_args()
    cmd_code = args.code
    
    if cmd_code == 0:
        try_request_uuid4()
    elif cmd_code == 1:
        try_request_snowid()
    else:
        print("Error: no such cmd code!")
