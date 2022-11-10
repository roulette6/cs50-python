import re

url = input("URL: ").strip()

# re.sub(pattern, repl, string, count=0, flags=0)
# username = re.sub(r"^(https?://)?(www.)?twitter\.com\", "", url)

# notice the non capturing group for the www
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
