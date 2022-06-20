import unicodedata
from utils.text_modifier import text_cleaner

contrat_assistance = [['Type de garantie:\xa0\xa0', 'Contrat'], ['Type de service:\xa0\xa0', 'HPE Foundation Care 24x7 SVC'], ['Type de service:\xa0\xa0', 'HPE Hardware Maintenance Onsite Support*'], ['\\xc3\\x89tat:\xa0\xa0', 'Active '], ['Date de d\\xc3\\xa9but:\xa0\xa0',
                                                                                                                                                                                                                                                '7 ao\\xc3\\xbbt 2020'], ['Date de fin:\xa0\xa0', '6 ao\\xc3\\xbbt 2025'], ['Type de service:\xa0\xa0', 'HPE Collaborative Remote Support'], ['\\xc3\\x89tat:\xa0\xa0', 'Active '], ['Date de d\\xc3\\xa9but:\xa0\xa0', '7 ao\\xc3\\xbbt 2020'], ['Date de fin:\xa0\xa0', '6 ao\\xc3\\xbbt 2025']]


def array_cleaner(array):
    for elements in array:
        array.append(text_cleaner(elements))


array_cleaner(contrat_assistance)

contrat_assistance = """type de garantie:   contrat
type de service:   hpe foundation care 24x7 svc
type de service:   hpe hardware maintenance onsite support*
etat:   active
date de debut:   7 aout 2020
date de fin:   6 aout 2025
type de service:   hpe collaborative remote support
etat:   active
date de debut:   7 aout 2020
date de fin:   6 aout 2025"""

garantie = """type de garantie:   garantie de base
type de service:   wty: hpe hw maintenance onsite support*
etat:   active
date de debut:   20 juil. 2020
date de fin:   18 aout 2023
niveaux de service :   standard material handling
global coverage
nextavail techresource remote
std office hrs std office days
nextavail techresource onsite
no usage limitation
next cov day onsite response
standard parts logistics
elements a livrer:   onsite support
parts and material provided
hardware problem diagnosis
type de service:   wty: hpe support for initial setup
etat:   expire
date de debut:   20 juil. 2020
date de fin:   16 nov. 2020
niveaux de service :   nextavail techresource remote
std office hrs std office days
2 hr remote response
unlimited named callers
elements a livrer:   initial setup assistance
* remarque : selon les termes d'assistance sur site hpe hw maintenance ; hpe peut a sa seule discretion decider si un defaut est reparable :
a distance
a l'aide d'une piece de reparation par le client
par une demande d'intervention a l'emplacement de l'appareil defectueux
pour plus de details consultez le document  garantie limitee et assistance technique internationales  qui a ete livre avec le produit."""

# text = "Date de fin:\xa0\xa0', '6 ao�t 2025"
# try:
#     text = unicode(text, 'utf-8')
# except NameError:
#     pass
#     text = unicodedata.normalize('NFD', text).encode(
#         'ascii', 'ignore').decode("utf-8")
# print(str(text))


def txt_cleaner():
    contrat_assistance = text_cleaner(contrat_assistance)
    garantie = text_cleaner(garantie)
    garantie = garantie[: -5]
    print(garantie)

    i = 0
    # for elem in contrat_assistance:
    #     print(dict([elem]))
    #     i = + 1

    for elem in garantie:
        # print(elem)
        try:
            print(dict([elem]))
        except ValueError:
            concatenate = str(elem[1] + ': ' + elem[2])
            print(dict([[elem[0], concatenate]]))
