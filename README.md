# tor-protect
It capcha service for protect you onion site 

# How to get
<code>git clone https://github.com/sypper-pit/tor-protect.git && cd tor-protect</code>

# How to start
Docker compouse service for protect you site.
1) Install Docker and docker-compouse <code>curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh && sudo apt install docker-compose</code>
2) Copy you first host and keys to ./onion_service/hidden_service
3) Edit <code>nano captcha_service/app/protect_me.cfg</code> to you onion site
4) Run <code>docker-compouse up -d</code>


donate:

TGCfuRND26Wfq1Wo5fvEHtvCsEpSHL1hfr USDT trc20

1CJyUNK3Buc8HZNipfPwf4DoQNT1PiQGxJ bitcoin

D6VpypvojNazF4febbviDFYHevHQLXH6gm doge
