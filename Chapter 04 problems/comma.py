def comma(sampleList):
    
    for i in range(len(sampleList)):
         if (i != (len(sampleList)-1)):
            print(sampleList[i]+ ", " , end='' )
         else:
            print('and ' + sampleList[-1])

x = ['apple','banana','grapes']
comma(x)