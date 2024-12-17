---
title: "Beat and Fit Adventure"
date: 2024-01-01
image: "images/projects/208/208cover.png"
category: "Gameplay / Human-Centered Design"
weight: 3
layout: "work"
abstract: "Beat&Fit Adventure is an innovative product aimed at revolutionizing people's daily fitness
routines and experiences. In today's fast-paced environment, health issues cannot be
overlooked, yet the monotony of traditional exercise makes it challenging for individuals to
develop long-term fitness habits. Additionally, considering communities such as fitness novices
and those with social anxiety, public fitness environments like gyms may not be ideal for them.
To address these challenges, our team has developed Beat&Fit Adventure, a virtual reality
based fitness adventure game...."
---

<div class="pdf-container">
    <iframe src="../../images/projects/208/poster.pdf" width="100%" height="500px" type="application/pdf">
        <p>Your browser does not support PDFs. 
        <a href="../../images/projects/208/poster.pdf">Click here to download the PDF</a>.</p>
    </iframe>
</div>

<div class="pdf-download">
    <a href="../../images/projects/208/poster.pdf" target="_blank" class="pdf-button">
        View Full PDF
    </a>
</div>

## Introduction

Beat&Fit Adventure is an innovative product aimed at revolutionizing people's daily fitness
routines and experiences. In today's fast-paced environment, health issues cannot be
overlooked, yet the monotony of traditional exercise makes it challenging for individuals to
develop long-term fitness habits. Additionally, considering communities such as fitness novices
and those with social anxiety, public fitness environments like gyms may not be ideal for them.
To address these challenges, our team has developed Beat&Fit Adventure, a virtual reality
based fitness adventure game.
In an increasingly demanding era where workloads and psychological stress are on the rise,
physical well-being becomes an inevitable concern [1]. However, traditional fitness methods,
such as going to the gym, often lack the necessary fun and have challenge to inspire people's
enthusiasm for exercise [2]. Moreover, for the average office worker and students, the intensity
of gym workouts may be too high, leading to fatigue and discouragement, making it difficult to
sustain. For fitness beginners, the abundance of fitness enthusiasts, advanced equipment, and
lack of confidence in their own workout techniques may result in feelings of shame about going
to the gym. Additionally, for introverted individuals and who have social anxiety, they may be
unwilling to enter unfamiliar and crowded environments [3]. The development of Beat&Fit
Adventure aims to change this situation by providing users with a relaxed, enjoyable, and
challenging fitness experience. By integrating virtual reality technology with exercise, we hope
to create a fully immersive, creative, and motivational fitness environment for users to enjoy,
alleviating their concerns about traditional gyms and making it easier for them to stay consistent,
thus promoting a healthy lifestyle. Beat&Fit Adventure aims to offer users a completely new and
exciting fitness experience, turning exercise from a burden into a source of pleasure and
enjoyment.

<div class="video-container">
    <iframe width="100%" height="400" src="https://www.youtube.com/embed/0PShZUoZ1Us" frameborder="0" allowfullscreen></iframe>
</div>

## Analysis of Requirements

### Market Research

We conducted market research and compared our product with Fitness Bar and Fitness Hoop.
Fitness Bar, due to its lack of entertainment value, offers a monotonous fitness experience,
leading users to lose motivation and enthusiasm, which makes it difficult for them to persist in
long-term engagement. In contrast, our design focuses on leveraging virtual reality technology
and gamification to enhance user engagement and enjoyment, thereby addressing the
shortcomings of Fitness Bar.
Furthermore, compared to Fitness Hoop, our product features a more intuitive and user-friendly
interface and guidance system, aimed at improving the accuracy of fitness postures,
accelerating user learning curves, and reducing entry barriers. Additionally, Fitness Hoop may
have higher intensity levels, we offer difficulty selection options to lower the intensity threshold,
catering to a wider range of fitness needs within the community.

### Questionnaire Survey

We designed a questionnaire divided into three sections to gain insights into market conditions
and user requirements. The first section focuses on the challenges of traditional exercises, aiming to understand users' perspectives on the common issues of boredom and difficulty in
sustaining traditional fitness routines. The second section investigates participants' views of
virtual reality, aiming to understand their acceptance and attitudes towards the emerging
technology, as well as the advantages they expect to gain from virtual reality in their fitness
experiences. The third section collects feedback on gaming elements, aiming to identify the
gaming elements preferred by users and provide directions for product design that better align
with the preferences of the general public.
We invited 66 university students to participate in the questionnaire survey (39 males and 27
females; aged between 18 to 24), and conducted the following analysis of their responses:

#### Challenges of traditional exercises

According to the statistical results shown in Fig.1, over four-fifths of the respondents

1. find it challenging to maintain long-term fitness routines. Additionally, the majority of participants (over
   80%)
2. perceive traditional exercise activities as dull. This indicates that traditional fitness
   methods lack appeal and are difficult to sustain over the long term for most individuals.
   Moreover, over 90% of them believe that incorporating entertainment elements into fitness
   activities would motivate them to achieve to their exercise routines. Therefore, enhancing
   entertainment elements may increase users' willingness to maintain long-term fitness
   activities.。
3. Furthermore, as illustrated in (d), most individuals choose activities like running or walking for
   their daily fitness, with this number exceeding twice the number of those who go to the gym.
   This is likely because university students, burdened with heavy academic workloads and lacking
   in exercise, find low-intensity activities like running or walking more suitable. Additionally,
   according to interviewees, beginners with no prior fitness experience feel embarrassed to visit
   the gym, leading to their reluctance to try.

#### User Perception of Virtual Reality

The findings shown in Fig. 2. reveal a high level of interest in VR gaming among the majority of
participants (over 85%)

1. However, it's noteworthy that less than half of them have had actual
   exposure to VR gaming

2. This indicates that those who have experienced VR gaming
   maintain an interest in it. Moreover, many individuals who haven't yet tried VR express a strong
   desire to explore it, highlighting the vast potential of the VR market.

<figure>
  <img src="../../images/projects/208/Fig1.png" alt="Example Image">
</figure>
---

<figure>
  <img src="../../images/projects/208/Fig2.png" alt="Example Image">
</figure>
---

#### Entertainment Element User Preferences

In our survey, we focused on users' attitudes towards daily goal mechanisms and music (a and
b). The results indicate that most of users hold optimistic views towards these two entertainment
elements. Additionally, we presented five game elements based on implementation for
participants to choose from (c). Through analysis, we found that they expressed a high level of
interest in the following elements: Visual reward animation, Virtual scene customization, and
Sound effects. This provides us with guidance to prioritize these game elements in product
design.

<figure>
  <img src="../../images/projects/208/Fig3.png" alt="Example Image">
</figure>
---

## Design Alternatives and Prototypes

Based on the market research findings and user needs analysis, we have designed a series of
innovative design alternatives and prototypes. Here are the main prototypes we have designed:
<div class="video-container">
    <iframe width="100%" height="400" src="https://www.youtube.com/embed/WJmjGsWcCY4" frameborder="0" allowfullscreen></iframe>
</div>

### Gameplay Scene

> Collider (Notes)

- **Collider type** We have designed two types of colliders shown in Fig. 4. , one circular and the
  other square (a). Through observing music games and sheet music (staff notation), we found
  that musical notes often have a circular appearance or shape, which is more visually aligned
  with the game elements. Additionally, we noticed that collision detection with circular bodies is
  relatively simpler compared to square bodies, which can reduce the computational load of the
  game and provide players with a smoother and more natural collision sensation. Taking all
  factors into consideration, we ultimately chose circles as the collision bodies for the notes in our
  game.

>

- **Rhythm** The coordination between music and movement is a crucial aspect of the gaming
  experience. When players synchronize their movements with the rhythm, they not only better
  sense the game's tempo but also experience the dynamism and joy that music brings during
  physical activity. Therefore, we parse the note information from MIDI files to extract the music's
  rhythm and dynamically generate collision bodies. This ensures that the musical rhythm in the
  game aligns with the players' movement tempo, providing a seamless integration of music and
  physical activity.
- **Notes Handle** We employ a differentiated approach to handle notes of different durations (b).
  For long notes, we generate five consecutive collision bodies to reflect the sustained nature of
  the note. Meanwhile, for short notes, we generate only one collision body to maintain the
  game's rhythm.
- **Generation positions** We have set up three collision body generation positions for the left and
  right hands respectively, with red indicating the left hand and blue indicating the right hand (c).
  The controller corresponds to the color of the collision body, allowing players to know which
  hand to use for collision. For each position, we designed under the guidance of professional
  coaches:

>

- **Upper position** (d) : Players need to raise their arms upwards. This movement
  effectively stretches and activates the shoulder and upper arm muscles, helping players
  exercise their shoulder and back muscles more effectively.
- **Middle position** : Players need to flatten their arms. This action helps maintain the
  stability and balance of the arms, strengthens the arm muscles, and improves coordination.
- **Lower position** (d) : Players need to squat to make a collision. This action effectively
  exercises the thigh and gluteal muscles, improves lower body strength and stability, and also
  increases overall calories burning effectiveness.

<figure>
  <img src="../../images/projects/208/Fig4.png" alt="Example Image">
</figure>
---

> Controller

In terms of controller selection, we initially considered using a ray as the controller, inspired by
designs commonly seen in some 3D music games such as Beat saber (a). However, during testing, we found that the collision with the ray was too easy, resulting in an inability to achieve
the desired fitness effect.
To address this issue, we designed a circular controller shown in (b). Compared to the ray
controller, the circular controller requires users to exert more physical effort to collide with the
collision bodies. This design better aligns with the fitness purpose, as users need more
movement and strength to complete the game, thus achieving better fitness results.

<figure>
  <img src="../../images/projects/208/Fig5.png" alt="Example Image">
</figure>
---

> Collision Effects

In terms of collision effects, we have designed the following effects shown in Fig. 6. :

- **Perfect Collision** (a) When the player successfully collides with a note, it triggers the 'Perfect'
  effect and adds +10 to the total score.
- **Bomb Collision** (b) If the player accidentally collides with a bomb, it triggers the 'Bomb' effect
  and deducts -5 from the total score.
- **Miss Effect** (c) When the player misses a note, it triggers the ‘Miss’ effect, but the score
  remains unchanged.
- **Combo Effect** (d) If the player consecutively collides with more than ten notes, it triggers the
  Combo effect and earns additional points. This design encourages players to maintain a steady
  collision rhythm to achieve a stable fat-burning state, thereby promoting more effective
  workouts.

<figure>
  <img src="../../images/projects/208/Fig6.png" alt="Example Image">
</figure>
---

#### Real-time Score and Consumption Display

In the top left corner of the game interface, we display the current total score in real-time.
This is done to evoke players' competitive spirit and encourage engagement by keeping track of
their scores. Additionally, we integrate calorie expenditure into the game by connecting devices
such as fitness trackers. This allows players to monitor the calories they burn during the game
in real-time, providing them with feedback on their fitness progress. This intuitive feedback not
only motivates players to complete the game but also enhances their satisfaction, ultimately
increasing long-term engagement with the game.

### Music and Scenes Customization

**Music and scene selection** Users have the option to customize based on their personal
preferences and fitness needs (a). We offer a variety of music styles and rhythms for users to
choose from, making the workout process more enjoyable. Additionally, we have designed a
diverse range of scenes (c), allowing users to choose environments they prefer and enjoy the
exercise process in a comfortable atmosphere.
**Difficulty** Users can also select the appropriate difficulty level based on their fitness level and
exercise requirements to ensure effectiveness and challenge (b).

<figure>
  <img src="../../images/projects/208/Fig7.png" alt="Example Image">
</figure>
---

### Game Settlement Interface

#### Daily Achievement Goals

Users can set daily exercise goals and track their progress in the settlement interface as shown
in Fig. 8. . After each game session, the calorie circle gradually closes based on the level of
calorie expenditure in the game until the daily exercise goal is achieved. This daily goal setting
helps users to maintain long-term exercise consistency.

### Competitive Scoring System

The settlement interface provides a competitive scoring feature, allowing users to view their
performance scores in the game and compare them with other players. This design stimulates
users' competitive mindset, encouraging them to continually improve in the game and achieve
good fitness results unconsciously.

<figure>
  <img src="../../images/projects/208/Fig8.png" alt="Example Image">
</figure>
---

## Evaluation: Data Collection and Results

### Evaluation methods and data collection

**Usability** was evaluated by the SUS (System Usability Scale) questionnaire [4]. This
questionnaire consists of two subscales representing learnability and usability. Participants
rated the system based on a series of statements, utilizing a 5-point Likert scale ranging from
"Strongly Disagree" to "Strongly Agree." Higher scores indicate a higher usability.

**WorkLoad** The workload associated with Beat&Fit Adventure was evaluated using the NASA
TLX workload questionnaire [5]. This questionnaire consists of six subscales representing
different aspects of workload, including mental demand, physical demand, temporal demand,
frustration, effort, and performance. Participants rated each subscale on a scale ranging from 0
to 100, with intervals of 5. Lower scores indicate a lower workload and better overall
performance.

**Interview** was a semi-structured regarding (1) their willingness to exercise using Beat&Fit
Adventure; (2) the experience of Beat&Fit Adventure; and (3) any possible improvements for the
game.

### Participants

Eleven participants (6 males; 5 females) between the age of 19-24 (M=21.89,SD = 1.41) were
recruited from the same university campus to participate in this study.

### Analysis results

**Usability** I utilized the relationship graph between text, letters, acceptable range, and SUS
scores [6], as well as the SUS Score grading curve ranges [7] to assess the SUS result.
According to Fig. 9. (a), the overall usability of the system (M=80.5, SD=5.68) was excellent
(SUS score 80.5, grade A-, percentage 85-89). In the SUS questionnaire, the subscale
composed of items 4 and 10 pertains to "Learnability," while the remaining eight items constitute "Usability." The Learnability subscale (M=65.9, SD=29.6) was rated as OK (SUS score 65.9,
grade C, percentage 41-59), and the Usability subscale (M=81.5, SD=13.3) was assessed as
excellent (SUS score 81.5, grade A, percentage 90-95).

**Workload** As shown in Fig. 9 (b), users' mental demand (M=26.8, SD=10.1) and frustration
(M=26.82, SD=12.3) are low, while performance (M=69.6, SD=18.6), physical (M=58.6,
SD=16.1), effort (M=55.9, SD=12.2), and temporal demand (M=53.1, SD=15.7) are moderately
high with large variances.

**Interview** All participants found Beat&Fit Adventure to be an engaging fitness game. However,
some individuals found the initial gameplay challenging because they lacked prior experience
with VR or rhythm games, causing them to feel nervous and seek guidance on how to play.
Additionally, there was feedback regarding the positioning of the collision bodies, with some
participants finding them too high and out of reach, while others found it easy to interact with,
leading to feelings of fatigue. Participants who had completed the requirements questionnaire
inquired why a virtual coach element was not included, as they believed it would add an
enjoyable aspect to the experience.

<figure>
  <img src="../../images/projects/208/Fig9.png" alt="Example Image">
</figure>
---

### Discussion

Overall, Beat&Fit Adventure exhibits strong usability and the workload aligns well with our
expectations. The higher levels of physical demand and effort meet our expectations for
exercise requirements, while the lower levels of mental demand and frustration satisfy our
entertainment needs. However, the learnability subscale results indicate that there is room for
improvement in learning the system, which is consistent with the feedback provided during
interviews regarding the lack of prior experience with VR and rhythm games. The high standard
deviations for Performance, Physical Demand, and Temporal Demand (>15) may be attributed
to individual differences among participants such as figure and gender, as mentioned during
interviews regarding variations in collision experiences.

## Discussion and Reflection

### Novelty and implications

Beat&Fit Adventure introduces a completely new approach to fitness gaming through immersive
experiences and innovative features, revolutionizing traditional exercise methods. By
seamlessly integrating fitness with gaming elements, Beat&Fit Adventure addresses the
boredom often associated with traditional workouts, transforming them into engaging and
motivating activities. This helps individuals across communities to adopt long-term exercise
habits, contributing to the realization of universal fitness goals.

### Limitations and future work

Although Beat&Fit Adventure has made significant progress in integrating fitness and gaming,
there are still some challenges to address. Particularly for newcomers who have not been
exposed to VR and music games, they may feel confused in the initial stages. Therefore, one of
the future tasks is to design a tutorial to guide them through familiarizing themselves with the
game mechanics. The tutorial could include instructions on using controllers, understanding the
cues and feedback on the game interface, and so on.

Due to individual differences, there is a need to develop a customized system based on gender
and body type. This system would involve tailoring collision bodies to ensure they are neither
too high nor too far away, nor too low or too close, thus achieving optimal fitness effects.

Furthermore, there is a high demand for virtual fitness coaches, which is one of the future
development directions. The development of virtual coaches can not only monitor user
movements and provide real-time corrections to their fitness postures, helping users avoid bad
habits and the risk of injury during exercise, but also provide emotional feedback during the
game, such as "Great job," to motivate users to keep exercising. These two points will be our
main focus for future development efforts.

## References

[1] Kouvonen, A., Vahtera, J., Oksanen, T., Pentti, J., Väänänen, A.K., Heponiemi, T., Salo, P.,
Virtanen, M. and Kivimäki, M., 2013. Chronic workplace stress and insufficient physical activity: a
cohort study. Occupational and environmental medicine, 70(1), pp.3-8.

[2] Hagberg, L.A., Lindahl, B., Nyberg, L. and Hellénius, M.L., 2009. Importance of enjoyment when
promoting physical exercise. Scandinavian journal of medicine & science in sports, 19(5), pp.740 747.

[3] Hausenblas, H.A., Brewer, B.W. and Van Raalte, J.L., 2004. Self-presentation and exercise. Journal
of applied sport psychology, 16(1), pp.3-18.

[4] Lewis, J.R., 2018. The system usability scale: past, present, and future. International Journal of
Human–Computer Interaction, 34(7), pp.577-590.

[5] Hart, S.G., 2006, October. NASA-task load index (NASA-TLX); 20 years later. In Proceedings of the
human factors and ergonomics society annual meeting (Vol. 50, No. 9, pp. 904-908). Sage CA: Los
Angeles, CA: Sage publications.

[6] Bangor, A., Kortum, P. and Miller, J., 2009. Determining what individual SUS scores mean: Adding
an adjective rating scale. Journal of usability studies, 4(3), pp.114-123.

[7] Sauro, J., 2011. A practical guide to the system usability scale: Background, benchmarks & best
practices. Measuring Usability LLC.
