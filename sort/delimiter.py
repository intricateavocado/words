with open('output.txt', 'w') as o:
    with open('input.txt') as i:
        for line in i:
            word = line.strip()
            word = word[1:(len(word)-2)]
            #words = line.split(',')
            #for word in words:
                #word = word[1:(len(word)-1)]
                #o.write(word)
                #o.write(',\n')
            #o.write('"' + line.strip() + '",')
            o.write(word)
            o.write('\n')