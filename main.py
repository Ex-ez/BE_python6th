from urllib.request import urlopen
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    data_set = set(x for x in parser.result)
    return data_set


def main():
    url = 'https://google.co.kr'
    with urlopen(url) as f:
        charset = f.headers.get_params('charset')[1][1]
        print(charset)
        data = f.read().decode(charset)

    data_set = parse_image(data)
    print('\n>>>>> Fetch Images from', url)
    print('\n'.join(sorted(data_set)))


if __name__ == '__main__':
    main()