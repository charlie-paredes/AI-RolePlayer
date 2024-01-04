from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(request):
    if request.method == 'POST':
        character_choice = request.POST.get('character_choice', '')
        media = request.POST.get('media', '')
        user_input = request.POST.get('user_input', '')

        user_prompt = f"respond to the following as if you were {character_choice} from {media}: {user_input}"

        # Call OpenAI API to generate text
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=user_prompt,
            max_tokens=300,
            temperature=0.5
        )

        # Log the number of tokens used
        print("Tokens used in response:", response['usage']['total_tokens'])
        
        generated_text = response.choices[0].text.strip()

        return render(request, 'generate_text.html', {'character_choice':character_choice, 'media':media, 'user_input': user_input, 'generated_text': generated_text})
    else:
        return render(request, 'generate_text.html')