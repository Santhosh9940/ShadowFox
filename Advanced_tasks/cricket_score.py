import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

file_path = "C:\\Users\\Santhosh\\Documents\\ShadowFox\\Advanced_tasks\\IPL sample data.xlsx - Sheet1.csv"
df_raw = pd.read_csv(file_path)

start_index = df_raw[df_raw.iloc[:, 1] == "Match No."].index[0] + 1
df = df_raw.iloc[start_index:].reset_index(drop=True)
df.columns = df_raw.iloc[start_index - 1]
df.dropna(how='all', inplace=True)

pick_counts = df['Pick'].value_counts(dropna=False)
pick_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Pick Outcomes')
plt.xlabel('Pick')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

top_pickers = df[df['Pick'] == 'Y']['Player Name'].value_counts().head(10)
top_pickers.plot(kind='bar', color='green')
plt.title('Top 10 Fielders with Most Successful Picks')
plt.xlabel('Player Name')
plt.ylabel('Number of Picks')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

throw_counts = df['Throw'].value_counts(dropna=False)
throw_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Throw Outcome Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

venue_counts = df['Stadium'].value_counts().head(10)
venue_counts.plot(kind='barh', color='coral')
plt.title('Top Stadiums by Fielding Events')
plt.xlabel('Event Count')
plt.ylabel('Stadium')
plt.tight_layout()
plt.show()

