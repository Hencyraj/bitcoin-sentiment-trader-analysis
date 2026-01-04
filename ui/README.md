# Bitcoin Market Sentiment vs Trader Performance Analysis

## Objective
The objective of this project is to analyze the relationship between Bitcoin market sentiment
(Fear and Greed) and trader performance using historical trading data.  
The goal is to uncover patterns in trader behavior and derive insights that can support
smarter trading strategies.

---

## Datasets Used

### 1. Bitcoin Market Sentiment Dataset
- Columns: Date, Classification (Fear / Greed)
- Represents overall market psychology for Bitcoin

### 2. Historical Trader Data (Hyperliquid)
- Columns include:
  - account
  - symbol
  - execution price
  - size
  - side
  - time
  - closedPnL
  - leverage
  - and other trade-related fields

---

## Approach

1. Loaded and inspected both datasets
2. Cleaned and preprocessed the data
   - Handled missing values
   - Converted timestamps to date format
3. Aligned sentiment and trader data by date
4. Merged both datasets for combined analysis
5. Performed Exploratory Data Analysis (EDA)
6. Compared trader performance under Fear and Greed market conditions
7. Generated summary statistics and visualizations
8. Extracted actionable insights from observed patterns

---

## Key Insights

- Trades executed during **Fear** market conditions show a **higher win rate** compared to Greed
- **Greed** markets exhibit higher risk-taking behavior
- **Contrarian strategies** tend to perform better during Fear periods
- Trader performance is strongly influenced by market psychology

---

## Output

- Cleaned and merged datasets
- Summary statistics saved as CSV files
- Visualizations illustrating sentiment vs performance
- All outputs are available in the `analysis_output/` folder

## Sample Visualizations

### Market Sentiment Distribution
![Market Sentiment Distribution](analysis_output/1_sentiment_distribution.png)

### PnL Distribution by Sentiment
![PnL Distribution](analysis_output/2_pnl_by_sentiment.png)

- A simple HTML UI is included for result visualization (optional)

---

## How to Run

Run the analysis using the following command:

```bash
python analysis.py
## Author
Hency Raj
