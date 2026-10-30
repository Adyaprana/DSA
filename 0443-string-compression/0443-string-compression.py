class Solution(object):
    def compress(self, chars):
        read = 0
        write = 0 
        while read < len(chars):
            current_char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == current_char:
                count = count + 1
                read = read + 1
            chars[write] = current_char
            write = write + 1
            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write = write + 1
        return write
