def domain_name(url):
 return url.split("//")[-1]#.split("www.")[-1].split(".")[0]

input = "http://www.youtube.com"

print(domain_name(input))

# test.assert_equals(domain_name("http://google.com"), "google")
# test.assert_equals(domain_name("http://google.co.jp"), "google")
# test.assert_equals(domain_name("www.xakep.ru"), "xakep")  
# test.assert_equals(domain_name("https://youtube.com"), "youtube")