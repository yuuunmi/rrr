from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# 観光地のテキストデータ
landmark_descriptions = [
    "東京タワーは東京の代表的な観光名所です。",
    "大阪城は大阪市内にある歴史的な建造物です。",
    "京都の清水寺は日本でも有名な仏教寺院です。",
    "北海道の旭山動物園は人気のある動物園です。"
]

# TfidfVectorizerを使用してテキストデータをベクトル化
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(landmark_descriptions)

# 観光地の類似度行列を計算
similarity_matrix = cosine_similarity(feature_vectors)

# 類似度行列を表示
for i in range(len(landmark_descriptions)):
    for j in range(len(landmark_descriptions)):
        print(f"観光地{i+1}と観光地{j+1}の類似度: {similarity_matrix[i][j]}")