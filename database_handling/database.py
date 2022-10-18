import psycopg2
import urllib.parse as up

# up.uses_netloc.append("postgres")
# url = 'postgres://sumpjdbw:uFahG7XpJSVCFfFre1yEdThagq2R766x@mouse.db.elephantsql.com/sumpjdbw'
# url = up.urlparse(url)
# conn = psycopg2.connect("dbname='sumpjdbw' user='sumpjdbw' password='uFahG7XpJSVCFfFre1yEdThagq2R766x' host='mouse.db.elephantsql.com'")
conn = psycopg2.connect("dbname='sumpjdbw' user='sumpjdbw' host='mouse.db.elephantsql.com' password='uFahG7XpJSVCFfFre1yEdThagq2R766x'")
# cursor = connection.cursor()