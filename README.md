## randomheader

Generates random HTTP headers for requests

### install
```
pip install randomheader
```

### usage

```python
from randomheader import RandomHeader

rh = RandomHeader()

print(rh.header())

```

### example header

```json
{
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "X-Forwarded-For": "16.64.120.135",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
    "Dnt": "0",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://bild.de/"
 }
```