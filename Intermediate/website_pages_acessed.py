'''
Acest script arata cate pagini au fost acesate si in acelasi timp separa adresa in url, protocol, domain si urn.
'''

class Website:
    pages_accessed = 0

    def __init__(self, url):
        self.url = url
        self.protocol = (str(url)).split("www")[0]
        self.domain, self.urn = ((str(url)).lstrip("https://www.")).split("/")
        Website.pages_accessed += 1

    @classmethod
    def number_of_pages(cls):
        print(f"You have accessed a number of {cls.pages_accessed} pages")


    @classmethod
    def access_website_list(cls, list):
        list_websites = []
        for element in list:
            website = "https://" + "www" + element + ".com/products"
            list_websites.append(cls(website))
        for object in list_websites:
            print(object.__dict__)
        return list_websites


domains = ["google", "yahoo", "youtube", "facebook"]

Website.number_of_pages()

Website.access_website_list(domains)

Website.number_of_pages()
