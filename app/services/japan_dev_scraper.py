import requests
from bs4 import BeautifulSoup
import re

def get_posted_jobs():
    """
    Scrapes job postings from the Japan Dev job board.

    Returns:
        List[Dict]: A list of job dictionaries, each containing:
            - jobTitle (str): Title of the job.
            - companyInfo (str): Company name and description.
            - companyLogoUrl (str): URL to the company's logo image.
            - jobUrl (str): Direct link to the job posting.
            - tags (List[str]): List of tags (e.g., tech stack, job type).
            - location (str | None): Job location if available.
            - salaryText (str | None): Formatted salary information if available.

    Note:
        This function scrapes only the first page of job listings.
        Future improvements may include handling pagination, dynamic scraping, or using the site's underlying API.
    """

    # Request the job listings page from Japan Dev
    job_page = requests.get("https://japan-dev.com/jobs")
    soup = BeautifulSoup(job_page.text, 'html')

    # Extract all job listings on the page
    posted_jobs = soup.findAll(class_='job-item')

    jobs = []
    for job in posted_jobs:
        # Extract job title and URL
        job_title_item = job.find(class_='job-item__title')
        job_title = job_title_item.text.strip()
        job_url = f"https://japan-dev.com{job_title_item['href']}"
       
        # Extract company logo image URL
        company_logo = job.find(class_='company-logo__inner')
        company_log_url = company_logo['src']

        # Extract company name and descriptor (e.g. "Money Forward・Top Japanese fintech")
        company = job.find(class_="job-item__contract-type")
        company_info = company.text.strip() if company else "Unknown"

        # Extract tags related to the job (e.g. "Frontend", "Remote")
        tags = job.find_all(class_="job-top-tag-list__job-top-tag")
        tag_list = [ re.sub(r"\s+", " ", tag.find('span').text.strip())  for tag in tags]
    

        # Extract job location and salary (if available)
        location = None
        salary = None
        for tag in job.find_all(class_="job__tag"):
            img = tag.find('img')
            if img:
                alt = img.get('alt')
                if alt == 'location-icon':
                    location = tag.find(class_="job__tag-desc").text.strip()
                elif alt == 'yen-icon-simple':
                    raw_salary = tag.find(class_="job__tag-desc").text
                    salary = re.sub(r"\s+", " ", raw_salary)

        jobs.append({
            "jobTitle": job_title,
            "companyInfo": company_info,
            "companyLogoUrl": company_log_url,
            "jobUrl": job_url,
            "tags": tag_list,
            "location": location,
            "salaryText": salary
        })
        
    
    return jobs