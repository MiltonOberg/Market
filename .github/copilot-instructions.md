# AI Agent Instructions for Market Project

## Project Overview
This is a stock market analysis and prediction application built with Python, using Streamlit for the frontend and machine learning models for predictions.

## Architecture
The project follows a clear component-based architecture:
- `frontend/`: Streamlit-based UI components
  - `dashboard.py`: Main application entry point
  - `ui/`: UI component implementations
- `backend/`: Core business logic and ML components
  - `components/`: Stock data handling
  - `features/`: ML model implementations and predictions
- `utils/`: Shared utilities and constants
- `arc/`: Jupyter notebooks for analysis and testing
- `test/`: Testing notebooks and components

## Key Workflows

### Development Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python run_dashboard.py
```

### Component Patterns

#### Frontend Components
- UI components are organized in `frontend/ui/`
- Each component follows the pattern of initialization and display methods (e.g., `show_table()`, `show_graph()`)
- Streamlit components are used for user input and visualization

#### Backend Components
- Stock data handling in `backend/components/stock.py`
- ML model implementation in `backend/features/agent.py`
- Prediction logic in `backend/features/predict_stock.py`

### Integration Points
1. Stock Data Flow:
   - User input → `Stock` class → Data fetching → Processing
   - `PredictStock` class integrates stock data with ML model
2. UI Integration:
   - `StockAnalysis` class handles visualization of both historical and predicted data

### Project-Specific Conventions
1. Class Structure:
   - Components accept either direct data or configuration in constructors
   - Example: `PredictStock(choice: str = None, stock: Stock = None)`

2. Data Visualization:
   - Stock data visualization is handled through the `StockAnalysis` class
   - Graphs and tables are standard display components

## Common Tasks
- Adding new stock analysis features: Extend `StockAnalysis` class
- Implementing new predictions: Create new methods in `PredictStock`
- Adding UI components: Follow the pattern in `frontend/ui/components/`