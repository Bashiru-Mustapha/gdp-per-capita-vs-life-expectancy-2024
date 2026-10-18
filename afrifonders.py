# Package and Data Import
import pandas as pd
GDP = pd.read_csv("GDP_Per_Capita.csv")
pop = pd.read_csv("Pop.csv")
life_exp = pd.read_csv("Life_expectancy.csv")
# Checking Data Informations
#print(GDP.info())
#print(pop.info())
#print(life_exp.info())


#Renaming Columns
df_GDP_pc = GDP.rename(columns={"2023":"GDP_2023",
                             "2024":"GDP_2024",
                            "2025":"GDP_2025",})
df_pop = pop.rename(columns={"2023":"Pop_2023",
                             "2024":"Pop_2024",
                             "2025":"Pop_2025",})
df_life_exp = life_exp.rename(columns={"2023":"Life_2023",
                                       "2024":"Life_2024",
                                       "2025":"Life_2025",})
#print(df_GDP_pc.head())
#print(df_pop.head())
#print(df_life_exp.head())

#Checking Dublicates
#print([df_GDP_pc.duplicated("iso3", keep=False)])
#print([df_pop.duplicated("iso3", keep=False)])
#print([df_life_exp.duplicated("iso3", keep=False)])

# Merging DataFrames
df_merged = pd.merge(df_GDP_pc, df_pop, on=["country_name", "iso3","continent"], how="outer", validate="one_to_one")
df_merged = pd.merge(df_merged, df_life_exp, on=["country_name", "iso3", "continent"], how="outer", validate="one_to_one")
#print(df_merged.head().to_string()) 



df = df_merged[["country_name", "iso3","continent", "GDP_2024", "Pop_2024", "Life_2024"]]
#print(df.to_string())
#print(df.shape)
df = df.dropna(subset=["continent", "GDP_2024", "Pop_2024", "Life_2024"])
#print("dataset shape:", df.shape)
#print("\nMissing values:")
#print(df.isna().sum())

#print("\nCountry_name by continent:")
#print(df["continent"].value_counts())

import matplotlib.pyplot as plt
import numpy as np

# Create a color map for continents
continent_colors = {'Africa': '#8B4789', 'America': '#5FD98B', 
                   'Asia': '#4FAFB3', 'Europe': '#F7A072', 'Oceania': '#D4AF37'}

# Select 2 countries from EACH continent
key_countries_list = []
for continent in df['continent'].unique():
    continent_df = df[df['continent'] == continent].nlargest(2, 'Pop_2024')
    key_countries_list.extend(continent_df['country_name'].tolist())

df_label = df[df['country_name'].isin(key_countries_list)].copy()

# Create scatter plot
fig, ax = plt.subplots(figsize=(20, 11))

# Plot all countries by continent
for continent in sorted(df['continent'].unique()):
    continent_data = df[df['continent'] == continent]
    ax.scatter(x = continent_data['GDP_2024'], 
                y = continent_data['Life_2024'], 
                s = np.array(continent_data['Pop_2024']) / 1000000 * 5,
                alpha = 0.6,
                label = continent,
                color = continent_colors.get(continent, 'gray'),
                edgecolors='none')

# Format and labels WITH YOUR NAME
ax.set_xlabel('GDP per Capita [in USD] - Log Scale', fontsize=13, fontweight='bold')
ax.set_ylabel('Life Expectancy [in years]', fontsize=13, fontweight='bold')
ax.set_title('GDP per Capita Vs Life Expectancy Analysis (2024) by Mustapha Bashiru', 
             fontsize=15, fontweight='bold', pad=20)

# Logarithmic scale
ax.set_xscale('log')
ax.set_xticks([500, 1000, 2000, 5000, 10000, 25000, 50000, 100000])
ax.set_xticklabels(['$500', '$1k', '$2k', '$5k', '$10k', '$25k', '$50k', '$100k'])

# Add country labels
for idx, row in df_label.iterrows():
    ax.text(row['GDP_2024'], row['Life_2024'] + 0.3, 
             row['country_name'], fontsize=10, fontweight='bold')

# Legend
ax.legend(title='Continent', loc='center left', 
          bbox_to_anchor=(1.02, 0.5), fontsize=12, 
          title_fontsize=13, frameon=True, fancybox=True, shadow=True)

ax.grid(True, alpha=0.3, which='both')
plt.subplots_adjust(left=0.08, right=0.85, top=0.95, bottom=0.1)

# Save
plt.savefig('GDP_per_Capita_VsLife_Expectancy_Analysis_2024_by_Mustapha_Bashiru.png', 
            dpi=300, bbox_inches='tight')

plt.show()
