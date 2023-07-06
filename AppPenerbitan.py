import streamlit as st

st.title(' Biaya Terbit Buku BIESTA MEDIA')

kertas = 250   #Kertas Hvs/halaman
cover = 13000  #Soft cover

jml_hal = st.number_input('Jumlah Halaman',0)
jml_eks = st.number_input('Jumlah Eksemplar',0)
ongkir = st.number_input('Jumlah Ongkir',0)
hitung = st.button('Hitung Biaya Terbit')

if hitung:
    biayaTerbit = ((kertas*jml_hal+cover)*jml_eks+ongkir)*2
    buku = format(biayaTerbit,',')
    st.success(f'Biaya Terbit Buku Adalah = Rp  {buku}')