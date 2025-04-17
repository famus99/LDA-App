# Customer Analysis Tool

## Overview
The Customer Analysis Tool is a Flask-based web application for analysing customer purchasing behaviour and categorising customers based on their activity patterns. It uses Latent Dirichlet Allocation (LDA) for topic modelling to identify distinct customer segments based on temporal purchasing patterns.

## Features
- **File Upload**: Upload CSV files containing customer purchase data
- **Variable Selection**: Select which columns to use for analysis
- **Timeframe Selection**: Analyse data by hours, days, weeks, months, or years
- **Customer Categorisation**: Group customers into categories based on purchasing patterns
- **Results Export**: Export categorised customer data to CSV

## Technical Stack
- **Flask**: Web framework for the application
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms including LDA
- **Flask-WTF**: Form handling and validation
- **Matplotlib**: Data visualization

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/customer-analysis-tool.git
   cd customer-analysis-tool
   ```

2. Create and activate a virtual environment (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

4. Create a static/files directory for file uploads
   ```bash
   mkdir -p static/files
   ```

## Usage

1. Start the Flask application
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5001`

3. Follow the workflow:
   - Start at the home page and review instructions
   - Upload your CSV file on the Submit page
   - Select your variables (customer ID, time, count) and analysis parameters
   - View the results on the Output page

## File Format Requirements

The application expects a CSV file with at least these columns:
- A customer identifier column (e.g., `customer_id`)
- A time/date column (e.g., `order_date`)
- A count or value column for analysis (e.g., `quantity` or `amount`)

Example CSV format:
```
customer_id,order_date,product_id,quantity
1001,2023-01-15 14:30:00,P100,2
1002,2023-01-16 09:45:00,P101,1
1001,2023-01-17 16:20:00,P102,3
```

## Application Workflow

1. **Home Page**: Starting point with navigation options
2. **Instructions Page**: Detailed instructions on how to use the tool
3. **Submit Page**: Upload your CSV file
4. **Variable Selection**: Choose the relevant columns and analysis parameters
5. **Output Page**: View the analysis results and download the categorised customer data

## Analysis Method

The application uses Latent Dirichlet Allocation (LDA) for customer categorisation:

1. The uploaded data is transformed into a pivot table with customers as rows and time periods as columns
2. The data is aggregated according to the selected timeframe (hours, days, weeks, months, years)
3. LDA is applied to identify patterns in customer purchasing behaviour
4. Each customer is assigned to the category where they have the highest probability of belonging

## Output

The application generates a CSV file with two columns:
- Customer ID
- Assigned category number

This output can be used for targeted marketing, customer segmentation, or further analysis.

## Troubleshooting

- **File Upload Issues**: Ensure your CSV file is properly formatted and not too large
- **Processing Errors**: Check that your data contains the columns you select for analysis
- **Empty Results**: Verify that your data contains sufficient information for categorisation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Flask documentation
- Scikit-learn documentation
- Pandas documentation
