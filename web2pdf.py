import requests
from bs4 import BeautifulSoup
import urllib.parse
import pdfkit

remaining_pages = 0
visited_urls = set()

def convert_website_to_pdf(url):
    """Converts an entire website to PDF.

    Args:
        url: The URL of the website to convert.

    Returns:
        A list of the PDF file paths that were created.
    """
    global remaining_pages
    global visited_urls

    if remaining_pages <= 0 or url in visited_urls:
        return []

    pdf_files = []
    remaining_pages -= 1
    visited_urls.add(url)

    # Get the HTML of the page.
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Print the URL of the page being parsed.
    print("Parsing:", url)

    # Convert the page to PDF and save it.
    pdf_path = f"{urllib.parse.quote(url, safe='')}.pdf"
    pdfkit.from_url(url, pdf_path)
    pdf_files.append(pdf_path)

    # Get a list of all links on the page.
    links = soup.find_all("a")

    if remaining_pages > 0:
        # Recursively convert linked pages to PDF.
        for link in links:
            link_url = link.get("href")
            if link_url and not urllib.parse.urlparse(link_url).netloc:
                abs_url = urllib.parse.urljoin(url, link_url)
                pdf_files += convert_website_to_pdf(abs_url)

    return pdf_files


if __name__ == "__main__":
    # Get the URL of the website to convert.
    url = input("Enter the URL of the website to convert: ")

    # Get the maximum number of pages to convert.
    max_pages = int(input("Enter the maximum number of pages to convert: "))

    # Set the remaining pages to the maximum number of pages.
    remaining_pages = max_pages

    # Convert the website to PDF.
    pdf_files = convert_website_to_pdf(url)

    # Print the paths of the PDF files that were created.
    for i, pdf_file in enumerate(pdf_files):
        print(f"PDF {i + 1}: {pdf_file}")
