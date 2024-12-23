import requests

def getNumDraws(year):
    """
    Get the number of drawn matches for a given year using the football matches API.
    A match is considered drawn when both teams score the same number of goals.
    
    Args:
        year (int): The year to get matches for
        
    Returns:
        int: The total number of drawn matches in that year
    """
    base_url = "https://jsonmock.hackerrank.com/api/football_matches"
    total_draws = 0
    
    # Since we know no team scores more than 10 goals (from constraints)
    for goals in range(11):  # 0 to 10 goals
        url = f"{base_url}?year={year}&team1goals={goals}&team2goals={goals}"
        
        try:
            response = requests.get(url)
            data = response.json()
            # Add the total number of matches for this score combination
            total_draws += data['total']
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return 0

    return total_draws

if __name__ == '__main__':
    # 从标准输入读取年份
    # year = int(input().strip())
    year = 2011    
    # 获取并打印结果
    result = getNumDraws(year)
    print(result)
