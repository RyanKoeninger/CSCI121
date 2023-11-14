def brick_maker(f):
    def brick(width,height):
        h = 0
        string = ''
        while h < height:
            w = 0
            while w < width:
                string += f 
                w += 1
            string += '\n'
            h += 1
        return string
    
    return brick