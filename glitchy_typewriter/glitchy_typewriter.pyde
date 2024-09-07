phrase = "Glitch is something that extends beyond the most literal technological mechanics: it helps us to celebrate failure as a generative force, a new way to take on the world."  
words = phrase.split(" ")  
drawnWords = []  
  
MARGIN = 40  

wordCount = 0  
nextUpdateMillis = 0  

minTextSize = 20  
maxTextSize = 30
  
cx = MARGIN  
cy = MARGIN
  
spaceWidth = 0    
lineHeight = 0 
  
class FadingWord:  
    def __init__(self, _word, _wordDelay):  
        self.word = _word  
        self.alpha = 255  
        self.startTime = millis()  
        self.letterDelay = _wordDelay / len(self.word)  
          
        self.red = 0  
        self.font = createFont("Sans-Serif", minTextSize)  
        self.size = minTextSize  
        self.yOffset = 0  
        self.fadeVel = -0.3  
  
        if self.word.lower() == "glitch" or random(1.0) > 0.95:  
            self.word = self.word.upper()  
            self.red = 200  
            self.font = createFont("Monospaced", maxTextSize)  
            self.size = maxTextSize  
            self.yOffset = -self.size / 6  
            self.fadeVel = -0.01  
  
        textFont(self.font)  
        textSize(self.size)  
        self.width = textWidth(self.word)  

        # update cx and cy and set this.x and this.y
        # if placing the next word on this line causes overflow
        global cx, cy  
        if cx + textWidth(self.word) > width - MARGIN:  
            cx = MARGIN  
            cy += lineHeight  
        
        # if larger than canvas
        if cy > height - MARGIN:  
            cy = MARGIN  
  
        self.x = cx  
        self.y = cy  
        cx += self.width + spaceWidth  
  
    def update(self):  
        self.alpha += self.fadeVel  
        # if self.alpha < 0:  
        #     self.alpha = 0  
  
    def draw(self):  
        elapsed = millis() - self.startTime  
        lastLetter = min(int(elapsed / self.letterDelay), len(self.word))  
        letters = self.word[:lastLetter]  
  
        fill(self.red, 0, 0, self.alpha)  
        textFont(self.font)  
        textSize(self.size)  
        text(letters, self.x, self.y + self.yOffset)  
  
def setup():  
    global spaceWidth, lineHeight  
    size(800, 600)  
    
    textAlign(LEFT, TOP);
    textFont(createFont("Sans-Serif", minTextSize))  
    
    spaceWidth = textWidth(" ")  
    lineHeight = 1.5 * textAscent()  
  
def isVisible(fw):
    return fw.alpha > 0

def draw():  
    global nextUpdateMillis, wordCount, cx, cy, drawnWords  
    background(220)  
    
    drawnWords = [word for word in drawnWords if isVisible(word)]

    # iterate over drawn words, update and draw them
    for wi in range(len(drawnWords)):
        nextWord = drawnWords[wi]
        nextWord.update()
        nextWord.draw() 
      
    # check if it's time to add a new FadingWord to array
    if millis() > nextUpdateMillis:
        nextWordIndex = wordCount % len(words)
        nextWord = words[nextWordIndex]
    
        # add word to array
        wordDelay = random(450, 600)
        drawnWords.append(FadingWord(nextWord, wordDelay))
    
        # always increment the word count
        wordCount += 1
    
        # next update time in millis, with some variation
        nextUpdateMillis = millis() + 1.2 * wordDelay
