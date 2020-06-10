from tkinter import *
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfilename
from googletrans import Translator
import random, json, os
import configparser

config = configparser.ConfigParser()
config.read('assets/config.ini')

with open('assets/languages/strings' + config['GENERAL']['UILanguage'] + '.json') as stringsjson:
  stringsJSON = json.load(stringsjson)


strings = stringsJSON['Normal'][0]
errors = stringsJSON['Errors'][0]
buttontext = stringsJSON['Buttons'][0]

mainwindow = Tk()
mainwindow.title('Obfuscator')
mainwindow.iconbitmap('assets/icon.ico')
mainwindow.geometry("649x450+553+314")
mainwindow.minsize(120, 1)
mainwindow.maxsize(3844, 1061)
mainwindow.resizable(1, 1)

proxyenabled = tk.IntVar()
proxystring = ""
customlanguages = ""
translatefilename = ""
translatedText2final = ""
massJSON = ""
langfilename = config['GENERAL']['languagefile']
langamount = 85
iterationsdefined = False
text = Text(mainwindow)
text.place(relx=0.015, rely=0.022, relheight=0.698, relwidth=0.972)
proxytext = Entry(mainwindow)
proxytext.place(relx=0.832, rely=0.756,height=20, relwidth=0.16)
proxytext.insert(END,'Proxy-Domain')

def tail(file, n=1, bs=1024):
    f = open(file)
    f.seek(0,2)
    l = 1-f.read(1).count('\n')
    B = f.tell()
    while n >= l and B > 0:
            block = min(bs, B)
            B -= block
            f.seek(B, 0)
            l += f.read(block).count('\n')
    f.seek(B, 0)
    l = min(l,n)
    lines = f.readlines()[-l:]
    f.close()
    return lines

def obfuscate():
    global text
    global translatefilename
    global customnum
    global translatedText2
    global translatedText2final
    global massJSON
    if iterationsdefined == False:
        return tk.messagebox.showerror(title='Error', message=errors['NoLanguagesOrIterations'])
    
    if len(text.get('1.0', 'end')) - 1 < 1:
       return tk.messagebox.showerror(title='Error', message=errors['NoTextEntered'])
    
    if proxyenabled.get() == 1:
        proxystring = proxytext.get()
        ProxyDict = {
                'https': proxystring
                }
        config['PROXY']['proxyip'] = proxytext.get()
        with open('assets/config.ini', 'w') as configfile:
            config.write(configfile)
        translator = Translator(proxies=ProxyDict)
    else:
        translator = Translator()
        
    openedfile = open(langfilename, 'r')
    openedfileread = openedfile.read()
    customlanguagesread = openedfileread.split(', ')
    if translatefilename != "":
        translatefileopen = open(translatefilename, 'r')
        originalText = translatefileopen.read()
    else:  
        
        originalText = text.get("1.0", "end")
    customnum = 0
    massJSONnum = 1
    for i in range(numberofiterations):
        if customlanguages != "":
            forcelanguage = customlanguages.split(' ')
            languagesd = forcelanguage[customnum]
            if languagesd == "rand":
                languagesd = random.choice(customlanguagesread)
            customnum += 1
        else:
            languagesd = random.choice(customlanguagesread)

        if massJSON != "":
            originalText = massJSON[str(massJSONnum)]
            print(strings['ConsoleTranslatingTo'] + languagesd)
            translatedText = translator.translate(originalText, dest=languagesd)

            print(strings['ConsoleTranslatingOut'] + translatedText.text + '\n')
            originalText = translatedText.text
            translatedText2 = translator.translate(translatedText.text, dest='en')
            translatedText2final += str(massJSONnum) + ": " + translatedText2.text + '\n'
            writetempfile = open("assets/temp.txt", "w+")
            writetempfile.write(translatedText2final)
            writetempfile.close()
            if massJSONnum < len(massJSON):
                massJSONnum += 1
            else:
                massJSONnum = 1

        else:
            print(strings['ConsoleTranslatingTo'] + languagesd)
            translatedText = translator.translate(originalText, dest=languagesd)

            print(strings['ConsoleTranslatingOut'] + translatedText.text + '\n')
            originalText = translatedText.text

            translatedText2 = translator.translate(translatedText.text, dest='en')

    customnum = 0
    if translatefilename != "":
        translatefilename = ""
        text["state"] = "normal"
        text.delete(1.0, END)
    if massJSON != "":
        translatefilename = ""
        text["state"] = "normal"
        text.delete(1.0, END)
    print(strings['ConsoleTranslatingFinalOut'] + translatedText2.text)
    outputwindow = Toplevel()
    outputwindow.title(strings["OutputwindowTitle"])
    outputwindow.iconbitmap('assets/icon.ico')
    TranslText = Text(outputwindow)
    TranslText.grid()
    if massJSON != "":
        outmass = tail("assets/temp.txt", len(massJSON))
        final_outmass = ','.join(outmass)
        outputfile = open("output.txt", "w+")
        outputfile.write(final_outmass.replace(",", ""))
        outputfile.close()
        os.remove("assets/temp.txt")
        TranslText.insert(END, "See output file")
    else:
        TranslText.insert(END, translatedText2.text)
        buttonCpy = Button(outputwindow, height=3, width=80, text=buttontext["OutputCopy"], command=copyoutput)
        buttonCpy.grid()
    massJSON = ""
    translatedText2final = ""


def iterations():
    global numberofiterations
    global customlanguages
    global iterationsdefined
    global massJSON

    iterationsprompt = askstring(strings['IterationsPromptTitle'], strings['IterationsPrompt'])
    numberofiterations = int(iterationsprompt)
    if numberofiterations < 1:
        tk.messagebox.showerror(title=errors['ErrormessageTitle'], message=errors['NoValidNumber'])
        return iterations()
        
    customlanguages = ''
    iterationsdefined = True
    print('')
    print(strings['ConsoleIterationsSet'] + str(numberofiterations))
    if massJSON != "":
        numberofiterations = int(iterationsprompt) * len(massJSON)




def customlanguagesoption():
    global customlanguages
    global numberofiterations
    global iterationsdefined
    global massJSON

    customlangprompt = askstring(strings['CustomlangPromptTitle'], strings['CustomLanguagesPrompt'])
    if len(str(customlangprompt)) < 2:
        return tk.messagebox.showerror(title=errors['ErrormessageTitle'], message=errors['NoValidLanguagesInput'])
    customlanguages = str(customlangprompt)
    numberofiterations = len(customlanguages.split(' '))
    iterationsdefined = True
    Iterationsbutton["state"] = "disabled"
    print(strings['ConsoleIterationsSetAuto'] + str(numberofiterations))
    if massJSON != "":
        numberofiterations = len(customlanguages.split(' ')) * len(massJSON)
    ResetCustomlangbutton["state"] = "normal"
    
def usecustomlanguagefile():
    global langfilename
    global langamount

    langfilenameask = askopenfilename(filetypes=(("Text File", "*.txt"),
                                              ("All files", "*.*") ))
    openedfile = open(langfilenameask,'r')
    openedfileread = openedfile.read()
    if len(openedfileread) < 2:
        return tk.messagebox.showerror(title=errors['ErrormessageTitle'], message=errors['NoValidLanguagesInFile'])

    customlanguagesread = openedfileread.split(', ')
    langfilename = langfilenameask
    config['GENERAL']['languagefile'] = langfilename
    with open('assets/config.ini', 'w') as configfile:
        config.write(configfile)
    print(strings['CustomlangfileRead1'] + str(len(customlanguagesread)) + strings['CustomlangfileRead2'])

def filetranslate():
    global translatefilename
    translatefilenameask = askopenfilename(filetypes=((strings['Textfilesname'], "*.txt"),
                                              (strings['Allfilesname'], "*.*") ))
    
    amountchars = len(open(translatefilenameask).read())
    if amountchars < 1:
        return tk.messagebox.showerror(title=errors['ErrormessageTitle'],message=errors['EmptyDocument'])

    translatefilename = translatefilenameask

    print(translatefilename + strings['ConsoleTranslateDocSelected'])
    text.delete(1.0,END)
    text.insert(1.0,strings['DocumentTranslationText'])
    text["state"] = "disabled"

def copyoutput():
    mainwindow.clipboard_clear()
    mainwindow.clipboard_append(translatedText2.text)

def editproxyconfig():
    config['PROXY']['proxyenabled'] = str(proxyenabled.get())
    with open('assets/config.ini', 'w') as configfile:
        config.write(configfile)

def moreoptions():
    moreoptionswindow = Toplevel()
    moreoptionswindow.title(buttontext["MoreOptionsButton"])
    moreoptionswindow.iconbitmap('assets/icon.ico')
    CustomLangFilebutton = Button(moreoptionswindow, height=2, width=25, text=buttontext['CustomlangFileButton'], command=usecustomlanguagefile)
    TranslateDocbutton = Button(moreoptionswindow, height=2, width=25, text=buttontext['TranslateDocButton'], command=filetranslate)
    MassTranslateDocbutton = Button(moreoptionswindow, height=2, width=25, text=buttontext['MassTranslateDocButton'], command=masstranslate)
    CustomLangFilebutton.grid()
    TranslateDocbutton.grid()
    MassTranslateDocbutton.grid()

def resetcustomlang():
    Iterationsbutton["state"] = "normal"
    print('Custom languages successfully cleared.')
    ResetCustomlangbutton["state"] = "disabled"

def masstranslate():
    global massJSON
    translatefilenameask = askopenfilename(filetypes=((strings['JSONfilesname'], "*.json"),
                                                      (strings['Allfilesname'], "*.*")))

    with open(translatefilenameask) as massfile:
        massJSON = json.load(massfile)
    if len(massJSON) < 1:
        return tk.messagebox.showerror(title=errors['ErrormessageTitle'], message=errors['EmptyDocument'])

    print(translatefilenameask + strings['ConsoleTranslateDocSelected'])
    text.delete(1.0, END)
    text.insert(1.0, strings['DocumentMassTranslationText'])
    text["state"] = "disabled"

Obfuscatebutton = Button(mainwindow, height=1, width=100, text=buttontext['ObfuscateButton'], command=obfuscate)
Customlangbutton = Button(mainwindow, height=1, width=100, text=buttontext['CustomlangButton'], command=customlanguagesoption)
Iterationsbutton = Button(mainwindow, height=1, width=100, text=buttontext['IterationsButton'], command=iterations)
ResetCustomlangbutton = Button(mainwindow, height=1, width=100, text=buttontext['ResetCustomLangButton'], command=resetcustomlang)
MoreOptionsbutton = Button(mainwindow, height=1, width=100, text=buttontext['MoreOptionsButton'], command=moreoptions)
Proxybutton = tk.Checkbutton(mainwindow, command=editproxyconfig, text=buttontext['UseProxyCheckbutton'], variable=proxyenabled, onvalue=1, offvalue=0)

Obfuscatebutton.place(relx=0.015, rely=0.733, height=64, width=527)
Customlangbutton.place(relx=0.015, rely=0.889, height=44, width=157)
Iterationsbutton.place(relx=0.508, rely=0.889, height=44, width=157)
ResetCustomlangbutton.place(relx=0.262, rely=0.889, height=44, width=157)
MoreOptionsbutton.place(relx=0.755, rely=0.889, height=44, width=157)
Proxybutton.place(relx=0.832, rely=0.8, relheight=0.078, relwidth=0.16)
ResetCustomlangbutton["state"] = "disabled"
if int(config['PROXY']['proxyenabled']) == 1:
    Proxybutton.select()
    
if config['PROXY']['proxyip'] != "":
    proxytext.delete(0, END)
    proxytext.insert(END, config['PROXY']['proxyip'])

mainwindow.mainloop()

