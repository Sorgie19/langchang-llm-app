from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

#load_dotenv()

def generate_band_names(music_genre, sub_genre, openai_api_key, amount):
    llm = OpenAI(api_key=openai_api_key, temperature=0.75)
    prompt_template_name = PromptTemplate(
        input_variables=['music_genre', 'sub_genre', 'amount'],
        template = "I have a {music_genre} music group that falls into the {sub_genre} category and I want a cool name for it. Suggest me {amount} cool names for my music group"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="band_names")

    response = name_chain({'music_genre': music_genre, 'sub_genre': sub_genre, 'amount': amount})
    return response


if __name__ == "__main__":
    print (generate_band_names("EDM", "SpaceBass"))