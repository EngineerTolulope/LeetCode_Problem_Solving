class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_length = 0

        for word in words:
            # If the current line length plus the length of the next word and the necessary spaces is greater than maxWidth, justify the current line
            if line_length + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '  # Distribute extra spaces evenly
                
                result.append(''.join(line))
                line = []
                line_length = 0

            line.append(word)
            line_length += len(word)

        result.append(' '.join(line).ljust(maxWidth))  # Left justify the last line

        return result