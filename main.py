import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')

import streamlit as st
import pickle

df = pd.read_csv('C:/Users/LENOVO/Data Science/Machine Learning/homeprices.csv')
df.head()

x = df.iloc[:,:1]
y = df.iloc[:,1:]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression()
model.fit(x,y)

predict = model.predict(x)
r2_score(y,predict)



import pickle 
pickle_out = open("regression.pkl", mode = "wb") 
pickle.dump(model, pickle_out) 
pickle_out.close()


pickle_in = open('regression.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache

# defining the function which will make the prediction using the data which the user inputs 
def prediction(area):   
 
    # Pre-processing user input      
    Area = area
    # Making predictions 
    prediction = classifier.predict([[Area]])
    return prediction
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:black;padding:13px">
    <h1 style ="color:white;text-align:center;">My First Streamlit ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    
#     Gender = st.selectbox('Gender',("Male","Female"))      this is for drop down box
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    Area = st.number_input("Area") 
    result = ""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        result = prediction(Area)
        st.success('Your Area By Area is {}'.format(result))
     
if __name__=='__main__': 
    main()
