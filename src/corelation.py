import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Load Watch Data ---
df_watches = pd.read_csv('saat_verileri_son.csv')
df_watches = df_watches[df_watches['Name'] != 'Richard_Mille_RM011']

avg_prices = df_watches.groupby('Name')['Value'].mean().sort_values()
n = len(avg_prices)
entry_watches = avg_prices.iloc[:n//3].index
mid_watches = avg_prices.iloc[n//3:2*n//3].index
luxury_watches = avg_prices.iloc[2*n//3:].index

def assign_category(name):
    if name in luxury_watches: return 'Luxury'
    elif name in mid_watches: return 'Mid-Range'
    else: return 'Entry-Level'

df_watches['Category'] = df_watches['Name'].apply(assign_category)

# Get average price per category per year
watch_yearly = df_watches.groupby(['Year', 'Category'])['Value'].mean().unstack()
watch_yearly.columns = [f"Watch_{c}" for c in watch_yearly.columns]

# --- 2. Load Finance Data ---
df_finance = pd.read_csv('finance.csv')
finance_yearly = df_finance.pivot(index='Year', columns='Indicator_Name', values='Value')

# --- 3. Merge Data ---
merged_df = pd.concat([watch_yearly, finance_yearly], axis=1)

# --- 4. Calculate Correlation ---
corr_matrix = merged_df.corr()
watch_cols = watch_yearly.columns
finance_cols = finance_yearly.columns
cross_corr = corr_matrix.loc[watch_cols, finance_cols]

# --- 5. Plotting Heatmap ---
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.matshow(cross_corr, cmap='RdYlGn', vmin=-1, vmax=1)
fig.colorbar(cax)

ax.set_xticks(range(len(finance_cols)))
ax.set_yticks(range(len(watch_cols)))
ax.set_xticklabels([c.replace('_', ' ') for c in finance_cols], rotation=45, ha='right')
ax.set_yticklabels([c.replace('_', ' ') for c in watch_cols])
ax.xaxis.set_ticks_position('bottom')

for i in range(len(watch_cols)):
    for j in range(len(finance_cols)):
        val = cross_corr.iloc[i, j]
        color = 'white' if abs(val) > 0.6 else 'black'
        ax.text(j, i, f"{val:.2f}", ha='center', va='center', color=color)

plt.title('Korelasyon Analizi: Saat Fiyatları ve Finans Göstergeleri', pad=20)

plt.tight_layout()
plt.savefig('correlation_heatmap.png', bbox_inches='tight')
plt.close()


print(cross_corr)