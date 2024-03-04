import pandas as pd
import numpy as np

sentences = [
    "As spring unfolds, the warmth of the season encourages the first blossoms to open, signaling longer days ahead.",
    "Spring brings not only blooming flowers but also the anticipation of sunny days and outdoor activities.",
    "With the arrival of spring, people begin planning their summer vacations, eager to enjoy the seasonal warmth.",
    "The mild spring weather marks the transition from the cold winter to the inviting warmth of summer.",
    "During spring, families often start spending more time outdoors, enjoying the season's pleasant temperatures and the promise of summer fun.",
    "Summer continues the season's trend of growth and warmth, with gardens full of life and days filled with sunlight.",
    "The summer season is synonymous with outdoor adventures and enjoying the extended daylight hours that began in spring.",
    "As summer arrives, the warm weather invites a continuation of the outdoor activities that people began enjoying in spring.",
    "The transition into summer brings even warmer temperatures, allowing for beach visits and swimming, much awaited since the spring.",
    "Summer vacations are often planned as the days grow longer, a pattern that starts in the spring, culminating in peak summer leisure."
]

all_words = set()
for sentence in sentences:
    words = [word.strip(".,!?") for word in sentence.split()]
    all_words.update(words)

word_counts = {}
for word in all_words:
    word_counts[word] = []


for sentence in sentences:
    sentence_word_count = {word: sentence.split().count(word.strip(",.!?")) for word in all_words}
    for word, count in sentence_word_count.items():
        #print(count)
        #print(word)
        word_counts[word].append(count)

word_count_df = pd.DataFrame(word_counts)

word_count_df = word_count_df.fillna(0)
print(word_count_df)

from numpy.linalg import norm
def cosineSimilarity(vec1, vec2):
    V1 = np.array(vec1)
    V2 = np.array(vec2)
    cosine = np.dot(V1, V2)/(norm(V1)*norm(V2))
    return cosine

heatmap_matrix = []
for i in range(len(sentences)):
    similarity_row = []
    for j in range(len(sentences)):
        similarity = cosineSimilarity(word_count_df.iloc[i], word_count_df.iloc[j])
        similarity_row.append(similarity)
    heatmap_matrix.append(similarity_row)

heatmap_matrix_df = pd.DataFrame(heatmap_matrix, index = sentences, columns = sentences)

print(heatmap_matrix_df)
