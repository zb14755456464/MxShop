def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = 'http://127.0.0.1:8000/complete/weibo'
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id="2717334989",re_url=redirect_url)
    print(auth_url)

def get_access_token(code='cd3bcdad7d73f9bf9b60b621ebec839a'):
    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    import requests
    re_dict = requests.post(access_token_url,data={
        "client_id":"2717334989",
        "client_secret":"eb24e184aa12e66c76066a18d59a5037",
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://127.0.0.1:8000/complete/weibo"

    })

    print(re_dict.text)
    """
    {"access_token":"2.00BsFdOHhxetxCb9a33ee55bw3SS6E","remind_in":"157679999","expires_in":157679999,"uid":"6629115889","isRealName":"true"}
    """

def get_user_info(access_token='2.00BsFdOHhxetxCb9a33ee55bw3SS6E'):
    user_show = "https://api.weibo.com/2/users/show.json?&access_token={access}&uid={uuid}".format(access=access_token,uuid='6629115889')
    print(user_show)


if __name__ == '__main__':
    get_user_info()
