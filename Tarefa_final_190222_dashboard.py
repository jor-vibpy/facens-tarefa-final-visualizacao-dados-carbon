import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

#-----------------------------------------------
#Load transformed dataset for dashboard creation
#-----------------------------------------------

df_merge_co2_inc_reg_new = pd.read_csv('transformed_co2_dataset.csv')

#Income groups list for dashboard filters
income_groups = ['High-income countries', 'Low-income countries', 
                'Lower-middle-income countries', 'Upper-middle-income countries']

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

#--------------------------------------------------------
#Dash Application for Global Emissions and Warming Impact
#--------------------------------------------------------

#Initialize Dash app
app = dash.Dash(__name__)
server = app.server

#---------------------------------
#Layout: Structure of the Web App
#---------------------------------

app.layout = html.Div([
	#Title
    html.H1('Distribution of Global Emissions and Warming Impact'),
	
	#Dropdown: select warming impact source
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

	#Dropdown: select polluent gas
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

	#-----------------------------------------------
	#Section 1: Line plot (Emissions vs Temperature)
	#-----------------------------------------------

    html.H2('1. Global Evolution of emissions and surface temperature rise'),

	#Dropdown: select country or region
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

	#Radio: Relative change or raw values
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

	#Radio: Emissions vs warming impact
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

	#Title
    dcc.Markdown(id = 'line-temp-title', mathjax=True,
                 style={
                     'fontSize': '24px',
                     'fontFamily': 'Open Sans',
                     'fontweight': 'bold',
                 }),

	#Message text
    dcc.Markdown(id = 'line-temp-text', mathjax=True,
                 style={
                     'fontSize': '20px',
                     'fontFamily': 'Open Sans',
                 }),

	#Line grath to temperaure and emission
    dcc.Graph(id = 'line-temp'),

	#--------------------------------------------
	#Section 2: Bar plot (Top Emitters over time)
	#--------------------------------------------

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

	#--------------------------------------------
	#Section 3: Choropleth map (Warming Impact)
	#--------------------------------------------
	
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

	#----------------------------------------------
	#Section 4: Boxplot (Income group distribution)
	#----------------------------------------------
	
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

	#--------------------------------------------
	#Section 5: Scatter plot (GDP vs Emissions)
	#--------------------------------------------
	
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

	#--------------------------------------------
	#Section 6: Heatmap (Correlation Matrix)
	#--------------------------------------------
	
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

#--------------------------------------------
#Callbacks
#--------------------------------------------

#Update bar dropdown: auto-select top emitters in latest year
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

#Update scatter slider: set auto year range based on selected gas
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

#Update line chart: emissions or warming impact
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

#Update bar chart: historicall emitters
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

#Update map plot: warming impact distribution
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

#Update boxplot: emissions by income
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

#Update scatter chart: emissions vs GDP
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

#Update heatmap: correlation matrix
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

#---------------------------------
#Run Dash App
#---------------------------------

if __name__ == "__main__":
  app.run()
