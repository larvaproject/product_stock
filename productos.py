import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from urllib.request import urlopen
import urllib.request
import json

def main():
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)

	#Extraemos los valores
	sheet = client.open("Product Units")
	worksheet = sheet.get_worksheet(1)
	products = worksheet.col_values(1)

	print(products)

	#Para 
	worksheet = sheet.get_worksheet(0)

	insertRow = []
	count = 2
	"""products = ["1063584", "870112", "1137235", "761128", "972677", "1088019", "1080739", "1141844", "784545", "941151", "761453",
	"712373", "1050589", "1066926", "1160560", "1069422", "973189", "1139268", "840140", "1160363", "945537", "1147531", "721385",
	"802119", "858305", "750192"]"""

	worksheet.clear()
	cols = ["ID", "PRODUCTO", "STOCK"]
	worksheet.insert_row(cols, 1)

	for prod in products:
		url = 'https://csapi.claroshop.com/producto/'+ prod
		webUrl = urllib.request.urlopen(url)
		data = json.loads(webUrl.read().decode())

		index_count = worksheet.row_count

		id_m = data["data"]["id"]
		nombre = data["data"]["title"]
		stock =  data["data"]["stock"]

		insertRow = [id_m, nombre, stock]
		worksheet.insert_row(insertRow, count)

		count +=1

if __name__ == "__main__":
	main()