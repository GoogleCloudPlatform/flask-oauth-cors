# A small class that helps with authentication and CORS for HTTP-triggered cloud functions written in Python and hosted on GCP

_Please note: This is not an officially supported Google product._

If you are using OAuth to authenticate to a [Cloud Function written in Python](https://cloud.google.com/functions/docs/concepts/python-runtime) and hosted on GCP, and your client is running in a browser, this is for you. If not, you probably won't find this useful.

This class does two things:

* Responds correctly and configurably to the HTTP OPTIONS method used by browsers to do pre-flight checks as part of CORS
* Retrieves an OAuth2 token supplied in the `Authorization` HTTP header, validates it, and then fetches the information encoded by the token
* Gives you back either a valid token, or a response to send back to the user in case a valid token can't be found

## Use

If you don't have one, [create an OAuth client ID](https://developers.google.com/identity/protocols/OAuth2WebServer) and [pass it as an environment variable](https://cloud.google.com/functions/docs/env-var) to your cloud function. Then, you can use the following: 

```
import gcloud_flask_oauth_cors as oauth

def my_function_name(request):
    auth = oauth.Auth(os.getenv("OAUTH_CLIENT_ID"))
    id_info = auth.get_id_info(request)
    if id_info is None:
        # If we were called with the HTTP OPTIONS method, this will return the relevant CORS headers.
        # If another HTTP method was used and we can't authenticate, this will return a 401 (Unauthorized)
        return auth.get_response()

    # Do something with the id_info, for example:
    print(id_info["sub"])
```

On the client side, you can use [Google Sign-in](https://developers.google.com/identity/sign-in/web/). Make sure you pass your `id_token` in any requests like this:

```
let xhr = new XMLHttpRequest();
xhr.setRequestHeader("Authorization", "Bearer " + id_token);
```