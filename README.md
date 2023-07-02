# tor-protect
It capcha service for protect you onion site

Docker compouse service for protect you site.
1) install Docker <code>curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh</code>
2) install docker-compouse
   in ubuntu <code>sudo apt install docker-compose</code>
3) copy you first host to ./onion_service/hidden_service
4) edit /captcha_service/app/main.py string 56 <code>async with session.get('http://to_my_non_protect_site.onion/', max_redirects=40, ssl=False, headers=headers) as resp</code> to you site.onion
