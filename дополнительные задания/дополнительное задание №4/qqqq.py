import re
import urllib.request
import csv

base_url = "https://msk.spravker.ru/avtoservisy-avtotehcentry"

with urllib.request.urlopen(base_url) as response:
    page_content = response.read().decode("utf-8")

capture_pattern = r'(?:class="org-widget-header__title-link"[^>]*>)(?P<Name>[^<]+)</a>(?:.*?class="[^"]*org-widget-header__meta--location"[^>]*>\s*)(?P<Address>[^<]+)</span>(?:.*?Телефон</span></dt>\s*<dd class="spec__value">\s*(?P<Phone>[^<]+)</dd>)?(?:.*?Часы работы</span></dt>\s*<dd class="spec__value">\s*(?P<WorkHours>[^<]+)</dd>)?'

all_hits = re.findall(capture_pattern, page_content, re.S)
print(f"Общее количество найденных элементов: {len(all_hits)}")

data_to_write = []
for entry in all_hits:
    obj_name = entry[0].strip()
    obj_addr = entry[1].strip()
    obj_phone = entry[2].strip()
    obj_hours = entry[3].strip()

    if not obj_phone:
        obj_phone = "-"
    if not obj_hours:
        obj_hours = "-"
    
    data_to_write.append([obj_name, obj_addr, obj_phone, obj_hours])


output_filename = "result1.csv"
headers = ["Name", "Address", "Phone", "Hours"]

try:
    with open(output_filename, mode="w", newline="", encoding="utf-8") as file_handle:
        writer = csv.writer(file_handle)
        writer.writerow(headers)
        writer.writerows(data_to_write)
    print("Задача завершена")
except IOError as e:
    print(f"Ошибка при записи в файл {output_filename}: {e}")


