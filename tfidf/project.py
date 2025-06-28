# 1. Adım: Hikayeleri ve Soruyu Tanımla

# hikayeler = [
#     "Ormanda kaybolan bir grup maceracı vardı.",
#     "Küçük bir köyde herkes birbirine yardım ederdi.",
#     "Bir gün deniz kenarında ilginç bir taş bulundu.",
#     "Şehirde büyük bir festival düzenlendi.",
#     "Yaşlı adam her sabah parkta yürüyüş yapardı.",
#     "Çocuklar okul bahçesinde oyun oynuyordu.",
#     "Bir köpek sahibini bulmak için uzun bir yolculuğa çıktı.",
#     "Kütüphanede eski bir kitap keşfedildi.",
#     "Dağ köyünde bir gece fırtına çıktı.",
#     "Genç kadın yeni bir işe başladı."
# ]

# soru = "Ormanda ne oldu?"


# 2. Adım: Embedding (Vektörleştirme)
# # Hikayeleri ve soruyu TF-IDF ile vektörleştireceğiz.

# from sklearn.feature_extraction.text import TfidfVectorizer #TfidfVectorizer: Metinleri sayısal vektörlere (embedding) dönüştürmek için kullanılır. Her kelimenin önemini ölçer.

# # Tüm metinleri (hikayeler + soru) birleştir
# tum_metinler = hikayeler + [soru]

# # TF-IDF vektörleştirici oluştur
# vectorizer = TfidfVectorizer()
# tfidf_matrisi = vectorizer.fit_transform(tum_metinler) #fit_transform: tüm_metinler listesindeki her metni sayısal vektöre çevirir. Sonuç: (11, n) boyutunda bir matris (11 metin, n kelime).
 
# # Hikaye ve soru embeddinglerini ayır
# hikaye_embedding = tfidf_matrisi[:-1] #hikaye_embeddingleri: Son satır hariç tüm satırlar (ilk 10 satır) hikaye embeddingleri olur.

# # soru_embedding: Son satır ([-1]) soru embeddingidir.
# soru_embedding = tfidf_matrisi[-1]


# 3. Adım: Cosine Similarity Hesapla

# Her hikaye ile sorunun embedding'i arasındaki benzerliği bulalım.

# from sklearn.metrics.pairwise import cosine_similarity #İki vektör arasındaki benzerliği (cosine similarity) hesaplar.
# import numpy as np #numpy: Sayısal işlemler ve diziler için kullanılır (en yüksek değerin indeksini bulmak gibi).

# # Soru ile tüm hikayeler arasındaki cosine similarity
# benzerlikler = cosine_similarity(soru_embedding, hikaye_embedding).flatten()  
# # cosine_similarity: Soru embedding'i ile tüm hikaye embedding'leri arasındaki benzerliği hesaplar.
# # flatten(): Sonucu tek boyutlu diziye çevirir (10 elemanlı bir liste).


# 4. Adım: En Yüksek Benzerliği Bul

# En yüksek benzerliğe sahip hikayeyi bulalım.

# en_yuksek_indeks = np.argmax(benzerlikler)  #np.argmax: En yüksek benzerlik değerinin indeksini bulur.
# en_yuksek_benzerlik = benzerlikler[en_yuksek_indeks] #
# en_uygun_hikaye = hikayeler[en_yuksek_indeks]

# 5. Adım: Sonucu Yazdır

# Sonucu ekrana yazdıralım.

# print("En yüksek cosine similarity:", en_yuksek_benzerlik)
# print("En uygun hikaye:", en_uygun_hikaye)


# TF-IDF'de Birleştirmenin Sebebi (tum_metinler = hikayeler + [soru])
# 1. Ortak Kelime Sözlüğü Oluşturmak
# TF-IDF algoritması, tüm metinlerde geçen kelimelerden bir "kelime sözlüğü" (vocabulary) oluşturur.
# Eğer hikayeleri ve soruyu ayrı ayrı vektörleştirirsek, iki farklı kelime sözlüğü oluşur. Yani, vektörlerin boyutları ve sıralamaları farklı olur.
# Aynı kelime farklı indekslerde olabilir veya bir metinde olup diğerinde olmayan kelimeler vektörde sıfır olur.
# Sonuç olarak, iki farklı kelime uzayında oluşan vektörlerin birbiriyle benzerliğini (cosine similarity) karşılaştırmak anlamsız ve yanlış olur.

# 2. Aynı Boyutta ve Sıralamada Vektörler
# Tüm metinleri birleştirip tek seferde vektörleştirirsen, hem hikayeler hem soru aynı boyutta ve aynı kelime sıralamasında vektörlere sahip olur.
# Böylece, cosine similarity ile doğru şekilde karşılaştırabilirsin.
# Birleştirerek vektörleştirmek, hem hikayeler hem soru için aynı kelime uzayında, karşılaştırılabilir vektörler üretir.
# Bu yüzden, TF-IDF ile embedding işlemlerinde tüm metinleri tek seferde vektörleştirmek en doğru yoldur.


