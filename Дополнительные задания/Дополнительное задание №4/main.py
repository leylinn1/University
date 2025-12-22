import re
import csv
import urllib.request

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry"

page = urllib.request.urlopen(url)
text = page.read().decode("utf-8")

reg = r'(?:class="org-widget-header__title-link"[^>]*>)(?P<Name>[^<]+)</a>(?:.*?class="[^"]*org-widget-header__meta--location"[^>]*>\s*)(?P<Address>[^<]+)</span>(?:.*?Телефон</span></dt>\s*<dd class="spec__value">\s*(?P<Phone>[^<]+)</dd>)?(?:.*?Часы работы</span></dt>\s*<dd class="spec__value">\s*(?P<WorkHours>[^<]+)</dd>)?'

result = re.findall(reg, text, re.S)
print(f": {len(result)}")

f = open("result.csv", "w", encoding="utf-8")
f.write("Name,Address,Phone,Hours\n")

for item in result:
    n = item[0].strip()
    a = item[1].strip()
    p = item[2].strip()
    h = item[3].strip()

    if not p:
        p = "-"
    if not h:
        h = "-"

    line = n + ',"' + a + '","' + p + '","' + h + '"\n'

    f.write(line)

f.close()
print("готово")
