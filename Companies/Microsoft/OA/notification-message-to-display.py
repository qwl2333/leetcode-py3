# we have a message, and a limit k, returns a notification message not exceeding k, if message is longer than k
# crop the message with '...'
# For instance, message = 'And now here is my secret', k = 15, the notification message is 'And now here ...'
class Solution:
    # Time O(n), space O(n), n - number of words in message
    def show_notification_message(self, message: str, k: int) -> str:
        if len(message) <= k:
            return message

        words_arr = message.split(' ')
        res = ''
        for word in words_arr:
            if len(res) + len(word) + 4 > k:
                if res == '':
                    return '...'
                else:
                    return res + '' + '...'
            else:
                res += word + ' '
        
        return '123'

s = Solution()
print(s.show_notification_message('how are you', 20))