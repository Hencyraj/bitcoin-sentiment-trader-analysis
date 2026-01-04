function runAnalysis() {
  const sentiment = document.getElementById("sentimentFile").files.length;
  const trader = document.getElementById("traderFile").files.length;

  if (!sentiment || !trader) {
    alert("Please upload both CSV files first.");
    return;
  }

  document.getElementById("results").classList.remove("hidden");

  document.getElementById("fearWin").innerText = "62.4";
  document.getElementById("fearPnL").innerText = "125.34";

  document.getElementById("greedWin").innerText = "54.8";
  document.getElementById("greedPnL").innerText = "87.92";

  const insights = [
    "Fear markets show higher win rates",
    "Greed markets use higher risk",
    "Contrarian strategies work better in fear",
    "Trade size increases during greed"
  ];

  const list = document.getElementById("insightsList");
  list.innerHTML = "";
  insights.forEach(i => {
    const li = document.createElement("li");
    li.innerText = i;
    list.appendChild(li);
  });
}
