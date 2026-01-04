import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

print("="*80)
print("BITCOIN MARKET SENTIMENT VS TRADER PERFORMANCE ANALYSIS")
print("="*80)

# =============================================================================
# STEP 1: LOAD DATA
# =============================================================================
sentiment_df = pd.read_csv("bitcoin_sentiment.csv")
trader_df = pd.read_csv("trader_data.csv")

print("Sentiment data shape:", sentiment_df.shape)
print("Trader data shape:", trader_df.shape)

# =============================================================================
# STEP 2: CLEAN SENTIMENT DATA
# =============================================================================
sentiment_df = sentiment_df.rename(columns={
    "classification": "sentiment"
})

sentiment_df["date"] = pd.to_datetime(sentiment_df["date"], dayfirst=True)
sentiment_df["sentiment"] = sentiment_df["sentiment"].str.title()
sentiment_df = sentiment_df.drop_duplicates(subset=["date"])

print("Unique sentiment dates:", sentiment_df.shape[0])

# =============================================================================
# STEP 3: CLEAN TRADER DATA
# =============================================================================
trader_df.columns = trader_df.columns.str.lower().str.replace(" ", "_")

trader_df = trader_df.rename(columns={
    "closed_pnl": "closed_pnl",
    "size_usd": "trade_size",
    "execution_price": "execution_price",
    "start_position": "start_position",
    "timestamp_ist": "time"
})

trader_df["time"] = pd.to_datetime(trader_df["time"], errors="coerce")
trader_df["date"] = trader_df["time"].dt.date
trader_df["date"] = pd.to_datetime(trader_df["date"])

numeric_cols = ["closed_pnl", "trade_size", "execution_price", "start_position"]
for col in numeric_cols:
    trader_df[col] = pd.to_numeric(trader_df[col], errors="coerce")

trader_df = trader_df.dropna(subset=["date", "closed_pnl"])

print("Clean trader trades:", trader_df.shape[0])

# =============================================================================
# STEP 4: MERGE DATASETS
# =============================================================================
merged_df = trader_df.merge(
    sentiment_df[["date", "sentiment"]],
    on="date",
    how="left"
)

merged_df = merged_df.dropna(subset=["sentiment"])
print("Merged trades:", merged_df.shape[0])

# =============================================================================
# STEP 5: FEATURE ENGINEERING
# =============================================================================
merged_df["is_win"] = (merged_df["closed_pnl"] > 0).astype(int)

merged_df["side"] = merged_df["side"].str.lower()
merged_df["is_long"] = (merged_df["side"] == "buy").astype(int)
merged_df["is_short"] = (merged_df["side"] == "sell").astype(int)

# =============================================================================
# STEP 6: EDA VISUALS
# =============================================================================
import os
os.makedirs("analysis_output", exist_ok=True)

# Sentiment distribution
merged_df["sentiment"].value_counts().plot(kind="bar", color=["red","green","orange","blue","purple"])
plt.title("Market Sentiment Distribution")
plt.tight_layout()
plt.savefig("analysis_output/1_sentiment_distribution.png")
plt.close()

# PnL by sentiment
sns.boxplot(data=merged_df, x="sentiment", y="closed_pnl")
plt.axhline(0, color="black", linestyle="--")
plt.title("PnL Distribution by Sentiment")
plt.tight_layout()
plt.savefig("analysis_output/2_pnl_by_sentiment.png")
plt.close()

# Win rate
win_rate = merged_df.groupby("sentiment")["is_win"].mean() * 100
win_rate.plot(kind="bar", color="green")
plt.title("Win Rate by Sentiment")
plt.ylabel("Win Rate (%)")
plt.tight_layout()
plt.savefig("analysis_output/3_winrate.png")
plt.close()

# Trade size
merged_df.groupby("sentiment")["trade_size"].mean().plot(kind="bar")
plt.title("Average Trade Size (USD) by Sentiment")
plt.tight_layout()
plt.savefig("analysis_output/4_trade_size.png")
plt.close()

# Long vs Short
pd.crosstab(merged_df["sentiment"], merged_df["side"], normalize="index").plot(kind="bar")
plt.title("Long vs Short by Sentiment")
plt.tight_layout()
plt.savefig("analysis_output/5_long_short.png")
plt.close()

# =============================================================================
# STEP 7: STATISTICS
# =============================================================================
summary = merged_df.groupby("sentiment").agg({
    "closed_pnl": ["count", "mean", "median", "sum"],
    "is_win": "mean",
    "trade_size": "mean",
    "start_position": "mean"
}).round(2)

summary.to_csv("analysis_output/summary_statistics.csv")

merged_df.to_csv("analysis_output/merged_analysis_data.csv", index=False)

print("\nANALYSIS COMPLETE")
print("Files saved in analysis_output/")