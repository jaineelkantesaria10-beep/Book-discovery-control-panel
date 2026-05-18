import requests

def search_books_from_api(query):
    # Open Library ki free link jahan se data aayega
    url = f"https://openlibrary.org/search.json?q={query}"
    
    try:
        response = requests.get(url) # Internet se data manga
        if response.status_code == 200: # Agar net connection success raha
            data = response.json()      # JSON data ko parse kiya
            docs = data.get('docs', [])
            
            parsed_books = []
            # Sirf pehle 5 books ka data nikal rahe hain sample ke liye
            for doc in docs[:5]:
                book_info = {
                    'title': doc.get('title', 'Unknown Title'),
                    'author': doc.get('author_name', ['Unknown Author'])[0],
                    'isbn': doc.get('isbn', ['No ISBN'])[0]
                }
                parsed_books.append(book_info)
            return parsed_books 
    except Exception as e:
        print(f"Error aaya bhai API chalane me: {e}")
    return []