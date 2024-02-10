import streamlit as st
st.set_page_config(page_title='Mystreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My menu',('Home','FillForm','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('Onlei Technologies')
st.header('By Abhinav Srivastav')
st.text('This is a tutorial on streamlit library')
if(mymenu=='Home'):
	st.markdown('<center><h1>WELCOME</h2></center>',unsafe_allow_html=True)
	st.video('https://www.youtube.com/watch?v=QDcAK6glJZ4')
elif(mymenu=='FillForm'):
	with st.form('My Form'):
		name=st.text_input('Enter Name')
		dob=st.date_input("Choose Date of Birth")
		marks=st.slider('Choose Marks')
		k=st.form_submit_button("Submit Form")
		if k:
			st.write('Name:',name,'DOB:',dob,'Marks:',marks)

elif(mymenu=='Downloads'):
     st.header("Downloads")
     st.download_button('Download Now','Hello this is the downloaded data','onlei.txt')