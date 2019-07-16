import requests

class colour():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def rgb_to_ansi(r, g, b):
    if (r == g and g == b):
        if (r < 8): 
            return 16
        elif (r > 248):
            return 231
        else:
            return int(((r - 8) / 247) * 24) + 232;

    ansi = 16 + (36 * int(r / 255 * 5)) + (6 * int(g / 255 * 5)) + int(b / 255 * 5);

    return ansi

def rgb_middles(colour1, colour2, count):
    middles = []

    for i in range(count):
        middles.append(colour(colour1.r+((colour2.r-colour1.r)/count)*i,colour1.g+(colour2.g-colour1.g)/count*i,colour1.b+(colour2.b-colour1.b)/count*i))

    return middles

def print_gradient(col):
    for colour in col:
        print("\033[48;2;" + str(int(colour.r)) + ";" + str(int(colour.g)) + ";" + str(int(colour.b)) +  "m                       \033[0m")

def main(count):
    hex_colours = []
    col = []

    for i in range(count):
        hex_colours.append(requests.get("http://api.noopschallenge.com/hexbot").json())
    
    for c in hex_colours:
        r = int(c["colors"][0]["value"][1:3], 16)
        g = int(c["colors"][0]["value"][3:5], 16)
        b = int(c["colors"][0]["value"][5:7], 16)
    
        col.append(colour(r, g, b))
    
    for i in rgb_middles(col[0], col[1], 20):
        col.insert(-1, i)

    print(hex_colours[0]["colors"][0]["value"])
    print_gradient(col)
    print(hex_colours[1]["colors"][0]["value"])
    
    
if __name__ == "__main__":
    while True:
        main(2)

        count = input()
        if count == "exit":
             quit()
