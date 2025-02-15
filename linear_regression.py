# Dustin Le
# 1001130689

from sys import argv
import numpy as np

def linear_regression(training_file, degree, lamb, test_file):
    train = []
    test = []
    phi = []

    with open(training_file, 'r') as training:
        for line in training:
            train.append(line.split())
    
    with open(test_file, 'r') as testing:
        for line in testing:
            test.append(line.split())
    
    train = np.array(train).astype(np.float)
    test = np.array(test).astype(np.float)

    rows = train.shape[0]
    columns = train.shape[1]

    for i in range(rows):
        temp = [1]
        for j in range(columns-1):
            for k in range(int(degree)):
                temp.append(train[i][j]**(k+1))
        phi.append(temp)
       
    phi = np.array(phi).astype(np.float)
    identity = np.identity(phi.shape[1])
    t = train.T[columns-1]
    w = (np.linalg.inv(int(lamb) * identity + phi.T @ phi)) @ phi.T @ t
    

    for i in range(w.size):
        print('w%d=%.4f' % (i, w[i]))

    # ╭─━━━━━━━━━━━━━─╮
    #   Testing Phase
    # ╰─━━━━━━━━━━━━━─╯

    rows = test.shape[0]
    columns = test.shape[1]
    t = test.T[columns-1]
    phi = []

    for i in range(rows):
        temp = [1]
        for j in range(columns-1):
            for k in range(int(degree)):
                temp.append(test[i][j]**(k+1))
        phi.append(temp)
    
    phi = np.array(phi).astype(np.float)
    e = []
    
    for i in range(rows):
        e.append ( w.T @ phi[i] )
    
    e = np.array(e).astype(np.float)
    
    for i in range(rows):
        print('ID=%5d, output=%14.4f, target value = %10.4f, squared error = %.4f' % (i+1, e[i], t[i], (e[i] - t[i])**2))

linear_regression(argv[1], argv[2], argv[3], argv[4])