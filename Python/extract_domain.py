#function that when given a URL as a string, parses out just the domain name and returns it as a string.
#domain_name("http://github.com/carbonfive/raygun") == "github" 

def domain_name(url):
    link = url.split('://')[-1].split('.')
    domain = ''
    if "www" in link:
      domain = link[1]
    else:
      domain = link[0]
    return domain
  
if __name__ == __main__:
  urls = ["http://google.com", "http://google.co.jp", "www.xakep.ru", "https://youtube.com"]
  for url in urls:
    print(domain_name(url))
