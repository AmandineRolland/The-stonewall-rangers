import streamlit as st
import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

st.image('./images/logo.png')
#st.title("The Stonewall Rangers")
#st.header('Real Estate')

st.subheader('Price predictor')
col1, col2,col3 = st.columns([3,1,1])

with col1 :
# entrée des paramètres pour l'estimation du prix

    surface_reelle_bati = st.number_input(label='Insert an area (m²)',step=1,min_value=0)

    nombre_pieces_principales=st.number_input('Insert the number of room',step=1,min_value=0)

# Liste des codes postaux
    zip_code_list=[75001, 75002, 75003, 75004, 75005, 75006, 75007, 75008, 75009,
       75010, 75011, 75012, 75013, 75014, 75015, 75016, 75017, 75018,
       75019, 75020, 77000, 77090, 77100, 77111, 77114, 77115, 77118,
       77120, 77122, 77123, 77124, 77126, 77127, 77130, 77131, 77133,
       77134, 77135, 77138, 77139, 77140, 77141, 77144, 77145, 77148,
       77150, 77151, 77154, 77157, 77160, 77163, 77164, 77165, 77166,
       77167, 77169, 77170, 77171, 77173, 77174, 77176, 77177, 77178,
       77181, 77183, 77184, 77185, 77186, 77190, 77200, 77210, 77220,
       77230, 77240, 77250, 77260, 77270, 77280, 77290, 77300, 77310,
       77320, 77330, 77340, 77350, 77360, 77370, 77380, 77390, 77400,
       77410, 77420, 77430, 77440, 77450, 77460, 77470, 77480, 77500,
       77510, 77515, 77520, 77540, 77550, 77560, 77570, 77580, 77590,
       77600, 77610, 77620, 77630, 77640, 77650, 77660, 77670, 77680,
       77690, 77700, 77710, 77720, 77730, 77750, 77760, 77780, 77810,
       77820, 77830, 77840, 77850, 77860, 77870, 77880, 77890, 77910,
       77920, 77930, 77940, 77950, 77970, 77990, 78000, 78100, 78110,
       78111, 78113, 78114, 78117, 78120, 78121, 78124, 78125, 78126,
       78130, 78140, 78150, 78160, 78170, 78180, 78190, 78200, 78210,
       78220, 78230, 78240, 78250, 78260, 78270, 78280, 78290, 78300,
       78310, 78320, 78330, 78340, 78350, 78360, 78370, 78380, 78390,
       78400, 78410, 78420, 78430, 78440, 78450, 78460, 78470, 78480,
       78490, 78500, 78510, 78520, 78530, 78540, 78550, 78560, 78570,
       78580, 78590, 78600, 78610, 78620, 78630, 78640, 78650, 78660,
       78670, 78680, 78690, 78700, 78710, 78711, 78720, 78730, 78740,
       78750, 78760, 78770, 78780, 78790, 78800, 78810, 78820, 78830,
       78840, 78850, 78860, 78870, 78890, 78910, 78920, 78930, 78940,
       78950, 78955, 78960, 78970, 78980, 78990, 91000, 91070, 91090,
       91100, 91120, 91130, 91140, 91150, 91160, 91170, 91180, 91190,
       91200, 91210, 91220, 91230, 91240, 91250, 91260, 91270, 91280,
       91290, 91300, 91310, 91320, 91330, 91340, 91350, 91360, 91370,
       91380, 91390, 91400, 91410, 91420, 91430, 91440, 91450, 91460,
       91470, 91480, 91490, 91510, 91520, 91530, 91540, 91550, 91560,
       91570, 91580, 91590, 91600, 91610, 91620, 91630, 91640, 91650,
       91660, 91670, 91680, 91690, 91700, 91710, 91720, 91730, 91740,
       91750, 91760, 91770, 91780, 91790, 91800, 91810, 91820, 91830,
       91840, 91850, 91860, 91870, 91880, 91890, 91910, 91930, 91940,
       92000, 92100, 92110, 92120, 92130, 92140, 92150, 92160, 92170,
       92200, 92210, 92220, 92230, 92240, 92250, 92260, 92270, 92290,
       92300, 92310, 92320, 92330, 92340, 92350, 92370, 92380, 92390,
       92400, 92410, 92420, 92430, 92500, 92600, 92700, 92800, 93000,
       93100, 93110, 93120, 93130, 93140, 93150, 93160, 93170, 93190,
       93220, 93230, 93240, 93250, 93260, 93270, 93290, 93300, 93310,
       93320, 93330, 93340, 93350, 93360, 93370, 93380, 93390, 93400,
       93410, 93420, 93430, 93440, 93450, 93460, 93470, 93500, 93600,
       93700, 93800, 94000, 94110, 94120, 94130, 94140, 94150, 94160,
       94170, 94190, 94200, 94220, 94230, 94240, 94250, 94260, 94270,
       94290, 94300, 94310, 94320, 94340, 94350, 94360, 94370, 94380,
       94400, 94410, 94420, 94430, 94440, 94450, 94460, 94470, 94480,
       94490, 94500, 94510, 94520, 94550, 94600, 94700, 94800, 94880,
       95000, 95100, 95110, 95120, 95130, 95140, 95150, 95160, 95170,
       95180, 95190, 95200, 95210, 95220, 95230, 95240, 95250, 95260,
       95270, 95280, 95290, 95300, 95310, 95320, 95330, 95340, 95350,
       95360, 95370, 95380, 95390, 95400, 95410, 95420, 95430, 95440,
       95450, 95460, 95470, 95480, 95490, 95500, 95510, 95520, 95530,
       95540, 95550, 95560, 95570, 95580, 95590, 95600, 95610, 95620,
       95630, 95640, 95650, 95660, 95670, 95680, 95690, 95700, 95710,
       95720, 95740, 95750, 95760, 95770, 95780, 95800, 95810, 95820,
       95830, 95840, 95850, 95870, 95880]


    Code_Postal=st.selectbox('Insert a zip code',zip_code_list)

    cp_ville=pd.read_csv("https://raw.githubusercontent.com/AmandineRolland/The-stonewall-rangers/main/cp_ville.csv")
    #st.dataframe(cp_ville)
    city=cp_ville[cp_ville['Code Postal']==Code_Postal]['nom_commune'].unique().tolist()
    #st.write(Code_Postal)
    villes=''
    for ville in city:
        villes=villes+str(ville)+"/"
    
    st.write(villes)

    type_local= st.radio("What type of property  are you looking for ?",
    ('House', 'Appartment', 'Industrial/commercial permises'))

    if type_local == 'House':
        maison=1
        appartement=0
        local_industriel=0

    elif type_local=='Appartment':
        appartement=1
        maison=0
        local_industriel=0
    else:
        local_industriel=1
        appartement=0
        maison=0


###################### MODELE MACHINE LEARNING ######################
X=pd.read_csv("https://raw.githubusercontent.com/AmandineRolland/The-stonewall-rangers/main/X.csv")
#st.dataframe(X)
y=pd.read_csv("https://raw.githubusercontent.com/AmandineRolland/The-stonewall-rangers/main/y.csv")

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=30)
modelLR=LinearRegression()
modelLR.fit(X_train,y_train)

X_predict=[[surface_reelle_bati,nombre_pieces_principales,Code_Postal, appartement,local_industriel,maison]]

estimation=int(modelLR.predict(X_predict)[0][0])

########################### AFFICHE L'ESTIMATION ######################################
#st.subheader('Price estimation (€)')
#st.info(estimation)

with col2:
    st.write('')
    #utilisé juste pour avoir un espace vide

with col3 :

    if estimation>0:
        st.metric(label='Price estimation ',value=(f"{estimation} €"))
    else:
        st.metric(label='Price estimation (€)',value='')
############################

