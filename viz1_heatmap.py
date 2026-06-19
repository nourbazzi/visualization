"""
TTC Subway Delay Heatmap 2024
Produces a seaborn heatmap of average delay duration (minutes) by
day of week x hour of day, using TTC Subway Delay Data 2024.

Input files (in the same directory as this script):
  - ttc-subway-delay-data-2024.xlsx   (City of Toronto Open Data; https://open.toronto.ca/dataset/ttc-subway-delay-data/)
  - Code Descriptions.json        (incident code lookup, same source)

Output:
  - viz1_heatmap.png

Usage:
  python viz1_heatmap.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns


DATA_FILE   = "ttc-subway-delay-data-2024.xlsx"
OUTPUT_FILE = "viz1_heatmap.png"

# Ordered days so heatmap rows run Mon to Sun
DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]

PALETTE = "viridis" #colorblind-friendly

# Cap colour scale to reveal most relevant variation.
# Friday 04h is a statistical outlier (avg 77 min).
VMAX = 20

# Load data from Excel
df = pd.read_excel(DATA_FILE, sheet_name="Subway")

# Filter: keep only rows with a measurable delay
df = df[df["Min Delay"] > 0].copy()

# Parse hour from time string (format "HH:MM")
df["Hour"] = df["Time"].str[:2].astype(int)

# Enforce ordered day-of-week categories for correct heatmap row order
df["Day"] = pd.Categorical(df["Day"], categories=DAY_ORDER, ordered=True)

# Build pivot: mean delay by Day × Hour
pivot = (
    df.groupby(["Day", "Hour"])["Min Delay"]
    .mean()
    .unstack(level="Hour")     # columns = hours 0-23
    .reindex(DAY_ORDER)        # rows = Mon-Sun
    .fillna(0)                 # hours with no events as dark purple
)

# Build figure
fig, ax = plt.subplots(figsize=(16, 5))

sns.heatmap(
    pivot,
    ax=ax,
    cmap=PALETTE,
    linewidths=0.3,
    linecolor="white",
    annot=False,                # individual values will create clutter
    vmin=0,
    vmax=VMAX,
    cbar_kws={
        "label": "Avg delay (min)",
        "shrink": 0.85,
        "pad": 0.02,
    },
)

# Labels & title
# Title states the insight and not just the axes
ax.set_title(
    "TTC subway delays are relatively consistent throughout the day - 2024\n",
    fontsize=13, fontweight="bold", pad=14,
)
ax.set_xlabel("Hour of day", fontsize=11, labelpad=8)
ax.set_ylabel("")

# Show every other hour to reduce clutter (data-ink ratio)
hour_labels = [str(h) if h % 2 == 0 else "" for h in pivot.columns]
ax.set_xticklabels(hour_labels, fontsize=9, rotation=0)
ax.set_yticklabels(pivot.index, fontsize=10, rotation=0)

# Caption 
fig.text(
    0.01, -0.07,
    "Source: City of Toronto Open Data; TTC Subway Delay Data 2024 ;"
    "Note that the colour scale was capped at 20 min; Friday 04h outlier (avg 77 min) excluded from scale; "
    "Palette: viridis (colorblind-safe)",
    fontsize=7.5, color="#555555",
)

plt.tight_layout()
plt.savefig(OUTPUT_FILE, dpi=180, bbox_inches="tight")
print(f"Saved > {OUTPUT_FILE}")
