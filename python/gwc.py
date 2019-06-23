shopping_menu = []
goods = [['电脑', 1999], ['鼠标', 20], ['游艇', 20],  ['美女', 998]]
pay = int(input("你的工资是："))
while True :
        YN = 1
        print("商品列表如下")
        for index, p in enumerate(goods):
            print("%s. %s    %s" % (index, p[0], p[1]))
        choice = input("输入你想买的商品编号:")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(goods):
                if pay <goods[choice][1] :
                    print("对不起你的余额不足以买下此商品，请充值")
                    pay = pay + (int(input('请输入需要充值的金额')))
                    print('您的余额为：', pay)
                    YN = 0
                if YN ==1 :
                    shopping_menu.append(goods[choice])
                    pay = pay - goods[choice][1]
                    print("您已成功选择购买", (goods[choice]), "剩余余额:",pay)
            else:
                print("商品不存在，请重新选择")
        elif choice == 'q':
            if len(shopping_menu) > 0:
                print("您已将以下商品加入购物车")
                for index, p in enumerate(shopping_menu):
                    print("%s.  %s    %s" % (index, p[0], p[1]))
                print("您的余额为:", pay)
        elif choice == 'w':
            if len(shopping_menu) > 0:
             print("您已将以下商品加入购物车")
            for index, p in enumerate(shopping_menu):
                print("%s.  %s    %s" % (index, p[0], p[1]))
                scsp=int(input('请输入你要删除的商品'))
                shopping_menu.pop(scsp)

        elif choice == 'exit':
            exit()


