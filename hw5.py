def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
      >>> w = make_withdraw(100, 'hax0r')
      >>> w(25, 'hax0r')
      75
      >>> w(90, 'hax0r')
      'Insufficient funds'
      >>> w(25, 'hwat')
      'Incorrect password'
      >>> w(25, 'hax0r')
      50
      >>> w(75, 'a')
      'Incorrect password'
      >>> w(10, 'hax0r')
      40
      >>> w(20, 'n00b')
      'Incorrect password'
      >>> w(10, 'hax0r')
      "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
      >>> w(10, 'l33t')
      "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
     """
     attempts = []  # 学习这里存储尝试密码的用法
     def withdraw(amount, password_attempt):
         nonlocal balance  # 学习这里nonlocal的用法
         if len(attempts) == 3:
             return 'Your account is locked! Attempts: ' + str(attempts)
         if password_attempt != password:
             attempts.append(password_attempt)
             return 'Incorrect password!'
         if amount > balance:
             return 'Insufficient funds'
         balance = balance - amount
         return balance
     return withdraw
# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量,是python 3.0中新加的关键字
