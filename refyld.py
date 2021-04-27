import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime as dt, timedelta
import plotly.express as px
import plotly.graph_objects as go

import dash_auth


df_insights = pd.read_csv('FB_Insights.csv')
df_likes_fb = pd.read_csv('FB_Likes.csv')
df3 = pd.read_csv('Sub_Nw.csv')
df4 = pd.read_csv('Talking_Pays.csv')
df_insta = pd.read_csv('Insta_Insights.csv')
df_members = pd.read_csv('Members_Refyld.csv')

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial_scale = 1.0'}] # for mobile vizu
                )

colors = {
    'background': '#F5F3EA',
    'text': '#343a40'
}

#auth = dash_auth.BasicAuth(app, [['Username', 'Password'],['refyld_adm', 'refyld2021']])

card_title2 = dbc.Card(children = [
    dbc.CardBody(
        dbc.Row([
            dbc.CardImg(src='https://cdn.shopify.com/s/files/1/0442/6219/5368/files/REFYLD_LOGO-noir_85x@2x.png?v=1601997372',
                  title = 'Refyld Dashboard', alt='Refyld Logo',
                  style={'textAlign': 'left','width': 200}),

            dbc.Col([
            html.Div('Dashboard', className='app_title',
                style={'font-family' : 'Brioso Pro Light Display',
                       'font-type': 'bold',
                       'fontSize': 60,
                       'color' : 'black',
                       "text-align": "right", 'maxWidth': '100%'})
            ]),
            dbc.Col([
                html.H3(dt.now().ctime(), className= 'Current Time',
                        style={'font-family': 'Brioso Pro Light Display',
                              'font-type': 'bold',
                              'color': 'black',
                              "text-align": "right", 'maxWidth': '100%'})
            ])
        ])
    )
], style={'backgroundColor': colors['background']} ,className= 'border-0',
)


card_title = dbc.Card(children = [
    dbc.CardImg(src='https://cdn.shopify.com/s/files/1/0442/6219/5368/files/REFYLD_LOGO-noir_85x@2x.png?v=1601997372',
                top=True, title = 'Refyld Dashboard', alt='Refyld Logo'),
    dbc.CardBody(
        html.H1('Dashboard', className='app_title',
                style={'font-family' : 'Brioso Pro Light Display',
                       'font-type': 'bold',
                       'color' : 'black',
                       "text-align": "center", 'maxWidth': '100%'})
    )
], style={'backgroundColor': colors['background'],"width": "18rem"}, className= 'border-0',
)

card_metrics = dbc.Card(children=[
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                html.H1('Facebook Page Likes', className='fb total likes',
                    style={'font-family' : 'Brioso Pro Light Display',
                       'font-type': 'bold',
                       'color' : 'black',
                       "text-align": "center", 'maxWidth': '100%'}),
                html.Br(),
                html.H1(df_likes_fb['Lifetime Total Likes'][0], className='amount likes',
                    style={'font-family': 'Brioso Pro Light Display',
                           'font-type': 'bold',
                           'color': 'black',
                           "text-align": "center", 'maxWidth': '100%'}
                    )
        ]),
            dbc.Col([
                html.H1('Instagram Followers', className='insta followers',
                    style={'font-family' : 'Brioso Pro Light Display',
                       'font-type': 'bold',
                       'color' : 'black',
                       "text-align": "center", 'maxWidth': '100%'}),
                html.Br(),
                html.H1(df_insta.Followers[0], className='amount likes',
                    style={'font-family': 'Brioso Pro Light Display',
                           'font-type': 'bold',
                           'color': 'black',
                           "text-align": "center", 'maxWidth': '100%'}
                    )
        ]),
            dbc.Col([
                html.H1('Total Members Refyld', className='adhérants',
                    style={'font-family' : 'Brioso Pro Light Display',
                       'font-type': 'bold',
                       'color' : 'black',
                       "text-align": "center", 'maxWidth': '100%'}),
                html.Br(),
                html.H1(df_members[df_members['Titre de la contrepartie'].str.contains('Ad')].shape[0]+1, className='total members',
                    style={'font-family': 'Brioso Pro Light Display',
                           'font-type': 'bold',
                           'color': 'black',
                           "text-align": "center", 'maxWidth': '100%'}
                    )
        ]),
            dbc.Col([
                html.H1('Newsletter Subcribers', className='nwl subscribers',
                    style={'font-family' : 'Brioso Pro Light Display',
                       'font-type': 'bold',
                       'color' : 'black',
                       "text-align": "center", 'maxWidth': '100%'}),
                html.Br(),
                html.H1(df3['Email Address'].count(), className='amount likes',
                    style={'font-family': 'Brioso Pro Light Display',
                           'font-type': 'bold',
                           'color': 'black',
                           "text-align": "center", 'maxWidth': '100%'}
                    )
            ])
        ])

    ], style={'backgroundColor': '#2E8B57'}, className= 'border-0')
])
card_facebook_insights = dbc.Card(children = [
    dbc.Col([

        html.H3('Facebook Insights'),

        html.Label(['Get Visualization by:'],style={'font-weight': 'bold', "text-align": "center", 'marginBottom': '1.5em'}),

        dcc.RadioItems(id = 'date_vizu_fb',
                       options=[{'label': 'Day of the Week', 'value': 'Day of the Week'},
                                {'label': 'Month', 'value': 'Month'}],
                       value='Day of the Week'),

        html.Label(['Select Insight:'],style={'font-weight': 'bold', "text-align": "center", 'marginBottom': '1.5em'}),

        dcc.Dropdown(id='my_dropdown_fb',
                 options=[{'label' : 'Impressions', 'value': 'Impressions'},
                         {'label': 'Reach', 'value': 'Reach'}
                ],
                optionHeight = 35,
                value = 'Reach',
                disabled = False,
                multi = False,
                searchable = False,
                placeholder = 'Please select...',
                clearable = True,
                style = {'width': '50%', 'offset': 4}
                ),
        dcc.Graph(id='my_bar_fb', figure = {})
        ])
], style={'backgroundColor': colors['background']}, className= 'border-0',)

card_insta_insights = dbc.Card(children = [
    dbc.Col([

        html.H3('Instagram Insights'),

        html.Label(['Get Visualization by:'],style={'font-weight': 'bold', "text-align": "center", 'marginBottom': '1.5em'}),

        dcc.RadioItems(id = 'date_vizu_insta',
                       options=[{'label': 'Day of the Week', 'value': 'Day of the Week'},
                                {'label': 'Month', 'value': 'Month'}],
                       value='Day of the Week'),

        html.Label(['Select Insight:'],style={'font-weight': 'bold', "text-align": "center", 'marginBottom': '1.5em'}),

        dcc.Dropdown(id='my_dropdown_insta',
                 options=[{'label' : 'Impressions', 'value': 'Impressions'},
                         {'label': 'Reach', 'value': 'Reach'}
                ],
                optionHeight = 35,
                value = 'Reach',
                disabled = False,
                multi = False,
                searchable = False,
                placeholder = 'Please select...',
                clearable = True,
                style = {'width': '50%', 'offset': 4}
                ),
        dcc.Graph(id='my_bar_insta', figure = {})
        ])
], style={'backgroundColor': colors['background']}, className= 'border-0',)


card_facebook_likes = dbc.Card(children = [
    dbc.Col([

        html.Label(['Select Date:    '],style={'font-weight': 'bold', "text-align": "center"}),

        html.Br(),

        dcc.DatePickerRange(id = "selected_date", calendar_orientation='horizontal', day_size=30,
                            #end_date_placeholder_text='End Date',
                            with_portal=False, first_day_of_week=0, reopen_calendar_on_clear=True, is_RTL=False,
                            clearable=True, number_of_months_shown=1, min_date_allowed=dt(2020, 10, 1),max_date_allowed=pd.to_datetime("today").date(),
                            initial_visible_month= dt(dt.today().year, dt.today().month, 1).date().isoformat(),
                            start_date=(dt.today() - timedelta(days=7)).date().isoformat(), end_date=pd.to_datetime("today").date(),
                            display_format="DD-MMM-YYYY", minimum_nights=6,
                            persistence=True, persisted_props=["start_date"], persistence_type="local",
                            updatemode="singledate", style={'width': '70%', 'offset': 2}),

        dcc.Graph(id = 'my-second', figure = {}, style={'marginTop': '1.5em'})
    ])
], style={'backgroundColor': colors['background']}, className= 'border-0',)

card_insta_followers = dbc.Card(children = [
    dbc.Col([

        html.Label(['Select Date:    '],style={'font-weight': 'bold', "text-align": "center"}),

        html.Br(),

        dcc.DatePickerRange(id = "selected_date_insta", calendar_orientation='horizontal', day_size=30,
                            #end_date_placeholder_text='End Date',
                            with_portal=False, first_day_of_week=0, reopen_calendar_on_clear=True, is_RTL=False,
                            clearable=True, number_of_months_shown=1, min_date_allowed=dt(2020, 10, 1),max_date_allowed=pd.to_datetime("today").date(),
                            initial_visible_month= dt(dt.today().year, dt.today().month, 1).date().isoformat(),
                            start_date=(dt.today() - timedelta(days=7)).date().isoformat(), end_date=pd.to_datetime("today").date(),
                            display_format="DD-MMM-YYYY", minimum_nights=6,
                            persistence=True, persisted_props=["start_date"], persistence_type="local",
                            updatemode="singledate", style={'width': '70%', 'offset': 2}),

        dcc.Graph(id = 'my_insta_followers', figure = {}, style={'marginTop': '1.5em'})
    ])
], style={'backgroundColor': colors['background']}, className= 'border-0',)

card_regions = dbc.Card(children=[
    dbc.Col(dcc.Graph(id = 'my-global', figure={}))
], style={'backgroundColor': colors['background']}, className= 'border-0', )



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dbc.Row([
        dbc.Col(card_title2)
    ], justify = 'around'),
    dbc.Row([
        html.Br()
    ]),

    dbc.Row([
        dbc.Col(card_metrics
        )
    ]),

    dbc.Row([
        dbc.Col(card_facebook_insights, width=6),
        dbc.Col(card_insta_insights, width = 6)
    ], justify = 'simple'),

    dbc.Row([
        dbc.Col(card_facebook_likes, width=6),
        dbc.Col(card_insta_followers, width=6)
    ]),
    dbc.Row([
        dbc.Col(card_regions)
    ])
])





@app.callback(
    Output(component_id='my_bar_fb', component_property='figure'),
    [Input(component_id='date_vizu_fb', component_property='value')],
    [Input(component_id='my_dropdown_fb', component_property='value')]
)

def build_graph_facebook(select_vizu_fb, column_chosen_fb):
    week_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_order = ['October', 'November', 'December', 'January', 'February', 'March']

    dff = df_insights.groupby([f'{select_vizu_fb}', f'{column_chosen_fb}'])[[f'Amount of {column_chosen_fb}']].sum().reindex(month_order if 'Month' in select_vizu_fb else week_order, level=0).reset_index()

    fig_bar = px.bar(data_frame=dff, x=f'{select_vizu_fb}', y = f'Amount of {column_chosen_fb}',
                     color=f'{column_chosen_fb}',
                     color_discrete_sequence=px.colors.qualitative.Dark2,
                     title = 'Total of '+f'{column_chosen_fb}'+' by :', )
    fig_bar.update_layout(

        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig_bar

@app.callback(
    Output(component_id='my_bar_insta', component_property='figure'),
    [Input(component_id='date_vizu_insta', component_property='value')],
    [Input(component_id='my_dropdown_insta', component_property='value')]
)

def build_graph_insta(select_vizu_insta, column_chosen_insta):
    week_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_order = ['December', 'January', 'February', 'March']

    dff = df_insta.groupby(f'{select_vizu_insta}')[[f'{column_chosen_insta}']].sum().reindex(month_order if 'Month' in select_vizu_insta else week_order).reset_index()

    fig_bar = px.bar(data_frame=dff, x=f'{select_vizu_insta}', y = f'{column_chosen_insta}',
                     color=f'{column_chosen_insta}',
                     labels={f'{column_chosen_insta}': 'Amount of '+f'{column_chosen_insta}'},
                     color_discrete_map=px.colors.qualitative.Dark2,
                     title = 'Total of '+f'{column_chosen_insta}'+' by :', )
    fig_bar.update_layout(

        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig_bar


@app.callback(
    Output(component_id='my-second', component_property='figure'),
    [Input(component_id='selected_date', component_property='start_date'),
     Input(component_id='selected_date', component_property='end_date')])

def likes_graph_fb(start_date, end_date):

    start_date = pd.to_datetime(start_date).date().isoformat()
    end_date = pd.to_datetime(end_date).date().isoformat()
    df_likes_fb['Date'] = pd.to_datetime(df_likes_fb.Date, yearfirst=True)
    #dff = dataset_with_correct_dates(df_likes_fb.copy(), 'Date', start_date, end_date)
    dff = df_likes_fb.copy()
    dff.set_index('Date', inplace = True)
    dff = dff.loc[start_date:end_date]
    neg = dff.loc[dff['Page Likes'] == 'Daily Unlikes']
    pos = dff.loc[dff['Page Likes']== "Daily New Likes"]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=neg.index, y=neg['Amount'],
                         marker_color='crimson',
                         name='Unlikes'))
    fig.add_trace(go.Bar(x=pos.index, y=pos['Amount'],
                         marker_color='lightslategrey',
                         name='Likes'
                         ))
    fig.update_layout(
        title = 'Facebook Page Likes and Unlikes',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])

    return fig

@app.callback(
    Output(component_id='my_insta_followers', component_property='figure'),
    [Input(component_id='selected_date_insta', component_property='start_date'),
     Input(component_id='selected_date_insta', component_property='end_date')])

def followers_graph_insta(start_date, end_date):

    start_date = pd.to_datetime(start_date).date().isoformat()
    end_date = pd.to_datetime(end_date).date().isoformat()
    df_insta['Date'] = pd.to_datetime(df_insta.Date, yearfirst=True)
    #dff = dataset_with_correct_dates(df_likes_fb.copy(), 'Date', start_date, end_date)
    dff2 = df_insta.copy()
    dff2.set_index('Date', inplace = True)
    dff3 = dff2.loc[start_date:end_date]
    #dff.reset_index(inplace=True)
    fig = go.Figure(go.Scatter(x=dff3.index, y=dff3['Followers']))
    fig.update_layout(
        title='Instagram Followers',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])

    return fig

@app.callback(
    Output(component_id='my-global', component_property='figure'),
    Input(component_id='fig_global', component_property='value'))

def global_graph( ):
    fig_global = px.choropleth(df4, locations="ISO 3",
                        color="Talking About",  # lifeExp is a column of gapminder
                        hover_name="Pays",  # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Aggrnyl)
    return fig_global
#-------------------------------------------------------------

# must have Dash version 1.16.0 or higher
#@app.callback(
 #   Output(component_id='my-bar', component_property='figure'),
  #  Input(component_id='fig_bar', component_property='value'))

#def update_graph(fig_ar):
 #   dff = df.copy()

  #  fig_bar = px.bar(data_frame=dff, x = 'day_week', y = 'Amount',color = 'Type of Impression',
   #          hover_data=['Percentage'])

    #return fig_bar

if __name__ == '__main__':
    app.run_server(debug=True)

