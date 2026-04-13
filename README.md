# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Each `Song' stores ten attributes: `id`, `title`, `artist`, `genre`, `mood`, 
`energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. The 
`UserProfile` stores the user's `favorite_genre`, `favorite_mood`, `target_energy`, 
and a boolean `likes_acoustic` flag. The `Recommender` scores each song by comparing 
it against the user profile using this recipe: 

- +2.0 points for a genre match 
- +1.0 point for a mood match 
- +1.0 × (1 - |target_energy - song.energy|) for energy proximity 
- +0.5 if the user likes acoustic music and the song's acousticness is above 0.6 

Once every song has a score, the list is sorted from highest to lowest and 
the top `k` results are returned, each paired with a score and a plain language 
explanation of why it was chosen. The maximum possible score is 4.5. 

**Potential biases:** 
Because genre is weighted twice as much as mood, the system may overlook 
songs that are a near-perfect mood and energy match just because they belong to a 
different genre. It also has no sense of variety, so if five lofi songs all score 
similarly, the top five results could feel repetitive. Users whose favorite genre is 
underrepresented in the catalog will consistently get weaker recommendations than 
users whose genre has many songs in the dataset.

Song features: id, title, artist, genre, mood, energy, tempo_bpm, valence, 
danceability, acousticness

UserProfile features: favorite_genre, favorite_mood, target_energy, likes_acoustic

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
```

## 8. Screenshots

1. Working CLI
![CLI Pop profile output](assets/WorkingCLI.png)

2. Diverse Profiles
![Profile 1](assets/Output1.png)
![Profile 2](assets/Output2.png)
![Profile 3](assets/Output3.png)
![Profile 4](assets/Output4.png)
![Profile 5](assets/Output5.png)
![Profile 6](assets/Output6.png)

