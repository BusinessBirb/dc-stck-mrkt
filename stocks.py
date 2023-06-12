import discord
import random
from discord.ext import commands, tasks
import matplotlib.pyplot as plt
import json

class stocks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reminder.start()
    
    @tasks.loop(hours = 3)
    async def reminder(self):
        with open('users.json', 'r') as f:
            users = json.load(f)

        timegraph = [90, 87, 84, 81, 78, 75, 72, 69, 66, 63, 60, 57, 54, 51, 48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
        pricegraph1 = users['Stocks'][f'StocksHistory1']
        pricegraph2 = users['Stocks'][f'StocksHistory2']
        pricegraph3 = users['Stocks'][f'StocksHistory3']
        pricegraph4 = users['Stocks'][f'StocksHistory4']
        pricegraph5 = users['Stocks'][f'StocksHistory5']
        pricegraph6 = users['Stocks'][f'StocksHistory6']
        pricegraph7 = users['Stocks'][f'StocksHistory7']
        pricegraph8 = users['Stocks'][f'StocksHistory8']
        pricegraph9 = users['Stocks'][f'StocksHistory9']
        # 

        plt.clf()
        plt.figure(figsize = (16,8))
        plt.subplot(3, 3, 1)
        plt.plot(timegraph, pricegraph1, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock1')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')
        
        plt.subplot(3, 3, 2)
        plt.plot(timegraph, pricegraph2, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock2')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')
        
        plt.subplot(3, 3, 3)
        plt.plot(timegraph, pricegraph3, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock3')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')

        plt.subplot(3, 3, 4)
        plt.plot(timegraph, pricegraph4, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock4')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')

        plt.subplot(3, 3, 5)
        plt.plot(timegraph, pricegraph5, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock5')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')
        plt.tight_layout()

        plt.subplot(3, 3, 6)
        plt.plot(timegraph, pricegraph6, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock6')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')
        
        plt.subplot(3, 3, 7)
        plt.plot(timegraph, pricegraph7, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock7')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')

        plt.subplot(3, 3, 8)
        plt.plot(timegraph, pricegraph8, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock8')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')

        plt.subplot(3, 3, 9)
        plt.plot(timegraph, pricegraph9, 'r')
        plt.gca().invert_xaxis()
        plt.ticklabel_format(style='plain')
        plt.title('stock9')
        plt.xlabel('time (h)')
        plt.ylabel('price ($$$)')
        plt.tight_layout()

        plt.savefig('stocks.png', bbox_inches = "tight")

        for x in range(1, 10):
            stockincrease = ['1', '2']
            rate1 = random.choices(stockincrease, weights=(99.9, 0.1), k=1)
            rate1 = '{}'.format(rate1)
            if rate1 == "['1']":
                amount = random.randint(1, 50000)
                addminus = random.randint(1, 2) 

                if addminus == 1:
                    amount1 = 1 - (amount/1000000)
                
                if addminus == 2:
                    amount1 = 1 + (amount/1000000)

                users['Stocks'][f'Stocks{x}'] = round(users['Stocks'][f'Stocks{x}']*amount1)
                
            
            if rate1 == "['2']":
                amount = random.randint(1, 15000)
                addminus = random.randint(1, 2)

                if addminus == 1:
                    amount1 = 1 - (amount/10000)
                else:
                    amount1 = 1 + (amount/10000)

                if amount1 <= 0.6:
                    amount1 = 1
                    
                users['Stocks'][f'Stocks{x}'] = round(users['Stocks'][f'Stocks{x}']*amount1)

            if users['Stocks'][f'Stocks{x}'] <= 0: 
                users['Stocks'][f'Stocks{x}'] = 69
            
            mylist = users['Stocks'][f'StocksHistory{x}']

            del mylist[0]

            mylist.append(users['Stocks'][f'Stocks{x}'])

            users['Stocks'][f'StocksHistory{x}'] = mylist

            with open('users.json', 'w') as f:
                json.dump(users, f, indent = 2)

        for user in users:
            try:
                if users[str(user)]['Stocks']['TotalStocks'] > 0:
                    users[str(user)]['Networth'] = users[str(user)]['Bank'] + users[str(user)]['Wallet'] + (users[str(user)]['Stocks']['Stocks1']*users['Stocks']['Stocks1']) + (users[str(user)]['Stocks']['Stocks2']*users['Stocks']['Stocks2']) + (users[str(user)]['Stocks']['Stocks3']*users['Stocks']['Stocks3']) + (users[str(user)]['Stocks']['Stocks4']*users['Stocks']['Stocks4']) + (users[str(user)]['Stocks']['Stocks5']*users['Stocks']['Stocks5']) + (users[str(user)]['Stocks']['Stocks6']*users['Stocks']['Stocks6']) + (users[str(user)]['Stocks']['Stocks7']*users['Stocks']['Stocks7']) + (users[str(user)]['Stocks']['Stocks8']*users['Stocks']['Stocks8']) + (users[str(user)]['Stocks']['Stocks9']*users['Stocks']['Stocks9'])  
            except:
                pass

        with open('users.json', 'w') as f:
            json.dump(users, f, indent = 2)



        global embedVarj23kj45nk23n4
        Capitalization = users['Stocks'][f'Stocks1'] * users['Stocks'][f'TotalStocks1'] + users['Stocks'][f'Stocks2'] * users['Stocks'][f'TotalStocks2'] + users['Stocks'][f'Stocks3'] * users['Stocks'][f'TotalStocks3'] + users['Stocks'][f'Stocks4'] * users['Stocks'][f'TotalStocks4'] + users['Stocks'][f'Stocks5'] * users['Stocks'][f'TotalStocks5'] + users['Stocks'][f'Stocks6'] * users['Stocks'][f'TotalStocks6'] + users['Stocks'][f'Stocks7'] * users['Stocks'][f'TotalStocks7'] + users['Stocks'][f'Stocks8'] * users['Stocks'][f'TotalStocks8'] + users['Stocks'][f'Stocks9'] * users['Stocks'][f'TotalStocks9']
        colours = [0, 0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5]
        embedVarj23kj45nk23n4 = discord.Embed(title="Stock Market:", description="Here's the stock list...", color = random.choice(colours))
        embedVarj23kj45nk23n4.add_field(name="stock1 stocks", value= f"Current Price: {users['Stocks'][f'Stocks1']} per stock \n Available: {users['Stocks'][f'TotalStocks1']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock2 stocks", value= f"Current Price: {users['Stocks'][f'Stocks2']} per stock \n Available: {users['Stocks'][f'TotalStocks2']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock3 stocks", value= f"Current Price: {users['Stocks'][f'Stocks3']} per stock \n Available: {users['Stocks'][f'TotalStocks3']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock4 stocks", value= f"Current Price: {users['Stocks'][f'Stocks4']} per stock \n Available: {users['Stocks'][f'TotalStocks4']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock5 stocks", value= f"Current Price: {users['Stocks'][f'Stocks5']} per stock \n Available: {users['Stocks'][f'TotalStocks5']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock6 stocks", value= f"Current Price: {users['Stocks'][f'Stocks6']} per stock \n Available: {users['Stocks'][f'TotalStocks6']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock7 stocks", value= f"Current Price: {users['Stocks'][f'Stocks7']} per stock \n Available: {users['Stocks'][f'TotalStocks7']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock8 stocks", value= f"Current Price: {users['Stocks'][f'Stocks8']} per stock \n Available: {users['Stocks'][f'TotalStocks8']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="stock9 stocks", value= f"Current Price: {users['Stocks'][f'Stocks9']} per stock \n Available: {users['Stocks'][f'TotalStocks9']} stocks", inline=True)
        embedVarj23kj45nk23n4.add_field(name="Stock Market Capitalization (available)", value= f"{Capitalization} $$$", inline=False)
        embedVarj23kj45nk23n4.set_image(
        url="attachment://stocks.png"
        )


    @reminder.before_loop
    async def reminder_before(self):
        await self.bot.wait_until_ready()

    global stockshow
    stockshow = False
    @commands.command(aliases=['Stocks', 'stocks', 'Stonks', 'stonks'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def _Stocks(self, ctx):
        with open('users.json', 'r') as f:
            users = json.load(f) 
    
        chart = discord.File("stocks.png")
        await ctx.reply(embed=embedVarj23kj45nk23n4, file = chart)

    @_Stocks.error
    async def command_name_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("come back in {} seconds.".format(round(error.retry_after)))

        

async def setup(bot):
    await bot.add_cog(stocks(bot))
