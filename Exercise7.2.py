def eval_loop():
    a = raw_input('Please enter a string or enter done.')
    while a != 'done':
        
        result = eval(a)

        print result
        eval_loop()
        return result

eval_loop()
    
