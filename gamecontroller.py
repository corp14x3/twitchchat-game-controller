from twitchio.ext import commands
import pyautogui , keyboard

buttons = ["w","s","a","d"]
buttons2 = ["w","s","a","d","j"]

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='urtoken', prefix='.', initial_channels=["urchannel"])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        
        if message.echo:
            return

        if message.content == "g":
           pyautogui.press("g")

        if message.content == "uc":
            pyautogui.press("space")
        
        if message.content == "1":
           pyautogui.press("1")
        
        if message.content == "2":
           pyautogui.press("2")
        
        if message.content == "3":
           pyautogui.press("3")
        
        if message.content == "4":
           pyautogui.press("4")

        if message.content == "ctrl":
            keyboard.press("v")

        if message.content == "shift":
            keyboard.press("shift")

        if message.content == "w":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("w")

        if message.content == "a":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("a")

        if message.content == "s":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("s")

        if message.content == "d":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("d")
        
        if message.content == "e":
            keyboard.release("e")
            keyboard.press("e")

        if message.content == "q":
            keyboard.release("q")
            keyboard.press("q")
        
        if message.content == "x":
            keyboard.release("x")
            keyboard.press("x")
        
        if message.content == "c":
            keyboard.release("c")
            keyboard.press("c")

        if message.content == "spray":
            keyboard.release("j")
            keyboard.press("j")
        
        if message.content == "ot":
            keyboard.press("j")
            keyboard.release("j")

        if message.content == "res":
            for key in buttons2:
                keyboard.release(key)

        if message.content.startswith("chat"):
            text = message.content.replace("chat" , "")
            pyautogui.press("enter")
            pyautogui.typewrite(text)
            pyautogui.press("enter")

        print(message.content)

        
        await self.handle_commands(message)

        


bot = Bot()
bot.run()