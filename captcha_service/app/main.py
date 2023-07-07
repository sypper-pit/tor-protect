from fastapi import FastAPI, Request, HTTPException, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from redis import Redis
from captcha.image import ImageCaptcha
import aiohttp
from aiohttp_socks import ProxyConnector
from aiohttp import ClientSession
import uuid
import random
import io
import base64

class CaptchaInput(BaseModel):
    captcha_text: str

app = FastAPI()

image_captcha = ImageCaptcha()
redis_client = Redis(host='redis', port=6379, db=0)

templates = Jinja2Templates(directory="templates/")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

@app.get("/")
async def read_root(request: Request, response: Response):
    session_id = str(uuid.uuid4())
    captcha_text = ''.join(random.choices('0123456789', k=4))
    data = image_captcha.generate(captcha_text)
    redis_client.setex(session_id, 900, captcha_text)

    captcha_image_base64 = base64.b64encode(data.read()).decode()

    response.set_cookie(key="session_id", value=session_id)

    return templates.TemplateResponse("captcha.html", {"request": request, "captcha_image": captcha_image_base64, "session_id": session_id})

@app.post("/validate_captcha/{session_id}")
async def validate_captcha(session_id: str, response: Response, captcha_text: str = Form(...)):

    real_captcha_text = redis_client.get(session_id)
    if not real_captcha_text:
        raise HTTPException(status_code=400, detail="Invalid session ID")
    if real_captcha_text.decode() != captcha_text:
        raise HTTPException(status_code=400, detail="Invalid captcha")

    connector = ProxyConnector.from_url('socks5://tor-proxy:9050', rdns=True)

    async with ClientSession(connector=connector) as session:
        try:
            async with session.get('http://to_my_non_protect_site.onion/', max_redirects=40, ssl=False, headers=headers) as resp:
                content = await resp.text()
        except aiohttp.client_exceptions.TooManyRedirects:
            raise HTTPException(status_code=400, detail="Too many redirects")

    return HTMLResponse(content=content, status_code=200)
