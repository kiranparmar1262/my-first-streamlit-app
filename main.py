import streamlit as st
import pickle 

pickle_in = open('regression.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache

# defining the function which will make the prediction using the data which the user inputs 
def prediction(area):   
 
    # Pre-processing user input      
    # Making predictions 
    prediction = classifier.predict([[area]])
    return prediction
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:Yellow;padding:8px;border-radius:30px;text-align:center">
    <h1 style ="color:black">House Price Prediction ML App</h1> 
    </div> 
    <br/>
    """
    
    page_bg_img = '''

    <style>
    body {
    
    background-image: url("https://image.freepik.com/free-photo/abstract-black-white-bokeh-background_1962-1324.jpg");
    background-size: cover;
    }
    </style>
    '''
    
   
    #st.image('houseprice.jpg')  
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)   
    # following lines create boxes in which user can enter data required to make prediction 
    
#     Gender = st.selectbox('Gender',("Male","Female"))      this is for drop down box
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    area = st.number_input("Area") 
    result = ""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        result = prediction(area)
        st.success('House Price is {}'.format(result[0],[0]))
     
if __name__=='__main__': 
    main()

