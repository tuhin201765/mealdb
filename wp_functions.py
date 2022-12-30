def list_html(line_list):
    start = '<!-- wp:list --><ul>'
    for number in line_list:
        start+= f'<!-- wp:list-item --><li>{number}</li><!-- /wp:list -->'
    ends = '</ul><!-- /wp:list -->'
    codes = start +ends

    return codes

def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key , value in dicts.items():
        start+= f'<!-- wp:list-item --><li><strong>{key.title()}</strong>: {value.title()}</li><!-- /wp:list -->'
    ends = '</ul><!-- /wp:list -->'
    codes = start + ends
    return codes


def headers(username , password):
    import base64
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    code = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return code

def image_url(src, name):
    first = '<!-- wp:image {"align":"center","sizeSlug":"large"} -->'
    middle = f'<figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{name}"/>'
    last = f'<figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    code = f'{first}{middle}{last}'
    return code


def wp_h2(text):
    return f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'

def open_ai(promt):
    import openai
    import os
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv('API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    data= response.get('choices')[0].get('text').strip()
    code = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
    return code

# print(dict_list({'tuhin':'21','name':'age'}))