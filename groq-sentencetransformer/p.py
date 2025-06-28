
# # kutuphaneler
# # env dosyası
# # hikaye
# # soru 
# # embedding modeli
# # embedding yapma kısmı
# # cosine similarity
# # prompt olustur
# # api call
# # yazdir

# from sentence_transformer import SentenceTrasformer
# stories = ["","","",""]
# soru = "soru"
# embed_model = SentenceTransformer("sentence-transformer/......")
# emb_story = embed_model.encode(stories)
# emb_ques = emb_ques.encode(soru)


# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# similarities = cosine_similarity([emb_ques], emb_story)
# best_match_idx = np.argmax(similarities)
# best_story = stories[best_match_idx]


# from groq import Groq
# import os
# from dotenv import load_dotenv
# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")
# client = Groq(api_key = groq_api_key)
# prompt = f""" Kullanıcı sorusu:{soru} , ilgili hikaye:{best_stories} Bu bilgilerle kullanıcı sorusunu cevapla"""

# response = client.chat.completions.create(
#   messages = [
#     "role":"system" "content":"",
#     "role":"user" "content":prompt
#   ],
#   model = "llama3-70b-8192",
#   temprature = 0.7,
#   max_tokens = 500
# )

# print("cevap", response.choises[0].message.content)
# print("ilgili hikaye", best_story)
