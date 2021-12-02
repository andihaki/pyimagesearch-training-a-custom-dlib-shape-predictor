await fetch("https://ibug.doc.ic.ac.uk/download/annotations/300w.zip.001/", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    },
    "referrer": "https://ibug.doc.ic.ac.uk/download/annotations/300w.zip.001/",
    "body": "csrfmiddlewaretoken=7Bvh2D3dDUgDyd4C5rfIGLLAFlCiFEMx&first_name=andi&last_name=hakim+arif&email_address=1911601431%40student.budiluhur.ac.id&affiliation=university",
    "method": "POST",
    "mode": "cors"
});

!wget --post-data 'csrfmiddlewaretoken=7Bvh2D3dDUgDyd4C5rfIGLLAFlCiFEMx&first_name=andi&last_name=hakim+arif&email_address=1911601431%40student.budiluhur.ac.id&affiliation=university' https://ibug.doc.ic.ac.uk/download/annotations/300w.zip.001/

!wget --header "Cookie: csrftoken=7Bvh2D3dDUgDyd4C5rfIGLLAFlCiFEMx" \
--post-data "csrfmiddlewaretoken=7Bvh2D3dDUgDyd4C5rfIGLLAFlCiFEMx&first_name=andi&last_name=hakim+arif&email_address=1911601431%40student.budiluhur.ac.id&affiliation=university" \
--save-cookies cookies.txt \
https://ibug.doc.ic.ac.uk/download/annotations/300w.zip.001/

!wget -c --load-cookies cookies.txt \
https://ibug.doc.ic.ac.uk/download/annotations/300w.zip.001/