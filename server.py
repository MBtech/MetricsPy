import falcon
import shlex
import subprocess
 
#How to run the server
#uwsgi --http :8082 --wsgi-file server.py --callable wsgi_app
class RawCMD(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        params = req.query_string.split('&')
        for i in range(0,len(params)):
        	param_dict[params[i].split('=')[0]] = params[i].split('=')[1]
        print param_dict
        args = shlex.split(param_dict['cmd'])
        p = subprocess.Popen(args, stdout=subprocess.PIPE,
        	stderr=subprocess.PIPE)
        out,err = p.communicate()
        resp.body = out

class Mpstat(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        params = req.query_string.split('&')
        print params
        param_dict = dict()
        print params[0].split('=')[0]
        for i in range(0,len(params)):
        	param_dict[params[i].split('=')[0]] = params[i].split('=')[1]
        print param_dict
        p = subprocess.Popen(['top', '-i', '1', '-l' ,'2'], stdout=subprocess.PIPE,
        	stderr=subprocess.PIPE)
        out,err = p.communicate()
        resp.body = out
 
# falcon.API instances are callable WSGI apps
wsgi_app = api = falcon.API()
 
# Resources are represented by long-lived class instances
rawcmd = RawCMD()
 
# things will handle all requests to the '/things' URL path
api.add_route('/rawcmd', rawcmd)
api.add_route('/mpstat', mpstat)