# AdInsight: Reddit Ad Performance Dashboard

## Description
AdInsight is a powerful, interactive dashboard for analyzing Reddit ad performance. It provides real-time insights into key advertising metrics, helping advertisers optimize their campaigns and maximize ROI on the Reddit platform.

## Features
- Interactive date range selection for customized analysis
- Key performance metrics display (Impressions, Clicks, CTR, Conversions)
- Dynamic time series visualization of clicks and conversions
- Raw data view with download option
- SQLite database integration for efficient data storage and retrieval
- Responsive design for various screen sizes

  <img width="1515" alt="Screenshot 2024-09-10 at 5 11 58 PM" src="https://github.com/user-attachments/assets/fcc9eb03-ccc6-41f1-ad81-e35eaa074b8e">


## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- SQLite

## Installation
1. Clone this repository:
git clone https://github.com/yourusername/adinsight.git
cd adinsight
Copy2. Create a virtual environment:
python3 -m venv venv
source venv/bin/activate
Copy3. Install required packages:
pip install -r requirements.txt
Copy
## Usage
1. Ensure your virtual environment is activated
2. Run the Streamlit app:
streamlit run app.py
Copy3. Open your web browser and navigate to the URL provided by Streamlit (typically http://localhost:8501)

## Data Management
- The app uses a SQLite database located at `data/ad_performance.db`
- To update or modify the data, use SQL commands or SQLite management tools

## Future Enhancements
- Integration with live Reddit Ads API
- Advanced analytics features (e.g., predictive modeling)
- Multi-campaign comparison tools
- User authentication and personalized dashboards

## Contributing
Contributions to AdInsight are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Reddit for inspiration and the advertising platform
- Streamlit for making it easy to create data apps in Python
- The open-source community for the amazing tools and libraries
