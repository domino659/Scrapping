from bs4 import BeautifulSoup as bs


from utils.xlsx_manager import open_xlsx
from utils.text_modifier import normalizer

# data = '''<tbody><tr><td style="width:25%" class="hpui-padding-bottom-10">Type de garantie:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">Garantie de base</td></tr><tr><td class="hpui-padding-bottom-10">Type de service:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10"><b>Wty: HPE HW Maintenance Onsite Support*</b></td></tr><tr><td class="hpui-padding-bottom-10">État:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10 hpui-emphasized-text" style="color: Green">Active </td></tr><tr><td class="hpui-padding-bottom-10">Date de début:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">20 juil. 2020</td></tr><tr><td class="hpui-padding-bottom-10">Date de fin:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">18 août 2023</td></tr><tr><td valign="top" class="hpui-padding-bottom-10">Niveaux de service&nbsp;:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">Standard Material Handling<br>Global Coverage<br>NextAvail TechResource Remote<br>Std Office Hrs Std Office Days<br>NextAvail TechResource Onsite<br>Next Cov Day Onsite Response<br>Standard Parts Logistics<br>No Usage Limitation<br></td></tr><tr><td valign="top" class="hpui-padding-bottom-10">Éléments à livrer:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">Onsite Support<br>Parts and Material provided<br>Hardware Problem Diagnosis<br></td></tr><tr><td class="hpui-padding-bottom-10">Type de service:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10"><b>Wty: HPE Support for Initial Setup</b></td></tr><tr><td class="hpui-padding-bottom-10">État:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10 hpui-emphasized-text" style="color: Red">Expiré</td></tr><tr><td class="hpui-padding-bottom-10">Date de début:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">20 juil. 2020</td></tr><tr><td class="hpui-padding-bottom-10">Date de fin:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">16 nov. 2020</td></tr><tr><td valign="top" class="hpui-padding-bottom-10">Niveaux de service&nbsp;:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">NextAvail TechResource Remote<br>Std Office Hrs Std Office Days<br>2 Hr Remote Response<br>Unlimited Named Callers<br></td></tr><tr><td valign="top" class="hpui-padding-bottom-10">Éléments à livrer:&nbsp;&nbsp;</td><td class="hpui-padding-bottom-10">Initial Setup Assistance<br></td></tr><tr><td colspan="2" class="hpui-secondary-text1"><span class="hpui-emphasized-text">* Remarque&nbsp;:</span> Selon les termes d'assistance sur site HPE HW Maintenance&nbsp;; HPE peut à sa seule discrétion décider si un défaut est réparable&nbsp;:<ul><li>À distance</li><li>À l'aide d'une pièce de réparation par le client</li><li>Par une demande d'intervention à l'emplacement de l'appareil défectueux</li></ul>Pour plus de détails consultez le document «&nbsp;Garantie limitée et assistance technique internationales&nbsp;» qui a été livré avec le produit.<p></p></td></tr></tbody>'''

# content = unescape(unicodedata.normalize('NFKC', data))


# soup = bs((content), 'lxml')
# table = []
# rows = soup.find_all('tr')
# for row in rows:
#     table_row = []
#     columns = row.find_all('td')
#     for column in columns:
#         table_row.append(column.get_text())
#     table.append(normalizer(table_row))
# print(table)


contrat = [['Type de garantie:', 'Contrat'], ['Type de service:', 'HPE Foundation Care 24x7 SVC'], ['Type de service:', 'HPE Hardware Maintenance Onsite Support*'], ['État:', 'Active'], ['Date de début:',
                                                                                                                                                                                           '7 août 2020'], ['Date de fin:', '6 août 2025'], ['Type de service:', 'HPE Collaborative Remote Support'], ['État:', 'Active'], ['Date de début:', '7 août 2020'], ['Date de fin:', '6 août 2025']]
garantie = [['Type de garantie:', 'Garantie de base'], ['Type de service:', 'Wty: HPE HW Maintenance Onsite Support*'], ['État:', 'Active'], ['Date de début:', '20 juil. 2020'], ['Date de fin:', '18 août 2023'], ['Niveaux de service :', 'Standard Material HandlingGlobal CoverageNextAvail TechResource RemoteStd Office Hrs Std Office DaysNextAvail TechResource OnsiteNext Cov Day Onsite ResponseStandard Parts LogisticsNo Usage Limitation'], ['Éléments à livrer:', 'Onsite SupportParts and Material providedHardware Problem Diagnosis'], ['Type de service:', 'Wty: HPE Support for Initial Setup'], ['État:', 'Expiré'], ['Date de début:',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           '20 juil. 2020'], ['Date de fin:', '16 nov. 2020'], ['Niveaux de service:', 'NextAvail TechResource RemoteStd Office Hrs Std Office Days2 Hr Remote ResponseUnlimited Named Callers'], ['Éléments à livrer:', 'Initial Setup Assistance'], ["* Remarque : Selon les termes d'assistance sur site HPE HW Maintenance; HPE peut à sa seule discrétion décider si un défaut est réparable:À distanceÀ l'aide d'une pièce de réparation par le clientPar une demande d'intervention à l'emplacement de l'appareil défectueuxPour plus de détails consultez le document « Garantie limitée et assistance technique internationales » qui a été livré avec le produit."]]


def write_xlsx(data):
    array = open_xlsx()
    # print(array)


write_xlsx(contrat)


# pop first element array
# put this element as Key
# and rest as value wiht index

my_list = ['Nagendra', 'Babu', 'Nitesh', 'Sathya']
my_dict = dict()
for index, value in enumerate(contrat):
    my_dict[index] = value
print(my_dict)
# OUTPUT
{0: 'Nagendra', 1: 'Babu', 2: 'Nitesh', 3: 'Sathya'}
