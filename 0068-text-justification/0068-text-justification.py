class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # Store the final justified lines
        i = 0

        while i < len(words):
            line_length = len(words[i])  # Initialize line length with the first word
            line = [words[i]]  # Initialize the line with the first word
            i += 1

            # Add words to the line until it reaches maxWidth
            while i < len(words) and line_length + len(words[i]) + len(line) <= maxWidth:
                line_length += len(words[i])
                line.append(words[i])
                i += 1

            # Justify the line
            if i < len(words) and len(line) > 1:
                spaces_needed = maxWidth - line_length
                num_gaps = len(line) - 1
                spaces_between_words = spaces_needed // num_gaps
                extra_spaces = spaces_needed % num_gaps

                justified_line = []  # Store the justified line

                for j in range(len(line) - 1):
                    justified_line.append(line[j])  # Add word to justified line
                    justified_line.append(" " * (spaces_between_words + (extra_spaces > 0)))  # Add spaces between words
                    extra_spaces -= 1

                justified_line.append(line[-1])  # Add the last word in the line
                result.append("".join(justified_line))  # Convert justified line to string and append to result
            else:
                result.append(" ".join(line).ljust(maxWidth))  # Left-justify the line with single word

        return result
        
    # Initial 
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line, length = [], [], 0

        i = 0
        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1) 

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                result.append("".join(line))
                line, length = [], 0
            
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        result.append(last_line + " " * trail_space)
        return result