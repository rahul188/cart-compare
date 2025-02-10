import streamlit as st
import pandas as pd

# Load data
cab_data = pd.read_json('data-json/cab.json')
courier_data = pd.read_json('data-json/courier.json')
essentials_data = pd.read_json('data-json/essentials.json')

# App title and tagline
st.title("Cart Compare")
st.subheader("Compare Choose Save")

# Vision
st.write("User will get a platform that simplifies service comparison across providers and empowering smarter choices in Everyday essentials.")

# Problem Statement
st.header("Problem Statement")
st.write("""
- No Single platform offers comprehensive fare and time comparisons for courier, cabs and daily essentials.
- Time consuming to check manually across multiple platforms often overpaying or facing delays.
- Consumers struggle to find the best deals.
""")

# Solution
st.header("Solution")
st.write("""
Consumers will be able to effortlessly compare below:
- A unified app to compare courier service fares & delivery times, cab fares & driver availability and daily essentials delivery fares & times.
- Daily Essentials prices and delivery times.
- Intercity cheapest courier services i.e. prices and delivery times.
- Earliest cab/moto arriving time and prices.
""")

# Key Features
st.header("Key Features")
st.write("""
- Real time price & Time comparison
- Estimated Delivery/Arrival time display
- Direct Redirection to service providers
- Services filters for great deals
""")

# No Booking Service
st.header("No Booking Service")
st.write("Neutral platform solely focused on comparisons ensuring unbiased results.")

# User Flow
st.header("User Flow")
st.write("""
1. Home Screen: Where user can select required category (Essentials, Courier and CAB)
2. Search/Filter: Input delivery or destination details so user will get all the vendor details in his/her location.
3. Comparison result: view service providers ranked by price and time
4. Select & Redirect: Choose the best deal with provider and user will redirect in the app and complete the order.
""")

# Target Audience
st.header("Target Audience")
st.write("It will connect all kind of consumers especially in metro cities Urban Professionals, Time Conscious Consumers.")

# App Architecture
st.header("App Architecture")
st.write("""
- Frontend: Interactive UI for quick comparison
- Backend: Real Time API integration
- Database: Service data storage and user data storage
- Service providers Partnerships for Information feeds
""")

# Revenue Model
st.header("Revenue Model")
st.write("""
- Affiliate Commission
- Featured Listing (Paid Promotion)
- Click per pay
- Advertisement Pop Up
""")

# Market Strategy
st.header("Market Strategy")
st.write("""
- Launch in Tier 1 cities with high demand of vendors.
- Social Media Campaign
- Influencers Partnership
- SEO and Content Marketing
- Referral Program
""")

# Market opportunity
st.header("Market opportunity")
st.write("Growing demand for efficient service comparisons. Faster and Easier decision-making process.")

# App Development Plan
st.header("App Development Plan")
st.write("""
- MVP
- Beta Testing
- Launch
""")

# Service Comparison
st.header("Service Comparison")

# Select category
category = st.selectbox("Select Category", ["Daily Essentials", "Courier", "Cab & Moto"])

if category == "Daily Essentials":
    st.subheader("Daily Essentials")
    st.write(essentials_data)
elif category == "Courier":
    st.subheader("Courier Services")
    st.write(courier_data)
elif category == "Cab & Moto":
    st.subheader("Cab & Moto Services")
    st.write(cab_data)

# Footer
st.write("© 2023 Cart Compare. All rights reserved.")
