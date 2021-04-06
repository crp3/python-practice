class Button(object):
    html = ""
    def get_html(self):
        return self.html
    

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class SVG(Button):
    html = "<svg></svg>"

class ButtonFactory():
    def create(self, kind):
        return globals()[kind]()

if __name__ == '__main__':
    kinds = ['Image', 'Input', 'SVG']
    factory = ButtonFactory()

    for index, kind in enumerate(kinds):
        obj = factory.create(kind)
        if index == 0:
            assert type(obj) == Image
        elif index == 1:
            assert type(obj) == Input
        elif index == 2:
            assert type(obj) == SVG
        print(obj.get_html())
