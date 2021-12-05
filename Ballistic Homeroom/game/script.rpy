# The script of the game goes in this file.
# Declare characters used by this game.

define stranger = Character("????")

define avenger = Character("AvengerL9")
image avenger1 = im.FactorScale("images/avengerl9.png", 2)
image avenger2 = im.FactorScale("images/avengerl9flipped.png", 2)

define gamemaster = Character("121gamemaster")
image gamemaster1 = im.FactorScale("images/121gamemaster.png", 2)

define adam = Character("AdamTheCookiez")
image adam1 = im.FactorScale("images/adamthecookiez.png", 2)
image adam2 = im.FactorScale("images/adamthecookiezflipped.png", 2)

define epic = Character("epiclyepicface")
image epic1 = im.FactorScale("images/epiclyepicface.png", 2)

define frag = Character("FuFuFrag")
image frag1 = im.FactorScale("images/fufufrag.png", 2)

define jb = Character("jbsucks26")
image jb1 = im.FactorScale("images/jbsucks26.png", 2)

define lexy = Character("Lexy916")
image lexy1 = im.FactorScale("images/lexy916.png", 2)

define oko = Character("Okotemasu")
image oko1 = im.FactorScale("images/okotemasu.png", 2)

define pat = Character("patrickrush")
image pat1 = im.FactorScale("images/patrickrush.png", 2)

define power = Character("PowerWordDie")
image power1 = im.FactorScale("images/powerworddie.png", 2)

define qisme = Character("Q_isme")
image qisme1 = im.FactorScale("images/qisme.png", 2)
image qisme2 = im.FactorScale("images/qismeflipped.png", 2)

define spiral = Character("SpiralCarve")
image spiral1 = im.FactorScale("images/spiralcarve.png", 2)

define squid = Character("squidwardtikiland")
image squid1 = im.FactorScale("images/squidwardtikiland.png", 2)

define surprise = Character("SurpriseGuy624")
image surprise1 = im.FactorScale("images/surpriseguy624.png", 2)

define will = Character("willdash")
image will1 = im.FactorScale("images/willdash.png", 2)

define zawarudo = Character("ZaWarudoO_O")
image zawarudo1 = im.FactorScale("images/zawarudooo.png", 2)

transform right1:
    xanchor 0.5
    xpos 0.9
    yanchor 1.0
    ypos 1.0

transform right2:
    xanchor 0.5
    xpos 0.7
    yanchor 1.0
    ypos 1.0

transform left2:
    xanchor 0.5
    xpos 0.3
    yanchor 1.0
    ypos 1.0

transform left1:
    xanchor 0.5
    xpos 0.1
    yanchor 1.0
    ypos 1.0


# The game starts here.

label start:
    play music "audio/bgm.mp3" fadein 1.0 volume 0.8
    scene room_dawn_light_off
    show avenger1

    avenger "Today is my first day of highschool."

    avenger "Time to brush my teeth, eat some breakfast, and then head out."

    scene room_morning_light_off
    show avenger1

    avenger "I'm all prepared, time to go to school!"

    scene home_morning:
        zoom 1.5

    avenger "Just one last look at my house before I head to school."

    avenger "Alright no more stalling, I have to get to school on time."

    scene childrens_park_day

    avenger "I used to play here all the time."

    avenger "I just slowly grew out of it."

    scene deep dark fantasy

    avenger "Here's a shortcut I can take."

    show avenger2 at left
    play music "audio/scary.mp3" fadein 1.0 volume 0.8

    stranger "Hey kid ... want some candy?"

    stranger "Just get inside my van, there's plenty of candy."

    stranger "It'll be fun, what do you say?"

    avenger "What? No! Who's there?"

    stranger "Doesn't matter who I am, I'm just giving out free candy."

    stranger "My place isn't too far from here, just get into my van."

    avenger "No, I'm calling the police."

    show pat1 at right
    play music "audio/bgm.mp3" fadein 1.0 volume 0.8

    stranger "Wait! Don't call the police!"

    stranger "Please! I'll stop!"

    stranger "I already got in trouble with Chris Hansen, I can't get into anymore trouble!"

    stranger "Here! Take my wallet, I have $40 in cash. Lets pretend this never happened!"

    hide pat1

    avenger "Cool I guess I just got $40 for free."

    avenger "I better get a move on, this took up a lot of my time."

    scene bus_stop_morning

    avenger "There's the bus stop."

    avenger "Good timing, the bus just got here too."

    avenger "The bus should take me straight to school."

    scene generic_school_gate

    avenger "I see the school gate!"

    avenger "Looks like that incident didn't make me late."

    scene applegate_school_gate_3_entrance

    avenger "I can just forget it ever happened."

    avenger "I'll find my homeroom and meet my classmates."

    scene classroom_01_day

    avenger "This should be the right room."

    avenger "I wonder if any of my classmates are here..."

    show gamemaster1
    with easeintop

    stranger "I take it you're in this class as well?"

    avenger "Woah you scared me, are you a ninja?"

    stranger "Sorry about that, it's a bad habit of mine."

    stranger "My name is 121gamemaster, you can just call me gamemaster."

    avenger "Good to know, and I'm AvengerL9, I go by Avenger."

    avenger "I transferred here over the summer so it's my first time at this school."

    gamemaster "Oh that makes sense, no wonder I haven't seen you before."

    gamemaster "Don't worry I've been here for a year now, I can help you if you get lost."

    gamemaster "By the way, have you heard about today being a half day?"

    avenger "A half day on the first day of school?"

    gamemaster "Yea it's school tradition to have a half day on the first and last day of school!"

    avenger "That's cool, thanks for letting me know."

    gamemaster "No problem, just let me know if you need any help."

    avenger "Yea will do."

    hide gamemaster1
    with easeoutleft

    show squid1
    with easeinright

    stranger "Any friend of gamemaster is a friend of mine."

    stranger "My name is squidwardtikiland but that's a mouthful, just call me squid."

    avenger "My name is AvengerL9, call me Avenger."

    squid "Alright class seems to be starting but I'll catch you later, Avenger."

    hide squid1
    with easeoutleft

    play sound "audio/bell.mp3"

    show will1
    with easeinright

    stranger "..."

    hide will1
    with easeoutleft

    show surprise1
    with easeinright

    stranger "I call dibs on a seat by the window!"

    stranger "I called dibs so you have to respect it!"

    hide surprise1
    with easeoutleft

    show epic1 at left
    with easeinright

    stranger "Did everyone see what I just did?"

    stranger "I slid in so you can't tell whether or not I was late!"

    hide epic1
    with easeoutleft

    show oko1
    with easeinright

    stranger "And here I thought I was late!"

    stranger "If the teacher doesn't show up in 15 minutes we can leave!"

    hide oko1
    with easeoutleft

    show adam1
    with easeinright

    stranger "My Wife's boyfriend bought the new Xbox Series X!"

    stranger "I hope I get a turn so me and my Wife's son get to bond together!"

    hide adam1
    with easeoutleft

    show frag1
    with easeinright

    stranger "XQC WELCOMED ME TO THE JUNGLE!"

    stranger "IM A PROUD JUICER, BEEN WATCHING HIS STREAM SINCE THE OVERWATCH DAYS!"

    stranger "HOW DID YOU KNOW I NEVER TOUCHED A GIRL IN MY LIFE BEFORE?"

    show jb1 at right
    with easeinright

    stranger "Heh, last year I kept poking that gamemaster kid with a really sharp pencil."

    stranger "He poked me back and drew some of my blood, I licked it and I said it tasted like chicken!"

    stranger "I wonder if he still remembers that LOL!"

    hide frag1
    with easeoutleft
    hide jb1
    with easeoutleft

    show spiral1
    with easeinright

    stranger "I was up all night playing a gacha game for my waifu"

    show zawarudo1 at right
    with easeinright

    stranger "That's lame! Dio is our lord and savior, my husbando is the best!"

    hide spiral1
    with easeoutleft
    hide zawarudo1
    with easeoutleft

    show power1
    with easeinright

    stranger "Wanna do some karaoke after school? With it being a half day and all?"

    show lexy1 at right
    with easeinright

    stranger "Yea sounds like fun!"

    hide power1
    with easeoutleft
    hide lexy1
    with easeoutleft

    show qisme1
    with easeinright

    stranger "You're all still here? Haven't you all heard?"

    stranger "Our teacher, Mr. patrickrush called in saying he is unable to make it in today."

    stranger "He said he had to hide from Chris Hansen ... whatever that means."

    stranger "No one can fill in for him right now and the school's already understaffed as it is."

    hide qisme1
    show qisme2

    stranger "School is cancelled for the day. Be sure to come prepared tomorrow as a substitute will be found by then."

    hide qisme2
    with easeoutright

    show adam2 at right
    with easeinleft

    stranger "OMG! MY WIFE'S BOYFRIEND JUST TEXTED SAYING HE HAS TO MOVE ABROAD ALL BECAUSE OF CHRIS HANSEN!!!"
    stranger "THIS CHRIS HANSEN GUY IS GETTING ON MY NERVES!"
    stranger "I WON'T GET TO WATCH MY WIFE GETTING IT ON WITH HER BOYFRIEND!"
    stranger "But raising my Wife's son isn't too bad either!"
    stranger "I hope my Wife's boyfriend will let their son keep the new Xbox Series X!"
    stranger "But first I have to ask him if that's okay. I'll also need permission to get inside the house I paid for."

    hide adam2
    with easeoutright

    avenger "Jesus who was that?"

    show gamemaster1
    with easeinleft

    gamemaster "Yea that guy is AdamTheCookiez, he prefers we call him by his nickname: cuckold."

    gamemaster "Try not to talk to him, he's been held back for 7 years in a row."

    gamemaster "If he ever causes you trouble, send him my way. A little violence goes a long way!"

    avenger "Good to know! I pray to god that, that cuckold doesn't try to talk to me."

    gamemaster "Hey Avenger! Do you have any plans now that school is cancelled? I was thinking we could hang out."

    menu:
        "Hmm my schedule is pretty free right now."

        "Yea sure why not! Sounds like fun!":
            jump hangout

        "Sorry maybe next time! I gotta get home; I have plenty of chores to do.":
            jump home

label hangout:

    show gamemaster1

    gamemaster "We can go to the beach or the pond! They're both within walking distance."

    show epic1 at left
    with easeinbottom

    stranger "Did I hear fun?"

    show surprise1 at right
    with easeinbottom

    stranger "Oh can I tag along?"

    gamemaster "Sure! The more the merrier."

    gamemaster "Guys, meet AvengerL9, you can call him Avenger."

    gamemaster "The person to your left is epiclyepicface! He likes to go by epic for short."

    epic "Hi! The only thing special about me are my needs! YOROSHIKU ONEGAISHIMASU!"

    gamemaster "And to your right is SurpriseGuy624! You can call him SurpriseGuy."

    surprise "Don't mind my friend epic over there, he was shook as a baby. It's nice to meet you."

    gamemaster "Avenger, you get to choose where we go!"

    menu:
        "Hmm lets see... the pond or the beach?"

        "Let's go to the pond!":
            jump pond

        "Let's go to the beach!":
            jump beach

label pond:

    scene classroom_01_day

    show gamemaster1

    show epic1 at left

    show surprise1 at right

    epic "YAY POND!"

    hide epic1
    with easeoutright

    surprise "Wait up epic! No running in the halls!"

    surprise "I'll catch up to him before he gets himself hurt."

    hide surprise1
    with easeoutright

    gamemaster "Hey squid, you joining us?"

    show squid1 at left
    with easeinleft

    squid "Yea let's go."

    hide gamemaster1
    with easeoutright

    hide squid1
    with easeoutright

    scene 1:
        zoom 1.5

    show epiclyepicface at right2
    with easeinleft

    show surpriseguy624
    with easeinleft

    show 121gamemaster at left2
    with easeinleft

    show squidwardtikiland at left1
    with easeinleft

    gamemaster "Check out this amazing pond!"

    gamemaster "We can catch some wild frogs."

    surprise "Hey epic stop eating the wild frogs!"

    epic "NOM NOM NOM."

    surprise "Stop eating them! You don't know where they've been."

    epic "YUM."

    surprise "Woah check that out! There's a fully grown turtle!"

    surprise "Stop epic! Don't mess with the turtle, it can snap your finger off!"

    squid "HAHAHA you two are hilarious!"

    avenger "Look what I found! This is a huge tree branch!"

    squid "I found one too, I challenge you to a duel!"

    gamemaster "The winner has to get past me!"

    scene black
    with dissolve

    "Epic continues to eat the local wildlife as SurpriseGuy tries his best to keep him safe."

    "Squid defeats both you and gamemaster in a duel. Squid took fencing lessons growing up so this was expected."

    "Everyone had a great time at the pond today."

    scene 1:
        zoom 1.5

    show epiclyepicface at right2

    show surpriseguy624

    show 121gamemaster at left2

    show squidwardtikiland at left1

    surprise "It was great hanging out with you guys today."

    surprise "I'll escort epic home since we both live on the same block."

    surprise "Follow me epic we gotta get home. We can't miss your favorite anime show right?"

    epic "YAY ANIME!"

    hide surprise1
    with easeoutleft

    hide epic1
    with easeoutleft

    squid "Yawn I'm kinda tired too. I'm gonna head home and take a nap! Cya guys later!"

    hide squid1
    with easeoutleft

    gamemaster "I'll head out too, my parents get worried pretty easily."

    hide gamemaster1
    with easeoutleft

    avenger "Bye bye!"

    avenger "I should head home, I'm feeling kinda exhausted as well."

    scene generic_school_gate

    avenger "This bus arrives every 15 minutes"

    avenger "Speak of the devil it's here. This will take me within walking distance to home."

    scene bus_stop_noon

    avenger "I'll take the same route I did to get to school."

    avenger "There's no way that creepy guy is still there."

    scene deep dark fantasy

    avenger "I just hope I never see that creepy person again."

    avenger "He'll stay away if he knows what's good for him."

    scene childrens_park_day

    avenger "Home is just right around the corner!"

    scene home_morning:
        zoom 1.5

    avenger "Over there! My house is within my sights!"

    scene room_afternoon_light_off

    avenger "Home sweet home!"

    avenger "Time to take a shower. My clothes are dirty from playing at the pond."

    avenger "Afterwards I'll have some lunch then I'll get around to those chores."

    avenger "Then I can relax and chill on my computer."

    scene black
    with dissolve

    "You take a shower, get into some new clothes, eat a nice lunch, and then finish the chores."

    "You have some extra free time you spend browsing the Internet and watching Youtube videos."

    scene room_dusk_light_off

    avenger "Time flies by when you're having fun."

    avenger "I'll make myself some dinner and chill on my computer until it's bed time."

    scene black
    with dissolve

    "You have a nice dinner and watch chill Youtube videos until bed time."

    scene room_night_light_off

    avenger "Today I had a lot of fun. I made a ton of frends."

    avenger "I'm pretty tired. Time to go to bed."

    scene black
    with dissolve

    "You went to the pond with a bunch of your new friends today."

    "You fall asleep wondering ..."

    "Why was epiclyepicface shook as a baby?"

    "How is that cuckold from class still in this grade?"

    "Where has the homeroom teacher fled to?"

    "So many questions, not enough answers. You have a wild dream filling in those gaps."

    "{b}Pond Ending{/b}."

    return

label beach:

    scene classroom_01_day

    show gamemaster1

    show epic1 at left

    show surprise1 at right

    epic "YAY BEACH!"

    hide epic1
    with easeoutright

    surprise "Wait up epic! No running in the halls!"

    surprise "I'll catch up to him before he gets himself hurt."

    hide surprise1
    with easeoutright

    gamemaster "Hey squid, you joining us?"

    show squid1 at left
    with easeinleft

    squid "Yea let's go."

    hide gamemaster1
    with easeoutright

    hide squid1
    with easeoutright

    scene beach_noon

    show epiclyepicface at right2
    with easeinleft

    show surpriseguy624
    with easeinleft

    show 121gamemaster at left2
    with easeinleft

    show squidwardtikiland at left1
    with easeinleft

    gamemaster "We're here! This is the beach."

    gamemaster "We can go build a sandcastle!"

    avenger "Interesting I never built a sandcastle before."

    squid "Don't worry, we'll show you ropes to building a great sandcastle."

    surprise "What the-"

    surprise "Hey stop trying to eat the sand!"

    epic "Mmmm sand tasty."

    epic "Eating sand is kino."

    surprise "Woah a crab is coming near us!"

    surprise "It could pinch us so be careful!"

    epic "gOtTa PeT tHe CrAb!"

    surprise "NO! Don't mess with the crab!"

    squid "HAHAHA you two are hilarious!"

    avenger "I think I'm getting the hang of this."

    gamemaster "Yea you're doing great. The sandcastle is coming along nicely."

    squid "Wow a huge wave is coming in!"

    scene black
    with dissolve

    "Epic enjoys eating the sand and Surprise is watching out for his shook friend."

    "The wave destroyed the sandcastle. It was bound to happen sooner or later."

    "Everyone had a great time at the beach today."

    scene beach_noon

    show epiclyepicface at right2

    show surpriseguy624

    show 121gamemaster at left2

    show squidwardtikiland at left1

    surprise "It was great hanging out with you guys today."

    surprise "I'll escort epic home since we both live on the same block."

    surprise "Follow me epic we gotta get home. We can't miss your favorite anime show right?"

    epic "YAY ANIME!"

    hide surprise1
    with easeoutleft

    hide epic1
    with easeoutleft

    squid "Yawn I'm kinda tired too. I'm gonna head home and take a nap! Cya guys later!"

    hide squid1
    with easeoutleft

    gamemaster "I'll head out too, my parents get worried pretty easily."

    hide gamemaster1
    with easeoutleft

    avenger "Bye bye!"

    avenger "I should head home, I have some chores to do."

    scene generic_school_gate

    avenger "This bus arrives every 15 minutes"

    avenger "Speak of the devil it's here. This will take me within walking distance to home."

    scene bus_stop_noon

    avenger "I'll take the same route I did to get to school."

    avenger "There's no way that creepy guy is still there."

    scene deep dark fantasy

    avenger "I just hope I never see that creepy person again."

    avenger "He'll stay away if he knows what's good for him."

    scene childrens_park_day

    avenger "Home is just right around the corner!"

    scene home_morning:
        zoom 1.5

    avenger "Over there! My house is within my sights!"

    scene room_afternoon_light_off

    avenger "Home sweet home!"

    avenger "Time to take a shower. My clothes are dirty from playing at the beach."

    avenger "Afterwards I'll have some lunch then I'll get around to those chores."

    avenger "Then I can relax and chill on my computer."

    scene black
    with dissolve

    "You take a shower, get into some new clothes, eat a nice lunch, and then finish the chores."

    "You have some extra free time you spend browsing the Internet and watching Youtube videos."

    scene room_dusk_light_off

    avenger "Time flies by when you're having fun."

    avenger "I'll make myself some dinner and chill on my computer until it's bed time."

    scene black
    with dissolve

    "You have a nice dinner and watch chill Youtube videos until bed time."

    scene room_night_light_off

    avenger "Today I had a lot of fun. I made a ton of frends."

    avenger "I'm pretty tired. Time to go to bed."

    scene black
    with dissolve

    "You went to the beach with a bunch of your new friends today."

    "You fall asleep wondering ..."

    "Why was epiclyepicface shook as a baby?"

    "How is that cuckold from class still in this grade?"

    "Where has the homeroom teacher fled to?"

    "So many questions, not enough answers. You have a wild dream filling in those gaps."

    "{b}Beach Ending{/b}."

    return

label home:

    scene classroom_01_day

    show gamemaster1

    gamemaster "Yea I totally understand, maybe we can hangout some other time?"

    avenger "Sounds good to me!"

    scene generic_school_gate

    avenger "I'll wait for the bus to come, it should take me within walking distance to home."

    scene bus_stop_morning

    avenger "School ended pretty early."

    avenger "I'll walk home by taking the same route I did to get to school."

    scene deep dark fantasy

    avenger "This place should be safe."

    avenger "It's not even a bad shortcut. This saves me a lot of time walking."

    avenger "Hopefully what happened this morning was just a one-off occurrence."

    scene childrens_park_day

    avenger "Home is just right around the corner!"

    scene home_morning:
        zoom 1.5

    avenger "Over there! My house is within my sights!"

    scene room_morning_light_off

    avenger "Home sweet home!"

    avenger "Time to get to those chores."

    scene black
    with dissolve

    "You finish cleaning your room."

    scene room_noon_light_off

    avenger "There! My room is all clean."

    avenger "I'll have some lunch and then I can browse the Internet and watch some Youtube videos."

    scene black
    with dissolve

    "You eat lunch then spend hours on the computer to pass the time."

    scene room_dusk_light_off

    avenger "Time to make dinner and then I can go back to watching Youtube videos."

    scene black
    with dissolve

    "You have dinner then go back on your computer for a couple more hours."

    scene room_evening_light_on

    avenger "It's almost time for bed."

    avenger "I'll take a shower and brush my teeth."

    scene black
    with dissolve

    "You take a shower then brush your teeth before bed."

    scene room_night_light_off

    avenger "My only regret is not hanging out with my classmates."

    avenger "Oh well, what's done is done."

    avenger "I can always hang out with them some other time."

    scene black
    with dissolve

    "Your day ends with more to be sought after."

    "You fall asleep and dream of Chris Hansen catching child predators and putting them behind bars."

    "{b}Normal Ending{/b}."

    return
