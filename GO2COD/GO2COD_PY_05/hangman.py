
# This is my fifth and final Python project as an intern at GO2COD, now tailored with cybersecurity terms.

import random

# Step 1: I create a list of cybersecurity-related words
# These words form the basis for the Hangman game. Each term relates to cybersecurity concepts.
word_list = [
    "firewall", "malware", "phishing", "ransomware", "trojan", "spyware", "adware",
    "encryption", "decryption", "password", "hashing", "spoofing", "botnet", "backdoor",
    "honeypot", "sandboxing", "cyberattack", "breach", "forensics", "keylogger", 
    "antivirus", "patching", "cipher", "token", "rootkit", "whitelist", "blacklist",
    "multifactor", "authentication", "vulnerability", "honeypot", "exploit", "payload", "bruteforce", "credential", "intrusion", "skimmer", 
    "zero-day", "keygen", "worm", "denial-of-service", "social-engineering", 
    "man-in-the-middle", "packet-sniffer", "cryptojacking", "darkpool", 
    "key-escrow", "salting", "obfuscation", "penetration", "red-team", 
    "blue-team", "white-hat", "black-hat", "gray-hat", "fuzzing", 
    "port-scanning", "eavesdropping", "tampering", "replay-attack", 
    "side-channel", "cross-site", "sql-injection", "clickjacking", 
    "dns-poisoning", "privilege-escalation", "session-hijacking", 
    "certificate", "public-key", "private-key", "digital-signature", 
    "intrusion-detection", "siem", "endpoint", "proxy", "vpn", 
    "tor-network", "deepfake", "ratting", "shodan", "airgap", 
    "chroot", "cold-boot", "dead-drop", "exfiltration", "geofencing", 
    "hashcat", "jailbreak", "keyspace", "logic-bomb", "metasploit", 
    "nmap", "onion-routing", "phreaking", "rainbow-table", "root-ca", 
    "scanning", "steganography", "sysadmin", "threat-model", "war-dialing", 
    "watering-hole", "wiretapping", "zombie", "backscatter", "beaconing", 
    "code-signing", "data-leak", "evil-twin", "fileless", "ghosting", 
    "hardening", "kerberos", "ldap", "nonce", "over-the-air", 
    "polymorphic", "quarantine", "remote-shell", "rogue-ap", "sandbox-evasion", 
    "secure-boot", "sinkhole", "tailgating", "tunneling", "upnp", 
    "virtualization", "web-shell", "xss", "yara", "zeus"
]

# Step 2: Randomly select a word from the list
# This is the word the user has to guess.
chosen_word = random.choice(word_list)

# Step 3: Prepare the word display
# Convert each letter in the chosen word to an underscore for the initial display.
display = ["_" for _ in chosen_word]

# Step 4: Set the number of attempts
# Limit the incorrect guesses to 6.
attempts = 6

# Step 5: Keep track of guessed letters
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the cybersecurity-related word, one letter at a time.")
print("You have", attempts, "incorrect guesses available.\n")
print(" ".join(display))  # Show the initial blank word

# Step 6: The main game loop
while attempts > 0 and "_" in display:
    # Ask the user for their guess
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        # Reveal the guessed letter in the display
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = letter
        print("Good job! That letter is in the word.")
    else:
        # Deduct an attempt for an incorrect guess
        attempts -= 1
        print("Wrong guess! You have", attempts, "guesses left.")

    # Display the updated state of the word
    print(" ".join(display))

# Step 7: End of game
if "_" not in display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame over! The word was:", chosen_word)
