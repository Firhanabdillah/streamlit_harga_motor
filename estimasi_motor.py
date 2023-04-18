import pickle
import streamlit as st

model = pickle.load(open('estimasi_motor.sav', 'rb'))

st.title('Estimasi Harga Motor Bekas')

year = st.number_input('Input Tahun Motor')
km_driven = st.number_input('Input Km Motor')
ex_showroom_price = st.number_input('kisaraan Harga Motor Baru yang akan di beli')


predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, km_driven, ex_showroom_price]]
    )
    st.write ('harga motor baru dalam Dollar : ', ex_showroom_price)
    st.write ('Estimasi harga motor bekas dalam hanya Dollar : ', predict)
    st.write ('Estimasi harga motor bekas dalam IDR (Juta) :', predict*19000)