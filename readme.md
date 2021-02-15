# pAyPI, a fake payment gateway.

## installation
```sh
git clone https://github.com/JakeIsMeh/fakepaymentgateway.git
cd fakepaymentgateway
# --upgrade-deps only works on python 3.8+
py -m venv venv --upgrade-deps # remember to activate venv immediately
. venv/Scripts/activate # activating venv
(venv) pip install wheel # important!
(venv) pip install flask requests
```

## usage
### configuration
set the endpoint in  `__init__.py`

### api reference
adding:
`/api/add?ref=[REF]&amt=[AMT]&method=[METHOD]`

approving:
`/api/[REF]/approve`

denying:
`/api/[REF]/deny`

when approving/denying we attempt to send a GET request to the appropriate endpoint to change the status on the client's side.