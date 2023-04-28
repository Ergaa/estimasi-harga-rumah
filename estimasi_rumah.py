import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumah.sav', 'rb'))

st.title('Estimasi Harga Rumah')

#bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated
bedrooms = st.number_input('Input Kamar Tidur')
bathrooms = st.number_input('Input Kamar Mandi')
sqft_living = st.number_input('Input Luas Ruang Tamu')
sqft_lot = st.number_input('Input Luas Rumah ')
floors = st.number_input('Input Tingkat Rumah')
waterfront = st.number_input('Input Tepi Laut')
view = st.number_input('Input Pemandangan')
condition = st.number_input('Input Kondisi')
sqft_above = st.number_input('Input Luas lantai atas')
sqft_basement = st.number_input('Input Luas Ruang Bawah Tanah')
yr_built = st.number_input('Input Tahun Dibangun')
yr_renovated = st.number_input('Input Tahun Renovasi')

predict = ''

if st.button('Estimasikan'):
    predict = model.predict(
        [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated]]
    )
    st.write ('Estimasi Harga Rumah USD: ', predict, 'USD')
    st.write ('Estimasi Harga Rumah IDR : ', predict*14679,60, 'IDR')