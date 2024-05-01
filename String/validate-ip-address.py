# lc 468
class Solution:
    # 此题无聊
    # time / space O(n) - n = len of queryIP
    def validIPAddress(self, queryIP: str) -> str:
        ipv4_list = queryIP.split('.')
        ipv6_list = queryIP.split(':')

        def is_ipv4(ipv4_list: list[str]) -> bool:
            for ipv4 in ipv4_list:
                if len(ipv4) > 3 or len(ipv4) == 0:
                    return False
                if len(ipv4) > 1 and ipv4[0] == '0':
                    return False
                for c in ipv4:
                    if c not in '0123456789':
                        return False
                ipv4_int = int(ipv4)
                if 0 > ipv4_int or ipv4_int > 255:
                    return False
            return True

        def is_ipv6(ipv6_list: list[str]) -> bool:
            for ipv6 in ipv6_list:
                if len(ipv6) > 4 or len(ipv6) == 0:
                    return False
                for c in ipv6:
                    if c not in '0123456789abcdefABCDEF':
                        return False
            return True


        if len(ipv4_list) != 4 and len(ipv6_list) != 8:
            return 'Neither'
        elif len(ipv4_list) == 4:
            if is_ipv4(ipv4_list):
                return 'IPv4'
            else:
                return 'Neither'
        else: # len(ipv6_list) == 6
            if is_ipv6(ipv6_list):
                return 'IPv6'
            else:
                return 'Neither'

s = Solution()
print(s.validIPAddress('1.0.1.'))