from Secret import get_linkedin_token
from linkedin import linkedin

APPLICATION_KEY, APPLICATION_SECRET, RETURN_URL = get_linkedin_token()

auth = linkedin.LinkedInAuthentication(APPLICATION_KEY, APPLICATION_SECRET, RETURN_URL)
auth.authorization_code = input("Manually input the code after '?code=...' in\n{}\nHere: ".format(auth.authorization_url))
auth.authorization_code = auth.authorization_code.split("&state=")[0]
result = auth.get_access_token()
app = linkedin.LinkedInApplication(token=result.access_token)

print("Access Token:", result.access_token)
print("Expires in (seconds):", result.expires_in)
app.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}],
                   params={'keywords': 'apple microsoft'})