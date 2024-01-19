from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def generate_band_names(music_genre, sub_genre):
    name_chain = LLMChain(
            llm=OpenAI(temperature=0.75), 
            prompt=PromptTemplate(
                input_variables=['music_genre', 'sub_genre'],
                template="I have a {music_genre} music group that falls into the {sub_genre} category and I want a cool name for it. Suggest me five cool names for my music group"
            )
        )
    return name_chain({'music_genre': music_genre, 'sub_genre': sub_genre})


if __name__ == "__main__":
    print (generate_band_names("EDM", "SpaceBass"))