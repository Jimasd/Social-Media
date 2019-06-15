from Secret import get_fb_access_token

import facebook
import json

ACCESS_TOKEN = get_fb_access_token()

def pretty_print(o):
    print(json.dumps(o, indent=1))

fb_graph =  facebook.GraphAPI(ACCESS_TOKEN)

pretty_print(fb_graph.get_object("me"))
pretty_print(fb_graph.get_connections(id="me", connection_name="likes"))
pretty_print(fb_graph.request("search", {"type": "place",
                                         "center": "40.749444, 73.968056",
                                         "fields": "name, location"
                                         }))