# Python Obfuscator

## What's this?

This is a python script that runs a message through Google Translate multiple times, then translates it back to English. This will result in a nonsensical version of your input text.

## How do I use this?

1. Install the dependencies googletrans (for translation) and pyperclip (to copy the output)
2. Run the .py script. You will be able to configure the following things:
 - Iterations (All random): This will change the number of times your text is translated. Using this option, all custom languages will be disabled.
 - Custom Languages: You can use this to force languages for translations. Example: `de fr it rand` will translate your text into German, French, Italian and a randomly selected language.
 - Set Custom language file: Allows you to specify a file with languages possible to translate to. By default, the file assets/languages.json is used.
 - File Translate: Allows you to translate text documents.
