#app.wsgi
import sys
sys.path.insert(0, '/var/www/html/placement_chatbot')

from placement_chatbot import app as application