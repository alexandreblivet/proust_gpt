import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://fr.wikisource.org/wiki/Du_c%C3%B4t%C3%A9_de_chez_Swann/Partie_1",
    "https://fr.wikisource.org/wiki/Du_c%C3%B4t%C3%A9_de_chez_Swann/Partie_2",
    "https://fr.wikisource.org/wiki/Du_c%C3%B4t%C3%A9_de_chez_Swann/Partie_3",
    "https://fr.wikisource.org/wiki/%C3%80_l%E2%80%99ombre_des_jeunes_filles_en_fleurs/Premi%C3%A8re_partie",
    "https://fr.wikisource.org/wiki/%C3%80_l%E2%80%99ombre_des_jeunes_filles_en_fleurs/Deuxi%C3%A8me_partie",
    "https://fr.wikisource.org/wiki/%C3%80_l%E2%80%99ombre_des_jeunes_filles_en_fleurs/Troisi%C3%A8me_partie",
    "https://fr.wikisource.org/wiki/Le_C%C3%B4t%C3%A9_de_Guermantes/Premi%C3%A8re_partie",
    "https://fr.wikisource.org/wiki/Le_C%C3%B4t%C3%A9_de_Guermantes/Deuxi%C3%A8me_partie",
    "https://fr.wikisource.org/wiki/Le_C%C3%B4t%C3%A9_de_Guermantes/Troisi%C3%A8me_partie",
    "https://fr.wikisource.org/wiki/Sodome_et_Gomorrhe/Partie_1",
    "https://fr.wikisource.org/wiki/Sodome_et_Gomorrhe/Partie_2",
    "https://fr.wikisource.org/wiki/Sodome_et_Gomorrhe/Partie_2_-_chapitre_1",
    "https://fr.wikisource.org/wiki/Sodome_et_Gomorrhe/Partie_2_-_chapitre_2",
    "https://fr.wikisource.org/wiki/Sodome_et_Gomorrhe/Partie_2_-_chapitre_3",
    "https://fr.wikisource.org/wiki/Sodome_et_Gomorrhe/Partie_2_-_chapitre_4",
    "https://fr.wikisource.org/wiki/La_Prisonni%C3%A8re/Chapitre_1",
    "https://fr.wikisource.org/wiki/La_Prisonni%C3%A8re/Chapitre_2",
    "https://fr.wikisource.org/wiki/La_Prisonni%C3%A8re/Chapitre_3",
    "https://fr.wikisource.org/wiki/Albertine_disparue/Chapitre_I",
    "https://fr.wikisource.org/wiki/Albertine_disparue/Chapitre_II",
    "https://fr.wikisource.org/wiki/Albertine_disparue/Chapitre_III",
    "https://fr.wikisource.org/wiki/Le_Temps_retrouv%C3%A9/I",
    "https://fr.wikisource.org/wiki/Le_Temps_retrouv%C3%A9/II",
    "https://fr.wikisource.org/wiki/Le_Temps_retrouv%C3%A9/III"
]

# Function to get the BeautifulSoup object for a given URL
def get_soup(url):
    """Fetches content of the given URL and returns a BeautifulSoup object."""
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

# Function to extract the main text from a given URL
def get_text_from_page(url):
    """Scrapes the main text content from the given URL."""
    soup = get_soup(url)
    
    # Find the div where the main text resides
    content_div = soup.find('div', id='mw-content-text')
    if not content_div:
        return "No content found"
    
    # Extract the paragraphs within the main content area
    paragraphs = content_div.find_all('p')

    # Join the text from all paragraphs
    text = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])
    
    return text

def scrape_full_text(urls, output_file):
    """Scrapes text from all URLs and writes it to a single file."""
    with open(output_file, "w", encoding="utf-8") as f:
        for url in urls:
            print(f"Scraping: {url}")
            text = get_text_from_page(url)
            
            # Write the title of the part being scraped
            f.write(f"\n\n--- Scraped from: {url} ---\n\n")
            
            # Write the actual text
            f.write(text)
            f.write("\n\n")  # Add a double newline as separator

    print(f"Scraping complete! Full text saved in '{output_file}'")

# Run the scraper
output_file = "A_la_recherche_du_temps_perdu_full.txt"
scrape_full_text(urls, output_file)
