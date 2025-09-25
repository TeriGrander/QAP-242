def generate_urls(url, start, end):
    for i in range(start, end+1):
        yield url + str(i)


url_generator = generate_urls("/product/", 1, 3)
for url in url_generator:
   print(url)
# /product/1
# /product/2
# /product/3

print(list(generate_urls("https://example.com/page_", 1, 5)))