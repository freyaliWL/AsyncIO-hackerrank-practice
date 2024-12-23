import aiohttp
import asyncio

async def get_goals_scored(competition, year):
    ans = 0
    goals = list(range(11))  # 创建一个包含0到10的列表

    async with aiohttp.ClientSession() as session:
        # 获取赛事的胜者
        url = f"https://jsonmock.hackerrank.com/api/football_competitions?year={year}&name={competition}"
        async with session.get(url) as response:
            data = await response.json()
            winner = data['data'][0]['winner']
            print(winner)

        # 为team1请求每个目标得分的数据
        tasks = []
        for goal in goals:
            task = fetch_goals(session, f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={winner}&team1goals={goal}", goal)
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        ans += sum(results)

        # 为team2请求每个目标得分的数据
        tasks = []
        for goal in goals:
            task = fetch_goals(session, f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team2={winner}&team2goals={goal}", goal)
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        ans += sum(results)

    return ans

async def fetch_goals(session, url, goal):
    async with session.get(url) as response:
        data = await response.json()
        return data['total'] * goal

# 使用 asyncio 的事件循环来运行异步函数
async def main():
    total_score = await get_goals_scored("UEFA Champions League", 2011)
    print(f"Total goals scored by the winner in 2011: {total_score}")

if __name__ == "__main__":
    asyncio.run(main())
