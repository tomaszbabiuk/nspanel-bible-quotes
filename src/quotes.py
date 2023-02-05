import json
from nextion import *

class NextQuoteAction(NextionAction):
    def __init__(self, writer: NextionWriter):
        super().__init__(writer)
        with open("quotes.json", "r") as f:
            self.quotes = json.load(f)["pl"]
            self.count = len(self.quotes)
            self.i = 0

    def checkMatch(self, data: bytearray):
        return len(data) == 2 and data[0] == 0x01 and data[1] == 0x01

    def act(self, data: bytearray):
        quote = self.quotes[self.i % self.count]
        self.writer.write('titleTxt.txt="', insertDelimeter=False)
        self.writer.write(quote["from"], insertDelimeter=False)
        self.writer.write('"')

        print(quote["from"])

        self.writer.write('messageTxt.txt="{}"'.format(quote["quote"]))
        self.i += 1

def createBibleActions(actionsBag, writer: NextionWriter):
    nextQuoteAction = NextQuoteAction(writer)
    actionsBag.append(nextQuoteAction)