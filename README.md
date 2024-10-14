# 🎃 Halloween Candy Dashboard

## Overview

The Halloween Candy Dashboard is an interactive web application designed to help users select the perfect assortment of candies for Halloween trick-or-treaters. Using data-driven analysis of 85 candy types, this dashboard provides insights into candy popularity, nutritional content, and price points to assist in making informed decisions for Halloween candy selection.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Analysis Methodology](#analysis-methodology)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


**Live Demo:** [Halloween Candy Dashboard](https://halloween-candy-rankings.streamlit.app/)

**Detailed Analysis:** [Candy Analysis Page](https://halloween-candy-rankings-analysis.netlify.app/)

## Features

1. **Top Recommendations:**
   - Displays the top 3 recommended candies based on comprehensive data analysis.
   - Provides detailed information on each candy, including characteristics, win percentage, sugar content, and price.
   - Offers a radar chart visualization comparing the attributes of recommended candies.

2. **Custom Selection:**
   - Allows users to filter candies based on various characteristics (e.g., chocolate, fruity, nut-free).
   - Provides sliders to adjust sugar and price ranges.
   - Enables users to select up to 3 candies for their personalized Halloween assortment.

3. **Analysis of User Selection:**
   - Calculates and displays average metrics (win rate, sugar content, price) for user-selected candies.
   - Compares user selection to overall candy averages.
   - Generates a radar chart for visual comparison of selected candies.
   - Provides tailored analysis and recommendations based on the user's selection.

4. **Interactive Visualizations:**
   - Utilizes Plotly for creating interactive charts and graphs.
   - Implements a responsive design for optimal viewing on various devices.

5. **Themed UI:**
   - Features a Halloween-themed color scheme and design elements.
   - Uses custom CSS for an engaging and festive user experience.

## Data Source

This project uses data from the [Maven Halloween Challenge](https://mavenanalytics.io/challenges/maven-halloween-challenge/701f06a2-a19b-41e9-95d3-37a0dcc5492f). The dataset includes information on 85 candy types, with attributes such as sugar content, price, and various characteristics.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- HTML/CSS

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/halloween-candy-dashboard.git
   cd halloween-candy-dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1. **Viewing Top Recommendations:**
   - Navigate to the "Top Recommendations" tab to see the top 3 recommended candies.
   - Click on the "Why We Recommend" popover for each candy to understand the reasoning behind the recommendation.

2. **Creating a Custom Selection:**
   - Go to the "Custom Selection" tab.
   - Use the checkboxes to select desired candy characteristics.
   - Adjust the sugar and price range sliders as needed.
   - Choose up to 3 candies from the filtered list.

3. **Analyzing Your Selection:**
   - After selecting your candies, scroll down to view the analysis.
   - Check the radar chart to compare your selected candies.
   - Read the provided analysis for insights on your selection's win rate, sugar content, and price.

4. **Exploring Additional Information:**
   - Click on the "Dive into Our Analysis" button for more detailed candy analysis.
   - Refer to the sidebar for information about the project and contact details.

## Project Structure

```
halloween-candy-dashboard/
│
├── app.py                 # Main Streamlit application
├── data/
│   └── candy-data.csv     # Dataset containing candy information
├── analysis.html          # Detailed analysis page
├── analysis.ipynb         # Detailed analysis Notebook
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Analysis Methodology

The candy recommendations and analysis are based on several factors:

1. **Win Percentage:** Derived from head-to-head matchups between candies.
2. **Sugar Content:** Analyzed relative to other candies in the dataset.
3. **Price:** Considered to balance quality with affordability.
4. **Variety:** Ensuring a mix of different candy types (chocolate, fruity, etc.).
5. **Allergen Considerations:** Noting candies containing common allergens like nuts.

The final recommendations aim to provide a balanced selection that appeals to a wide range of preferences while considering nutritional and cost factors.

## Contributing

Contributions to improve the Halloween Candy Dashboard are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

Santanu Jha
- LinkedIn: [Santanu Jha](https://www.linkedin.com/in/santanu-jha-845510292/)
- GitHub: [jhasantanu9](https://github.com/jhasantanu9)
- Portfolio: [santanujha.netlify.app](https://santanujha.netlify.app/)

For any questions or feedback, please feel free to reach out!
