import json,re,threading
from urllib import parse


def hello(name):
    print("hello %s\n" % name)

    global timer
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()


if __name__ == "__main__":
    abc = 'https://chenluo3.chenluo.org/csm3u8.php?url=https://m3u8.chenluo.org/csstv/dy/jishengchong720.m3u8&type=1'
    parsed_tuple = parse.urlparse(abc)
    print(parsed_tuple.query)
    print(parse.parse_qs(parsed_tuple.query))
    print(parse.parse_qs(parsed_tuple.query)['url'])
