class News_Source:
    """
    Details for the News Source
    """
    def __init__(self,name,url,description,country,language,category,id):
        self.name = name
        self.url = url
        self.description = description
        self.country = country
        self.category = category
        self.language = language
        self.id = id
        
class Articles:
    """
    Details of an article
    """
    def __init__(self,author,title,description,url_to_image,url,published_at):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.published_at = published_at
        self.url_to_image = url_to_image
        
        
                