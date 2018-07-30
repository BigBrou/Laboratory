VdLanguage = {
    'Korean'   : 'Number9',
    'English'  : 'Number2',
    'Chinese'  : 'Number3',
    'Taiwan'   : 'Number1'
}

def printDictionaryKey():
    for Language in VdLanguage.keys():
        print(Language)
    print('')

def printDictionaryValue():
    for Language in VdLanguage.values():
        print(Language)
    print('')

def printDictionaryItem():
    for LanguageKey, LanguageValue in VdLanguage.items():
        print('{}, {}'.format(LanguageKey, LanguageValue))
    print('')

printDictionaryKey()

VdLanguage['Japanese'] = 'Number4';
printDictionaryValue()

del(VdLanguage['Japanese'])
printDictionaryItem()
