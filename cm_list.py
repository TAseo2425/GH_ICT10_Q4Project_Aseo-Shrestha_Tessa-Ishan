from pyscript import display, document
class cm:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        display(f'Hi! I am {self.name} from {self.section}. My favorite subject is {self.subject}.', target='output5')


cm1 = cm('Benigo Rivera', 'Sapphire', 'PE')
cm2 = cm('Seth Ngo', 'Sapphire', 'Social Studies')
cm3 = cm('Vito DeGuzman', 'Sapphire' , 'Break Time')
cm4 = cm('Tessa Aseo', 'Sapphire', 'Science')
cm5 = cm('Jennifer Uy', 'Sapphire', 'Music')

classmates = [cm1, cm2, cm3, cm4, cm5]

for c in classmates:
    c.introduce()


def create_cm(e):
    class cm6(cm):
        pass

    document.getElementById('output5').innerHTML = ''

    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('favorite_subject').value

    new_cm = cm6(name, section, subject)

    classmates.append(new_cm)

    for c in classmates:
        c.introduce()