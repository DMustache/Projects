d(text[i + j]) - ord(elems[-1][-1]) <= 1:
                elems[-1] += text[i + j]
            else:
                elems.append('')
                p