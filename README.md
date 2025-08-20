# PriceWise – AI-Powered Dynamic Pricing Engine

A smart pricing simulator that uses machine learning to recommend revenue-maximizing prices in real time. Inspired by how Amazon, Uber, and airlines dynamically price based on demand, competition, and customer behavior.

#### NOTE: A simulated dataset was used for this project.

## Demo Features
- Predict demand using market and behavioral inputs
- Run simulations to identify optimal pricing points
- Visualize price vs. demand and revenue curves
- Built using Python, scikit-learn, and Streamlit

## Input Factors
- Base Price
- Competitor Price
- Inventory
- User Type (e.g., price-sensitive, brand-loyal)
- Weather Condition
- Day of Week

## ML Techniques Used
- Linear Regression
- Feature engineering with One-Hot Encoding
- Model performance:  
  - R² = 0.701  
  - MAE ≈ 8.75  
  - RMSE ≈ 11.12

## Sample Result
Optimal Price: `$175.00`  
Expected Demand: `49 units`  
Projected Revenue: `$8,575.00`

## Future Enhancements
- Add Reinforcement Learning for multi-day strategy
- Use real-time weather/price APIs
- Support for multi-product pricing optimization

## Tech Stack
- Python
- scikit-learn
- Streamlit
- pandas, seaborn, matplotlib

## 📁 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.

