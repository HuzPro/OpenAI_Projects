import openai
import webbrowser

# I prefer edge but you can use any supported browser.
edge = # Path to browser executable.


print("\033[35;1;4mWelcome to the DALL-E the image generating AI! Enter 'exit' to end the conversation.\x1b[0m")
while True:
    prompt = input("\033[36;1mEnter the prompt to generate image: \x1b[0m")
    if prompt.lower() == "exit":
        break
    numberOfImages = int(input("\033[36;1mNumber of images to generate: \x1b[0m"))
    while True:
        # There are 3 possible sizes you can generate images for, 256x256, 512x512, 1024x1024. 
        sizeOption = int(input("\033[36;1mSizes:\x1b[0m \033[34m\n1.256x256 \n2.512x512 \n3.1024x1024\nPick a size (1, 2 or 3): \x1b[0m"))
        if sizeOption == 1:
            res = "256x256"
            break
        elif sizeOption == 2:
            res = "512x512"
            break
        elif sizeOption == 3:
            res = "1024x1024"
            break
        else:
            print("\033[31;1mIncorrect option entered.\x1b[0m")
    
    # Using openai API to generate a response.
    # See https://platform.openai.com/docs/guides/images/usage for more info.
    response = openai.Image.create(
      prompt=prompt,
      n=numberOfImages,
      size=res
    )
    
    image_urls = []
    # Appending all the urls generated into a list.
    for image in range(numberOfImages): image_urls.append(response['data'][image]['url'])
    
    # Opening the urls in the browser.
    for url in image_urls:
        webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge))
        webbrowser.get("edge").open_new_tab(url)
