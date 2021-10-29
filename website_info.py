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


def status():  # For each status code, I will add the description and it will show up whenever status() is called upon
    global r
    if r.status_code == 100:
        print("Status Code: {}({})".format(r.status_code, "Continue"))
    elif r.status_code == 101:
        print("Status Code: {}({})".format(r.status_code, "Switching Protocol"))
    elif r.status_code == 102:
        print("Status Code: {}({})".format(r.status_code, "Processing"))
    elif r.status_code == 103:
        print("Status Code: {}({})".format(r.status_code, "Early Hints"))
    elif r.status_code == 200:
        print("Status Code: {}({})".format(r.status_code, "OK"))
    elif r.status_code == 201:
        print("Status Code: {}({})".format(r.status_code, "Created"))
    elif r.status_code == 202:
        print("Status Code: {}({})".format(r.status_code, "Non-Authoritative Information"))
    elif r.status_code == 203:
        print("Status Code: {}({})".format(r.status_code, "Switching Protocol"))
    elif r.status_code == 204:
        print("Status Code: {}({})".format(r.status_code, "No Content"))
    elif r.status_code == 205:
        print("Status Code: {}({})".format(r.status_code, "Reset Content"))
    elif r.status_code == 206:
        print("Status Code: {}({})".format(r.status_code, "Partial Content"))
    elif r.status_code == 207:
        print("Status Code: {}({})".format(r.status_code, "Multi-Status"))
    elif r.status_code == 208:
        print("Status Code: {}({})".format(r.status_code, "Already Reported"))
    elif r.status_code == 226:
        print("Status Code: {}({})".format(r.status_code, "IM Used"))
    elif r.status_code == 300:
        print("Status Code: {}({})".format(r.status_code, "Multiple Choice"))
    elif r.status_code == 301:
        print("Status Code: {}({})".format(r.status_code, "Moved Permanently"))
    elif r.status_code == 302:
        print("Status Code: {}({})".format(r.status_code, "Found"))
    elif r.status_code == 303:
        print("Status Code: {}({})".format(r.status_code, "See Other"))
    elif r.status_code == 304:
        print("Status Code: {}({})".format(r.status_code, "Not Modified"))
    elif r.status_code == 305:
        print("Status Code: {}({})".format(r.status_code, "Use Proxy"))
    elif r.status_code == 307:
        print("Status Code: {}({})".format(r.status_code, "Temporary Redirect"))
    elif r.status_code == 308:
        print("Status Code: {}({})".format(r.status_code, "Permanent Redirect"))
    elif r.status_code == 400:
        print("Status Code: {}({})".format(r.status_code, "Bad Request"))
    elif r.status_code == 401:
        print("Status Code: {}({})".format(r.status_code, "Unauthorized"))
    elif r.status_code == 402:
        print("Status Code: {}({})".format(r.status_code, "Payment Required"))
    elif r.status_code == 403:
        print("Status Code: {}({})".format(r.status_code, "Forbidden"))
    elif r.status_code == 404:
        print("Status Code: {}({})".format(r.status_code, "Not Found"))
    elif r.status_code == 405:
        print("Status Code: {}({})".format(r.status_code, "Method Not Allowed"))
    elif r.status_code == 406:
        print("Status Code: {}({})".format(r.status_code, "Not Acceptable"))
    elif r.status_code == 407:
        print("Status Code: {}({})".format(r.status_code, "Proxy Authentication Required"))
    elif r.status_code == 408:
        print("Status Code: {}({})".format(r.status_code, "Request Timeout"))
    elif r.status_code == 409:
        print("Status Code: {}({})".format(r.status_code, "Conflict"))
    elif r.status_code == 410:
        print("Status Code: {}({})".format(r.status_code, "Gone"))
    elif r.status_code == 411:
        print("Status Code: {}({})".format(r.status_code, "Length Required"))
    elif r.status_code == 412:
        print("Status Code: {}({})".format(r.status_code, "Precondition Failed"))
    elif r.status_code == 413:
        print("Status Code: {}({})".format(r.status_code, "Payload Too Large"))
    elif r.status_code == 414:
        print("Status Code: {}({})".format(r.status_code, "URI Too Long"))
    elif r.status_code == 415:
        print("Status Code: {}({})".format(r.status_code, "Unsupported Media Type"))
    elif r.status_code == 416:
        print("Status Code: {}({})".format(r.status_code, "Range Not Satisfiable"))
    elif r.status_code == 417:
        print("Status Code: {}({})".format(r.status_code, "Expectation Failed"))
    elif r.status_code == 418:
        print("Status Code: {}({})".format(r.status_code, "I'm a teapot"))
    elif r.status_code == 421:
        print("Status Code: {}({})".format(r.status_code, "Misdirected Request"))
    elif r.status_code == 422:
        print("Status Code: {}({})".format(r.status_code, "Unprocessable Entity"))
    elif r.status_code == 423:
        print("Status Code: {}({})".format(r.status_code, "Locked"))
    elif r.status_code == 424:
        print("Status Code: {}({})".format(r.status_code, "Failed Dependency"))
    elif r.status_code == 425:
        print("Status Code: {}({})".format(r.status_code, "Too Early"))
    elif r.status_code == 426:
        print("Status Code: {}({})".format(r.status_code, "Upgrade Required"))
    elif r.status_code == 428:
        print("Status Code: {}({})".format(r.status_code, "Precondition Required"))
    elif r.status_code == 429:
        print("Status Code: {}({})".format(r.status_code, "Too Many Requests"))
    elif r.status_code == 431:
        print("Status Code: {}({})".format(r.status_code, "Request Header Fields Too Large"))
    elif r.status_code == 451:
        print("Status Code: {}({})".format(r.status_code, "Unavailable For Legal Reasons"))
    elif r.status_code == 500:
        print("Status Code: {}({})".format(r.status_code, "Internal Server Error"))
    elif r.status_code == 501:
        print("Status Code: {}({})".format(r.status_code, "Not Implemented"))
    elif r.status_code == 502:
        print("Status Code: {}({})".format(r.status_code, "Bad Gateway"))
    elif r.status_code == 503:
        print("Status Code: {}({})".format(r.status_code, "Service Unavailable"))
    elif r.status_code == 504:
        print("Status Code: {}({})".format(r.status_code, "Gateway Timeout"))
    elif r.status_code == 505:
        print("Status Code: {}({})".format(r.status_code, "HTTP Version Not Supported"))
    elif r.status_code == 506:
        print("Status Code: {}({})".format(r.status_code, "Variant Also Negotiates"))
    elif r.status_code == 507:
        print("Status Code: {}({})".format(r.status_code, "Insufficient Storage"))
    elif r.status_code == 508:
        print("Status Code: {}({})".format(r.status_code, "Loop Detected"))
    elif r.status_code == 510:
        print("Status Code: {}({})".format(r.status_code, "Not Extended"))
    elif r.status_code == 511:
        print("Status Code: {}({})".format(r.status_code, "Network Authentication Required"))


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


def header():   # This function shows us the header of the URL we requested
    request()
    print(r.headers)


def cookie():   # We can see if the website is using any cookies with us.
    request()
    print(r.cookies)


def content():  # We can see the contents of the website in human readable form
    request()
    print(r.text)


def end_prog(): # Ends the program. Created to complete an if condition.
    exit()


if "-u" in sys.argv:    # Makes sure the request() is called only when the appropriate switch is there
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

