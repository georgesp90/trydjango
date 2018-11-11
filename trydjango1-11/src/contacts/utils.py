import random
import string
from twilio.rest import Client
import sys
import schedule
import datetime
import time
import threading




from django.utils.text import slugify
'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

account_sid = "ACbbbd9efe355a2376772ffcf060f6794a"
auth_token = "c025f7bb1a54431e67824b107bca44a9"
my_twilio = "+1(201) 552-4734"
welcome_message = "welcome my name is Ellie and im here to inspire!"
test_message = "you did it"

contacts_to_message = {}

client = Client(account_sid, auth_token)


def send_welcome_message(**kwargs):
    message = client.api.account.messages.create(**kwargs)


def send_quote_to_multi_contacts():
    q = UserContacts.objects.values('phone')
    for phome in q:
        message = client.messages.create(to=phone, from_=my_twilio, bod=test_message)



DONT_USE =['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


quote =[
"The gem cannot be polished without friction, nor man perfected without trials. -- Chinese proverb ",
"An investment in knowledge always pays the best interest. --  Benjamin Franklin",
"Remember, you can earn more money, but time when spent is gone forever. -- Zig Ziglar",
"The greatest of all weaknesses is the fear of appearing weak. -- J. B. Bossuet, Politics from Holy Writ, 1709",
"The first requisite of success is the ability to apply your physical and mental energies to one problem without growing weary. -- Thomas Edison",
"We don't stop playing because we grow old; we grow old because we stop playing. -- George Bernard Shaw",
"Great things are not done by impulse, but by a series of small things brought together. -- Vincent Van Gogh",
"I feel that the greatest reward for doing is the opportunity to do more. -- Jonas Salk ",
"You've got to be before you can do, and do before you can have. -- Zig Ziglar ",
"A superior man is modest in his speech, but exceeds in his actions. -- Confucius",
"Ability will never catch up with the demand for it. -- Confucius ",
"No matter how busy you may think you are, you must find time for reading, or surrender yourself to self - chosen ignorance.-- Confucius",
"Our greatest glory is not in never falling, but in rising every time we fall. -- Confucius",
"Real knowledge is to know the extent of one's ignorance. -- Confucius",
"We become what we think about. -- Earl Nightingale",
"The mind is everything. What you think you become. -- Buddha",
"Life shrinks or expands in proportion to one's courage. -- Anais Nin",
"Either you run the day, or the day runs you. --Jim Rohn",
"https://www.youtube.com/watch?v=pnDdpGLsJ3I",
"https://www.youtube.com/watch?v=MXghcI8hcWU",
"The only person you are destined to become is the person you decide to be. -- Ralph Waldo Emerson",
"Whatever you can do, or dream you can, begin it.  Boldness has genius, power and magic in it. --Johann Wolfgang von Goethe",
"Learning without thought is labor lost; thought without learning is perilous. -- Confucius", 
"The only worthwhile achievements of man are those which are socially useful. -- Alfred Adler",
"God put me on Earth to accomplish a certain number of things. Right now I'm so far behind I will never die!  -- Anonymous",
"Lack of direction, not lack of time, is the problem. We all have twenty - four hour days. -- Zig Ziglar",
"Destiny is not a matter of chance, it is a matter of choice; it is not a thing to be waited for, it is a thing to be achieved. -- William Jennings Bryan",
"Unless a man undertakes more than he possibly can do, he will never do all that he can. -- Henry Drummond",
"The best job goes to the person who can get it done without passing the buck or coming back with excuses. -- Napolean Hill",
"Only those who dare to fail greatly can ever achieve greatly. -- Robert Francis Kennedy",
"The heights by great men reached and kept; Were not obtained by sudden flight; But they, while their companions slept; Were toiling upward in the night. -- Henry Wadsworth Longfellow",
"You don't drown by falling in water; you only drown if you stay there. -- Zig Ziglar",
"What you get by achieving your goals is not as important as what you become by achieving your goals. -- Zig Ziglar",
"Obstacles are things a person sees when he takes his eyes off his goal. -- E. Joseph Crossman",
"The man who can drive himself further once the effort gets painful is the man who will win. -- Roger Bannister", 
"You'll never achieve your dreams if they don't become goals. -- Anonymous",
"The spirit, the will to win, and the will to excel are the things that endure. These qualities are so much more important than the events that occur. -- Vince Lombardi",
"'Lombardi time' is the principle that one should arrive 10 - 15 minutes early, or else be considered late. -- Vince Lombardi",
"Every worthwhile accomplishment, big or little, has its stages of drudgery and triumph; a beginning, a struggle and a victory. -- Ghandi",
"The price of success is hard work, dedication to the job at hand, and the determination that whether we win or lose, we have applied the best of ourselves to the task at hand. -- Vince Lombardi",
"A failure establishes only this, that our determination to succeed was not strong enough. -- Christian Nestell Bovee",
"He who has a why to live for can bear almost any how. -- Friedrich Nietzsche",
"https://youtu.be/PuPYIfcSz_Y",
"For every minute you are angry you lose sixty seconds of happiness. -- Ralph Waldo Emerson also, Tim YoungBlood",
"Happiness lies in the joy of achievement and the thrill of creative effort. -- Franklin D. Roosevelt",
"Happiness is not something you postpone for the future; it is something you design for the present. -- Jim Rohn",
"A leader, once convinced that a particular course of action is the right one, must....be undaunted when the going gets tough.  -- Ronald Reagan",
"it is not what happens to you that determines how far you will go in life ;it is how you handle what happens to you. -- Zig Ziglar",
"Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned. -- Buddha",
"The optimist sees opportunity in every danger; the pessimist sees danger in every opportunity. -- Winston Churchill",
"A positive attitude may not solve all your problems, but it will annoy enough people to make it worth the effort. -- Herm Albright",
"There are no menial jobs, only menial attitudes. -- William John Bennett",
"hard work beats talent when talent doesnt work hard -- Tom Notke",
"If you do what you've always done, you'll get what you've always got -- ? ",
"https://youtu.be/us-GVbuyz74",
"Stay hungry, stay foolish. -- Steve Jobs",
"Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do. -- Pele",
"Success isn't always about greatness. It's about consistency. Consistent hard work leads to success. Greatness will come. -- Dwayne Johnson",
"Happiness is when what you think, what you say, and what you do are in harmony. -- Mahatma Gandhi",
"What lies behind us and what lies before us are tiny matters compared to what lies within us. -- Ralph Waldo Emerson",
"On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow. -- Friedrich Nietzsche",
"People of mediocre ability sometimes achieve outstanding success because they don't know when to quit. Most men succeed because they are determined to. -- George E. Allen",
"Success seems to be connected with action. Successful men keep moving. They make mistakes, but they don't quit. -- Conrad Hilton",
"Good ideas are not adopted automatically. They must be driven into practice with courageous patience. -- Admiral Hyman Rickover",
"In order to get from what was to what will be, you must go through what is. -- Anonymous",
"Perseverance is not a long race; it is many short races one after another. -- Walter Elliott",
"Victory is always possible for the person who refuses to stop fighting. -- Napoleon Hill",
"Learning is not compulsory. . . neither is survival. -- Dr. W. Edwards Deming",
"What we think or what we believe is, in the end, of little consequence. The only thing of consequence is what we do. -- John Ruskin",
"Have no fear of perfection - you'll never reach it. -- Salvidor Dali",
"https://youtu.be/fLeJJPxua3E",
"The important thing is this: to be able, at any moment, to sacrifice what we are for what we could become. -- Maharishi Mahesh Yogi",
"Undoubtedly a man is to labor to better his condition, but first to better himself -- William Ellery Channing",
"Getting what you want is not nearly as important as giving what you have. -- Tom Krause",
"To gain that which is worth having, it may be necessary to lose everything else. -- Bernadette Devlin",
"Sweat plus sacrifice equals success. -- Charlie Finley",
"https://youtu.be/0wdUDD6HaC0",
"https://www.youtube.com/watch?v=a5SMyfbWYyE",
"One half of knowing what you want is knowing what you must give up before you get it. -- Sidney Howard",
"Dreams do come true, if we only wish hard enough, You can have anything in life if you will sacrifice everything else for it. -- James Matthew Barrie",
"Artists must be sacrificed to their art. Like bees, they must put their lives into the sting they give. -- Ralph Waldo Emerson",
"Success is often the result of taking a misstep in the right direction. -- Al Bernstein",
"A successful man is one who can lay a firm foundation with the bricks others have thrown at him. -- David Brinkley",
"Are you bored with life? Then throw yourself into some work you believe in with all your heart, live for it, die for it, and you will find happiness that you had thought could never be yours. -- Dale Carnegie",
"Instead of worrying about what people say of you, why not spend time trying to accomplish something they will admire. -- Dale Carnegie",
"The successful man will profit from his mistakes and try again in a different way. -- Dale Carnegie",
"Inaction breeds doubt and fear. Action breeds confidence and courage. If you want to conquer fear, do not sit home and think about it. Go out and get busy. -- Dale Carnegie",
"Success means getting up one more time than you fall. -- Oliver Goldsmith",
"Never stop. -- Greg Bigwood",
"https://www.youtube.com/watch?v=fLeJJPxua3E",
"Don't cry because it's over, smile because it happened. -- Dr. Seuss",
"Living well is the best revenge. -- George Herbert",
"dont watch the clock do what it does. Keep going. -- Sam Levenson",
"the future belongs to those who believe in the beauty of their dreams. -- Eleanor Roosevelt",
"Think like a man of action, act like a man of thought. -- Henry Bergson",
"An ounce of practice is worth more than tons of preaching. -- Gandhi",
"Pres forward. Do not stop, do not linger in your journey, but strive for the mark set before you -- George Whitefield",
"There will be obstacles. there will be doubters. There will be mistakes. But with hard work, there are no limits -- Michael Phelps",
"First they ignore you, then they laugh at you, then they fight you, then you win. -- Gandhi",
"Man becomes great exactly in the degree in which he works for the welfare of his fellow - men. -- Gandhi",
"I suppose leadership at one time meant muscles; but today it means getting along with people. -- Gandhi",
"Constant development is the law of life, and a man who always tries to maintain his dogmas in order to appear consistent drives himself into a false position. -- Gandhi",
"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. --Albert Einstein",
"Any change, even a change for the better, is always accompanied by drawbacks and discomforts. --Arnold Bennett",
"Change is inevitable. Change is constant. --Benjamin Disraeli",
"When you're finished changing, you're finished. --Benjamin Franklin",
"The price of doing the same old thing is far higher than the price of change. --Bill Clinton",
"Be yourself everyone else is already taken - Oscar Wilde",
"You've gotta dance like there's nobody watching, Love like you'll never be hurt, Sing like there's nobody listening, And live like it's heaven on earth. -- William W. Purkey"
]


def get_random_quote():
    return random.choice(quote)


def my_quote():
    return get_random_quote()