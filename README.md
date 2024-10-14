# Halloween Candy Selection Dashboard 🎃🍬

## Challenge Objective
This project is part of the **Maven Halloween Challenge**. The goal is to take a data-driven approach to become the most popular trick-or-treating house on the block. Using online votes ranking 85 types of candy, we've created a dashboard to help you **find the 3 treats to give out on Halloween that will guarantee trick-or-treaters of all tastes find something they'll love**.

## Project Overview
This Streamlit application provides an interactive dashboard for selecting the perfect Halloween candy assortment. It offers two main features:

1. **Top Recommendations**: Our data-driven top 3 candy recommendations with detailed analysis.
2. **Custom Selection**: An interactive tool to create your own Halloween candy mix based on various criteria.

## Data-Driven Approach
Our analysis, detailed in `analysis.ipynb`, follows a rigorous data-driven methodology to select the optimal candy assortment:

1. **Data Exploration**: We began by examining the distribution of key variables such as win percentage, sugar content, and price across all candies.

2. **Feature Engineering**: We created composite scores combining popularity (win percentage) with other factors like sugar content and price to identify well-rounded candidates.

3. **Correlation Analysis**: We investigated relationships between various candy attributes to understand what makes a candy popular.

4. **Optimization**: We used a weighted scoring system to balance popularity, nutritional concerns (sugar content), and cost-effectiveness.

5. **Validation**: Our selections were cross-validated against different subsets of the data to ensure robustness.

Key insights from our analysis:

- Chocolate-based candies generally have higher win percentages.
- There's a sweet spot for sugar content – too little or too much correlates with lower popularity.
- Price doesn't strongly correlate with popularity, allowing for cost-effective choices.
- Diversity in texture and flavor profiles (e.g., fruity vs. chocolate) increases the likelihood of satisfying varied preferences.

These insights directly inform both our top recommendations and the custom selection tool in the dashboard.

## Features
- Data visualization of candy characteristics
- Interactive selection of candy based on ingredients, sugar content, and price
- Analysis of selected candy assortment
- Comparison with overall averages
- Accessibility considerations for screen readers

## Installation

### Prerequisites
- Python 3.7+
- pip

### Steps
1. Clone this repository:
   ```
   git clone https://github.com/your-username/halloween-candy-dashboard.git
   cd halloween-candy-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the Streamlit app:

```
streamlit run app.py
```

Navigate to the URL provided in the terminal (usually `http://localhost:8501`).

For a deep dive into the analysis:
1. Open `analysis.ipynb` in Jupyter Notebook or JupyterLab.
2. Run all cells to see the full analytical process and visualizations.

## Data Source
The candy data used in this project is from the [Maven Halloween Challenge](https://mavenanalytics.io/challenges/maven-halloween-challenge/701f06a2-a19b-41e9-95d3-37a0dcc5492f).

## Project Structure
- `app.py`: Main Streamlit application
- `analysis.ipynb`: Jupyter notebook containing detailed data analysis
- `data/candy-data.csv`: Dataset containing candy information
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Contributing
Contributions to improve the dashboard or extend the analysis are welcome. Please feel free to submit a Pull Request.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
- LinkedIn: [Santanu Jha](https://www.linkedin.com/in/santanu-jha-845510292/)
- GitHub: [jhasantanu9](https://github.com/jhasantanu9)
- Portfolio: [santanujha.netlify.app](https://santanujha.netlify.app/)

## Acknowledgments
- Maven Analytics for providing the challenge and dataset
- Streamlit for the amazing framework
- All contributors and users of this dashboard

Happy Halloween! 🎃👻
