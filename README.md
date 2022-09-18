# Automate Cookie Clicker with Playwright

---
## Welcome
Selenium is my favorite when I want to play around with web automation. This 
time, the framework I use for this kind of task is [Playwright](https://playwright.dev/python/). Playwright is 
pretty new in the browser automation playground and is developed by 
Microsoft developers. I've been introduced to Playwright a couple of days ago 
and decided to test it by creating this small project.

[Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) is the chosen 
website for this project. I use Playwright to create a bot that navigates to 
this website, clicks on the cookie and buys any available upgrades.

## Installation
Clone this project to your computer and install necessary dependencies. 
There are two ways you can install the dependencies.

* First way: If you have `pipenv` already installed globally on your computer, 
  you can type the following command in your terminal.

```commandline
pipenv sync
```

* Second way: If you prefer using `pip`, I also provide a `requirements.txt` 
  file for you to install.

```commandline
pip install -r requirements.txt
```

## How to run
Before you can do anything, you have to run this command: 
```commandline
playwright install msedge
```
This will install Microsoft Edge on your computer since this project uses 
Edge to run automation. More details on [how to install Playwright browsers](https://playwright.dev/python/docs/browsers).

Next, to the main thing, make sure you `cd` into the same directory level as 
`main.py` and type:
```commandline
python main.py
```
This will spin up a new Microsoft Edge InPrivate window and automate all the 
game-playing tasks.

To run tests, simply type:
```commandline
pytest
```

## Change game-play settings
There is only one setting to change, it's `GAMEPLAY_SESSION_MINUTES`. It 
determines how long the automation runs before it ends in minutes. Currently, 
it is set to 5 minutes, you can change it to however you like. You can find 
this setting in the `main.py` file.

## Enjoy! 💻
