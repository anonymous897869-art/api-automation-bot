import requests

url = "https://api.agify.io/?name=suryansh"

response = requests.get(url)
data = response.json()

print("👤 Name:", data["name"])
print("🎂 Predicted Age:", data["age"])
print("📊 Count:", data["count"])
