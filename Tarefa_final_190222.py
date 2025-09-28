import requests
import pandas as pd
import numpy as np

#Function to download and save data from a given URL
def get_data_web(repo_file, file_name):

  url = repo_file
  response = requests.get(url)
  #Save response content to a local file
  with open(file_name, 'w', encoding='utf-8') as f:
    f.write(response.text)

#-----------------------------
#Download raw datasets
#-----------------------------

url_1 = 'https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-codebook.csv'
url_2 = 'https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-data.csv'
file_name_1 = 'owid-co2-codebook.csv'
file_name_2 = 'owid-co2-data.csv'
url_download = 'https://zenodo.org/records/14054503/files/GMST_response_1851-2023.csv'
file_name_3 = 'GMST_response_1851-2023.csv'

#Download files locally
get_data_web(url_1, file_name_1)
get_data_web(url_2, file_name_2)
get_data_web(url_download, file_name_3)

#-----------------------------
#Load OWID datasets
#-----------------------------

df_codebook = pd.read_csv('owid-co2-codebook.csv')
df_co2 = pd.read_csv('owid-co2-data.csv')

# Data inspection
print ("Tabela 1 - Verificação de dados")
print(df_co2.info())
print("\n")

# Checking for missing values
print ("Tabela 2 - Verificação de dados vazios")
print(df_co2.isna().any())
print("\n")

# Cheking missing values count
print ("Tabela 3 - Verificação de quantidade de dados vazios")
print(df_co2.isna().sum())
print("\n")

#-----------------------------
#Create per capita indicators
#-----------------------------

df_co2['ghg_person'] = (df_co2['total_ghg']*(10**6))/df_co2['population']

df_co2['ghg_person']=df_co2['ghg_person']

df_co2['co2_person'] = (df_co2['co2']*(10**6))/df_co2['population']

df_co2['co2_person'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2011)]

df_co2['methane_person'] = (df_co2['methane']*(10**6))/df_co2['population']

df_co2['methane_person'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2011)]

df_co2['nitrous_oxide_person'] = (df_co2['nitrous_oxide']*(10**6))/df_co2['population']

df_co2['nitrous_oxide_person'][(df_co2['country'] == 'Afghanistan') & (df_co2['year'] == 2011)]

#Warming impact = CO2 + CH4 + N2O temperature contribution

df_co2['warming_impact'] = (df_co2['temperature_change_from_co2'] +
                            (df_co2['temperature_change_from_ch4'] +
                            df_co2['temperature_change_from_n2o']))

#-----------------------------
#Load GMST response Dataset
#containig temperature data
#From Jones et. al
#-----------------------------

df_temp_data = pd.read_csv('GMST_response_1851-2023.csv')

# Data inspection
print ("Tabela 1 - Verificação de dados")
print(df_temp_data.info())
print("\n")

# Checking for missing values
print ("Tabela 2 - Verificação de dados vazios")
print(df_temp_data.isna().any())
print("\n")

# Cheking missing values count
print ("Tabela 3 - Verificação de quantidade de dados vazios")
print(df_temp_data.isna().sum())
print("\n")

#Standardize country column name
df_temp_data = df_temp_data.rename(columns={'CNTR_NAME': 'country'})

#Dictionary to harmonize country names between datasets
#From owid co2 repository
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

#Excluded aggregated regions or groups that are not needed
#From owid co2 repository
excluded_countries_name_temperature = [
    "ANNEXI",
    "ANNEXII",
    "BASIC",
    "EIT",
    "LMDC",
    "NONANNEX",
    "Pacific Islands (Palau)"
]

#Filter and harmonize names
df_temp_data = df_temp_data[~df_temp_data['country'].isin(excluded_countries_name_temperature)]

df_temp_data['country'] = df_temp_data['country'].replace(new_countries_name_temperature)

#----------------------------------
#Load income groups classifications
#----------------------------------

url_income_groups = 'https://ourworldindata.org/grapher/world-bank-income-groups.csv?v=1&csvType=full&useColumnShortNames=true'
get_data_web(url_income_groups, 'world-bank-income-groups.csv')

df_income_groups = pd.read_csv('world-bank-income-groups.csv')

df_income_groups = df_income_groups[df_income_groups['Year'] == 2024] #Use most recent classification

df_income_groups = df_income_groups.rename(columns={'Entity': 'country'})

#Add countries without classification by World Bank, for calcularions (manual fix)
df_income_groups_ven_eth = pd.concat([
    df_income_groups,
    pd.DataFrame({'country': ['Venezuela', 'Ethiopia'],
                 'Code': ['VEN', 'ETH'],
                 'Year': [2024, 2024],
                 'classification': ['Upper-middle-income countries', 'Low-income countries']})
    ])

#Merge temperature data with income groups
df_merge_inc = df_temp_data.merge(
    df_income_groups_ven_eth[['country', 'classification']],
    on='country',
    how='left'
)

#Agreggate by classsification (income group), gas type, component of gas, year and unit (just to mantain)
df_group = df_merge_inc.groupby(['classification', 'Gas', 'Component','Year', 'Unit'])['Data'].sum().reset_index()

#Rename classification to country (so they can be treated as countries)
df_group = df_group.rename(columns={'classification': 'country'})

#Combine individual countries and aggregated groups
df_comb_temp = pd.concat([df_temp_data, df_group], axis=0, ignore_index=True)

#------------------------------
#Load OWID regional definitions
#------------------------------

import yaml

url_yaml = 'https://raw.githubusercontent.com/owid/etl/refs/heads/master/etl/steps/data/garden/regions/2023-01-01/regions.yml'
get_data_web(url_yaml, 'regions.yml')

with open('regions.yml') as file:
  df_regions = pd.DataFrame.from_dict(yaml.safe_load(file))


url_regions_code = 'https://raw.githubusercontent.com/owid/etl/refs/heads/master/etl/steps/data/garden/regions/2023-01-01/regions.codes.csv'
get_data_web(url_regions_code, 'regions_code.csv')

df_codes = pd.read_csv('regions_code.csv', keep_default_na=False, na_values=[''])

#Clean missing metadata
df_regions['short_name'] = df_regions['short_name'].fillna(df_regions['name'])
df_regions['region_type'] = df_regions['region_type'].fillna('country')

#Regions to be included
regions_filter = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America',
                  'Asia (excl. China and India)', 'Europe (excl. EU-27)', 'Europe (excl. EU-28)',
                  'North America (excl. USA)', 'European Union (28)']

#Build additional region UE-28
european_union_27 = df_regions.loc[df_regions['short_name'] == 'European Union (27)', 'members'].values[0]
european_union_28 = european_union_27 + ['GBR']
df_regions = pd.concat([
    df_regions,
    pd.DataFrame([{'short_name': 'European Union (28)', 'members': european_union_28}])
], ignore_index=True)

#Build special agreggate reions (excl. China, excl. USA, etc.)
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

#Combine original regions dataset with new regions dataset
df_region_final = pd.concat([df_regions, df_new_regions], ignore_index=True)

df_regions_short = df_region_final[['short_name','members']][df_region_final['short_name'].isin(regions_filter)]

#Explode member codes and merge with temperature dataset
df_regions_exploded = df_regions_short.explode('members')
df_merge_regions = df_regions_exploded.merge(df_temp_data, left_on='members',
                                             right_on='ISO3', how='left')

#Aggreagate by region
df_region_temp = (
    df_merge_regions.groupby(['short_name', 'Year', 'Gas','Component', 'Unit'], as_index=False)['Data'].sum()
)

df_region_temp = df_region_temp.rename(columns={'short_name': 'country'})

#Combine regions with country and income groups
df_comb_reg_inc = pd.concat([df_comb_temp, df_region_temp], axis=0, ignore_index=True)

#Create composite column (component + gas)
df_comb_reg_inc['category'] = df_comb_reg_inc['Component'] + '_' + df_comb_reg_inc['Gas']

#Pivot to wide format (columns = categories, rows = country/year)
df_comb_reg_inc_pivot = df_comb_reg_inc.pivot_table(
    index=['country', 'Year', 'Unit'],
    columns='category',
    values='Data'
).reset_index()

#Rename columns for easier access
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

#Merge CO2 dataset with temperature impacts
df_merge_co2 = df_co2.merge(
    df_comb_reg_inc_pivot_rename[['country', 'year', 'temperature_change_from_ch4_fossil',
                           'temperature_change_from_co2_fossil', 'temperature_change_from_n2o_fossil',
                           'temperature_change_from_ghg_fossil', 'temperature_change_from_ch4_lucf',
                           'temperature_change_from_co2_lucf', 'temperature_change_from_n2o_lucf',
                           'temperature_change_from_ghg_lucf']],
    on=['country', 'year'],
    how='left'
)

#-------------------------------------
#Add derived warming impact indicators
#-------------------------------------

income_groups = ['High-income countries', 'Low-income countries', 
                'Lower-middle-income countries', 'Upper-middle-income countries']

#Add warming impact from fossil fuels and industry
df_merge_co2['warming_impact_fossil'] = ((df_merge_co2['temperature_change_from_co2_fossil']) +
                            (df_merge_co2['temperature_change_from_ch4_fossil'] +
                            df_merge_co2['temperature_change_from_n2o_fossil']))

#Add warming impact from land use change
df_merge_co2['warming_impact_land'] = (df_merge_co2['temperature_change_from_co2_lucf'] +
                            (df_merge_co2['temperature_change_from_ch4_lucf'] +
                            df_merge_co2['temperature_change_from_n2o_lucf']))

#Merge with income groups
df_merge_co2_inc = df_merge_co2.merge(
    df_income_groups[['country', 'classification']],
    on='country',
    how='left'
)

#Merge with continent/region info
df_regions_exploded_2 = df_regions[df_regions['short_name'].isin(['Asia', 'Africa', 'Europe', 'Oceania', 'North America', 'South America'])].explode('members')
df_merge_co2_inc_reg = df_merge_co2_inc.merge(df_regions_exploded_2[['members', 'short_name']], right_on='members',
                                             left_on='iso_code', how='left')

df_merge_co2_inc_reg = df_merge_co2_inc_reg.drop(columns=['members'])

df_merge_co2_inc_reg = df_merge_co2_inc_reg.rename(columns={'classification': 'income_group', 'short_name':'region'})

#Total warming impact (from Jones et. al)
df_merge_co2_inc_reg['warming_impact_total_Jones'] = df_merge_co2_inc_reg['warming_impact_land'] + df_merge_co2_inc_reg['warming_impact_fossil']

#-----------------------------
#Helper functions
#-----------------------------

def min_year(df, col_year, col_country, col_ind, country):
  '''
  Return the first year with nonzero and non-NaN values
  for a given indicator and country.
  '''
  df = df[[col_ind, col_year, col_country]].copy()

  df = df[(df[col_ind] != 0)&(~df[col_ind].isna())]

  min_year = df[col_year][(df[col_country] == country)].min()

  return min_year

def relative_change(df, g, col, col_year='year'):
  '''
  Compute relative change (%) for a given column starting
  from the first nonzero valid year.
  '''
  start_year = min_year(df, 'year', 'country', col, g.name)
  g = g[g[col_year] >= start_year]
  if g.empty:
    return pd.Series([None]*len(g), index=g.index)
  base_value = g[col].iloc[0]
  rel = ((g[col]) - (base_value)) / abs((base_value))*100
  rel.iloc[0] = 0
  return rel

#---------------------------------
#Apply relative change computation
#---------------------------------

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

#------------------------------------------------------------
#Download and preprocess emissions data (Jones dataset + GCB)
#------------------------------------------------------------

#URL for annual emissions dataset Jones et. al (1830-2023)
url_all_emissions = 'https://zenodo.org/records/14054503/files/EMISSIONS_ANNUAL_1830-2023.csv'
get_data_web(url_all_emissions, 'all_emissions.csv')

#Load emissions dataset
df_all_emissions = pd.read_csv('all_emissions.csv')

# Standardize column name
df_all_emissions = df_all_emissions.rename(columns={'CNTR_NAME': 'country'})

#Conver units:
#Tg = teragrams = 1e6 tonnes
#Pg = petagrams = 1e9 tonnes
df_all_emissions.loc[df_all_emissions['Unit'].str.startswith('Tg'), 'Data'] *= 1e6
df_all_emissions.loc[df_all_emissions['Unit'].str.startswith('Pg'), 'Data'] *= 1e9

#Drop the unit column (no longer needed)
df_all_emissions = df_all_emissions.drop(columns='Unit')

#Remove agreggate/non-country entries
df_all_emissions = df_all_emissions[~df_all_emissions['country'].isin(excluded_countries_name_temperature)]

#Standardize country names
df_all_emissions['country'] = df_all_emissions['country'].replace(new_countries_name_temperature)

#Merge with income group classification
df_merge_inc_all_emissions = df_all_emissions.merge(
    df_income_groups_ven_eth[['country', 'classification']],
    on='country',
    how='left'
)

#Aggregate emissions by income group, gas, component and year
df_group_all_emissions = df_merge_inc_all_emissions.groupby(['classification', 'Gas', 'Component','Year'])['Data'].sum().reset_index()

#Rename classification to country for consistency
df_group_all_emissions = df_group_all_emissions.rename(columns={'classification': 'country'})

#Combine country-level and income-group-level datasets
df_comb_all_emissions = pd.concat([df_all_emissions, df_group_all_emissions], axis=0, ignore_index=True)

#Merge to add regional aggregations
df_merge_regions_all_emissions= df_regions_exploded.merge(df_all_emissions, left_on='members',
                                             right_on='ISO3', how='left')

#Aggregate emissions by region, year, gas and component
df_region_all_emissions = (
    df_merge_regions_all_emissions.groupby(['short_name', 'Year', 'Gas','Component'], as_index=False)['Data'].sum()
)

#Rename short name to country
df_region_all_emissions = df_region_all_emissions.rename(columns={'short_name': 'country'})

#Combine countries, income groups and regions
df_comb_reg_inc_all_emissions= pd.concat([df_comb_all_emissions, df_region_all_emissions], axis=0, ignore_index=True)

#Create a category column combining component and gas (e.g. "Fossil CO2")
df_comb_reg_inc_all_emissions['category'] = df_comb_reg_inc_all_emissions['Component'] + '_' + df_comb_reg_inc_all_emissions['Gas']

#Pivot to wide format:
#Rows = (country, year)
#Columns = emission categories
df_comb_reg_inc_all_emissions_pivot = df_comb_reg_inc_all_emissions.pivot_table(
    index=['country', 'Year'],
    columns='category',
    values='Data'
).reset_index()

#Keep only years >=1850 to avoid data mismatch and emissions jump from prior to 1850
df_comb_reg_inc_all_emissions_pivot = df_comb_reg_inc_all_emissions_pivot[df_comb_reg_inc_all_emissions_pivot['Year']>=1850].reset_index(drop=True)

#Rename columns for readability
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

#Recalculate methane total using GWP (different weights for fossil vs LULUCF)
df_comb_reg_inc_all_emissions_rename['ch4_total_jones'] = (
    df_comb_reg_inc_all_emissions_rename['ch4_fossil_jones']*29.8 +
    df_comb_reg_inc_all_emissions_rename['ch4_lucf_jones']*27.2
)

# Recalculate N2O total with GWP factor = 273
df_comb_reg_inc_all_emissions_rename['n2o_total_jones'] = (
    df_comb_reg_inc_all_emissions_rename['n2o_total_jones'] * 273
)

#Drop intermediate columns
df_comb_reg_inc_all_emissions_rename = df_comb_reg_inc_all_emissions_rename.drop(columns=[
    'ch4_fossil_jones', 'n2o_fossil_jones', 'ch4_lucf_jones', 'n2o_lucf_jones'
])

#------------------------------------------------------------
#Land-use change CO2 data (BLUE model + Global Carbon Budget)
#------------------------------------------------------------

#Load national land-use emissions dataset (BLUE model)
df_co2_land_use_gb = pd.read_excel('National_LandUseChange_Carbon_Emissions_2024v1.0-1.xlsx', sheet_name='BLUE', header=7)

#Load global dataset from GCB
df_co2_world_land = pd.read_excel('Global_Carbon_Budget_2024_v1.0-1.xlsx', sheet_name='Historical Budget', header=15)

#Keep only year and land-use emissions columns
df_co2_world_land = df_co2_world_land[['Year', 'land-use change emissions']]
df_co2_world_land = df_co2_world_land.dropna()
#Convert from MtC to ktCO2 (factor 1000)
df_co2_world_land['land-use change emissions'] = df_co2_world_land['land-use change emissions']*1000

#Reshape country-level dataset to long format
df_co2_land_use_gb = df_co2_land_use_gb.melt(
    id_vars=['unit: Tg C/year'],
    var_name = 'country',
    value_name='value'
)

#Rename columns for clarity
df_co2_land_use_gb = df_co2_land_use_gb.rename(columns={'unit: Tg C/year': 'year',
                                                        'value': 'Data'})

#Replace "Global" row with the global dataset from GCB
df_co2_land_use_gb.loc[df_co2_land_use_gb['country']=='Global', 'Data'] = (
    df_co2_land_use_gb.loc[df_co2_land_use_gb['country']=='Global', 'year']
    .map(df_co2_world_land.set_index('Year')['land-use change emissions']))

#Convert from TgC to tonnes of CO2
df_co2_land_use_gb['Data'] = df_co2_land_use_gb['Data']*3.664*1e6

#Exclude non-country entities
excluded_countries_name_temperature_land = [
	"KP Annex B",
	"Non KP Annex B",
	"DISPUTED",
	"OTHER",
]

#Dictionary to harmonize country names between datasets
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
#Remove excluded countries
df_co2_land_use_gb = df_co2_land_use_gb[~df_co2_land_use_gb['country'].isin(excluded_countries_name_temperature_land)]

#Standardize country names
df_co2_land_use_gb['country'] = df_co2_land_use_gb['country'].replace(new_countries_name_land)

#---------------------------------------------------
#Fossil CO2 emissions (Global Carbon Budget dataset)
#---------------------------------------------------

#Download fossil CO2 dataset
url_fossil_gb = 'https://zenodo.org/records/13981696/files/GCB2024v17_MtCO2_flat.csv'
get_data_web(url_fossil_gb, 'co2_fossil_emissions.csv')

#Load fossil dataset
df_co2_fossil = pd.read_csv('co2_fossil_emissions.csv')

#Conver from MTCO2 to tonnes
df_co2_fossil['Total'] = df_co2_fossil['Total']*1e6

#Standardize column names
df_co2_fossil = df_co2_fossil.rename(columns={'ISO 3166-1 alpha-3': 'ISO3',
                                              'Country': 'country',
                                              'Year': 'year'})

#Replace zeros with NaN when all individual sources are NaN
no_emission_replace_nan = df_co2_fossil.drop(columns=['country', 'year', 'Total', 'ISO3', 'UN M49']).isnull().all(axis=1)
df_co2_fossil.loc[no_emission_replace_nan, 'Total'] = np.nan

#Drop unneded columns
df_co2_fossil = df_co2_fossil.drop(columns=['UN M49', 'Coal', 'Oil', 'Gas', 'Cement', 'Flaring', 'Other', 'Per Capita'])

#Exclude aggregates
df_co2_fossil = df_co2_fossil[~df_co2_fossil['country'].isin(excluded_countries_name_temperature_land)]

#Standardize country names
df_co2_fossil['country'] = df_co2_fossil['country'].replace(new_countries_name_land)

#--------------------------------------------------
#Combine Fossil and Land-use to total CO2 emissions
#--------------------------------------------------

#Merge fossil and land-use dataframes
df_co2_total = df_co2_fossil.merge(
    df_co2_land_use_gb[['country', 'year','Data']],
    on=['country', 'year'],
    how='left'
)

#Rename columns
df_co2_total = df_co2_total.rename(columns={'Total': 'fossil', 'Data': 'land_use'})

#Compute total CO2
df_co2_total['Total'] = df_co2_total['fossil'] + df_co2_total['land_use']

#Add income groups
df_merge_inc_total = df_co2_total.merge(
    df_income_groups_ven_eth[['country', 'classification']],
    on='country',
    how='left'
)

#Aggregate by income group
df_group_co2_total = df_merge_inc_total.groupby(['classification', 'year'])[['fossil','land_use', 'Total']].sum().reset_index()

#Rename classification to country to standardize column name
df_group_co2_total = df_group_co2_total.rename(columns={'classification': 'country'})

#Combine countries and income groups
df_comb_co2_total = pd.concat([df_merge_inc_total, df_group_co2_total], axis=0, ignore_index=True)

df_merge_regions_co2_total = df_regions_exploded.merge(df_co2_total, left_on='members',
                                             right_on='ISO3', how='left')

df_region_co2_total = (
    df_merge_regions_co2_total.groupby(['short_name', 'year'], as_index=False)[['fossil','land_use', 'Total']].sum()
)

#Rename shor_name to country to standardize column name
df_region_co2_total = df_region_co2_total.rename(columns={'short_name': 'country'})

#Combine countries, income groups and regions
df_comb_reg_inc_total= pd.concat([df_comb_co2_total, df_region_co2_total], axis=0, ignore_index=True)

#-----------------------------------
#Merge Jones et. al with GCB dataset
#-----------------------------------

#Drop CO2 columns from Jones et. al dataset (using GCB instead)
df_comb_reg_inc_all_emissions_rename = df_comb_reg_inc_all_emissions_rename.drop(columns=['co2_fossil_jones', 'co2_lucf_jones',
                                                   'co2_total_jones'])

#Rename CO2 columns from GCB dataset
df_comb_reg_inc_total_rename = df_comb_reg_inc_total.rename(columns={'Total': 'co2_total_gb',
                                                                     'fossil': 'co2_fossil_gb',
                                                                     'land_use': 'co2_land_use_gb'})

#Merge datasets into master dataframe
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

#Final working dataframe
df_merge_co2_inc_reg_new = df_merge_co2_inc_reg_all

#---------------------------------
#Add relative change columns for
#Jones et. al and GCB columns
#---------------------------------

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

df_merge_co2_inc_reg_new.to_csv('transformed_co2_dataset.csv')