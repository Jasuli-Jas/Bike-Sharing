import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_season_effect_df(df):
    season_effect_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_effect_df


day_df = pd.read_csv("day.csv")
day_df.head()

day_df['season'] = day_df['season'].map({
    1: 'Spring/Semi', 2: 'Summer/Panas', 3: 'Fall/Gugur', 4: 'Winter/Dingin'
})

season_effect_df = create_season_effect_df(day_df)

month_map = {1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni',
             7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'}

# Grouping data and mapping month names
monthly_data = day_df.groupby('mnth')['cnt'].mean().reset_index()
monthly_data['month_name'] = monthly_data['mnth'].map(month_map)


st.header('Bike Sharing Dataset :bike:')

st.subheader("Total Bike Sharing")
st.title('Total Bike Sharing per Season')
st.write('This is a bar chart showing the total bike rentals for each season.')

# Create the plot
plt.figure(figsize=(12, 5))
ax = sns.barplot(x='season', y='cnt', data=day_df, palette='coolwarm')

# Customize the plot
plt.title('Total Bike Sharing', fontsize=16, fontweight='bold')
plt.xlabel('Seasons', fontsize=12)
plt.ylabel('Total Rental', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)


# Streamlit header
st.title("Tren Bulanan Penyewaan Sepeda dalam Setahun")
st.write("This plot shows the average bicycle rental trends per month.")

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(x='month_name', y='cnt', data=monthly_data, marker='o', linewidth=2, markersize=8, ax=ax)
ax.set_title('Tren Bulanan Penyewaan Sepeda', fontsize=16, fontweight='bold')
ax.set_xlabel('Bulan', fontsize=12)
ax.set_ylabel('Rata-rata Rental', fontsize=12)
ax.tick_params(axis='x', labelsize=10, rotation=45)
ax.tick_params(axis='y', labelsize=10)

# Show the plot in Streamlit
st.pyplot(fig)


st.title("Filter Interaktif Pengaruh Musim Terhadap Penyewaan Sepeda")

# Membuat pilihan dropdown untuk memilih musim
season_selected = st.selectbox(
    "Pilih Musim:",
    options=['Semua Musim', 'Spring/Semi', 'Summer/Panas', 'Fall/Gugur', 'Winter/Dingin']
)

# Filter data berdasarkan pilihan musim
if season_selected != 'Semua Musim':
    filtered_data = day_df[day_df['season'] == season_selected]
else:
    filtered_data = day_df

# Menampilkan grafik penyewaan sepeda berdasarkan musim
plt.figure(figsize=(8,5))
ax = sns.barplot(x='season', y='cnt', data=filtered_data, palette='coolwarm')
plt.title(f'Total Penyewaan Sepeda pada Musim: {season_selected}', fontsize=16, fontweight='bold')
plt.xlabel('Musim', fontsize=12)
plt.ylabel('Total Penyewaan', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()

# Menampilkan grafik di Streamlit
st.pyplot(plt)

