import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


st.title('Oui')

st.header('des test de trucs')
st.subheader('on verra hein')

st.write('blabla bla j\'ai la flemme de mettre un lorem')
st.markdown('# un titre ?')

df = pd.read_csv('test.csv')

st.write(df)
# st.dataframe(df)
# st.table(df)

st.button('Clique')
st.checkbox('oui ? ')
st.text_input('vasy fils')
st.toggle('?')
st.slider('1')
st.selectbox('le 1er poké',['sala','cara','bulbi'])
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    with st.expander('Plus de détails ?'):
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.checkbox("bg non ?")
            
onglet1, onglet2, onglet3 = st.tabs(['Cat', 'Dog', 'Owl'])

with onglet1: 
    st.header("A cat")
    with st.expander('Voir l\'image'):
        st.image("https://static.streamlit.io/examples/cat.jpg")
        st.checkbox("Bg ou pas le chat ?")

with onglet2: 
    st.header("A dog")
    with st.expander('Voir l\'image'):
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.checkbox("Tu trouves le chien bg ?")

with onglet3:
    st.header("An owl")        
    with st.expander('Voir l\'image'):
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.checkbox("Tu trouves le hibou bg ?")

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
st.pyplot(fig)
st.plotly_chart(fig)

df_iris = sns.load_dataset('iris')

sns.pairplot(df_iris, hue='species')

st.pyplot(plt.gcf())


option = st.selectbox(
    'Que voulez-vous voir ?',
    ("Cat", "Dog", "Owl"),

)
logger.info(f"Option sélectionnée : {option}")

@st.cache_data
def animaux(option):
    if option == "Cat":
        logger.info(f"Option sélectionnée : {option}")
        return {
            "header": "A cat",
            "image": "https://static.streamlit.io/examples/cat.jpg",
            "checkbox_label": "Bg ou pas le chat 1?"
        }
    elif option == "Dog":
        logger.info(f"Option sélectionnée : {option}")
        return {
            "header": "A dog",
            "image": "https://static.streamlit.io/examples/dog.jpg",
            "checkbox_label": "Et lui hein2 ?"
        }
    elif option == "Owl":
        logger.info(f"Option sélectionnée : {option}")    
        return {
            "header": "An owl",
            "image": "https://static.streamlit.io/examples/owl.jpg",
            "checkbox_label": "Lui oui 3?"
        }


animal_info = animaux(option)

if animal_info:
    st.header(animal_info["header"])
    with st.expander('Voir l\'image'):
        st.image(animal_info["image"])
        st.checkbox(animal_info["checkbox_label"])
        
        
        
# if option not in st.session_state:
#     st.session_state['option']
st.file_uploader('le projet')

Lecon = "Smartest Rick Roll but with a different link. ( 720 X 1280 ).mp4"
st.download_button('Clique', 
                   data=open(Lecon, "rb"),
                   file_name="clique vasy", 
                   mime="video/mp4"
                   )