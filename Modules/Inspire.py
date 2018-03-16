import random
triggers = ['inspire', 'inspiration']
options = ['Like a fish, one should look for a hole in the net. ~Samoan Proverb',
		'Persevere like a bird in the wind. ~Samoan Proverb',
		'Life is like this: sometimes sun, sometimes rain. ~Fijian Proverb',
		'All knowledge is not taught in one school. ~ Hawaiian Proverb',
		'Wonderful people come in different shapes and sizes.',
		'Beauty is how you feel on the inside.',
		'Take care of your body. It\'s the only place you have to live. ~Jim Rohn',
		'Of all things you wear, your expression is the most important.',
		'Beauty captures your attention but personality captures your heart.',
		'I\'ve never seen a smiling face that was not beautiful.',
		'Happiness is not a station you arrive at, but a manner of traveling. ~Margaret B. Runbeck',
		'Life isn\'t about finding yourself. Life is about creating yourself. ~George Bernard Shaw',
		'Failure is success if we learn from it. ~Malcolm S. Forbes',
		'But the real secret to total gorgeousness is to believe in yourself, have self confidence, and try to be secure in your decisions and thoughts. ~Kirsten Dunst',
		'Everything has beauty, but not everyone sees it. ~Confucius',
		'It\'s not what you look like, that makes you who you are. It\'s what you do, that makes you who you are.',
		'One can build a better world by using our talents.',
		'Beauty is not in the face; beauty is a light in the heart. ~Kahlil Gibran',
		'That which is striking and beautiful is not always good, but that which is good is always beautiful. ~Ninon de L\'Enclos']
def handle(f,sender,msg,loc,rsvp,send):
	for trigger in triggers:
		if trigger in msg:
			rsvp(f,loc,random.choice(options))
			return
def privhandle(f,sender,msg,loc,rsvp,send):
	handle(f,sender,msg,loc,rsvp,send)