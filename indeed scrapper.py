from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your API token
client = ApifyClient("api key")

# Prepare the Actor input
run_input = {
    "position": "web developer",  
    "country": "IN",  
    "location": "Chennai",  
    "maxItems": 50,  
    "parseCompanyDetails": True,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": False,
}

# Run the Actor and wait for it to finish
run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

# Initialize lists to hold the scraped data
positions = []
companies = []
salaries = []
locations = []
date = []
urls = []

# Fetch and process Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    positions.append(item.get("positionName", "N/A"))  
    companies.append(item.get("company", "N/A"))  
    salaries.append(item.get("salary", "N/A"))
    locations.append(item.get("location", "N/A"))
    date.append(item.get("postedAt", "N/A"))
    urls.append(item.get("url", "N/A"))

# Create a DataFrame from the scraped data
df = pd.DataFrame({
    "PositionName": positions,  
    "Company": companies,       
    "Salary": salaries,
    "Location": locations,
    "PostedAt": date,
    "URL": urls
})

# Save the DataFrame to an Excel file
df.to_excel("indeed_job.xlsx", index=False)

print("Scraped data saved to 'indeed_job.xlsx'.")# saved file
