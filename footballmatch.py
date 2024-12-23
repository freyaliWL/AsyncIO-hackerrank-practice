import aiohttp
import asyncio

async def get_drawn_matches(year):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for goal in range(11):  # 循环从0到10
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={goal}&team2goals={goal}"
            task = fetch_data(session, url, goal)  # 创建异步任务
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)  # 并行执行所有任务
        total_drawn_matches = sum(results)  # 计算所有平局比赛的总数
        return total_drawn_matches

async def fetch_data(session, url, goal):
    async with session.get(url) as response:
        data = await response.json()  # 获取响应的JSON数据
        print(f'Total matches drawn with {goal}: {data["total"]}')
        return data['total']

# 使用 asyncio 的事件循环来运行异步函数
if __name__ == "__main__":
    year = 2011
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_drawn_matches(year))
    print(f'Total drawn matches in {year}: {result}')
