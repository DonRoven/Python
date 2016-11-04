class Student(object):


    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.result = {'labs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'exam': 0}
        self.i = 0

    def make_lab(self, m, n = None):
        if self.conf['lab_max'] >= m:
            if n == None:
                self.result['labs'][self.i] = m
                self.i +=1
            else:
                self.result['labs'][n] = m
        else:
            if n == None:
                self.result['labs'][self.i] = self.conf['lab_max']
                self.i +=1
            else:
                self.result['labs'][n] = self.conf['lab_max']



    def make_exam(self, m):
        if self.conf['exam_max'] > m:
            self.result['exam'] = m
        else:
            self.result['exam'] = self.conf['exam_max']


    def is_certified(self):
        s = self.result['exam'] + sum(self.result['labs'])
        if s/((self.conf['lab_max'] * self.conf['lab_num']) + self.conf['exam_max']) > self.conf['k']:
            return (s, True)
        else:
            return (s, False)




conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}

oleg = Student('Oleg', conf)
oleg.make_lab(1).make_lab(8,0).make_lab(1).make_lab(10,7).make_lab(4,1).make_lab(5).make_lab(6.5).make_exam(32)
print (oleg.is_certified())
oleg.make_lab(7,1)
print (oleg.is_certified())

print(oleg.result)


