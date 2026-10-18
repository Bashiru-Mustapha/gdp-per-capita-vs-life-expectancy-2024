# GDP per Capita vs Life Expectancy, 2024

Author: Mustapha Bashiru
Script: `afrifonders.py`

## Overview

A bubble scatter plot of GDP per capita against life expectancy for about 200 countries in 2024, built with Python. Bubble size shows population and colour shows continent. The analysis looks at where Nigeria sits compared with the rest of Africa and the world.

## Data

2024 data on life expectancy, population and GDP per capita from the World Bank Data Bank, as three CSV files:

- `GDP_Per_Capita.csv`
- `Pop.csv`
- `Life_expectancy.csv`

Each file has `country_name`, `iso3` and `continent` columns plus one column per year. The CSV files are not included in this repository. Place them in the same folder as the script before running it.

## Method

1. Import the three files and rename the year columns (GDP_2024, Pop_2024, Life_2024, and the same for 2023 and 2025).
2. Merge them on country_name, iso3 and continent with an outer join, validated one-to-one.
3. Keep six columns and drop every row with a missing continent, GDP per capita, population or life expectancy value for 2024.
4. Plot GDP per capita (log scale) against life expectancy. Bubble area is population in millions multiplied by 5. The two most populous countries on each continent are labelled.

Full detail is in [PROJECT_LOG.md](PROJECT_LOG.md).

![GDP per capita vs life expectancy, 2024. Bubble size shows population, colour shows continent.](life_expectancy_vs_gdp_percapita.png)

## Chart interpretation

Nigeria is not the giant of Africa. It is not a stronger economy than the other African countries in any way that matters. Total GDP means little without population, and Nigeria's GDP is large because its population is large. An economy is doing well when its people have a good quality of life, and GDP per capita is the indicator of that. Governments and economies exist for Pareto efficiency, the betterment of humanity. A bigger GDP or a bigger population without a good quality of life is worth nothing.

### What the chart shows

Nigeria has a GDP per capita of about \$1,100 and a life expectancy of about 55 years. Among countries at a similar income, that is the lowest life expectancy in the sample. Almost all African countries do better than Nigeria on life expectancy. Some have more than 75 years at about \$5,000 GDP per capita, while Nigeria is below 60 years at about \$1,100.

The purple countries are African. All of them are below 80 years of life expectancy, and almost all are below \$10,000 GDP per capita. The gap in quality of life between Africa and the other continents is wide.

In general, countries with a higher GDP per capita have a longer life expectancy. India has about \$2,600 and 72 years. China has about \$12,500 and 78 years. The United States has about \$85,000 and 79 years. Some small European countries have about \$100,000 and 84 years. In Oceania, Australia has about \$64,000 and 83 years.

The relationship is general, not exact. Russia (about \$14,000, 74 years) is below Brazil (about \$10,300, 76 years) and China, which have lower incomes. The United States is below Germany (about \$55,000, 81 years) and Australia, which also have lower incomes. Papua New Guinea (about \$2,900, 66 years) is below India and Ethiopia (about \$1,150, 68 years). Income helps, but it does not decide the outcome on its own.

### Population

Bubble size shows population. Nigeria has the biggest population among the African countries in the data, and the chart shows that a bigger population does not mean a bigger GDP per capita. China and India are the most populous countries in the world.

GDP per capita is GDP divided by population, so population affects it directly. If population grows faster than production, inflation and poverty rise, and quality of life falls. That holds here: the African countries with a higher GDP per capita than Nigeria have smaller populations, which is why their GDP per capita and life expectancy are higher.

### Conclusion

Nigeria is not the giant of Africa. Its quality of life is very low, its population is bigger than its resources, and that is why Nigerians are suffering.

## Limitations

- The data covers one year, so it shows association, not cause.
- GDP per capita is an average and does not show how income is shared.
- The population theory is not tested. Population appears only as bubble size.
- Some African countries are missing, so statements about Africa apply to the sample only.
- Only the two most populous countries per continent are labelled.
- Life expectancy is one measure of quality of life.

## Run it

```
pip install pandas numpy matplotlib
python afrifonders.py
```

The script saves the figure as `GDP_per_Capita_VsLife_Expectancy_Analysis_2024_by_Mustapha_Bashiru.png`. The copy in this repository is named `life_expectancy_vs_gdp_percapita.png`.

## Files

- `afrifonders.py`: the analysis script
- `life_expectancy_vs_gdp_percapita.png`: the chart
- `PROJECT_LOG.md`: data collection, cleaning, methodology, interpretation and next steps
