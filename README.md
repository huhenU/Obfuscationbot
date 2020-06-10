# Python Obfuscator

## What's this?

This is a python script that runs a message through Google Translate multiple times, then translates it back to English. This will result in a nonsensical version of your input text.

## How do I use this?

1. Make sure you have the googletrans package installed (required to communicate with Google Translate)
2. Run the .py script. You will be able to configure the following things:
 - Iterations (All random): This will change the number of times your text is translated. Using this option, all custom languages will be disabled.
 - Custom Languages: You can use this to force languages for translations. Example: `de fr it rand` will translate your text into German, French, Italian and a randomly selected language.
 - Set Custom language file: Allows you to specify a file with languages possible to translate to. By default, the file assets/languages.json is used.
 - File Translate: Allows you to translate text documents.
 - Mass file translation: Allows you to mass translate a lot of strings in one file, while handling them as own sentences, not entire files. Currently, strings require to be structured in a very specific way. See example.json for an example on how to structure the file. Final translations will be written to output.txt, instead of the output window.
 - Use Proxy: Allows you to connect through a proxy in case you can't connect to Google Translate. HTTP and SOCKS proxies are supported. Example: `socks5://192.168.1.106:5555` would use a SOCKS proxy on IP-Address 192.168... and port 5555. For an HTTP proxy, just use IP and port. Example: `192.168.2.106:5555`
 - Ability to change language of the UI (requires editing the config in assets/config.ini). German translation included, restart the program after editing the config.
