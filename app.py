import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Halloween Candy Dashboard", layout="wide")

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv('data/candy-data.csv')
    return data

candy_data = load_data()

# Custom CSS for Halloween theme with improved readability
st.markdown("""
<style>
    .stApp {
        background-color: #F8F0E3;
        color: #333333;
    }
    h1, h2, h3, h4, h5 {
        color: #D35400;
        font-family: 'Arial', sans-serif;
    }
    .stPlotlyChart {
        background-color: #FFFFFF;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #D35400;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        color: #333333;
    }
    .stSelectbox>div>div>select {
        color: #333333;
    }
    .stMultiSelect>div>div>select {
        color: #333333;
    }
    .candy-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border: 2px solid #D35400;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height:370px;
    }
    .section-divider {
        border-top: 2px solid #D35400;
        margin: 30px 0;
    }
    .metric-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid #D35400;
    }
    .sidebar-info {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
        border: 1px solid #D35400;
    }
</style>
""", unsafe_allow_html=True)

# Add a spooky title
st.markdown("<h1 style='text-align:center;  font-size:36px; color: #D35400;'>🎃 Halloween Candy Selection Dashboard 🍬</h1>", unsafe_allow_html=True)

# Main content area
tab1, tab2 = st.tabs(["🍫 Top Recommendations", "🎃 Custom Selection"])

with tab1:
    st.markdown("<h2 style='text-align: center; font-size:30px; color: #D35400;'>Our Top 3 Candy Recommendations</h2>", unsafe_allow_html=True)
    
    # Our top 3 candy selection based on analysis
    selected_candies = ["Reese's Peanut Butter cup", "Twix", "Starburst"]
    selected_data = candy_data[candy_data['competitorname'].isin(selected_candies)]
    
    # Create columns for each candy
    cols = st.columns(3)
    
    for i, candy in enumerate(selected_candies):
        candy_data_item = selected_data[selected_data['competitorname'] == candy].iloc[0]
        characteristics = [
            "Chocolate" if candy_data_item['chocolate'] else None,
            "Fruity" if candy_data_item['fruity'] else None,
            "Caramel" if candy_data_item['caramel'] else None,
            "Peanuts/Almonds" if candy_data_item['peanutyalmondy'] else None,
            "Nougat" if candy_data_item['nougat'] else None,
            "Crispy/Wafer" if candy_data_item['crispedricewafer'] else None,
            "Hard" if candy_data_item['hard'] else None,
            "Bar" if candy_data_item['bar'] else None,
            "Pluribus" if candy_data_item['pluribus'] else None
        ]
        characteristics = [c for c in characteristics if c]
        characteristics_str = ", ".join(characteristics)
        
        with cols[i]:
            with st.container():
                st.markdown(f"""
                <div class="candy-card">
                    <p style=" font-size:18px; text-align: center; color: #D35400;"><strong>{candy}</strong></p>
                    <hr style="border-top: 1px solid #D35400;">
                    <p><strong>Characteristics:</strong> {characteristics_str}</p>
                    <p><strong>Win Percentage:</strong> {candy_data_item['winpercent']:.2f}%</p>
                    <p><strong>Sugar Percentile:</strong> {candy_data_item['sugarpercent']*100:.2f}th</p>
                    <p><strong>Price Percentile:</strong> {candy_data_item['pricepercent']*100:.2f}th</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Create a popover for each candy
                with st.popover("🍬 Why We Recommend", use_container_width = True):
                    st.write(f"#### Why We Recommend {candy}")
                    if candy == "Reese's Peanut Butter cup":
                        st.write("""
                        Reese's Peanut Butter cup stands out for several reasons:
                        1. Highest win percentage among all candies, indicating wide appeal.
                        2. Unique combination of chocolate and peanut butter, offering a distinctive flavor profile.
                        3. Recognizable brand with strong consumer loyalty.
                        4. Satisfying texture combination of smooth chocolate and creamy peanut butter.
                        5. Versatile size options, suitable for various treat-giving scenarios.
                        """)
                    elif candy == "Twix":
                        st.write("""
                        Twix is an excellent choice for these reasons:
                        1. High win percentage, showing strong popularity among consumers.
                        2. Unique texture combination of chocolate, caramel, and cookie.
                        3. Nut-free, making it suitable for those with nut allergies.
                        4. Comes in a bar form, which is easy to distribute and portion.
                        5. Offers a satisfying crunch, which many candy consumers enjoy.
                        """)
                    else:  # Starburst
                        st.write("""
                        Starburst rounds out our selection for these reasons:
                        1. Provides a fruity option, catering to non-chocolate preferences.
                        2. High win percentage among fruit-flavored candies.
                        3. Offers variety with multiple flavors in each pack.
                        4. Chewy texture provides a different experience from chocolate bars.
                        5. Individually wrapped pieces make for easy distribution and portion control.
                        """)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; font-size: 28px;'>🔮 Analysis of Recommendations</h3>", unsafe_allow_html=True)
    
    
    # Calculate average values for recommended candies
    avg_rec_win = candy_data_item['winpercent'].mean()
    avg_rec_sugar = candy_data_item['sugarpercent'].mean() * 100
    avg_rec_price = candy_data_item['pricepercent'].mean() * 100

    # Compare with overall averages
    overall_avg_win = candy_data['winpercent'].mean()
    overall_avg_sugar = candy_data['sugarpercent'].mean() * 100
    overall_avg_price = candy_data['pricepercent'].mean() * 100

    # Create three columns for the metrics
    col1, col2, col3 = st.columns(3)

    # Display metrics in the first column
    with col1:
        # Create sub-columns for Win Rate
        subcol1, subcol2 = st.columns(2)

        with subcol1:
            st.markdown("<h4 style='padding-top:40px; font-size:16px; font-weight:bold;'>Win Rate</h4>", unsafe_allow_html=True)

        with subcol2:
            st.metric(label="", value=f"{avg_rec_win:.2f}%", delta=f"{avg_rec_win - overall_avg_win:.2f}%")        

        st.markdown(
            "*Our selected candies have a significantly higher win rate, outperforming others by 16.72%. "
            "This suggests they are highly popular and well-received in head-to-head matchups.*"
        )        

    # Display metrics in the second column
    with col2:
        # Create sub-columns for Price Percentile
        subcol1, subcol2 = st.columns(2)

        with subcol1:
            st.markdown("<h4 style='padding-top:40px; font-size:16px; font-weight:bold;'>Price Percentile</h4>", unsafe_allow_html=True)

        with subcol2:
            st.metric(label="", value=f"{avg_rec_price:.2f}", delta=f"{avg_rec_price - overall_avg_price:.2f}")

        st.markdown(
            "*Our selection includes both higher and lower-priced options, offering a balanced assortment "
            "that's still 24.89% below average, making it affordable overall.*"
        )

    # Display metrics in the third column
    with col3:
        # Create sub-columns for Sugar Percentile
        subcol1, subcol2 = st.columns(2)

        with subcol1:
            st.markdown("<h4 style='padding-top:40px; font-size:16px; font-weight:bold;'>Sugar Percentile</h4>", unsafe_allow_html=True)

        with subcol2:
            st.metric(label="", value=f"{avg_rec_sugar:.2f}", delta=f"{avg_rec_sugar - overall_avg_sugar:.2f}")

        st.markdown(
            "*The sugar content in our selection is 32.76% below average, offering a healthier option. "
            "We included one with higher sugar to balance preferences for sweeter treats.*"
        )

    # Radar chart section
    categories = ['Win %', 'Sugar %', 'Price %', 'Chocolate', 'Fruity', 'Peanut/Almond', 'Nougat', 'Crispy/Wafer', 'Hard', 'Bar', 'Pluribus']

    fig_radar = go.Figure()

    for candy in selected_candies:
        candy_data_item = selected_data[selected_data['competitorname'] == candy].iloc[0]
        values = [
            candy_data_item['winpercent'],
            candy_data_item['sugarpercent'] * 100,
            candy_data_item['pricepercent'] * 100,
            100 if candy_data_item['chocolate'] else 0,
            100 if candy_data_item['fruity'] else 0,
            100 if candy_data_item['peanutyalmondy'] else 0,
            100 if candy_data_item['nougat'] else 0,
            100 if candy_data_item['crispedricewafer'] else 0,
            100 if candy_data_item['hard'] else 0,
            100 if candy_data_item['bar'] else 0,
            100 if candy_data_item['pluribus'] else 0
        ]
        
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=candy,
        ))

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        legend=dict(font=dict(color="#333333")),
        paper_bgcolor='#F8F0E3',
        plot_bgcolor='#FFFFFF',
        font_color='#333333',
    )

    # Display radar chart spanning full width below the metrics
    st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #2E2E2E; color: white; border-radius: 10px; padding: 20px; margin-top: 20px;">
        <h4 style="color: #FF6600;">Why These 3 Candies? 🎃</h4>
    <p>
        Our selection of top candies is based on a careful, data-driven approach to ensure they’re a Halloween hit, considering:
    </p>
        <ul>
            <li><strong>Popularity</strong> 🏆: These treats have consistently won in head-to-head matchups, making them crowd favorites.</li>
            <li><strong>Balanced Flavors</strong> 🍭: We’ve chosen a variety of sweet, rich, and fruity options to cater to diverse tastes.</li>
            <li><strong>Variety</strong> 🍫: From chewy to crunchy, we’ve included something for every texture preference.</li>
            <li><strong>Affordability</strong> 💸: By analyzing price data, we've ensured the selection fits within a reasonable budget without sacrificing quality.</li>
            <li><strong>Safety</strong> 🧙‍♀️: Allergy considerations are taken into account to keep all trick-or-treaters safe.</li>
        </ul>    
    <p><strong>Curious about the data behind our candy selection?</strong> Click the button below to dive deeper into our detailed analysis!</p>
    <a href='analysis.html' target='_blank' style='text-decoration: none; color: white; background-color: #D35400; padding: 10px 20px; border-radius: 5px;'>🔍 Dive into Our Analysis</a>
        
    """, unsafe_allow_html=True)
    
with tab2:
    st.markdown("<h2 style='text-align: center; font-size:30px; color: #D35400;'>Brew Your Own Halloween Candy Potion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🧪 Select Your Candy Ingredients")
        with st.container():
            col1_a, col1_b, col1_c = st.columns(3)
            with col1_a:
                chocolate = st.checkbox("Chocolate", key="chocolate")
                fruity = st.checkbox("Fruity", key="fruity")
                caramel = st.checkbox("Caramel", key="caramel")
            with col1_b:
                peanutyalmondy = st.checkbox("Peanut/Almond", key="peanutyalmondy")
                nougat = st.checkbox("Nougat", key="nougat")
                crispedricewafer = st.checkbox("Crispy/Wafer", key="crispedricewafer")
            with col1_c:
                hard = st.checkbox("Hard Candy", key="hard")
                bar = st.checkbox("Bar", key="bar")
                pluribus = st.checkbox("Pluribus (multiple pieces)", key="pluribus")
    
        st.markdown("##### 🎭 Adjust Your Candy Potion")
        col1_slider, col2_slider = st.columns(2)
        with col1_slider:
            sugar_range = st.slider("Sugar Percentile", 0.0, 100.0, (0.0, 100.0), step=1.0, key="sugar_range")
        
        with col2_slider:
            price_range = st.slider("Price Percentile", 0.0, 100.0, (0.0, 100.0), step=1.0, key="price_range")

        st.markdown("*Adjust the sugar and price percentiles to control the sweetness and cost of your selected candies relative to others: a higher percentile means more sugar or a higher cost, while a lower percentile indicates less sugar or a lower price.*")

    # Function to filter candies based on user preferences
    def filter_candies():
        mask = pd.Series(True, index=candy_data.index)
        
        if chocolate:
            mask &= candy_data['chocolate'] == 1
        if fruity:
            mask &= candy_data['fruity'] == 1
        if caramel:
            mask &= candy_data['caramel'] == 1
        if peanutyalmondy:
            mask &= candy_data['peanutyalmondy'] == 1
        if nougat:
            mask &= candy_data['nougat'] == 1
        if crispedricewafer:
            mask &= candy_data['crispedricewafer'] == 1
        if hard:
            mask &= candy_data['hard'] == 1
        if bar:
            mask &= candy_data['bar'] == 1
        if pluribus:
            mask &= candy_data['pluribus'] == 1
        
        mask &= (candy_data['sugarpercent'] >= sugar_range[0]/100) & (candy_data['sugarpercent'] <= sugar_range[1]/100)
        mask &= (candy_data['pricepercent'] >= price_range[0]/100) & (candy_data['pricepercent'] <= price_range[1]/100)
        
        return candy_data[mask]
    
    with col2:
        st.markdown("##### 🧙‍♂️ Your Magical Candy Selection")
        
        filtered_data = filter_candies()
        
        # Display the enhanced DataFrame
        st.dataframe(
            filtered_data[['competitorname', 'winpercent', 'sugarpercent', 'pricepercent']].reset_index(drop=True),
            hide_index=True,
            use_container_width=True
        )
    
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("##### 🎃 Select Your Halloween Candy Assortment")
    user_selected_candies = st.multiselect(
        "",
        options=filtered_data['competitorname'].tolist(),
        max_selections=3
    )

    if user_selected_candies:
        user_selected_data = filtered_data[filtered_data['competitorname'].isin(user_selected_candies)]
        
        st.markdown('<h3 style="text-align: center; font-size:30px; color: #D35400;">Your Spooky Selection:</h3>', unsafe_allow_html=True)
        
        candy_chunks = [user_selected_candies[i:i + 3] for i in range(0, len(user_selected_candies), 3)]
        
        for candy_row in candy_chunks:
            cols = st.columns(len(candy_row))
            
            for idx, candy in enumerate(candy_row):
                candy_info = user_selected_data[user_selected_data['competitorname'] == candy].iloc[0]
                
                with cols[idx]:
                    characteristics = [
                        "Chocolate" if candy_info['chocolate'] else None,
                        "Fruity" if candy_info['fruity'] else None,
                        "Caramel" if candy_info['caramel'] else None,
                        "Peanuts/Almonds" if candy_info['peanutyalmondy'] else None,
                        "Nougat" if candy_info['nougat'] else None,
                        "Crispy/Wafer" if candy_info['crispedricewafer'] else None,
                        "Hard" if candy_info['hard'] else None,
                        "Bar" if candy_info['bar'] else None,
                        "Pluribus" if candy_info['pluribus'] else None
                    ]
                    characteristics = [c for c in characteristics if c]
                    
                    st.markdown(f"""
                    <div class="candy-card">
                        <p style=" font-size:18px; text-align: center; color: #D35400;"><strong>{candy}</strong></p>
                        <hr style="border-top: 1px solid #D35400;">
                        <p><strong>Win Percentage:</strong> {candy_info['winpercent']:.2f}%</p>
                        <p><strong>Sugar Percentile:</strong> {candy_info['sugarpercent']*100 :.2f}th</p>
                        <p><strong>Price Percentile:</strong> {candy_info['pricepercent']*100 :.2f}th</p>
                        <p><strong>Characteristics:</strong> {", ".join(characteristics)}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center; font-size: 28px;'>🔮 Analysis of Your Spooky Selection</h3>", unsafe_allow_html=True)

        # Calculate average values for selected candies
        avg_win = user_selected_data['winpercent'].mean()
        avg_sugar = user_selected_data['sugarpercent'].mean() * 100
        avg_price = user_selected_data['pricepercent'].mean() * 100

        # Compare with overall averages
        overall_avg_win = candy_data['winpercent'].mean()
        overall_avg_sugar = candy_data['sugarpercent'].mean() * 100
        overall_avg_price = candy_data['pricepercent'].mean() * 100
        
        # Create three columns for the metrics
        col1, col2, col3 = st.columns(3)

        # Display metrics in the first column
        with col1:
            # Create sub-columns for Win Rate
            subcol1, subcol2 = st.columns(2)

            with subcol1:
                st.markdown("<h4 style='padding-top:40px; font-size:16px; font-weight:bold;'>Win Rate</h4>", unsafe_allow_html=True)

            with subcol2:
                st.metric(label="", value=f"{avg_win:.2f}%", delta=f"{avg_win - overall_avg_win:.2f}%")

            if avg_win > overall_avg_win:
                st.markdown(
                    "*Your selected candies have a higher-than-average win rate, meaning they are more popular in head-to-head matchups.*"
                )
            else:
                st.markdown(
                    "*Your selected candies have a lower-than-average win rate. Consider adding more popular options for better appeal.*"
                )

        # Display metrics in the second column
        with col2:
            # Create sub-columns for Sugar Percentile
            subcol1, subcol2 = st.columns(2)

            with subcol1:
                st.markdown("<h4 style='padding-top:40px; font-size:16px; font-weight:bold;'>Sugar Percentile</h4>", unsafe_allow_html=True)

            with subcol2:
                st.metric(label="", value=f"{avg_sugar:.2f}", delta=f"{avg_sugar - overall_avg_sugar:.2f}")

            if avg_sugar > overall_avg_sugar:
                st.markdown(
                    "*Your selected candies contain more sugar on average, which may be appealing to kids but could also be seen as too sweet by some.*"
                )
            else:
                st.markdown(
                    "*Your selected candies contain less sugar on average, making them a healthier option but possibly less appealing to those seeking sweetness.*"
                )

        # Display metrics in the third column
        with col3:
            # Create sub-columns for Price Percentile
            subcol1, subcol2 = st.columns(2)

            with subcol1:
                st.markdown("<h4 style='padding-top:40px; font-size:16px; font-weight:bold;'>Price Percentile</h4>", unsafe_allow_html=True)

            with subcol2:
                st.metric(label="", value=f"{avg_price:.2f}", delta=f"{avg_price - overall_avg_price:.2f}")

            if avg_price > overall_avg_price:
                st.markdown(
                    "*Your selected candies are priced above average, potentially indicating higher quality but also impacting your overall budget.*"
                )
            else:
                st.markdown(
                    "*Your selected candies are priced below average, making them a more budget-friendly choice, but ensure you're not compromising on quality.*"
                )
        # Radar chart for user-selected candies
        categories = ['Win %', 'Sugar %', 'Price %', 'Chocolate', 'Fruity', 'Peanut/Almond', 'Nougat', 'Crispy/Wafer', 'Hard', 'Bar', 'Pluribus']
        user_fig_radar = go.Figure()
        
        for candy in user_selected_candies:
            candy_data_item = user_selected_data[user_selected_data['competitorname'] == candy].iloc[0]
            values = [
                candy_data_item['winpercent'],
                candy_data_item['sugarpercent'] * 100,
                candy_data_item['pricepercent'] * 100,
                100 if candy_data_item['chocolate'] else 0,
                100 if candy_data_item['fruity'] else 0,
                100 if candy_data_item['peanutyalmondy'] else 0,
                100 if candy_data_item['nougat'] else 0,
                100 if candy_data_item['crispedricewafer'] else 0,
                100 if candy_data_item['hard'] else 0,
                100 if candy_data_item['bar'] else 0,
                100 if candy_data_item['pluribus'] else 0
            ]

            user_fig_radar.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name=candy
            ))

        user_fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            legend=dict(font=dict(color="#FF9900")),
            paper_bgcolor='#F8F0E3',
            plot_bgcolor= '#F8F0E3',
            font_color='#333333',
        )

        st.plotly_chart(user_fig_radar, use_container_width=True)

        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

        st.markdown("#### 🧛‍♂️ Candy Concoction Analysis")
        
        analysis_text = ""

        if avg_win > overall_avg_win:
            analysis_text += "🎃 Your selection has an above-average win rate. It's likely to be popular with trick-or-treaters!\n\n"
        else:
            analysis_text += "💀 Your selection has a below-average win rate. Consider adding some more popular candies to increase its appeal.\n\n"

        if avg_sugar > overall_avg_sugar:
            analysis_text += "🍭 Your selection has an above-average sugar content percentile. It might be extra sweet compared to other candies.\n\n"
        else:
            analysis_text += "🥕 Your selection has a below-average sugar content percentile. This might be appealing to health-conscious parents.\n\n"

        if avg_price > overall_avg_price:
            analysis_text += "💰 Your selection has an above-average price percentile. While this might indicate higher quality, consider including some more affordable options to balance your budget.\n\n"
        else:
            analysis_text += "💵 Your selection has a below-average price percentile, which could be good for your budget. Just ensure you're not compromising too much on quality or popularity.\n\n"

        # Check for common allergens
        contains_allergens = any(user_selected_data['peanutyalmondy'])
        if contains_allergens:
            analysis_text += "🚫 **Allergy Warning**: Some of your selected candies contain nuts. Consider adding nut-free options to accommodate those with allergies.\n\n"

        # Check for variety in candy types
        contains_chocolate = any(user_selected_data['chocolate'])
        contains_fruity = any(user_selected_data['fruity'])
        contains_caramel = any(user_selected_data['caramel'])

        if not contains_chocolate:
            analysis_text += "🍫 Consider adding chocolate: None of your selected candies contain chocolate. Including chocolate-based candies can appeal to many trick-or-treaters.\n\n"

        if not contains_fruity:
            analysis_text += "🍎 Consider adding fruity candies: None of your selected candies are fruity. Adding fruity candies can provide balance and variety.\n\n"

        if not contains_caramel:
            analysis_text += "🍬 Consider adding caramel candies: Your selection doesn't include caramel candies, which are popular. Including them can make your assortment more versatile.\n\n"

        st.markdown(analysis_text)

        st.markdown("""
        <div style="background-color: #2E2E2E; color: white; border-radius: 10px; padding: 20px; margin-top: 20px;">
            <h4 style="color: #FF6600;">🎭 Final Thoughts</h4>
            <p>Remember, the perfect Halloween candy assortment often includes a mix of different types, flavors, and price points to appeal to a wide range of trick-or-treaters. 
            Feel free to adjust your selection based on this analysis to create the ultimate Halloween treat experience!</p>
        </div>
        """, unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="background-color: #2E2E2E; color: white; border-radius: 10px; padding: 20px; margin-top: 20px;">
    <h4 style="color: #FF6600;">About This Dashboard</h4>
<p>
Welcome to our spooktacular candy selection tool! Discover the perfect mix of treats for your trick-or-treaters using our data-driven approach. 
Explore our top recommendations or create your own haunting blend of sweets!
</p>
<p>
    <a href="https://mavenanalytics.io/challenges/maven-halloween-challenge/701f06a2-a19b-41e9-95d3-37a0dcc5492f" style="color: #FF6600;">Created for Maven Halloween Challenge</a></li>
</p>
<p>Connect with me:</p>
<ul>
    <li><a href="https://www.linkedin.com/in/santanu-jha-845510292/" style="color: #FF6600;">LinkedIn</a></li>
    <li><a href="https://github.com/jhasantanu9" style="color: #FF6600;">GitHub</a></li>
    <li><a href="https://santanujha.netlify.app/" style="color: #FF6600;">Portfolio</a></li>
</ul>
""", unsafe_allow_html=True)