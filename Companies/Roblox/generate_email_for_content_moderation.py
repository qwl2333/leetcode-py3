'''
Auto generate email for content moderation
input:
- list of blacklisted words and category
[[password: phishing],[assg: spam]...]
- list of words found [assg]
- email body template base on words found [[spam, we found the spam content],[phising, there are contents violating security]...]
output:
- email with body containing what content was found and why it is a violation (email body)
'''
class AutoEmailGenerator:
    def __init__(self) -> None:
        pass

    def generate_email(self, words_found: list[str], blacklisted_words_categories: list[str], category_email_template: list[list[str]]):
        # need a map from category to set of words
        word_to_category = {}
        category_to_body = {}
        for word_category in blacklisted_words_categories:
            word, category = word_category.split(': ')
            word_to_category[word] = category

        # need a map from category to email body template
        for category, body_template in category_email_template:
            category_to_body[category] = body_template
        
        res = []
        for word in words_found:
            category = word_to_category[word]
            msg = category_to_body[category]
            res.append(f'{word} found, {msg}')
        
        return res

