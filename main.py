from FirstDatas import FirstDatas
from Options import Options

x = FirstDatas('https://www.youtube.com/watch?v=7EmboKQH8lM&ab_channel=UnityCoin')
x = Options()

x.get_data()
x.draw()

print('\n')
x.get_data()
