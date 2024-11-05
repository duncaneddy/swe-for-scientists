import httpx

client = httpx.Client(base_url="http://127.0.0.1:8000")

response = client.get("/")
print("GET to /: " + str(response.json()))

response = client.post("/hello", json={"name": "Alice"})
print("POST to /hello: " + str(response.json()))