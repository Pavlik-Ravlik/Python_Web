import asyncio
import aiohttp
import datetime
import sys
import json

async def get_exchange_rates(session, date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    
    async with session.get(url) as response:
        try:
            if response.status == 200:

                data = await response.json()
                exchange_rates = data.get('exchangeRate', [])
                rates = {}
            
                for rate in exchange_rates:
                    currency = rate.get('currency')
                
                    if currency in ['EUR', 'USD']:
                        rates[currency] = {
                            'sale': rate.get('saleRateNB'),
                            'purchase': rate.get('purchaseRateNB')
                        }
        except aiohttp.ClientConnectorError as err:
            print(f'Connection error: {url}', str(err))
            
        return {date: rates}


async def get_currency_rates(num_days):
    rates = []
    today = datetime.date.today()
    dates = [(today - datetime.timedelta(days=i)).strftime('%d.%m.%Y') for i in range(num_days)]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for date in dates:
            task = asyncio.ensure_future(get_exchange_rates(session, date))
            tasks.append(task)
        
        rates = await asyncio.gather(*tasks)
    return rates


async def main():
    num = int(sys.argv[1])
    
    if num >= 11:
        raise TypeError("The number of days should be less than 11.")
    
    else:
        rates = await get_currency_rates(num)
        formatted_rates = json.dumps(rates, indent=2, ensure_ascii=False)
        print(formatted_rates)

      
if __name__ == '__main__':
    asyncio.run(main())

  