from time import time

print('Press Enter to start typing or to break a new line')
print('Press Enter twice to finish typing')
input('-----------------------------------------------')
# record timestamp when user starts typing
start = time()
text = []
while True:
    line = input()
    if not line:
        break
    text.append(line)
# record timestamp when user finishes typing
end =time()
print('The text user typed in:')
for line in text:
    print(line)
print("[Finished in",round(end-start),"s]")
print("---------------------------------------------")
elapsed_time =(end-start) / 60
chars_count = sum(len(item) for item in text)
words_count = chars_count / 5
wpm = round (words_count / elapsed_time)
print (f'Your average Words Per Minute (WPM) is {wpm}')
if wpm < 30:
    print('You should learn the proper typing technique and practice more to improve your speed')
elif wpm < 40:
    print('Not bad, but still below average. Focus on your technique and keep practicing')
elif wpm < 50:
    print('You are now an average typist. You still have significant room for improvement')
elif wpm < 60:
    print('Congratulations! You are above average')
else:
    print('This is speed required for most jobs. You can now be a professional typist.')
print("[Finished in",round(end-start),"s]")
