def main():
    #Ask user if they want to hear a joke and keep asking if they don't respond yes, ok or okay.
    while True:
        joke = input("Want to hear a joke? ").strip().casefold()
        if joke.startswith("yes") or joke.startswith("ok"):
            break

    #Start the joke and the user have to respond to exactly the right thing
    knock = input("Knock, knock...\n").strip().lower()
    while knock != "who's there?":
        knock = input().strip().lower()
        if knock == "who's there?":
            break

    #Cow says part
    cow = input("Cow says.\n").strip().lower()
    while cow != "cow says who?":
        cow = input().strip().lower()
    print("No! Cow says Moooooo! lol! XD")

main()