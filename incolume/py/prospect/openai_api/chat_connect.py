import openai
import dotenv
import os
import logging

__author__ = "@britodfbr"  # pragma: no cover
dotenv.load_dotenv()
TOKEN = os.environ.get('OPENAI_KEY')

logging.debug(TOKEN)

openai.api_key = TOKEN


def get_api_response(
    prompt: str, model: str = None,
    temperature: float = 0, max_tokens: int = 0,
    top_p: float = 1,
    frequency_penalty: float = 0,
    presence_penalty: float = 0,
) -> str | None:
    text: str | None = None
    model = model or 'text-davinci-003'
    temperature = temperature or .9
    max_tokens = max_tokens or 150
    presence_penalty = presence_penalty or .6
    try:
        response: dict = openai.Completion.create(
            model=model,
            prompt='',
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
        )
    except Exception as e:
        logging.error(e)


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    prompt_list: list[str] = ['You are a potato and will answer as a potato',
                              '\nHuman: What time is it?',
                              '\nAI: I have no idea, I\'m a potato!']

    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')


if __name__ == '__main__':
    main()
