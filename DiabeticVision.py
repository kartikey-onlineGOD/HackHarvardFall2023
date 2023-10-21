import requests

API_URL = "https://api-inference.huggingface.co/models/Kontawat/vit-diabetic-retinopathy-classification"
headers = {"Authorization": f"Bearer {'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'}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("15_left.jpeg")
print(output)
