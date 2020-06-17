# Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
# Don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) in IPv6. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

class Solution:
    def validIPAddress(self, IP: str) -> str:

        if not IP  or IP[0] == "0" or "::" in IP: 
            return 'Neither'
        
        import re
        IPv4_leading_zeros = '''^.*\.0[0-9].*$'''
        if re.search(IPv4_leading_zeros, IP):
            return "Neither"
        
        import ipaddress
        try:
            ipX = ipaddress.ip_address(IP.lower())
            return "IPv" + str(ipX.version)
        except ValueError:
            return "Neither"
        
# could have done the whole thing in a regex, but it would be really hard to read.  just used a regex to check for the allowed case of a leading zero in an IPv4.

# ipaddress pretty much does the whole thing (except it allows things like "::" in IPv6, so used it.  and filtered out the things that the assignment specifically disallowed before.
