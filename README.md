# tor-protect
It capcha service for protect you onion site 

# How to get
<code>git clone https://github.com/sypper-pit/tor-protect.git && cd tor-protect</code>

# How to start
Docker compouse service for protect you site.
1) Install Docker and docker-compouse <code>curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh && sudo apt install docker-compose</code>
2) Copy you first host and keys to <code>./onion_service/hidden_service</code> ! <b>You external onion site</b> !
3) Edit <code>nano captcha_service/app/protect_me.cfg</code> to you onion site for protect ! <b>You hiden for all onion site</b> !
4) Run <code>docker-compouse up -d</code>


# How it work
hidden_service(user see it) -> main.py(capcha+proxy) -> tor_proxy -> protect_me.cfg(onion site): <br>
<b>site1.onion</b> ->->-> <b>site2.onion(you_secret_url)</b>



<h3>Your hidden_service and protect_me.cfg must not match!</h3>

donate:

TGCfuRND26Wfq1Wo5fvEHtvCsEpSHL1hfr USDT trc20

1CJyUNK3Buc8HZNipfPwf4DoQNT1PiQGxJ bitcoin

D6VpypvojNazF4febbviDFYHevHQLXH6gm doge
