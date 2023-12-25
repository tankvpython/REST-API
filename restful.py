import argparse
import requests
import json

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, method, path, data=None):
        url = f"{self.base_url}/{path}"
        print("url---------------", url, path)

        response = requests.request(method, url, json=data)

        print(f"Response Status Code: {response.status_code}")

        if not response.ok:
            print(f"Error: {response.text}")
            exit(1)

        return response.json()

def main():
    parser = argparse.ArgumentParser(description="Simple RESTful client.")

    # Change choices to lower case
    parser.add_argument("method", choices=["get", "post"], help="Request method")
    parser.add_argument("endpoint", help="Request endpoint URI fragment")

    # Change short options to -d and -o
    parser.add_argument("-d", "--data", help="Data to send with request")
    parser.add_argument("-o", "--output", help="Output to .json or .csv file (default: dump to stdout)")

    args = parser.parse_args()

    base_url = "https://jsonplaceholder.typicode.com/"  # Using httpbin as a testing endpoint
    rest_client = RestClient(base_url)

    data = None
    if args.data:
        data = args.data

    response_data = rest_client.make_request(args.method.upper(), args.endpoint, data)

    if args.output:
        # write file using "-o", "--output" 
        with open(args.output, "w") as output_file:
            json.dump(response_data, output_file, indent=2)
        print(f"Response data written to {args.output}")
    else:
        # Print the response data to stdout if no output file is specified
        print("Response Data:", response_data)


if __name__ == "__main__":
    main()
