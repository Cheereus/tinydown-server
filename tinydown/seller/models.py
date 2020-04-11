from django.db import models

# 卖家
class Seller(models.Model):

    # id
    seller_id = models.IntegerField(default=0)
    # 余额
    balance = models.FloatField(default=1.0)  
    # 用户名
    seller_name = models.CharField(max_length=200, default='NULL')
    # 密码
    seller_password = models.CharField(max_length=200, default='NULL')


    def __str__(self):
        return self.seller_name

# 账号
class Account(models.Model):

    # id
    account_id = models.IntegerField(default=0)
    # 关联号主
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    # 用户名
    account_name = models.CharField(max_length=200, default='NULL')
    # 密码
    account_password = models.CharField(max_length=200, default='NULL')
    # 状态
    state = models.IntegerField(default=0)
    # 创建时间
    create_date = models.DateTimeField('date created')
    # 账户类型
    account_type = models.IntegerField(default=1)
    # 账户价格
    account_price = models.FloatField(default=1.0)
    # 当前使用人数
    current_users = models.IntegerField(default=0)
    # 总计使用人数
    his_users = models.IntegerField(default=0)

    def __str__(self):
        return self.account_name

# 订单
class Order(models.Model):

    # id
    order_id = models.IntegerField(default=0)
    # 关联账户
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # 创建时间
    create_date = models.DateTimeField('date created')
    # 结束时间
    end_date = models.DateTimeField('date end')
    # 类型
    order_type = models.IntegerField(default=0)
    # 状态
    state = models.IntegerField(default=0)
    # 价格
    price = models.FloatField(default=1.0)
    # 历史
    history = models.CharField(max_length=200, default='NULL')

    def __str__(self):
        return self.history