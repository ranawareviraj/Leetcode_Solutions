class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(octate):
            return not ((octate[0] == "0" and len(octate) > 1) or int(octate) > 255)

        def backtrack(curr, index):
            if len(curr) > 4:
                return

            if index == len(s) and len(curr) == 4:
                ip_addresses.append(".".join(curr[:]))
            
            if index >= len(s):
                return

            for i in range(1, 4):
                octate = s[index : index + i]
                if valid(octate):
                    curr.append(octate)
                    backtrack(curr, index + i)
                    curr.pop()

        ip_addresses = []
        backtrack([], 0)
        return ip_addresses
