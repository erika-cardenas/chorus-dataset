import base64
import requests

# Set the image URL
url = 'https://www.galaxus.de/im/Files/2/9/6/1/5/8/8/3/eh-tw7000_2.jpg.jpg?impolicy=ProductTileImage&resizeWidth=992&resizeHeight=504&cropWidth=992&cropHeight=504&quality=high'

# Retrieve the image data
response = requests.get(url)
image_data = response.content

# Encode the image data as Base64
base64_image = base64.b64encode(image_data).decode('utf-8')

# Output the Base64-encoded value
print(base64_image)
