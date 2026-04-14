import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import patheffects


sns.set_theme(style="whitegrid")

try:
    # --- 1. DATA PREPARATION ---
    df_watches = pd.read_csv('saat_verileri_son.csv')
    df_watches = df_watches[df_watches['Name'] != 'Richard_Mille_RM011']

    # Classify Watches
    avg_prices = df_watches.groupby('Name')['Value'].mean().sort_values()
    n = len(avg_prices)
    luxury_watches = avg_prices.iloc[2*n//3:].index
    mid_watches = avg_prices.iloc[n//3:2*n//3].index
    
    def assign_category(name):
        if name in luxury_watches: return 'Luxury'
        elif name in mid_watches: return 'Mid-Range'
        return 'Entry-Level'

    df_watches['Category'] = df_watches['Name'].apply(assign_category)

    # Calculate Cumulative Growth (% Change since 2005)
    def calc_pct_change(group):
        base_val = group.loc[group['Year'] == 2005, 'Value'].values
        if len(base_val) > 0:
            group['Pct_Increase'] = ((group['Value'] - base_val[0]) / base_val[0]) * 100
        else:
            group['Pct_Increase'] = 0.0
        return group

    df_watches_pct = df_watches.sort_values(['Name', 'Year']).groupby('Name', group_keys=False).apply(calc_pct_change)
    avg_watch_pct = df_watches_pct.groupby(['Category', 'Year'])['Pct_Increase'].mean().reset_index()

    # Finance Data
    df_finance = pd.read_csv('finance.csv')
    df_finance_pct = df_finance.sort_values(['Indicator_Name', 'Year']).groupby('Indicator_Name', group_keys=False).apply(calc_pct_change)

    # --- 2. SINGLE COMPREHENSIVE PLOT ---
    plt.figure(figsize=(16, 10))
    ax = plt.gca()

    # Watch Colors (Premium Palette)
    watch_colors = {'Luxury': '#D4AF37', 'Mid-Range': '#2C3E50', 'Entry-Level': '#7F8C8D'}
    
    # A. Plot Finance Indicators (Clear Background)
    fin_indicators = df_finance_pct['Indicator_Name'].unique()
    fin_palette = sns.color_palette("husl", len(fin_indicators))
    
    for i, ind in enumerate(fin_indicators):
        data = df_finance_pct[df_finance_pct['Indicator_Name'] == ind]
        plt.plot(data['Year'], data['Pct_Increase'], 
                label=ind.replace('_', ' '), 
                linestyle='--', linewidth=2, alpha=0.5, color=fin_palette[i])

    # B. Plot Watch Categories (Main Highlights)
    for cat in ['Luxury', 'Mid-Range', 'Entry-Level']:
        data = avg_watch_pct[avg_watch_pct['Category'] == cat]
        
        # Calculate CAGR for the legend (Compound Annual Growth Rate)
        start_val = 100 # Base is 100%
        end_val = 100 + data['Pct_Increase'].iloc[-1]
        years = data['Year'].max() - data['Year'].min()
        cagr = ((end_val / start_val) ** (1/years) - 1) * 100
        
        line, = plt.plot(data['Year'], data['Pct_Increase'], 
                        label=f'WATCH: {cat} (CAGR: {cagr:.1f}%)', 
                        linewidth=5.5, color=watch_colors[cat], zorder=10)
        
        # Glow/Outline Effect
        line.set_path_effects([patheffects.withStroke(linewidth=8, foreground='white', alpha=0.7)])

    # C. Vertical Annotations (Key Events)
    plt.axvline(x=2020, color='#8B0000', linestyle=':', linewidth=1.5, alpha=0.6)
    plt.text(2020.2, ax.get_ylim()[1]*0.9, 'COVID-19 Pandemic Impact', color='#8B0000', fontweight='bold')

    # D. Aesthetics & Final Touches
    plt.title('20-Year Investment Performance: Luxury Watches vs. Financial Assets', fontsize=20, fontweight='bold', pad=25)
    plt.ylabel('Cumulative Growth Since 2005 (%)', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    
    # Format Y-axis
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: f'%{int(x):,}'))
    
    # Customizing Legend
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=11, frameon=True, shadow=True)
    
    # Add a horizontal base line
    plt.axhline(0, color='black', linewidth=1.2, alpha=0.5)

    sns.despine()
    plt.tight_layout()
    plt.savefig('full_market_analysis_2005_2026.png', dpi=300, bbox_inches='tight')
    plt.show()

except Exception as e:
    print(f"Error: {e}")