import csv
from io import StringIO
import os
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from django.http import HttpResponse
from django.shortcuts import render


def scrap_email(request):
    if request.method == 'POST':
        # Recover URL input of users
        url = request.POST.get('url')

        user_agent = UserAgent().random
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                email_links = soup.find_all('a', href=True)
                emails = [link['href'][7:] for link in email_links if link['href'].startswith('mailto:')]

                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="emails.csv"'

                writer = csv.writer(response)
                writer.writerow(['Emails'])
                for email in emails:
                    writer.writerow([email])

                return response
            else:
                return HttpResponse('The request havefailed. Check your URL input.')
        except Exception as e:
            return HttpResponse(f'An error occured : {str(e)}')

    return render(request, 'csv_scrapper/scrap_email.html') 

def scrap_href(request):
    if request.method == 'POST':
        # Recover URL input of users
        url = request.POST.get('url')

        user_agent = UserAgent().random
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all links with the 'href' attribute
                href_links = soup.find_all('a', href=True)

                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="hrefs.csv"'

                writer = csv.writer(response)
                writer.writerow(['Hrefs'])
                for link in href_links:
                    href = link['href']
                    writer.writerow([href])

                return response
            else:
                return HttpResponse('The request has failed. Check your URL input.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

    return render(request, 'csv_scrapper/scrap_href.html')

def scrap_text(request):
    if request.method == 'POST':
        # Recover URL input of users
        url = request.POST.get('url')

        user_agent = UserAgent().random
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all links with the 'href' attribute
                href_links = soup.find_all('a', href=True)

                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="text.csv"'

                writer = csv.writer(response)
                writer.writerow(['Text'])
                for link in href_links:
                    text = link.get_text()
                    writer.writerow([text])

                return response
            else:
                return HttpResponse('The request has failed. Check your URL input.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

    return render(request, 'csv_scrapper/scrap_text.html')

def scrap_images(request):
    if request.method == 'POST':
        # Recover URL input of users
        url = request.POST.get('url')

        user_agent = UserAgent().random
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all image tags
                img_tags = soup.find_all('img', src=True)

                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="images.csv"'

                writer = csv.writer(response)
                writer.writerow(['Image URLs'])
                for img_tag in img_tags:
                    img_url = img_tag['src']
                    writer.writerow([img_url])

                return response
            else:
                return HttpResponse('The request has failed. Check your URL input.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

    return render(request, 'csv_scrapper/scrap_images.html')

def scrap_list(request):
    if request.method == 'POST':
        # Recover URL input of users
        url = request.POST.get('url')

        user_agent = UserAgent().random
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all list items within ordered and unordered lists
                list_items = soup.find_all(['ol', 'ul']) + soup.find_all('li')

                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="lists.csv"'

                writer = csv.writer(response)
                writer.writerow(['List Items'])
                for item in list_items:
                    text = item.get_text()
                    writer.writerow([text])

                return response
            else:
                return HttpResponse('The request has failed. Check your URL input.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

    return render(request, 'csv_scrapper/scrap_list.html')

def scrap_numbers(request):
    if request.method == 'POST':
        # Recover URL input of users
        url = request.POST.get('url')

        user_agent = UserAgent().random
        headers = {'User-Agent': user_agent}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all elements containing numeric values
                numeric_elements = soup.find_all(['p', 'span', 'div', 'td', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'], text=True)

                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="numbers.csv"'

                writer = csv.writer(response)
                writer.writerow(['Numeric Values'])
                for element in numeric_elements:
                    text = element.get_text()
                    # Filter numeric values using isnumeric()
                    numeric_values = [value for value in text.split() if value.isnumeric()]
                    writer.writerow(numeric_values)

                return response
            else:
                return HttpResponse('The request has failed. Check your URL input.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

    return render(request, 'csv_scrapper/scrap_numbers.html')

def scrap_content(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if not url:
            return HttpResponse("No URL provided.")

        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            scraped_data = []
            email_links = soup.find_all('a', href=re.compile(r'^mailto:'))

            for link in email_links:
                email = link['href'][7:]
                scraped_data.append({
                    "tag": "email",
                    "text": email,
                    "href": "",
                    "email": email,
                    "images": ""
                })

            img_tags = soup.find_all('img', src=True)
            for img in img_tags:
                img_src = img.get("src", "")
                scraped_data.append({
                    "tag": "img",
                    "text": "",
                    "href": img_src,
                    "email": "",
                    "images": img_src
                })

            numbers_with_text = []

            for tag in soup.find_all(["a", "p", "span", "img"]):
                tag_text = tag.text.strip()

                number_pattern = r"([-+]?\d*\.\d+|\d+)(\D+)"
                number_matches = re.findall(number_pattern, tag_text)
                for match in number_matches:
                    number, text = match
                    numbers_with_text.append({"number": number, "text": text})

                scraped_data.append({
                    "tag": tag.name,
                    "text": tag_text,
                    "href": tag.get("href", ""),
                    "email": "",
                    "images": ""
                })

            for num_entry in numbers_with_text:
                scraped_data.append({
                    "tag": "number",
                    "text": num_entry["text"],
                    "href": "",
                    "email": "",
                    "number": num_entry["number"],
                    "images": ""
                })

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="scraped_data.csv"'

            writer = csv.DictWriter(response, fieldnames=["tag", "text", "href", "email", "number", "images"])
            writer.writeheader()

            for entry in scraped_data:
                writer.writerow(entry)

            return response

        except Exception as e:
            return HttpResponse(f"An error occurred while scraping: {str(e)}")
    return render(request, 'csv_scrapper/scrap_content.html')