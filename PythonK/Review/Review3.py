#Setting List Class Variable
LGender = ['Man', 'Woman']

#Class Review
class CPerson:
    VsName   = ''
    ViAge    = 0
    VlGender = LGender

    def __init__(self, VsName, ViAge, VlGender):
        self.VsName   = VsName
        self.ViAge    = ViAge
        self.VlGender = VlGender

    def DIntroduce(self):
        return self.VsName, self.ViAge

#Class Instance
Kangster = CPerson('Kang', 29, LGender[0])
    ##Kangster.FName = 'Kang'
    ##Kangster.FAge  = 29
    ##Kangster.FGender = Gender[0]
print(Kangster.DIntroduce());

#Class Inheritance
class CDeveloper(CPerson):
    VsLanguage = ''

    def __init__(Self, VsName, viAge, VlGender):
        DInitParent = super(CDeveloper, self)

    def DIntroduceLanguage(self):
        return self.VsLanguage

IEunFlower = CDeveloper('Kwon', 28, LGender[1]);
IEunFlower.VsLanguage = 'Delphi'
print(IEunFlower.VsName, IEunFlower.DIntroduceLanguage())
