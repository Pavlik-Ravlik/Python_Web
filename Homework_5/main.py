import asyncio
import aiohttp
import datetime
import sys
import json

async def get_exchange_rates(session, date, currency_exchange):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    
    async with session.get(url) as response:
        try:
            if response.status == 200:

                data = await response.json()
                exchange_rates = data.get('exchangeRate', [])
                rates = {}
            
                for rate in exchange_rates:
                    currency = rate.get('currency')
                    
                    for i in currency_exchange:
                        
                        if currency in ['EUR', 'USD', i]:
                        
                                rates[currency] = {
                                    'sale': rate.get('saleRateNB'),
                                    'purchase': rate.get('purchaseRateNB')
                                }
        except aiohttp.ClientConnectorError as err:
            print(f'Connection error: {url}', str(err))
            
        return {date: rates}
    

async def get_currency_rates(num_days, currency_exchange):
    rates = []
    today = datetime.date.today()
    dates = [(today - datetime.timedelta(days=i)).strftime('%d.%m.%Y') for i in range(num_days)]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for date in dates:
            task = asyncio.ensure_future(get_exchange_rates(session, date, currency_exchange))
            tasks.append(task)
        
        rates = await asyncio.gather(*tasks)   
    return rates


async def run_main():
    num_days = int(sys.argv[1])
    currency_exchange = (sys.argv[2:])
    
    if num_days >= 11 or num_days < 1:
        raise TypeError("The number of days should be less than 11.")
    
    else:
        rates = await get_currency_rates(num_days, currency_exchange)
        formatted_rates = json.dumps(rates, indent=2, ensure_ascii=False)
        print(formatted_rates)

      
if __name__ == '__main__':
    asyncio.run(run_main())
 