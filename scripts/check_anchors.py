import sys
from html.parser import HTMLParser

class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = set()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr == "href" and value.startswith("#") and len(value) > 1:
                self.hrefs.add(value[1:])
            if attr == "id":
                self.ids.add(value)

def main():
    parser = AnchorParser()
    with open("index.html", encoding="utf-8") as f:
        parser.feed(f.read())
    missing = sorted(parser.hrefs - parser.ids)
    if missing:
        for anchor in missing:
            print(f"Missing anchor: #{anchor}")
        sys.exit(1)
    print("All anchor links resolve to existing ids.")

if __name__ == "__main__":
    main()
