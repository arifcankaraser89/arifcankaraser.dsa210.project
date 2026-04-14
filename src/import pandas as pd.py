import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- WATCHES  ---
try:
    df_watches = pd.read_csv('saat_verileri_son.csv')
    df_watches = df_watches[df_watches['Name'] != 'Richard_Mille_RM011']

    avg_prices = df_watches.groupby('Name')['Value'].mean().sort_values()

    n = len(avg_prices)
    entry_watches = avg_prices.iloc[:n//3].index
    mid_watches = avg_prices.iloc[n//3:2*n//3].index
    luxury_watches = avg_prices.iloc[2*n//3:].index

    fig, axes = plt.subplots(3, 1, figsize=(12, 20))

    
    colors = plt.cm.tab20.colors 

    def plot_with_distinct_colors(ax, watch_list, title):
        
        for i, watch in enumerate(watch_list):
            data = df_watches[df_watches['Name'] == watch]
            
            color = colors[i % len(colors)] 
            ax.plot(data['Year'], data['Value'], label=watch.replace('_', ' '), 
                    marker='o', color=color, linewidth=2)
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_ylabel('Price (USD)')
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
        ax.grid(True, linestyle='--', alpha=0.7)

    plot_with_distinct_colors(axes[0], luxury_watches, 'Luxury Watches - Price Over Time')
    plot_with_distinct_colors(axes[1], mid_watches, 'Mid-Range Watches - Price Over Time')
    plot_with_distinct_colors(axes[2], entry_watches, 'Entry-Level Watches - Price Over Time')

    plt.tight_layout()
    plt.savefig('watches_plot.png', bbox_inches='tight')
    plt.show()

except FileNotFoundError:
    print("Error: 'saat_verileri_son.csv' file not found.")

# --- FINANCE  ---
try:
    df_finance = pd.read_csv('finance.csv')
    indicators = df_finance['Indicator_Name'].unique()

    plt.figure(figsize=(12, 8))

    
    finance_colors = plt.cm.get_cmap('Dark2', len(indicators))

    for i, ind in enumerate(indicators):
        data = df_finance[df_finance['Indicator_Name'] == ind]
        plt.plot(data['Year'], data['Value'], label=ind.replace('_', ' '), 
                 marker='s', color=finance_colors(i), linewidth=2)

    plt.title('Finance Indicators - Value Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Value (Log Scale)')
    plt.yscale('log')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True, which="both", ls="--", alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('finance_plot.png', bbox_inches='tight')
    plt.show()
    
except FileNotFoundError:
    print("Hata: 'finance.csv' dosyası bulunamadı.")