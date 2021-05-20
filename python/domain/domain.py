def domain_name(url):
    domain = url
    if (url.find("//") != -1):
        domain = url[(url.find("//"))+2:url.find("."):]
    if (url.find("www.") != -1):
        domain = url[(url.find("www."))+4::]
        domain = domain[:domain.find("."):]
    if ((url.find("//") == -1) and (url.find("www.") == -1)):
        domain = domain[:domain.find("."):]
    return domain

input = "youtube.com"

print(domain_name(input))

# test.assert_equals(domain_name("http://google.com"), "google")
# test.assert_equals(domain_name("http://google.co.jp"), "google")
# test.assert_equals(domain_name("www.xakep.ru"), "xakep")  
# test.assert_equals(domain_name("https://youtube.com"), "youtube")