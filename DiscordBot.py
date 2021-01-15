from selenium import webdriver
import discord
import os


def webScrapper():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument('window-size=1920x1480')
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    driver.get('https://nhentai.net')
    random = driver.find_element_by_xpath('/html/body/nav/div/ul[1]/li[1]/a')
    random.click()
    sauce = driver.find_element_by_xpath('//*[@id="gallery_id"]').text[1:]
    driver.close()
    return sauce

TOKEN = os.environ['DISCORD_TOKEN']
client = discord.Client()

@client.event
async  def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if 'sauce please' in message.content.lower():
        if message.channel.id == 763237720247631913:
            if message.author.id == 294235145802874883:
                await message.channel.send("Sauce 4 Day " + webScrapper())
            else:
                await message.channel.send('CulturedWeebBot ignored orders!')

client.run(TOKEN)