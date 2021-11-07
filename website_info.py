#!/bin/python3
import requests
import sys


def help_message():  # This help_message() function just describes what each function in the program stands for
    print("\t" * 3 + "The Help Menu!")
    print("GET Procedures")
    print("\t-c" + "\t" * 6 + "Cookies Found")
    print("\t-h: equivalent to --help" + "\t" * 3 + "Help Menu")
    print("\t--headers" + "\t" * 5 + "Headers of the URL")
    print("\t--history" + "\t" * 5 + "History of the response\n " + "\t" * 7 + " object")
    print("\t--json" + "\t" * 6 + "Presents the data in JSO\n" + "\t" * 7 + " N format")
    print("\t-s" + "\t" * 6 + "Status Code")
    print("\t-u" + "\t" * 6 + "URL")
    print("\t-x" + "\t" * 6 + "Contents of the website\n" + "\t" * 7 + " in human-readable form")


x = len(sys.argv)
if len(sys.argv) in range(2):  # If the break is not there, it would print it two times because of the range we've
    # given it.
    help_message()
    exit()

for x in range(2, ):
    if sys.argv[1].startswith("http"):  # After the program's name, if a URL is present it raises this error
        print("Please enter the appropriate switch before the URL.")
        break
    elif len(sys.argv) == 2 and "-h" in sys.argv or "--help" in sys.argv:
        help_message()
        break
    elif len(sys.argv) < 3:  # If there is only one switch given and no URL
        print("Please enter a URL with the appropriate switch.")
        exit()  # If there is no url given in the argument, the program displays this message and exits.
    elif sys.argv[2].startswith("http"):
        url = sys.argv[2]
        continue
    else:
        continue

global r


def status():  # For each status code, I will add scthe description and it will show up whenever status() is called upon
    global r
    codes = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 306,
             307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418,
             421, 422, 423, 424, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
    messages = ["Continue", "Switching Protocol", "Processing", "Early Hints", "OK", "Created",
                "Non-Authoritative Information", "Switching Protocol", "No Content", "Reset Content", "Partial Content"
                , "Multi-Status", "Already Reported", "IM Used", "Multiple Choice", "Moved Permanently", "Found",
                "See Other", "Not Modified", "Use Proxy", "Temporary Redirect", "Permanent Redirect", "Bad Request",
                "Unauthorized", "Payment Required", "Forbidden", "Not Found", "Method Not Allowed", "Not Acceptable",
                "Proxy Authentication Required", "Request Timeout", "Conflict", "Gone", "Length Required",
                "Precondition Failed", "Payload Too Large", "URI Too Long", "Unsupported Media Type",
                "Range Not Satisfiable", "Expectation Failed", "I'm a teapot", "Misdirected Request",
                "Unprocessable Entity", "Locked", "Failed Dependency", "Too Early", "Upgrade Required",
                "Precondition Required", "Too Many Requests", "Request Header Fields Too Large",
                "Unavailable For Legal Reasons", "Internal Server Error", "Not Implemented", "Bad Gateway",
                "Service Unavailable", "Gateway Timeout", "HTTP Version Not Supported", "Variant Also Negotiates",
                "Insufficient Storage", "Loop Detected", "Not Extended", "Network Authentication Required"]
    for i in range(0, len(codes)):
        if codes[i] == r.status_code:   # We iterate through each status code using it's index then when it is equal
            # to the request's status code, we print it along with the corresponding message
            print(codes[i], messages[i])


def request():  # Our main function that we can use with our URL
    global r
    r = requests.get(url, stream=True, timeout=5)
    if len(sys.argv) < 3:
        print("Please enter the appropriate switch based on your needs.")


def jason():  # We can get results using json format when this function is called
    request()
    print(r.json())


def history():  # This function shows the response objects that were created in order to complete a request. Not
    # fully implemented yet.
    request()
    print(r.history)


def header():  # This function shows us the header of the URL we requested
    request()
    print(r.headers)


def cookie():  # We can see if the website is using any cookies with us.
    request()
    print(r.cookies)


def content():  # We can see the contents of the website in human readable form
    request()
    print(r.text)


def end_prog():  # Ends the program. Created to complete an if condition.
    exit()


if "-u" in sys.argv:  # Makes sure the request() is called only when the appropriate switch is there
    request()
    if "--headers" in sys.argv:
        header()
    if "-x" in sys.argv:
        content()
    if "-c" in sys.argv:
        cookie()
    if "-s" in sys.argv:
        status()
    if "--json" in sys.argv:
        jason()
    if "--history" in sys.argv:
        history()
    else:
        end_prog()
