# About this project

On July 2021, I was taking a Python specialization to work on deepening my knowledge of the standard library and its built-in capabilities. As a final project for the course, we were given the task of building a hangman game from scratch, leveraging whatever language resources we wanted. The objective of a project like this is to have a fun pretext to explore and play around with the standard library and its built-in data structures and functions to see how much you can achieve with it. Not only is it useful to deepen your knowledge about a programming language in particular but also to practice thinking with the object oriented programming (OOP) design paradigm. 

Working in this project has been very educational for me, I hope it can be educational for you too. You can fork this repository and try to make it into your own version, try to parse its functionalities into your preferred language or you can try to break it in as many ways as you can imagine (test it) and raise some issues or suggest to contribute, that would be nice too.

I will be updating this repository with more features I have been ideating. This project is still at a very early stage of development.

### Installation

1. Clone this repository

```
$ git clone https://github.com/cemar-ortiz/hangman_cli.git
```

2. On the cloned directory, setup a virtual environment and activate it:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install the requirements:

```
$ pip install -r requirements.xt
```

4. Run the source file using the python interpreter:

```
$ python3 main.py
```

### Usage

A list of 'blank' spaces will be displayed to you and the program will be on stand by for your input. Only 1 character at a time may be accepted. 

### On this version

This Hangman game runs on the command line interface (CLI). As of this moment, the only way to change the word to be guessed is directly on the source file. It is the self._word variable. You get as many attempts as letters the word has, you can only input 1 character at a time, full words won't work, even if they are the right answer. If you guess the word before your number of attempts run out or if they do, the game ends its execution.


### Coming up features

These are some of the features I'll be working in in the near future:

- Input type error exception catching
- Incremental difficulty mode
- No-vowels-alone mode (Vowels can't be accepted as player input unless the full word is spelled)
- Scoreboard
- Mode against the clock
- Loading custom source file to source words
- Load an HTML source from a given URL to source words
- Change language settings (menus and gameplay)
- Multiplayer mode
- ASCII art for decoration

If you want to suggest some features, you can raise an issue with the corresponding flag (feature).

  
