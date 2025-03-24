from random import randint

complment_list = [
    'I can’t take my eyes off of you.',
    'Your perfume smells like heaven.',
    'I could listen to you talk for hours.',
    'You inspire me to become a better person.',
    'You’re the type of girl that every guy dreams of.',
    'My face hurts from how much you make me smile.',
    'If you were a song, you’d be the hottest single on Spotify.']

insult_list = [
    'I was today years old when I realized I didn’t like you.',
    'Someday you’ll go far. And I really hope you stay there.',
    'Oops, my bad. I could’ve sworn I was dealing with an adult.',
    'I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?',
    'Remember that time you were saying that thing I didn’t care about? Yeah, that is now.',
    'You’re the reason God created the middle finger.',
    'I’m busy right now, can I ignore you another time?',
    'Oh, you don’t like being treated the way you treat me? That must suck.',
    'I wish I had a flip phone, so I could slam it shut on this conversation.',
    'N’Sync said it best, “BYE, BYE, BYE!”',
    'You’re a gray sprinkle on a rainbow cupcake.',
    'Your secrets are always safe with me. I never even listen when you tell me them.',
    'You bring everyone so much joy! You know, when you leave the room. But, still.',
    'How many licks until I get to the interesting part of this conversation?'
]
def compliment() -> str:
    return complment_list[randint(0, len(complment_list)-1)]

def insult() -> str:
    return insult_list[randint(0,len(insult_list)-1)]