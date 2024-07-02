---
title: Codename: TEABAG
---

*This is the guide for **Codename: TEABAG**.
If you are looking for the files to accompany the guide, please visit [https://github.com/atom-dispencer/CodenameTeabag]()*

# Greetings, Adventurer!

> *[A voice speaks to you, as if from a great distance...]*
>
> ***Welcome to the Forgotten Lands!***
>
> ***What's that? The Forgotten Lands don't exist yet!?***
>
> ***No matter! Together, we shall build them...***

To all my engineering buddies who 'hate programming', this guide is for you. 😉

As students, we have neither the time nor the energy to devote a year of our lives to a full 
    [boot.dev](boot.dev) Python course (which I haven't used, but seems decent), so I'm going to 
    distill as much wisdom as I can into three (*yes, I said '3'*) lessons.

Most programming tutorials are, for want of a better word, *crap*[^1].
Either they're way too advanced for beginners, or they show some mediocre code for you to copy-paste and 
    expect you to divine it's purpose via séance.

That's why this is not a tutorial.

[^1]: Source: Just Google 'programming tutorial'

## 📖 The story so far...

In school about five years ago (2019-ish), I was tasked with making a 
    '**T**ext-**B**ased **A**dventure-**G**ame' (T-BAG) - a game where the player controls their character 
    through simple typed commands such as **WALK**  or **FIGHT**.
Being myself five years ago, I wildly overcomplicated the task and planned multiple expansions which I 
    never even started making... though I did ace the test! [^2]

Later, starting my degree, I was surprised at just how many of my peers in
    [STEM](https://www.britannica.com/topic/STEM-education) treat programming like a monster you only 
    poke with a long stick...

So now that I'm slightly less incompetent than I was in 2019, I think I have something to offer, so 
    let's try to ✨de-mystify✨ programming.

[^2]: It was finding the code for my original TBAG that partly inspired me to write this... I'd link the code repository, but I made it private because it's all unintelligable spaghetti.

---

## ✔️ Requirements & FAQs

You don't need any special equipment to use this guide.
A computer or laptop with a functioning internet connection is required, but if you're reading 
    this, you've probably got that sorted.

- ***Do I need to be "smart"?***
  - Nope - I'll guide you through.
  Besides, you're smarter than you think. 😉
- ***Do I need to be good at maths?***
  - Nope. 
  Maths and programming are different skills, but they share some traits, so learning one might 
  make you better at the other.
- ***Do I need a powerful computer?***
  - Nope. 
  Everything we'll do here can be done on an internet-enabled potato[^3].
- ***What do I do if I get ambushed by goblins?***
  - You can try negotiating, but most goblins aren't very talkative.
  In that case, I recommend a
  [*Wand of Magic Missiles*](https://www.dndbeyond.com/magic-items/4794-wand-of-magic-missiles).
- ***Do I need to be able to touch-type?***
  - Nope. 
  If you don't know what touch-typing is, that's fine - it doesn't matter anyway.
- ***Does my operating system matter?***
  - Not for what we're doing. 
  If you don't know what an operating system is,
  **a**) It doesn't matter anyway,
  **b**) You're probably on Microsoft Windows.

[^3]: Maris Pipers have the lowest latency.

---

## 🚀 What this guide will do

This guide will:
 - Teach you that programming ain't that scary
 - Show you how to find help
 - Help you to set up your environment
 - Introduce some programing fundamentals
 - Warn you of pitfalls and demonstrate best practises

This guide will *not*:
 - Take more than 8 hours to finish
 - Abandon you to tutorial-hell
 - Make you a professional software developer
 - Tell you about any tools that are not required for the guide
 - Teach you to brew a [*Draft of Living Death*](https://www.wizardingworld.com/fact-file/plants-and-potions/the-draught-of-living-death)

---

## 🔥 What is tutorial-hell?
First, take a minute to watch this YouTube Short:

<iframe
    width="315" height="560"
    src="https://www.youtube.com/embed/O99NMMk4I4g"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
></iframe>

*Did you watch it? I'll wait...*

Tutorial-hell is where you end up if all you do is blindly copy-paste from tutorials:
    you never learn or become independent.
A sure-fire way to get there is by not listening to people who try to help you 🤨... 
    ***Did you watch that Short??***

This is not a tutorial, it's a *guide* for avoiding or escaping tutorial-hell.
For that, you need skills which a standard *tutorial* won't teach you, namely how to
    think-through problems and find help when things go wrong...

Say this after me: ***"I will not copy and paste in Codename: TEABAG"***... Coz it ain't gonna help you.
If you copy-paste the answer, you won't learn: learning takes practise.

*Together* in this *guide*, we will build a **T**ext-**B**ased **A**dventure **G**ame, just like I did 
    back-in-the-day, but I'm also going to show you how to think for yourself and get help on your own.
Throughout, there will be sections where you have to look things up or use your initiative.
This may be challenging but I'll guide you through.
***Do not skip these sections.***

You *do* want to escape tutorial-hell... Right?

---

## 🤔 What, Why and How

### What is programming?
It may seem like a silly question in a programming tutorial, but it's work asking!

> To Program: Provide (a computer or other machine) with coded instructions for the automatic 
> performance of a task. (Oxford Languages)

Or, in simpler terms, you tell a computer the steps it needs to do some helpful task.
    
Computers are not smart - they're just very fast at executing simple instructions called "machine-code",
Machine-code just tells the computer where to move data from and to inside itself, and it's hard to 
    write because it's all binary, like so:

```
010101000100010101000001010000100100000101000111
```

If that makes any sense to you, you're definitely some kind of demigod and certainly don't need me.

If, on the other hand, you're a normal human being, a "programming language" may be helpful.
Programming languages give humans an easier way to instruct the computer in its task, and they come in
    all shapes and sizes.
Together, these instructions form a "program" which can be translated into the machine-code that the computer
    so desperately craves.


### Why learn programming?

Maybe you're learning because you need it for your education or job.
Perhaps you have some grand project you want to make - the game to end all games?
Some people just want to try it out. All of these are valid reasons to want to learn.

I learned because I wanted to 
    [modify the game *Minecraft*](https://github.com/atom-dispencer/MagiksMostEvile/tree/1.7.10/)
    (I warn you, my old code is dreadful) but I kept going because it lets me make whatever I want.
Given some time and commitment I can create games, helpful tools for myself, or even a [computer inside
    a computer](https://github.com/atom-dispencer/iAtomSys).


### How do I learn to program?
You learn to program the same as any other skill - the piano, perhaps?

To learn an instrument, you'll do some reading and learn some theory, but practise is key!
Any musician will tell you that "theory can only take you so far", which is why this guide will try to 
    make you sweat a bit... (***"I will not copy-paste... I will not copy-paste..."***).
If any mistakes come up (and I'll make sure they will 😉), I encourage you to explore and find out 
    what went wrong so we can learn from and (hopefully) enjoy the experience.

---

## ⏰ Ready to start!?
When you're ready to set up your tools, head to [Lesson #0](./lesson-0)!
