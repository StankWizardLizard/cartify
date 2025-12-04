from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
import requests
import csv
import os

if(__name__ == '__main__'):

    # Load Nintendo Switch font
    try:
        print('[+] Fetching nintendo switch font')
        font = ImageFont.truetype(r'assets/switch-font.ttf', 45)
    except Exception as e:
        print('[!] Error loading switch font, Exiting...')
        print(e)
        exit()

    # Load Nintendo Switch cartridge template
    try:
        print('[+] Fetching switch cartridge template')
        template = Image.open(r'assets/switch-cart.png').convert('RGBA')
    except Exception as e:
        print('[!] Error loading switch cartridge template, Exiting...')
        print(e)
        exit()

    # Open titles file generated from switch console
    try:
        print('[+] Fetching titles')
        with open('assets/titles.csv','r') as title_handle:
            
            # Create dir if it doesnt exist already
            if(not os.path.exists('contents')):
                os.mkdir('contents')

            # Load csv file
            reader_object = csv.DictReader(title_handle, delimiter='|')
    
            # Iterate through each entry in titles
            for entry in reader_object:

                print()

                # Extract values for each entry
                title_id = entry['Title ID']
                title_name = entry['Title Name']

                print(f'[+] Processing title: {title_name}')

                # Cover exception case where title code isnt known
                try:
                    title_code = entry['Title Code']
                except:
                    title_code = None

                # Create dir if it doesnt exist already
                if(not os.path.exists(f'contents/{title_id}')):
                    os.mkdir(f'contents/{title_id}')

                # Generate media fetch url
                title_art_url = f'https://tinfoil.media/ti/{title_id}/512/512'

                # Start fetch request for media image
                try:
                    print(f'[+] Fetching title icon at: {title_art_url}')

                    # Create fetch request for media image
                    response = requests.get(title_art_url)

                    # Check if response checks out and write reply into file
                    if(response.status_code == 200):
                        # Save contents of request as a jpg
                        with open(f'contents/{title_id}/raw.jpg', 'wb') as image_handle:
                            image_handle.write(response.content)
                    else:
                        raise Exception(f'Unexpected response code from net request: {response.status_code}')

                except Exception as e:
                    print('[!] Error fetching title icon, Skipping...')
                    print(e)
                    continue

                # Start formatting images
                try:
                    print(f'[+] Processing title icon')
                    
                    # Load Raw Image
                    raw_image = Image.open(fr'contents/{title_id}/raw.jpg').convert('RGBA')

                    # Create Image Base
                    base_image = Image.new('RGB', (600,900))

                    # Insert title image into base image
                    base_image.paste(raw_image, (43, 217), raw_image)

                    # Insert cartridge template over base image
                    base_image.paste(template, (0,0), template)

                    # Check if there is a provided Title Code
                    if(title_code != None):
                        # Convert image to draw object
                        cart = ImageDraw.Draw(base_image)

                        # Paste Title Code onto image centered
                        cart.text((300, 760), title_code, font=font, anchor='mm')
                    
                    # TODO REMOVE THIS LINE IN FINAL
                    base_image.save(f'contents/{title_id}/original.jpg', 'JPEG', quality=100)

                    # Resize base image for aspect ratio
                    base_image = base_image.resize((256,256), Image.LANCZOS)

                    # Save finished image
                    print(f'[+] Saving title icon')
                    base_image.save(f'contents/{title_id}/icon.jpg', 'JPEG', quality=100)

                    # Delete raw image
                    os.remove(f'contents/{title_id}/raw.jpg')

                except Exception as e:
                    print('[!] Error formatting image, Skipping...')
                    print(e)
                    continue

    except Exception as e:
        print('[!] Error loading titles, Exiting...')
        print(e)
