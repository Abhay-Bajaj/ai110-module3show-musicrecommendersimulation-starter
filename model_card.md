# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

## VibeFinder 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeFinder generates song recommendations from a small catalog based on a user's
preferred genre, mood, energy level, and acoustic preference. It assumes the user can
be described by a single fixed taste profile and that their preferences do not change
between sessions. It also assumes the user knows what genre and mood they want, which
is not always true in real life. This is built for classroom exploration only and is
not intended for real users or production use.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The system looks at four things about each song: its genre, its mood, its energy level
on a scale from 0 to 1, and how acoustic it sounds. On the user side, it stores their
favorite genre, favorite mood, a target energy level, and whether they like acoustic
music. To turn those into a score, it checks each song one at a time. A genre match
adds the most points, a mood match adds a medium amount, and energy is scored by how
close the song's intensity is to what the user wants rather than just rewarding the
loudest or quietest songs. The only change from the starter logic was adding the
acousticness bonus, which gives a small reward to songs with a strong acoustic feel
when the user has indicated they like that quality.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog has 20 songs stored in a CSV file. Genres represented include lofi, pop,
rock, jazz, synthwave, ambient, hip hop, classical, punk, r&b, folk, electronic, and
country. Moods include happy, chill, intense, focused, relaxed, moody, melancholic,
angry, romantic, sad, and energetic. The original starter file had 10 songs and 10
more were added manually to increase genre and mood diversity. The dataset is missing
non-English language music, world music, gospel, blues, and metal entirely, so users
whose taste falls into any of those areas will get recommendations that do not reflect
what they actually want.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works best for users whose favorite genre has multiple songs in the catalog,
like lofi or folk, because the scoring has more options to choose from and the results
feel varied rather than repetitive. It captures energy matching well because the
proximity formula rewards closeness rather than just high or low values, so a user who
wants medium energy does not always get the loudest songs. The Chill Lofi and Deep
Intense Rock profiles both returned results that matched intuition exactly, with the
right song at the top and reasonable runners-up filling the remaining spots. The plain
language explanations also make it easy to understand why each song was chosen, which
is something most real recommenders do not offer.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system does not consider tempo, valence, or danceability at all, so a user who loves fast danceable songs gets the 
same results as someone who prefers slow ballads as long as their genre, mood, and energy match. Genres like classical, 
punk, and electronic only have one song each in the catalog, which means users who prefer those genres are at a structural 
disadvantage compared to lofi or folk users who have multiple songs competing for the top spots. Genre is worth twice as 
much as mood in the scoring, so a song in the right genre but the wrong mood will almost always outrank a song with a 
perfect mood and energy match from a different genre, which overfits the results toward genre above everything else. Users 
who like acoustic music get a small bonus that non-acoustic users never receive, which quietly favors that group in every 
single scoring round. There is no penalty for recommending the same artist twice, so the top 5 can feel repetitive and the 
system has no way to know if the user has already heard a song before.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Five profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, Conflicted
Listener, and Niche Taste. High-Energy Pop and Chill Lofi both returned results that
felt right, with Sunrise City and Focus Flow landing at #1 respectively since they
matched on genre, mood, and energy all at once. The most surprising result was Gym Hero
showing up at #2 for the High-Energy Pop profile even though its mood is "intense" not
"happy." The reason is that Gym Hero is a pop song with very high energy, so it picks
up the full genre bonus and a strong energy score, and the missing mood point does not
hurt it enough to drop it out of the top 2. Deep Intense Rock worked exactly as
expected since Storm Runner is the only rock song in the catalog, so it dominates
completely. The Niche Taste profile, which wanted metal, never scored above 2.0 because
metal does not exist in the catalog and the system had no way to suggest anything close,
which revealed that a small catalog punishes niche users more than anyone else.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Adding tempo and danceability to the scoring would make better use of the data that is
already in the CSV, and would help separate songs that currently score identically
because they match on genre, mood, and energy but feel completely different in practice.
A better way to explain recommendations would be to show the user what the song is
missing as well as what it matches, so instead of just saying "genre match, energy
proximity" it could also say "mood did not match." To improve diversity, a filter could
prevent the same artist or genre from appearing more than twice in the top 5, which
would make the results feel less repetitive for users whose favorite genre dominates
the catalog. Handling more complex tastes would require letting users set a range for
energy instead of a single number, and eventually supporting multiple favorite genres
rather than just one.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

## Reflection

The biggest learning moment was realizing how much a single number controls the entire
output. When the genre weight was 2.0, the results felt genre-coherent but sometimes
ignored a perfect mood and energy match from a different genre, and dropping it to 1.0
fixed that but made the results feel less personal overall. That tradeoff does not have
an obvious right answer, and it taught me that recommender systems are not making smart
decisions, they are just doing arithmetic on a few numbers really fast, and whoever
picks the weights decides what every user experiences. Using AI tools helped most
during setup, like getting the CSV loading right and structuring the output, but I had
to slow down and double-check when generated code looked correct but had a subtle bug,
like when the genre match was adding 2.0 to the score but the reason string was saying
+1.0. The code ran without errors so there was no warning, and it took comparing the
output numbers manually to catch it.

The most surprising thing was how quickly the results started feeling like real
recommendations even with such a simple formula. Seeing Focus Flow appear at the top
for the Chill Lofi profile with a perfect 4.00 felt satisfying, like the system
understood what that user wanted, even though nothing intelligent was happening under
the hood. That gap between what the output feels like and what is actually going on
changed the way I think about apps like Spotify or YouTube. When a recommendation
feels weirdly accurate it is easy to assume the app knows you, but it is probably just
a weighted score on a handful of attributes scaled up to millions of songs and shaped
by years of feedback data. If I extended this project I would add a seen songs filter
first, and then experiment with letting users rate recommendations so the weights could
adjust automatically over time instead of being hardcoded.
