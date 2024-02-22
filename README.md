# Authorship-Identification-with-NLP

This repository conducts ongoing research in authorship attribution, see [Google Slides](https://docs.google.com/presentation/d/13mFosSg35QnXspCWcSJLv4J2v1jyebxrJwJnp7RhsjI/edit?usp=sharing) for more details.

## Learning Multi-Domain and Cross-Domain Authorship Representation

### Motivation

- Million-terabytes of contents are produced online by anonymous users every day
    - These contents inherently contain individual portrait information
    - Malicious agents may use these information to reveal their identities, which could potentially place them in danger
    - They may also generate fake contents and claim to be someone else’s opinion, thus control the public

- We are motivated to develop system to recognize and protect authorship privacy
    - We limit the content type to be text only
    - This research area is called **Authorship Attribution** (or Authorship Identification).

### Research Question

- *Given two pieces of text, are they written by the same person?*
    - We want to determine whether two documents come from the same author in a large-scale setting with hundreds of thousands of authors
    - We wish to know does author-level representation coming from one domain transfers to another domain, and whether multi-domain representations can be learned with carefully designed contrastive training objectives

- [HIATUS](https://www.iarpa.gov/research-programs/hiatus) (Human Interpretable Attribution of Text using Underlying Structure)
    - Our work is served as one of the performers in the HIATUS project
    - Teams across universities and companies compete to generate higher fidelity representations between individual authors’ unique linguistic fingerprints

### Abstract

Authorship identification and attribution aim to identify the belongings of the given text from a set of known authors. Previous approaches tried to learn author-level embeddings via contrastive learning that can be transferred to multiple domains that the author has written content about, but failed to give satisfactory results. We first scale the contrastive learning batch size beyond GPU memory constraint by using more negatives in each training batch and a larger pre-trained model backbone, then propose a data sampling and augmentation technique that greatly improves previous state-of-the-art results on multiple large-scale datasets, incorporating hard-positive and negative examples during in-batch sampling, and further augmenting this data by fine-tuning a generation model that produces the missing hard text corpora. We find that this method enables the model to focus its attention less on topic-related tokens of the authors, and more on the combination of punctuation and semantic properties, which is where its main performance improvement comes from.

[Full Paper Link](Authorship_COLM.pdf).

## (Cross-Repo) Graph-based Authorship Identification and Portrait Sketching

### Abstract

Our paper proposes a new method for authorship identification that incorporates graph structures and contrastive learning techniques. Authorship identification (AID) is the process of identifying the author of a given text using the structure of the text and the author’s writing style. It is usually treated as a text classification problem, which exhibits limitations when encountering real-world datasets with too many authors to classify. To overcome this issue, we used a method similar to contrastive learning, where the positive and negative pairs would be an article with its correct and incorrect author features, respectively. We further improve the model’s performance by utilizing graph machine learning, which could capture the inherent structure and relationships of authors and articles. In the end, we increased the model’s AUC value from 73% to 79% on a sampled subset from the Citation Network of DBLP.

[Full Paper Link](Graph-based%20AID.pdf).

### Data Illustration by Network Sampling

<img src="Graph-based AID/graph.png" width=1000 height=1500>
