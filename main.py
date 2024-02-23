import os
import openai
import random
from dotenv import load_dotenv
from player import nova_rift

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_log = []
def introduction():
    intro_prompt = '''You are a dungeon master running a game of Dungeons and Dragons. Describe the dark fantasy world where the adventure 
    starts and introduce the initial setting and quest for the player character, who's name and attributes are {}. Then, start the game off
    with an event.'''.format(nova_rift)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": intro_prompt},
        ]
    )
    
    chat_log.append(response)

    # Print the introductory story
    print(response.choices[0].message['content'] + "\n")


# Roll a d20
def roll_d20():
    """Rolls a virtual 20-sided die."""
    return random.randint(1, 20)
    # return 20


def main():
    playing = True

    # Introduction to the game
    introduction()

    while playing:
        # Prompt the user for their input
        user_input = input()

        # Roll a dice for the turn
        dice_roll = roll_d20()

        # Display the dice roll results
        roll_description = "Critical hit!" if dice_roll == 20 else "Critical miss!" if dice_roll == 1 else f"You rolled a {dice_roll}."
        print(roll_description)

        # D&D prompt for GPT-3.5-turbo
        prompt = f'''You are a dungeon master running a game of Dungeons and Dragons. Based on the player's dice roll, steer the course of 
        the game. A high roll (15-20) leads to favorable outcomes or successful skill checks. A low roll (1-5) results in challenges or failed 
        checks. Rolls in between (6-14) offer mixed results. Implement skill checks when appropriate, considering the player's strengths and 
        weaknesses. 

        Character: {nova_rift}
        Roll: {dice_roll} - {roll_description}
        '''

        # Append the current turn to the chat log
        chat_log.append({"role": "system", "content": prompt})

        # Convert the chat log to a string
        chat_log_str = ' '.join(str(chat) for chat in chat_log)

        # Call the OpenAI API with the updated chat log
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": chat_log_str}
            ],
        )

        # Print the AI's response
        print(response.choices[0].message['content'])


if __name__ == "__main__":
    main()
