def test():
    print("generator start")
    n = 1
    while True:
        print(n)
        yield_expression_value = yield n
        print("yield_expression_value = %d" % yield_expression_value)
        n += 1


# ①创建generator对象
generator = test()
print(type(generator))

print("\n---------------\n")

# ②启动generator
next_result = generator.__next__()
print("next_result = %d" % next_result)


#print("\n---------------\n")

# ②启动generator
#next_result = generator.__next__()
#print("next_result = %d" % next_result)


print("\n---------------\n")

# ③发送值给yield表达式
send_result = generator.send(666)
print("send_result = %d" % send_result)


print("\n---------------\n")

# ③发送值给yield表达式
send_result = generator.send(999)
print("send_result = %d" % send_result)