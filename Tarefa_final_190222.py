import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

def get_data_web(repo_file, file_name):

  url = repo_file
  response = requests.get(url)

  with open(file_name, 'w', encoding='utf-8') as f:
    f.write(response.text)

url_1 = 'https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-codebook.csv'
url_2 = 'https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-data.csv'
file_name_1 = 'owid-co2-codebook.csv'
file_name_2 = 'owid-co2-data.csv'
url_download = 'https://zenodo.org/records/14054503/files/GMST_response_1851-2023.csv'
file_name_3 = 'GMST_response_1851-2023.csv'

get_data_web(url_1, file_name_1)
get_data_web(url_2, file_name_2)
get_data_web(url_download, file_name_3)

df_codebook = pd.read_csv('owid-co2-codebook.csv')
df_co2 = pd.read_csv('owid-co2-data.csv')

# Verificando dados
print ("Tabela 1 - Verificação de dados")
print(df_co2.info())
print("\n")

# Verificando se há algum valor vazio
print ("Tabela 2 - Verificação de dados vazios")
print(df_co2.isna().any())
print("\n")

# Verificando quantidade de dados vazios
print ("Tabela 3 - Verificação de quantidade de dados vazios")
print(df_co2.isna().sum())
print("\n")

df_co2['ghg_person'] = (df_co2['total_ghg']*(10**6))/df_co2['population']

df_co2['ghg_person']=df_co2['ghg_person']

df_co2['co2_person'] = (df_co2['co2']*(10**6))/df_co2['population']

df_co2['co2_person'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2011)]

df_co2['methane_person'] = (df_co2['methane']*(10**6))/df_co2['population']

df_co2['methane_person'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2011)]

df_co2['nitrous_oxide_person'] = (df_co2['nitrous_oxide']*(10**6))/df_co2['population']

df_co2['nitrous_oxide_person'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2011)]

df_co2['warming_impact'] = (df_co2['temperature_change_from_co2'] +
                            (df_co2['temperature_change_from_ch4'] +
                            df_co2['temperature_change_from_n2o']))

df_co2['warming_impact'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2023)]

df_temp_data = pd.read_csv('GMST_response_1851-2023.csv')

# Verificando dados
print ("Tabela 1 - Verificação de dados")
print(df_temp_data.info())
print("\n")

# Verificando se há algum valor vazio
print ("Tabela 2 - Verificação de dados vazios")
print(df_temp_data.isna().any())
print("\n")

# Verificando quantidade de dados vazios
print ("Tabela 3 - Verificação de quantidade de dados vazios")
print(df_temp_data.isna().sum())
print("\n")

df_temp_data = df_temp_data.rename(columns={'CNTR_NAME': 'country'})

paises_1 = set(df_co2['country'].unique())
paises_2 = set(df_temp_data['country'].unique())

so_no_dfco2 = paises_1-paises_2
so_no_dftemp = paises_2-paises_1

print(so_no_dfco2)
print(so_no_dftemp)

new_countries_name_temperature = {
  "Afghanistan": "Afghanistan",
  "Albania": "Albania",
  "Algeria": "Algeria",
  "Andorra": "Andorra",
  "Angola": "Angola",
  "Anguilla": "Anguilla",
  "Antarctica": "Antarctica",
  "Antigua and Barbuda": "Antigua and Barbuda",
  "Argentina": "Argentina",
  "Armenia": "Armenia",
  "Aruba": "Aruba",
  "Australia": "Australia",
  "Austria": "Austria",
  "Azerbaijan": "Azerbaijan",
  "Bahamas": "Bahamas",
  "Bahrain": "Bahrain",
  "Bangladesh": "Bangladesh",
  "Barbados": "Barbados",
  "Belarus": "Belarus",
  "Belgium": "Belgium",
  "Belize": "Belize",
  "Benin": "Benin",
  "Bermuda": "Bermuda",
  "Bhutan": "Bhutan",
  "Bolivia": "Bolivia",
  "Bonaire, Saint Eustatius and Saba": "Bonaire Sint Eustatius and Saba",
  "Bosnia and Herzegovina": "Bosnia and Herzegovina",
  "Botswana": "Botswana",
  "Brazil": "Brazil",
  "British Virgin Islands": "British Virgin Islands",
  "Brunei Darussalam": "Brunei",
  "Bulgaria": "Bulgaria",
  "Burkina Faso": "Burkina Faso",
  "Burundi": "Burundi",
  "Cambodia": "Cambodia",
  "Cameroon": "Cameroon",
  "Canada": "Canada",
  "Cape Verde": "Cape Verde",
  "Central African Republic": "Central African Republic",
  "Chad": "Chad",
  "Chile": "Chile",
  "China": "China",
  "Christmas Island": "Christmas Island",
  "Colombia": "Colombia",
  "Comoros": "Comoros",
  "Congo": "Congo",
  "Cook Islands": "Cook Islands",
  "Costa Rica": "Costa Rica",
  "Croatia": "Croatia",
  "Cuba": "Cuba",
  "Cura\u00e7ao": "Curacao",
  "Cyprus": "Cyprus",
  "Czechia": "Czechia",
  "C\u00f4te d'Ivoire": "Cote d'Ivoire",
  "Democratic Republic of the Congo": "Democratic Republic of Congo",
  "Denmark": "Denmark",
  "Djibouti": "Djibouti",
  "Dominica": "Dominica",
  "Dominican Republic": "Dominican Republic",
  "EU27": "European Union (27)",
  "Ecuador": "Ecuador",
  "Egypt": "Egypt",
  "El Salvador": "El Salvador",
  "Equatorial Guinea": "Equatorial Guinea",
  "Eritrea": "Eritrea",
  "Estonia": "Estonia",
  "Ethiopia": "Ethiopia",
  "Faeroe Islands": "Faroe Islands",
  "Fiji": "Fiji",
  "Finland": "Finland",
  "France": "France",
  "French Polynesia": "French Polynesia",
  "GLOBAL": "World",
  "Gabon": "Gabon",
  "Gambia": "Gambia",
  "Georgia": "Georgia",
  "Germany": "Germany",
  "Ghana": "Ghana",
  "Greece": "Greece",
  "Greenland": "Greenland",
  "Grenada": "Grenada",
  "Guatemala": "Guatemala",
  "Guinea": "Guinea",
  "Guinea-Bissau": "Guinea-Bissau",
  "Guyana": "Guyana",
  "Haiti": "Haiti",
  "Honduras": "Honduras",
  "Hong Kong": "Hong Kong",
  "Hungary": "Hungary",
  "Iceland": "Iceland",
  "India": "India",
  "Indonesia": "Indonesia",
  "Iran": "Iran",
  "Iraq": "Iraq",
  "Ireland": "Ireland",
  "Israel": "Israel",
  "Italy": "Italy",
  "Jamaica": "Jamaica",
  "Japan": "Japan",
  "Jordan": "Jordan",
  "Kazakhstan": "Kazakhstan",
  "Kenya": "Kenya",
  "Kiribati": "Kiribati",
  "Kosovo": "Kosovo",
  "Kuwait": "Kuwait",
  "Kyrgyzstan": "Kyrgyzstan",
  "Laos": "Laos",
  "Latvia": "Latvia",
  "Lebanon": "Lebanon",
  "Lesotho": "Lesotho",
  "Liberia": "Liberia",
  "Libya": "Libya",
  "Liechtenstein": "Liechtenstein",
  "Lithuania": "Lithuania",
  "Luxembourg": "Luxembourg",
  "Macao": "Macao",
  "Madagascar": "Madagascar",
  "Malawi": "Malawi",
  "Malaysia": "Malaysia",
  "Maldives": "Maldives",
  "Mali": "Mali",
  "Malta": "Malta",
  "Marshall Islands": "Marshall Islands",
  "Mauritania": "Mauritania",
  "Mauritius": "Mauritius",
  "Mexico": "Mexico",
  "Micronesia (Federated States of)": "Micronesia (country)",
  "Moldova": "Moldova",
  "Mongolia": "Mongolia",
  "Montenegro": "Montenegro",
  "Montserrat": "Montserrat",
  "Morocco": "Morocco",
  "Mozambique": "Mozambique",
  "Myanmar": "Myanmar",
  "Namibia": "Namibia",
  "Nauru": "Nauru",
  "Nepal": "Nepal",
  "Netherlands": "Netherlands",
  "New Caledonia": "New Caledonia",
  "New Zealand": "New Zealand",
  "Nicaragua": "Nicaragua",
  "Niger": "Niger",
  "Nigeria": "Nigeria",
  "Niue": "Niue",
  "North Korea": "North Korea",
  "North Macedonia": "North Macedonia",
  "Norway": "Norway",
  "Occupied Palestinian Territory": "Palestine",
  "Oman": "Oman",
  "Pakistan": "Pakistan",
  "Palau": "Palau",
  "Panama": "Panama",
  "Papua New Guinea": "Papua New Guinea",
  "Paraguay": "Paraguay",
  "Peru": "Peru",
  "Philippines": "Philippines",
  "Poland": "Poland",
  "Portugal": "Portugal",
  "Qatar": "Qatar",
  "Romania": "Romania",
  "Russia": "Russia",
  "Rwanda": "Rwanda",
  "Saint Helena": "Saint Helena",
  "Saint Kitts and Nevis": "Saint Kitts and Nevis",
  "Saint Lucia": "Saint Lucia",
  "Saint Pierre and Miquelon": "Saint Pierre and Miquelon",
  "Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines",
  "Samoa": "Samoa",
  "Sao Tome and Principe": "Sao Tome and Principe",
  "Saudi Arabia": "Saudi Arabia",
  "Senegal": "Senegal",
  "Serbia": "Serbia",
  "Seychelles": "Seychelles",
  "Sierra Leone": "Sierra Leone",
  "Singapore": "Singapore",
  "Sint Maarten (Dutch part)": "Sint Maarten (Dutch part)",
  "Slovakia": "Slovakia",
  "Slovenia": "Slovenia",
  "Solomon Islands": "Solomon Islands",
  "Somalia": "Somalia",
  "South Africa": "South Africa",
  "South Korea": "South Korea",
  "South Sudan": "South Sudan",
  "Spain": "Spain",
  "Sri Lanka": "Sri Lanka",
  "Sudan": "Sudan",
  "Suriname": "Suriname",
  "Swaziland": "Eswatini",
  "Sweden": "Sweden",
  "Switzerland": "Switzerland",
  "Syria": "Syria",
  "Taiwan": "Taiwan",
  "Tajikistan": "Tajikistan",
  "Tanzania": "Tanzania",
  "Thailand": "Thailand",
  "Timor-Leste": "East Timor",
  "Togo": "Togo",
  "Tonga": "Tonga",
  "Trinidad and Tobago": "Trinidad and Tobago",
  "Tunisia": "Tunisia",
  "Türkiye": "Turkey",
  "Turkmenistan": "Turkmenistan",
  "Turks and Caicos Islands": "Turks and Caicos Islands",
  "Tuvalu": "Tuvalu",
  "USA": "United States",
  "Uganda": "Uganda",
  "Ukraine": "Ukraine",
  "United Arab Emirates": "United Arab Emirates",
  "United Kingdom": "United Kingdom",
  "Uruguay": "Uruguay",
  "Uzbekistan": "Uzbekistan",
  "Vanuatu": "Vanuatu",
  "Venezuela": "Venezuela",
  "Viet Nam": "Vietnam",
  "Wallis and Futuna Islands": "Wallis and Futuna",
  "Yemen": "Yemen",
  "Zambia": "Zambia",
  "Zimbabwe": "Zimbabwe",
  "Kuwaiti Oil Fires": "Kuwaiti Oil Fires",
  "Ryukyu Islands": "Ryukyu Islands",
  "LDC": "Least developed countries (Jones et al.)",
  "OECD": "OECD (Jones et al.)"
}

excluded_countries_name_temperature = [
    "ANNEXI",
    "ANNEXII",
    "BASIC",
    "EIT",
    "LMDC",
    "NONANNEX",
    "Pacific Islands (Palau)"
]

df_temp_data = df_temp_data[~df_temp_data['country'].isin(excluded_countries_name_temperature)]

df_temp_data['country'] = df_temp_data['country'].replace(new_countries_name_temperature)

url_income_groups = 'https://ourworldindata.org/grapher/world-bank-income-groups.csv?v=1&csvType=full&useColumnShortNames=true'
get_data_web(url_income_groups, 'world-bank-income-groups.csv')

df_income_groups = pd.read_csv('world-bank-income-groups.csv')

df_income_groups = df_income_groups[df_income_groups['Year'] == 2024]

df_income_groups = df_income_groups.rename(columns={'Entity': 'country'})

df_income_groups_ven_eth = pd.concat([
    df_income_groups,
    pd.DataFrame({'country': ['Venezuela', 'Ethiopia'],
                 'Code': ['VEN', 'ETH'],
                 'Year': [2024, 2024],
                 'classification': ['Upper-middle-income countries', 'Low-income countries']})
    ])

df_merge_inc = df_temp_data.merge(
    df_income_groups_ven_eth[['country', 'classification']],
    on='country',
    how='left'
)

df_group = df_merge_inc.groupby(['classification', 'Gas', 'Component','Year', 'Unit'])['Data'].sum().reset_index()

df_group = df_group.rename(columns={'classification': 'country'})

df_comb_temp = pd.concat([df_temp_data, df_group], axis=0, ignore_index=True)

import yaml

url_yaml = 'https://raw.githubusercontent.com/owid/etl/refs/heads/master/etl/steps/data/garden/regions/2023-01-01/regions.yml'
get_data_web(url_yaml, 'regions.yml')

with open('regions.yml') as file:
  df_regions = pd.DataFrame.from_dict(yaml.safe_load(file))


url_regions_code = 'https://raw.githubusercontent.com/owid/etl/refs/heads/master/etl/steps/data/garden/regions/2023-01-01/regions.codes.csv'
get_data_web(url_regions_code, 'regions_code.csv')

df_codes = pd.read_csv('regions_code.csv', keep_default_na=False, na_values=[''])

df_regions['short_name'] = df_regions['short_name'].fillna(df_regions['name'])
df_regions['region_type'] = df_regions['region_type'].fillna('country')

if 'defined_by' not in df_regions.columns:
  df_regions['defined_by'] = pd.Series(dtype=str)
df_regions['defined_by'] = df_regions['defined_by'].fillna('owid')
df_regions['is_historical'] = df_regions['is_historical'].fillna(False)

regions_filter = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America',
                  'Asia (excl. China and India)', 'Europe (excl. EU-27)', 'Europe (excl. EU-28)',
                  'North America (excl. USA)', 'European Union (28)']

df_regions[['code','members']][df_regions['short_name'] =='United Kingdom']

european_union_27 = df_regions.loc[df_regions['short_name'] == 'European Union (27)', 'members'].values[0]
european_union_28 = european_union_27 + ['GBR']
df_regions = pd.concat([
    df_regions,
    pd.DataFrame([{'short_name': 'European Union (28)', 'members': european_union_28}])
], ignore_index=True)

regions_add_dict = {}

regras = [
    ('Asia (excl. China and India)', ['CHN', 'IND'], 'Asia'),
    ('Europe (excl. EU-27)', european_union_27, 'Europe'),
    ('Europe (excl. EU-28)', european_union_28, 'Europe'),
    ('North America (excl. USA)', ['USA'], 'North America')
]

for new_region, to_remove, base_region in regras:

  base_members = df_regions.loc[df_regions['short_name'] == base_region, 'members'].iloc[0]
  new_members = list(set(base_members) - set(to_remove))
  regions_add_dict[new_region] = new_members

df_new_regions = pd.DataFrame(
    [{'short_name': k, 'members': v} for k, v in regions_add_dict.items()]
)

df_region_final = pd.concat([df_regions, df_new_regions], ignore_index=True)

df_regions_short = df_region_final[['short_name','members']][df_region_final['short_name'].isin(regions_filter)]

df_regions_exploded = df_regions_short.explode('members')
df_merge_regions = df_regions_exploded.merge(df_temp_data, left_on='members',
                                             right_on='ISO3', how='left')
df_region_temp = (
    df_merge_regions.groupby(['short_name', 'Year', 'Gas','Component', 'Unit'], as_index=False)['Data'].sum()
)

df_region_temp = df_region_temp.rename(columns={'short_name': 'country'})

df_comb_reg_inc = pd.concat([df_comb_temp, df_region_temp], axis=0, ignore_index=True)

df_comb_reg_inc['category'] = df_comb_reg_inc['Component'] + '_' + df_comb_reg_inc['Gas']

df_comb_reg_inc_pivot = df_comb_reg_inc.pivot_table(
    index=['country', 'Year', 'Unit'],
    columns='category',
    values='Data'
).reset_index()

df_comb_reg_inc_pivot_rename = df_comb_reg_inc_pivot.rename(
    columns={'Year': 'year',
             'Fossil_CH[4]': 'temperature_change_from_ch4_fossil',
             'Fossil_CO[2]': 'temperature_change_from_co2_fossil',
             'Fossil_N[2]*O': 'temperature_change_from_n2o_fossil',
             'Fossil_3-GHG': 'temperature_change_from_ghg_fossil',
             'LULUCF_CH[4]': 'temperature_change_from_ch4_lucf',
             'LULUCF_CO[2]': 'temperature_change_from_co2_lucf',
             'LULUCF_N[2]*O': 'temperature_change_from_n2o_lucf',
             'LULUCF_3-GHG': 'temperature_change_from_ghg_lucf'}
)

df_merge_co2 = df_co2.merge(
    df_comb_reg_inc_pivot_rename[['country', 'year', 'temperature_change_from_ch4_fossil',
                           'temperature_change_from_co2_fossil', 'temperature_change_from_n2o_fossil',
                           'temperature_change_from_ghg_fossil', 'temperature_change_from_ch4_lucf',
                           'temperature_change_from_co2_lucf', 'temperature_change_from_n2o_lucf',
                           'temperature_change_from_ghg_lucf']],
    on=['country', 'year'],
    how='left'
)

income_groups = ['High-income countries', 'Low-income countries', 
                'Lower-middle-income countries', 'Upper-middle-income countries']

df_merge_co2['warming_impact_fossil'] = ((df_merge_co2['temperature_change_from_co2_fossil']) +
                            (df_merge_co2['temperature_change_from_ch4_fossil'] +
                            df_merge_co2['temperature_change_from_n2o_fossil']))

df_merge_co2['warming_impact_land'] = (df_merge_co2['temperature_change_from_co2_lucf'] +
                            (df_merge_co2['temperature_change_from_ch4_lucf'] +
                            df_merge_co2['temperature_change_from_n2o_lucf']))

df_merge_co2_inc = df_merge_co2.merge(
    df_income_groups[['country', 'classification']],
    on='country',
    how='left'
)

df_regions_exploded_2 = df_regions[df_regions['short_name'].isin(['Asia', 'Africa', 'Europe', 'Oceania', 'North America', 'South America'])].explode('members')
df_merge_co2_inc_reg = df_merge_co2_inc.merge(df_regions_exploded_2[['members', 'short_name']], right_on='members',
                                             left_on='iso_code', how='left')

df_merge_co2_inc_reg = df_merge_co2_inc_reg.drop(columns=['members'])

df_merge_co2_inc_reg = df_merge_co2_inc_reg.rename(columns={'classification': 'income_group', 'short_name':'region'})

df_merge_co2_inc_reg['warming_impact_total_Jones'] = df_merge_co2_inc_reg['warming_impact_land'] + df_merge_co2_inc_reg['warming_impact_fossil']

def min_year(df, col_year, col_country, col_ind, country):
  df = df[[col_ind, col_year, col_country]].copy()

  df = df[(df[col_ind] != 0)&(~df[col_ind].isna())]

  min_year = df[col_year][(df[col_country] == country)].min()

  return min_year

def relative_change(df, g, col, col_year='year'):

  start_year = min_year(df, 'year', 'country', col, g.name)
  g = g[g[col_year] >= start_year]
  if g.empty:
    return pd.Series([None]*len(g), index=g.index)
  base_value = g[col].iloc[0]
  rel = ((g[col]) - (base_value)) / abs((base_value))*100
  rel.iloc[0] = 0
  return rel

df_merge_co2_inc_reg['co2_including_luc_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'co2_including_luc'))
)

df_merge_co2_inc_reg['warming_impact_total_Jones_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'warming_impact_total_Jones'))
)

df_merge_co2_inc_reg['warming_impact_fossil_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'warming_impact_fossil'))
)

df_merge_co2_inc_reg['warming_impact_land_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'warming_impact_land'))
)

df_merge_co2_inc_reg['co2_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'co2'))
)

df_merge_co2_inc_reg['land_use_change_co2_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'land_use_change_co2'))
)

df_merge_co2_inc_reg['methane_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'methane'))
)

df_merge_co2_inc_reg['nitrous_oxide_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'nitrous_oxide'))
)

df_merge_co2_inc_reg['total_ghg_relative_change'] = (
    df_merge_co2_inc_reg.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg,g, 'total_ghg'))
)

url_all_emissions = 'https://zenodo.org/records/14054503/files/EMISSIONS_ANNUAL_1830-2023.csv'
get_data_web(url_all_emissions, 'all_emissions.csv')

df_all_emissions = pd.read_csv('all_emissions.csv')

df_all_emissions = df_all_emissions.rename(columns={'CNTR_NAME': 'country'})

df_all_emissions.loc[df_all_emissions['Unit'].str.startswith('Tg'), 'Data'] *= 1e6
df_all_emissions.loc[df_all_emissions['Unit'].str.startswith('Pg'), 'Data'] *= 1e9

df_all_emissions = df_all_emissions.drop(columns='Unit')

df_all_emissions = df_all_emissions[~df_all_emissions['country'].isin(excluded_countries_name_temperature)]

df_all_emissions['country'] = df_all_emissions['country'].replace(new_countries_name_temperature)

df_merge_inc_all_emissions = df_all_emissions.merge(
    df_income_groups_ven_eth[['country', 'classification']],
    on='country',
    how='left'
)

df_group_all_emissions = df_merge_inc_all_emissions.groupby(['classification', 'Gas', 'Component','Year'])['Data'].sum().reset_index()
df_group_all_emissions = df_group_all_emissions.rename(columns={'classification': 'country'})

df_comb_all_emissions = pd.concat([df_all_emissions, df_group_all_emissions], axis=0, ignore_index=True)

df_merge_regions_all_emissions= df_regions_exploded.merge(df_all_emissions, left_on='members',
                                             right_on='ISO3', how='left')
df_region_all_emissions = (
    df_merge_regions_all_emissions.groupby(['short_name', 'Year', 'Gas','Component'], as_index=False)['Data'].sum()
)

df_region_all_emissions = df_region_all_emissions.rename(columns={'short_name': 'country'})

df_comb_reg_inc_all_emissions= pd.concat([df_comb_all_emissions, df_region_all_emissions], axis=0, ignore_index=True)

df_comb_reg_inc_all_emissions['category'] = df_comb_reg_inc_all_emissions['Component'] + '_' + df_comb_reg_inc_all_emissions['Gas']

df_comb_reg_inc_all_emissions_pivot = df_comb_reg_inc_all_emissions.pivot_table(
    index=['country', 'Year'],
    columns='category',
    values='Data'
).reset_index()

df_comb_reg_inc_all_emissions_pivot = df_comb_reg_inc_all_emissions_pivot[df_comb_reg_inc_all_emissions_pivot['Year']>=1850].reset_index(drop=True)

df_comb_reg_inc_all_emissions_rename = df_comb_reg_inc_all_emissions_pivot.rename(
    columns={'Year': 'year',
             'Fossil_CH[4]': 'ch4_fossil_jones',
             'Fossil_CO[2]': 'co2_fossil_jones',
             'Fossil_N[2]*O': 'n2o_fossil_jones',
             'LULUCF_CH[4]': 'ch4_lucf_jones',
             'LULUCF_CO[2]': 'co2_lucf_jones',
             'LULUCF_N[2]*O': 'n2o_lucf_jones',
             'Total_CH[4]': 'ch4_total_jones',
             'Total_CO[2]': 'co2_total_jones',
             'Total_N[2]*O': 'n2o_total_jones'}
)

df_comb_reg_inc_all_emissions_rename['ch4_total_jones'] = (
    df_comb_reg_inc_all_emissions_rename['ch4_fossil_jones']*29.8 +
    df_comb_reg_inc_all_emissions_rename['ch4_lucf_jones']*27.2
)

df_comb_reg_inc_all_emissions_rename['n2o_total_jones'] = (
    df_comb_reg_inc_all_emissions_rename['n2o_total_jones'] * 273
)

df_comb_reg_inc_all_emissions_rename = df_comb_reg_inc_all_emissions_rename.drop(columns=[
    'ch4_fossil_jones', 'n2o_fossil_jones', 'ch4_lucf_jones', 'n2o_lucf_jones'
])

df_co2_land_use_gb = pd.read_excel('National_LandUseChange_Carbon_Emissions_2024v1.0-1.xlsx', sheet_name='BLUE', header=7)

df_co2_world_land = pd.read_excel('Global_Carbon_Budget_2024_v1.0-1.xlsx', sheet_name='Historical Budget', header=15)

df_co2_world_land = df_co2_world_land[['Year', 'land-use change emissions']]
df_co2_world_land = df_co2_world_land.dropna()
df_co2_world_land['land-use change emissions'] = df_co2_world_land['land-use change emissions']*1000

df_co2_land_use_gb = df_co2_land_use_gb.melt(
    id_vars=['unit: Tg C/year'],
    var_name = 'country',
    value_name='value'
)

df_co2_land_use_gb = df_co2_land_use_gb.rename(columns={'unit: Tg C/year': 'year',
                                                        'value': 'Data'})

df_co2_land_use_gb.loc[df_co2_land_use_gb['country']=='Global', 'Data'] = (
    df_co2_land_use_gb.loc[df_co2_land_use_gb['country']=='Global', 'year']
    .map(df_co2_world_land.set_index('Year')['land-use change emissions']))

df_co2_land_use_gb['Data'] = df_co2_land_use_gb['Data']*3.664*1e6

excluded_countries_name_temperature_land = [
	"KP Annex B",
	"Non KP Annex B",
	"DISPUTED",
	"OTHER",
]

new_countries_name_land = {
    "Afghanistan": "Afghanistan",
    "Africa": "Africa (GCP)",
    "Albania": "Albania",
    "Algeria": "Algeria",
    "American Samoa": "American Samoa",
    "Andorra": "Andorra",
    "Angola": "Angola",
    "Anguilla": "Anguilla",
    "Antarctica": "Antarctica",
    "Antigua and Barbuda": "Antigua and Barbuda",
    "Argentina": "Argentina",
    "Armenia": "Armenia",
    "Aruba": "Aruba",
    "Asia": "Asia (GCP)",
    "Australia": "Australia",
    "Austria": "Austria",
    "Azerbaijan": "Azerbaijan",
    "Bahamas": "Bahamas",
    "Bahrain": "Bahrain",
    "Bangladesh": "Bangladesh",
    "Barbados": "Barbados",
    "Belarus": "Belarus",
    "Belgium": "Belgium",
    "Belize": "Belize",
    "Benin": "Benin",
    "Bermuda": "Bermuda",
    "Bhutan": "Bhutan",
    "Bolivia": "Bolivia",
    "Bolivia (Plurinational State of)": "Bolivia",
    "Bonaire, Saint Eustatius and Saba": "Bonaire Sint Eustatius and Saba",
    "Bonaire, Sint Eustatius and Saba": "Bonaire Sint Eustatius and Saba",
    "Bosnia and Herzegovina": "Bosnia and Herzegovina",
    "Botswana": "Botswana",
    "Brazil": "Brazil",
    "British Virgin Islands": "British Virgin Islands",
    "Brunei Darussalam": "Brunei",
    "Bulgaria": "Bulgaria",
    "Bunkers": "International transport",
    "Burkina Faso": "Burkina Faso",
    "Burundi": "Burundi",
    "Cabo Verde": "Cape Verde",
    "Cambodia": "Cambodia",
    "Cameroon": "Cameroon",
    "Canada": "Canada",
    "Cape Verde": "Cape Verde",
    "Central African Republic": "Central African Republic",
    "Central America": "Central America (GCP)",
    "Chad": "Chad",
    "Chile": "Chile",
    "China": "China",
    "Christmas Island": "Christmas Island",
    "Colombia": "Colombia",
    "Comoros": "Comoros",
    "Congo": "Congo",
    "Congo, Democratic Republic of the": "Democratic Republic of Congo",
    "Cook Islands": "Cook Islands",
    "Costa Rica": "Costa Rica",
    "Croatia": "Croatia",
    "Cuba": "Cuba",
    "Cura\u00e7ao": "Curacao",
    "Cyprus": "Cyprus",
    "Czech Republic": "Czechia",
    "Czechia": "Czechia",
    "C\u00f4te d'Ivoire": "Cote d'Ivoire",
    "Democratic Republic of the Congo": "Democratic Republic of Congo",
    "Denmark": "Denmark",
    "Djibouti": "Djibouti",
    "Dominica": "Dominica",
    "Dominican Republic": "Dominican Republic",
    "EU27": "European Union (27) (GCP)",
    "Ecuador": "Ecuador",
    "Egypt": "Egypt",
    "El Salvador": "El Salvador",
    "Equatorial Guinea": "Equatorial Guinea",
    "Eritrea": "Eritrea",
    "Estonia": "Estonia",
    "Eswatini": "Eswatini",
    "Ethiopia": "Ethiopia",
    "Europe": "Europe (GCP)",
    "EU27": "European Union (27)",
    "Faeroe Islands": "Faroe Islands",
    "Falkland Islands (Malvinas)": "Falkland Islands",
    "Faroe Islands": "Faroe Islands",
    "Fiji": "Fiji",
    "Finland": "Finland",
    "France": "France",
    "French Equatorial Africa": "French Equatorial Africa (GCP)",
    "French Guiana": "French Guiana",
    "French Polynesia": "French Polynesia",
    "French West Africa": "French West Africa (GCP)",
    "Gabon": "Gabon",
    "Gambia": "Gambia",
    "Georgia": "Georgia",
    "Germany": "Germany",
    "Ghana": "Ghana",
    "Global": "World",
    "Greece": "Greece",
    "Greenland": "Greenland",
    "Grenada": "Grenada",
    "Guadeloupe": "Guadeloupe",
    "Guatemala": "Guatemala",
    "Guernsey": "Guernsey",
    "Guinea": "Guinea",
    "Guinea-Bissau": "Guinea-Bissau",
    "Guyana": "Guyana",
    "Haiti": "Haiti",
    "Honduras": "Honduras",
    "Hong Kong": "Hong Kong",
    "Hungary": "Hungary",
    "Iceland": "Iceland",
    "India": "India",
    "Indonesia": "Indonesia",
    "International Aviation": "International aviation",
    "International Shipping": "International shipping",
    "Iran": "Iran",
    "Iran (Islamic Republic of)": "Iran",
    "Iraq": "Iraq",
    "Ireland": "Ireland",
    "Isle of Man": "Isle of Man",
    "Israel": "Israel",
    "Italy": "Italy",
    "Jamaica": "Jamaica",
    "Japan": "Japan",
    "Jersey": "Jersey",
    "Jordan": "Jordan",
    "Kazakhstan": "Kazakhstan",
    "Kenya": "Kenya",
    "Kiribati": "Kiribati",
    "Korea (Democratic People's Republic of)": "North Korea",
    "Korea, Republic of": "South Korea",
    "Kosovo": "Kosovo",
    "Kuwait": "Kuwait",
    "Kuwaiti Oil Fires": "Kuwaiti Oil Fires (GCP)",
    "Kyrgyzstan": "Kyrgyzstan",
    "Lao People's Democratic Republic": "Laos",
    "Laos": "Laos",
    "Latvia": "Latvia",
    "Lebanon": "Lebanon",
    "Leeward Islands": "Leeward Islands (GCP)",
    "Lesotho": "Lesotho",
    "Liberia": "Liberia",
    "Libya": "Libya",
    "Liechtenstein": "Liechtenstein",
    "Lithuania": "Lithuania",
    "Luxembourg": "Luxembourg",
    "Macao": "Macao",
    "Madagascar": "Madagascar",
    "Malawi": "Malawi",
    "Malaysia": "Malaysia",
    "Maldives": "Maldives",
    "Mali": "Mali",
    "Malta": "Malta",
    "Marshall Islands": "Marshall Islands",
    "Martinique": "Martinique",
    "Mauritania": "Mauritania",
    "Mauritius": "Mauritius",
    "Mayotte": "Mayotte",
    "Mexico": "Mexico",
    "Micronesia (Federated States of)": "Micronesia (country)",
    "Middle East": "Middle East (GCP)",
    "Moldova": "Moldova",
    "Moldova, Republic of": "Moldova",
    "Monaco": "Monaco",
    "Mongolia": "Mongolia",
    "Montenegro": "Montenegro",
    "Montserrat": "Montserrat",
    "Morocco": "Morocco",
    "Mozambique": "Mozambique",
    "Myanmar": "Myanmar",
    "Namibia": "Namibia",
    "Nauru": "Nauru",
    "Nepal": "Nepal",
    "Netherlands": "Netherlands",
    "Netherlands Antilles": "Netherlands Antilles",
    "New Caledonia": "New Caledonia",
    "New Zealand": "New Zealand",
    "Nicaragua": "Nicaragua",
    "Niger": "Niger",
    "Nigeria": "Nigeria",
    "Niue": "Niue",
    "Non-OECD": "Non-OECD (GCP)",
    "North America": "North America (GCP)",
    "North Korea": "North Korea",
    "North Macedonia": "North Macedonia",
    "Norway": "Norway",
    "OECD": "OECD (GCP)",
    "Occupied Palestinian Territory": "Palestine",
    "Oceania": "Oceania (GCP)",
    "Oman": "Oman",
    "Pacific Islands (Palau)": "Palau",
    "Pakistan": "Pakistan",
    "Palau": "Palau",
    "Palestine, State of": "Palestine",
    "Panama": "Panama",
    "Panama Canal Zone": "Panama Canal Zone (GCP)",
    "Papua New Guinea": "Papua New Guinea",
    "Paraguay": "Paraguay",
    "Peru": "Peru",
    "Philippines": "Philippines",
    "Poland": "Poland",
    "Portugal": "Portugal",
    "Puerto Rico": "Puerto Rico",
    "Qatar": "Qatar",
    "Romania": "Romania",
    "Russia": "Russia",
    "Russian Federation": "Russia",
    "Rwanda": "Rwanda",
    "Ryukyu Islands": "Ryukyu Islands (GCP)",
    "R\u00e9union": "Reunion",
    "Saint Helena": "Saint Helena",
    "Saint Kitts and Nevis": "Saint Kitts and Nevis",
    "Saint Lucia": "Saint Lucia",
    "Saint Martin (French part)": "Saint Martin (French part)",
    "Saint Pierre and Miquelon": "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Samoa": "Samoa",
    "San Marino": "San Marino",
    "Sao Tome and Principe": "Sao Tome and Principe",
    "Saudi Arabia": "Saudi Arabia",
    "Senegal": "Senegal",
    "Serbia": "Serbia",
    "Seychelles": "Seychelles",
    "Sierra Leone": "Sierra Leone",
    "Singapore": "Singapore",
    "Sint Maarten (Dutch part)": "Sint Maarten (Dutch part)",
    "Slovakia": "Slovakia",
    "Slovenia": "Slovenia",
    "Solomon Islands": "Solomon Islands",
    "Somalia": "Somalia",
    "South Africa": "South Africa",
    "South America": "South America (GCP)",
    "South Korea": "South Korea",
    "South Sudan": "South Sudan",
    "Spain": "Spain",
    "Sri Lanka": "Sri Lanka",
    "State of Palestine": "Palestine",
    "St. Kitts-Nevis-Anguilla": "St. Kitts-Nevis-Anguilla (GCP)",
    "Sudan": "Sudan",
    "Suriname": "Suriname",
    "Svalbard and Jan Mayen": "Svalbard and Jan Mayen",
    "Swaziland": "Eswatini",
    "Sweden": "Sweden",
    "Switzerland": "Switzerland",
    "Syria": "Syria",
    "Syrian Arab Republic": "Syria",
    "Taiwan": "Taiwan",
    "Taiwan, Province of China": "Taiwan",
    "Tajikistan": "Tajikistan",
    "Tanzania": "Tanzania",
    "Tanzania, United Republic of": "Tanzania",
    "Thailand": "Thailand",
    "Timor-Leste": "East Timor",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinidad and Tobago": "Trinidad and Tobago",
    "Tunisia": "Tunisia",
    "Türkiye": "Turkey",
    "Turkmenistan": "Turkmenistan",
    "Turks and Caicos Islands": "Turks and Caicos Islands",
    "Tuvalu": "Tuvalu",
    "USA": "United States",
    "Uganda": "Uganda",
    "Ukraine": "Ukraine",
    "United Arab Emirates": "United Arab Emirates",
    "United Kingdom": "United Kingdom",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "United States of America": "United States",
    "Uruguay": "Uruguay",
    "Uzbekistan": "Uzbekistan",
    "Vatican City": "Vatican",
    "Vanuatu": "Vanuatu",
    "Venezuela": "Venezuela",
    "Venezuela (Bolivarian Republic of)": "Venezuela",
    "Viet Nam": "Vietnam",
    "Virgin Islands (U.S.)": "United States Virgin Islands",
    "Wallis and Futuna Islands": "Wallis and Futuna",
    "Western Sahara": "Western Sahara",
    "World": "World",
    "Yemen": "Yemen",
    "Zambia": "Zambia",
    "Zimbabwe": "Zimbabwe",
    "\u00c5land Islands": "Aland Islands"
}

df_co2_land_use_gb = df_co2_land_use_gb[~df_co2_land_use_gb['country'].isin(excluded_countries_name_temperature_land)]

df_co2_land_use_gb['country'] = df_co2_land_use_gb['country'].replace(new_countries_name_land)

url_fossil_gb = 'https://zenodo.org/records/13981696/files/GCB2024v17_MtCO2_flat.csv'
get_data_web(url_fossil_gb, 'co2_fossil_emissions.csv')

df_co2_fossil = pd.read_csv('co2_fossil_emissions.csv')

df_co2_fossil['Total'] = df_co2_fossil['Total']*1e6

df_co2_fossil = df_co2_fossil.rename(columns={'ISO 3166-1 alpha-3': 'ISO3',
                                              'Country': 'country',
                                              'Year': 'year'})

no_emission_replace_nan = df_co2_fossil.drop(columns=['country', 'year', 'Total', 'ISO3', 'UN M49']).isnull().all(axis=1)
df_co2_fossil.loc[no_emission_replace_nan, 'Total'] = np.nan

df_co2_fossil = df_co2_fossil.drop(columns=['UN M49', 'Coal', 'Oil', 'Gas', 'Cement', 'Flaring', 'Other', 'Per Capita'])

df_co2_fossil = df_co2_fossil[~df_co2_fossil['country'].isin(excluded_countries_name_temperature_land)]

df_co2_fossil['country'] = df_co2_fossil['country'].replace(new_countries_name_land)

df_co2_total = df_co2_fossil.merge(
    df_co2_land_use_gb[['country', 'year','Data']],
    on=['country', 'year'],
    how='left'
)

df_co2_total = df_co2_total.rename(columns={'Total': 'fossil', 'Data': 'land_use'})

df_co2_total['Total'] = df_co2_total['fossil'] + df_co2_total['land_use']

df_merge_inc_total = df_co2_total.merge(
    df_income_groups_ven_eth[['country', 'classification']],
    on='country',
    how='left'
)

df_group_co2_total = df_merge_inc_total.groupby(['classification', 'year'])[['fossil','land_use', 'Total']].sum().reset_index()

df_group_co2_total = df_group_co2_total.rename(columns={'classification': 'country'})

df_comb_co2_total = pd.concat([df_merge_inc_total, df_group_co2_total], axis=0, ignore_index=True)

df_merge_regions_co2_total = df_regions_exploded.merge(df_co2_total, left_on='members',
                                             right_on='ISO3', how='left')

df_region_co2_total = (
    df_merge_regions_co2_total.groupby(['short_name', 'year'], as_index=False)[['fossil','land_use', 'Total']].sum()
)

df_region_co2_total = df_region_co2_total.rename(columns={'short_name': 'country'})

df_comb_reg_inc_total= pd.concat([df_comb_co2_total, df_region_co2_total], axis=0, ignore_index=True)

df_comb_reg_inc_all_emissions_rename = df_comb_reg_inc_all_emissions_rename.drop(columns=['co2_fossil_jones', 'co2_lucf_jones',
                                                   'co2_total_jones'])

df_comb_reg_inc_total_rename = df_comb_reg_inc_total.rename(columns={'Total': 'co2_total_gb',
                                                                     'fossil': 'co2_fossil_gb',
                                                                     'land_use': 'co2_land_use_gb'})

df_merge_co2_all = df_merge_co2_inc_reg.merge(
    df_comb_reg_inc_total_rename[['country', 'year', 'co2_fossil_gb', 'co2_land_use_gb', 'co2_total_gb']],
    on=['country', 'year'],
    how='left'
)

df_merge_co2_inc_reg_all = df_merge_co2_all.merge(
    df_comb_reg_inc_all_emissions_rename[['country', 'year', 'ch4_total_jones',
                                          'n2o_total_jones']],
    on=['country', 'year'],
    how='left'
)

df_merge_co2_inc_reg_new = df_merge_co2_inc_reg_all

df_merge_co2_inc_reg_new['co2_total_gb_relative_change'] = (
    df_merge_co2_inc_reg_new.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg_new,g, 'co2_total_gb'))
)

df_merge_co2_inc_reg_new['co2_fossil_gb_relative_change'] = (
    df_merge_co2_inc_reg_new.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg_new,g, 'co2_fossil_gb'))
)

df_merge_co2_inc_reg_new['co2_land_use_gb_relative_change'] = (
    df_merge_co2_inc_reg_new.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg_new,g, 'co2_land_use_gb'))
)

df_merge_co2_inc_reg_new['ch4_total_jones_relative_change'] = (
    df_merge_co2_inc_reg_new.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg_new,g, 'ch4_total_jones'))
)

df_merge_co2_inc_reg_new['n2o_total_jones_relative_change'] = (
    df_merge_co2_inc_reg_new.groupby('country', group_keys=False)
    .apply(lambda g: relative_change(df_merge_co2_inc_reg_new,g, 'n2o_total_jones'))
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Distribution of Global Emissions and Warming Impact'),

    html.P('Select font of warming impact:'),

    dcc.Dropdown(
        id='source-dropdown',
        options=[
            {'label': 'All fossil emissions', 'value': 'warming_impact_fossil'},
            {'label': 'Land use change', 'value': 'warming_impact_land'},
            {'label': 'All emissions', 'value': 'warming_impact_total_Jones'}
        ],
        value='warming_impact_total_Jones',
        style={'width': '50%'},
    ),

    html.P('Select polluent gas:'),
    dcc.Dropdown(
        id='gas-dropdown',
        options=[
            {'label': 'CO2 Fossil', 'value': 'co2_fossil_gb'},
            {'label': 'CO2 Land Use', 'value': 'co2_land_use_gb'},
            {'label': 'CO2 Total', 'value': 'co2_total_gb'},
            {'label': 'All GHG', 'value': 'total_ghg'},
            {'label': 'Methane', 'value': 'ch4_total_jones'},
            {'label': 'Nitrous Oxide', 'value': 'n2o_total_jones'}
        ],
        value='co2_fossil_gb',
        style={'width': '50%'},
    ),



    html.H2('1. Global Evolution of emissions and surface temperature rise'),

    html.P('Select a country or region:'),
    dcc.Dropdown(
            id='country-dropdown',
            options=[
                {'label': c, 'value':c} for c in df_merge_co2_inc_reg_new['country'].unique()
            ],
            value=income_groups,
            style={'width': '70%'},
            multi=True
        ),

    html.P('Select value display mode:'),

    dcc.RadioItems(
        id='line-value-mode',
        options=[
            {'label':'Relative Change', 'value': '_relative_change'},
            {'label': 'Per Year', 'value':''},

        ],
        value='_relative_change',
        inline=True
    ),

    html.P('Select property display mode (emissions or warming impact):'),

    dcc.RadioItems(
        id='line-gas-source',
        options=[
            {'label':'Emissions', 'value': 'gas-dropdown'},
            {'label': 'Warming Impact', 'value':'source-dropdown'},

        ],
        value='gas-dropdown',
        inline=True
    ),

    dcc.Markdown(id = 'line-temp-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),

    dcc.Markdown(id = 'line-temp-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),

    dcc.Graph(id = 'line-temp'),

    html.H2('2. Historical Evolution of Largest Emitters'),
    html.P('Select a country or region:'),
    dcc.Dropdown(
            id='country-bar-dropdown',
            options=[
                {'label': c, 'value':c} for c in df_merge_co2_inc_reg_new['country'].unique()
            ],
            value=[],
            style={'width': '70%'},
            multi=True
        ),

    dcc.Markdown(id = 'bar-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),

    dcc.Markdown(id = 'bar-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),

    dcc.Graph(id = 'bar-emissions'),

    html.H2('3. Global surface temperature rise'),
    dcc.Markdown(id = 'map-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),
    dcc.Markdown(id = 'map-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),

    dcc.Graph(id = 'map-warming'),
    dcc.Slider(
            id='year-map-slider',
            min = 1851,
            max = 2023,
            value = 1851,
            marks={int(y): str(y) for y in range(1851,
                                                2023+1,
                                                20)},
            step=1
        ),

    html.H2('4. Distribution of Emissions by Income Level'),
    dcc.Markdown(id = 'box-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),

    dcc.Markdown(id = 'box-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),

    dcc.Graph(id = 'box-warming'),

    html.H2('5. Relationship between Emissions and GDP'),
    dcc.RadioItems(
        id='scatter-mode',
        options=[
            {'label':'Last year available (static)', 'value': 'static'},
            {'label': 'All years (slider)', 'value':'animated'},

        ],
        value='static',
        inline=True
    ),
    dcc.Markdown(id = 'scatter-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),

    dcc.Markdown(id = 'scatter-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),

    dcc.Slider(
            id='year-scatter-slider',
            step=1,
            updatemode='drag'
        ),
    dcc.Graph(id = 'scatter-gdp-emissions'),

    html.H2('6. Correlations between factors'),
    dcc.Markdown(id = 'corr-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),
    dcc.Markdown(id = 'corr-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),
    dcc.Slider(
            id='year-corr-slider',
            min = 1851,
            max = 2022,
            value = 1851,
            marks={int(y): str(y) for y in range(1851,
                                                2022+1,
                                                10)},
            step=1,
            updatemode='drag'
        ),
    dcc.Graph(id = 'heatmap-warming'),
    html.P('Select columns for correlation:'),
    dcc.Dropdown(
        id='column-dropdown',
        options=[
            {'label': c, 'value':c} for c in df_merge_co2_inc_reg_new[['co2_total_gb', 'oil_co2', 'cement_co2', 'population', 'gdp',
                   'ch4_total_jones', 'warming_impact_total_Jones', 'n2o_total_jones',
                   'coal_co2', 'gas_co2', 'flaring_co2']].columns
        ],
        value=['co2_total_gb', 'gdp',
                'ch4_total_jones', 'warming_impact_total_Jones', 'n2o_total_jones',
                  ],
        style={'width': '70%'},
        multi=True
    ),

])

#Barra - filtro país novo
@app.callback(
    dash.Output('country-bar-dropdown', 'value'),
    [dash.Input('gas-dropdown', 'value'),]
)

def update_bar_dropdown(selected_gas):
  latest_year = df_merge_co2_inc_reg_new['year'].max()

  excluded_countries = df_merge_co2_inc_reg_new[df_merge_co2_inc_reg_new['region'].isna()]['country'].unique()

  dff = df_merge_co2_inc_reg_new[df_merge_co2_inc_reg_new['year']==latest_year][['country', selected_gas]]
  dff = dff[~dff['country'].isin(excluded_countries)]

  top_countries = dff.sort_values(by=selected_gas, ascending=False).head(5)['country'].tolist()
  return top_countries

#Scatter - slider ano
@app.callback(
    [dash.Output('year-scatter-slider', 'min'),
     dash.Output('year-scatter-slider', 'max'),
     dash.Output('year-scatter-slider', 'value'),
     dash.Output('year-scatter-slider', 'marks')],
    [dash.Input('gas-dropdown', 'value'),]
)

def update_scatter_slider(selected_gas):

  dff = df_merge_co2_inc_reg_new[['year', 'country', 'gdp', selected_gas]][df_merge_co2_inc_reg_new[selected_gas]!=0]
  dff_min = dff.dropna()

  minimal_year = dff_min['year'].min()

  min_year = minimal_year
  max_year = 2022
  value = minimal_year
  marks={int(y): str(y) for y in range(minimal_year,
                                      2022+1,
                                      10)}

  return min_year, max_year, value, marks

#Linha - Temperatura
@app.callback(
    [dash.Output('line-temp', 'figure'),
     dash.Output('line-temp-title', 'children'),
     dash.Output('line-temp-text', 'children')],
    [dash.Input('source-dropdown', 'value'),
     dash.Input('gas-dropdown', 'value'),
     dash.Input('country-dropdown', 'value'),
     dash.Input('line-value-mode', 'value'),
     dash.Input('line-gas-source', 'value'),
     ]
)

def update_line_temp(selected_source, selected_gas, selected_country, selected_value_mode, selected_filter):

  if selected_value_mode == '':
    value_display = r'$\text{Annual }'

  else:
    value_display = r'$\text{Relative Change (%) in annual }'

  dict_title_gas = {
      'total_ghg': r'\text{Greehouse gas } (CO_2eq) ',
      'ch4_total_jones': r'\text{Methane } (CH_4) ',
      'n2o_total_jones': r'\text{Nitrous Oxide } (N_2O) ',
      'co2_fossil_gb': r'\text{Fossil fuels and Industry Carbon Dioxide } (CO_2) ',
      'co2_land_use_gb': r'\text{Land Use Change Carbon Dioxide } (CO_2) ',
      'co2_total_gb': r'\text{Total Carbon Dioxide } (CO_2) ',
  }

  dict_title_source = {
      'warming_impact_fossil': r'\text{Contribution to global mean surface temperature rise from fossil fuels sources, 1851-2023}$',
      'warming_impact_land': r'\text{Contribution to global mean surface temperature rise from agriculture and land use, 1851-2023}$',
      'warming_impact_total_Jones': r'\text{Contribution to global mean surface temperature rise, 1851-2023}$'
  }

  if selected_filter == 'source-dropdown':
    column = selected_source+selected_value_mode
    title = value_display+ ' ' + dict_title_source[selected_source]
    text = 'The cumulative effect shows that the richest countries are still the most responsible for global warming.'
  else:
    column = selected_gas+selected_value_mode
    title = value_display+ ' ' + dict_title_gas[selected_gas]
    text = 'Although richer countries have higher absolute emissions, the speed of relative change is more intense in lower-income countries.'

  minimal_year = []
  for i in selected_country:
    minimal_year.append(min_year(df_merge_co2_inc_reg_new, 'year', 'country', column, i))

  if selected_value_mode == '':

    dff = df_merge_co2_inc_reg_new[(df_merge_co2_inc_reg_new['country'].isin(selected_country))&
                             (df_merge_co2_inc_reg_new['year']>=np.min(minimal_year))]

    if selected_filter == 'source-dropdown':
      title = title

    else:
      title_place = r' \text{ emissions in tonnes,'
      title_place_2 = r'}$'

      title_year = rf'{np.min(minimal_year)}-2023'

      title = title+' ' + title_place + ' ' + title_year + '' + title_place_2

  else:
    dff = df_merge_co2_inc_reg_new[(df_merge_co2_inc_reg_new['country'].isin(selected_country))&
                             (df_merge_co2_inc_reg_new['year']>=np.min(minimal_year)-1)]

    if selected_filter == 'source-dropdown':
      title = title

    else:
      title_place = r' \text{ emissions in tonnes,'
      title_place_2 = r'}$'

      title_year = rf'{np.min(minimal_year)-1}-2023'

      title = title+' ' + title_place + ' ' + title_year + '' + title_place_2

  fig = px.line(
      dff, x='year', y=column, color = 'country',
      title=''
  )

  fig.update_xaxes(title_text='')
  fig.update_yaxes(title_text='')

  return fig, title, text

#Barra - Emissões
@app.callback(
  [dash.Output('bar-emissions', 'figure'),
   dash.Output('bar-title', 'children'),
   dash.Output('bar-text', 'children')],
  [dash.Input('gas-dropdown', 'value'),
    dash.Input('country-bar-dropdown', 'value')]
)

def update_bar_emissions(selected_gas, selected_country):

  value_display = r'$\text{Annual }'

  dict_title_gas = {
      'total_ghg': r'\text{Greehouse gas } (CO_2eq) ',
      'ch4_total_jones': r'\text{Methane } (CH_4) ',
      'n2o_total_jones': r'\text{Nitrous Oxide } (N_2O) ',
      'co2_fossil_gb': r'\text{Fossil fuels and Industry Carbon Dioxide } (CO_2) ',
      'co2_land_use_gb': r'\text{Land Use Change Carbon Dioxide } (CO_2) ',
      'co2_total_gb': r'\text{Total Carbon Dioxide } (CO_2) ',
  }

  title_place = r' \text{ emissions in tonnes,'
  title_place_2 = r'}$'

  minimal_year = []
  for i in selected_country:
    minimal_year.append(min_year(df_merge_co2_inc_reg_new, 'year', 'country', selected_gas, i))

  title_year = rf'{np.min(minimal_year)}-2023'

  title = value_display+ ' ' + dict_title_gas[selected_gas] +' ' + title_place + ' ' + title_year + '' + title_place_2

  text = 'The largest emitters have changed over time, but most industrialized economies remain among the biggest contributors.'

  years = df_merge_co2_inc_reg_new['year'][df_merge_co2_inc_reg_new['year']>=np.min(minimal_year)].unique()

  df_full = pd.MultiIndex.from_product([selected_country, years], names = ['country', 'year']).to_frame(index=False)


  df_merged = df_full.merge(
      df_merge_co2_inc_reg_new[['country', 'year', selected_gas]],
      on=['country', 'year'],
      how='left'
  ).fillna(0)

  fig = px.bar(
      df_merged.sort_values(by='year'), x=selected_gas, y = 'country', color = 'country',
      title='', text= selected_gas,
      animation_frame='year'
  )

  fig.update_xaxes(title_text='')
  fig.update_yaxes(title_text='')

  return fig, title, text

#Mapa - warming
@app.callback(
  [dash.Output('map-warming', 'figure'),
   dash.Output('map-title', 'children'),
   dash.Output('map-text', 'children')],
  [dash.Input('source-dropdown', 'value'),
    dash.Input('country-dropdown', 'value'),
    dash.Input('year-map-slider', 'value')]
)

def update_map_warming(selected_source, selected_country, selected_year):

  value_display = r'$\text{Annual }'

  dict_title_source = {
      'warming_impact_fossil': r'\text{Contribution to global mean surface temperature rise from fossil fuels sources, 1851-2023}$',
      'warming_impact_land': r'\text{Contribution to global mean surface temperature rise from agriculture and land use, 1851-2023}$',
      'warming_impact_total_Jones': r'\text{Contribution to global mean surface temperature rise, 1851-2023}$'
  }

  title = value_display+ ' ' + dict_title_source[selected_source]

  text = "The warming tendecy isn't just a global average - it is widespread, but with varying intensities."

  dff = df_merge_co2_inc_reg_new[['country', 'year', selected_source, 'region']][df_merge_co2_inc_reg_new['year']==selected_year]
  dff = dff.dropna()
  fig = px.choropleth(
      dff, locations='country', locationmode='country names',
      color=selected_source, hover_name='country',
      title='',
      color_continuous_scale='reds',
      range_color=[0,0.1]
  )
  return fig, title, text

#Boxplot - warming-income
@app.callback(
  [dash.Output('box-warming', 'figure'),
   dash.Output('box-title', 'children'),
   dash.Output('box-text', 'children')],
  [dash.Input('source-dropdown', 'value'),
    ]
)

def update_box_warming(selected_source):

  value_display = r'$\text{Income Groups variation of }'

  dict_title_source = {
      'warming_impact_fossil': r'\text{Contribution to global mean surface temperature rise from fossil fuels sources, 1851-2023}$',
      'warming_impact_land': r'\text{Contribution to global mean surface temperature rise from agriculture and land use, 1851-2023}$',
      'warming_impact_total_Jones': r'\text{Contribution to global mean surface temperature rise, 1851-2023}$'
  }

  title = value_display+ ' ' + dict_title_source[selected_source]
  text = "Low-income countries aren't always more polluting. Income levels help understand patterns, but they don't explain everything."

  dff = df_merge_co2_inc_reg_new[['country', 'year', selected_source, 'income_group']]
  mask = dff.groupby('country')[selected_source].transform(lambda x: (x!=0).any())
  dff = dff[mask]
  dff = dff.dropna()
  fig = px.box(
      dff[dff['year']>=1851], x = 'income_group', y = selected_source,
      hover_name='country', log_y='True',
      title='',
      animation_frame='year'
  )

  fig.update_xaxes(title_text='')
  fig.update_yaxes(title_text='')

  return fig, title, text

#Disperção - Emissões - GDP
@app.callback(
  [dash.Output('scatter-gdp-emissions', 'figure'),
   dash.Output('scatter-title', 'children'),
   dash.Output('scatter-text', 'children')],
  [dash.Input('gas-dropdown', 'value'),
   dash.Input('scatter-mode', 'value'),
   dash.Input('year-scatter-slider', 'value'),
    ]
)

def update_scatter_emissions(selected_gas, mode, selected_year):
  value_display = r'$\text{Relationship between  }'

  dict_title_gas = {
      'total_ghg': r'\text{Greehouse gas } (CO_2eq) ',
      'ch4_total_jones': r'\text{Methane } (CH_4) ',
      'n2o_total_jones': r'\text{Nitrous Oxide } (N_2O) ',
      'co2_fossil_gb': r'\text{Fossil fuels and Industry Carbon Dioxide } (CO_2) ',
      'co2_land_use_gb': r'\text{Land Use Change Carbon Dioxide } (CO_2) ',
      'co2_total_gb': r'\text{Total Carbon Dioxide } (CO_2) ',
  }

  text = 'Economic growth has historically been tied to rising polluents emissions. Higher-income countries have continuously emitted more polluents historically.'

  if mode=='static':

    title_place = r' \text{ emissions in tonnes,'
    title_place_2 = r'}$'

    dff = df_merge_co2_inc_reg_new[['year', 'country', 'income_group', 'region', selected_gas, 'gdp']]
    latest_year = dff.dropna(subset=['gdp'])['year'].max()
    dff = dff[dff['year']==latest_year]

    title = value_display+ ' ' + dict_title_gas[selected_gas] +' ' + title_place + '' + rf' and GDP ({latest_year})' + title_place_2

    fig = px.scatter(
        dff, x='gdp', y = selected_gas, color = 'income_group',
        title='',
        log_x = True, log_y = True,
        hover_name='country'
    )

  else:

    title_place = r' \text{ emissions in tonnes,'
    title_place_2 = r'}$'

    title = value_display+ ' ' + dict_title_gas[selected_gas] +' ' + title_place + '' + r' and GDP (slider)' + title_place_2

    dff = df_merge_co2_inc_reg_new[
        df_merge_co2_inc_reg_new['year'] == selected_year
        ][['year', 'country', 'income_group', 'region', selected_gas, 'gdp']]
    fig = px.scatter(
        dff, x='gdp', y = selected_gas, color = 'income_group',
        title='',
        log_x = True, log_y = True,
        hover_name='country'
    )

  fig.update_xaxes(title_text='')
  fig.update_yaxes(title_text='')

  return fig, title, text

#Heatmap - warming
@app.callback(
  [dash.Output('heatmap-warming', 'figure'),
   dash.Output('corr-title', 'children'),
   dash.Output('corr-text', 'children')],
  [dash.Input('column-dropdown', 'value'),
   dash.Input('year-corr-slider', 'value'),
       ]
)

def update_heatmap_emissions(selected_column, selected_year):

  cols = ', '.join(selected_column)

  title = r'$\text{' + ' ' + r'Correlation Matrix of ' + ' ' + rf'{cols}' + ' '+ r'by year ' + ' ' + rf'({selected_year})' +r'}$'

  text_1 = 'Emissions, warmig impact and GDP are interconnected, reinforcing that development, demographics and climate cannot be discussed in isolation.'

  text_2='Higher-income countries have historically polluted more and are responsible for much of the global warming. Lower-income countries have seen faster emissions growth, but still have a lesser impact.'

  text_3 = 'Higher-income countries have an historical obligation and economic capacity to fund the energy transition.'

  text = f'''{text_1 } {text_2}

   **{text_3}**'''

  dff = df_merge_co2_inc_reg_new[df_merge_co2_inc_reg_new['year']==selected_year]

  corrs=[]

  fig = px.imshow(
      dff[selected_column].corr(),
      x=selected_column,
      y=selected_column,
      aspect='auto',
      zmin=-1, zmax=1,
      title = '',
      text_auto=True
  )

  return fig, title, text

if __name__ == '__main__':
  app.run()