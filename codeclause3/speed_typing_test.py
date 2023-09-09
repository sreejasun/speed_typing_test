import time
sample_text = "the quick brown fox jumps over the lazy dog"
def speed_typing_test():
    input("Press Enter to start the typing test.")
    print("\nType the following text:")
    print(sample_text)
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    correct_chars = sum(c1 == c2 for c1, c2 in zip(sample_text, user_input))
    words_per_minute = (correct_chars / 5) / (time_taken / 60)
    print("\nTime taken: {:.2f} seconds".format(time_taken))
    print("Correct characters: {}".format(correct_chars))
    print("Typing speed: {:.2f} WPM".format(words_per_minute))
if __name__ == "__main__":
    speed_typing_test()