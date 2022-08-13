from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        
        contador = 1
        qntd_vzs = int(input("Quantas vezes deseja repetir? "))

        # Opens the BotCity website.
        while qntd_vzs >= contador:
            self.execute(r'C:\Users\Public\Desktop\Google Chrome.lnk')
            self.wait(8000)
            self.click_at(244, 63)
            self.paste("freebitco.in")
            self.enter()
            if not self.find( "nothanks", matching=0.97, waiting_time=1000000):
                self.not_found("nothanks")
            self.wait(2000)
            self.click_at(796, 710)
            if not self.find( "ponteiro", matching=0.97, waiting_time=1000000):
                self.not_found("ponteiro")
            self.wait(2000)
            self.click_at(1907, 996)
            self.wait(2000)
            self.click_at(1907, 996)
            self.wait(2000)
            self.click_at(796, 710) # clicar na caixa de confirmação
            self.wait(2000)
            self.click_at(941, 830)
            self.wait(6000)
            self.click_at(1889, 11)
            self.wait(3600000)
            contador += 1


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()




























































