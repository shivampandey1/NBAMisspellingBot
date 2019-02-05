import praw #importing reddit API
client_id=odBkZtG0-Vl_wA
client_secret= ********
password= ********
username=thekaoswithin
user_agent=NBASpellingbot 0.1

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("nba") #indicating to the bot what subreddit it should be looking at

comment_log_path = "log.txt"

misspells = {
    "Kawhi": [
        "Kawii",
        "Kawai",
        "Kawahi",
        "Khawi",
        "Kwahi",
        "uruguary",
    ],
    "Derozan": [
        "Derozen",
        "Derosen",
    ],
    "Nowitzki": [
    	"Nowitski"
    ]

}

replies = [
    "Psst! It's spelled **{}**.",
    "Uhhh I think it's spelled **{}**...",
]

def find_substring(needle, haystack):
    """ Only returns true if needle is found and it's a whole word."""
    index = haystack.find(needle)
    if index == -1:
        return False
    if index != 0 and haystack[index-1] in string.letters:
        return False
    L = index + len(needle)
    if L < len(haystack) and haystack[L] in string.letters:
        return False
    return True


def is_quote(text):
    return len(text) > 1 and text[0] == '>'


def check_misspells(text, misspells):
    for version in misspells:
        if find_substring(version, text.lower()):
            return True


def get_reply():
    return random.choice(replies)


def check_condition(comment):
    """ Has the bot been called?"""
    paragraphs = [
        paragraph for paragraph in comment.body.split('\n')
        if not is_quote(paragraph)
    ]
    for paragraph in paragraphs:
        # Separate by paragraphs to avoid triggering by quoted text.
        for word in misspells:
            if check_misspells(paragraph, misspells[word]):
                return get_reply().format(word)