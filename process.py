import requests
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import boto3
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time

def load_companies():
    with open('companies.json', 'r') as f:
        return json.load(f)

def process_company(company, client):
    url = f"https://r.jina.ai/{company['link']}"
    headers = {
        "Authorization": "Bearer jina_d853da0cfeff4f7abc2a966ce73b1d60axdku-fIfEIubJXkigoIGX7H_YwD"
    }

    try:
        response = requests.get(url, headers=headers)
        
        insights = generate_sales_insights(client, response.text)
        
        return {
            'name': company['name'],
            'link': company['link'],
            'insights': insights,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        return {
            'name': company['name'],
            'link': company['link'],
            'error': str(e),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def generate_sales_insights(client, contractor_data):
    prompt = f"""Analyze this contractor profile and provide a concise analysis in the following format:

1. Business Overview (2-3 sentences):
   - Company size and type
   - Main services offered
   - Years in business (if available)

2. Key Strengths (3-4 bullet points):
   - Unique selling points
   - Specializations
   - Notable achievements

3. Market Position:
   - Target market/area
   - Competitive advantages
   - Service differentiators

4. Growth Potential:
   - Opportunities for expansion
   - Areas for improvement
   - Market trends alignment

Keep each section brief and focused on actionable insights. Avoid generic statements.

Contractor Data:
{contractor_data}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a sales intelligence expert."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error generating insights: {str(e)}")

def main():
    load_dotenv()
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    companies = load_companies()
    
    results = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_company = {
            executor.submit(process_company, company, client): company['name']
            for company in companies
        }
        
        with tqdm(total=len(companies), desc="Processing companies") as pbar:
            for future in as_completed(future_to_company):
                company_name = future_to_company[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"Error processing {company_name}: {str(e)}")
                pbar.update(1)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f'analysis_results_{timestamp}.json'
    
    with open(output_filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {output_filename}")
    

if __name__ == "__main__":
    main()