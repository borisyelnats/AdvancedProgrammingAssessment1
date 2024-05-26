def scoresort(array, AscendingOrder=True):
    '''
    scoresort will sort an array of objects that have an object.score attribute
    array: the array to be sorted
    AscendingOrder: by default, will sort in ascending AscendingOrder, if AscendingOrder set to 0, in descending AscendingOrder
    '''


    if len(array) <=1:
        return array
        
    else:
        #split into sub arrays of values larger and smaller than pivot respectively, then recursively break down to array of length 1
        #then reassamble array with sub arrays that are ordered
        pivot_index = (len(array)//2)
        pivot = array[pivot_index]
        left = []
        right = []
        
        for index, player in enumerate(array):
            if index == pivot_index:
                continue
            if (player.score <=pivot.score) == AscendingOrder:
                left.append(player)
            
            else:
                right.append(player)

        left = scoresort(left, AscendingOrder)
        right = scoresort(right, AscendingOrder)
        return (left + [pivot] + right)

    

