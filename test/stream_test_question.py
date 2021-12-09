def parentStream(streamAtLeaves,type):
    res = []
    tmp = []
    i = 0

    for ele in type:
        tmp = []
        if ele == 0:
            tmp = (streamAtLeaves[i][:])
            tmp.extend(streamAtLeaves[i+1])
            res.append(tmp)
        else:
            l = 0
            arr1 = streamAtLeaves[i]
            arr2 = streamAtLeaves[i+1]
            j = 0
            k = 0

            while j<len(arr1) and k<len(arr2):
                tmp.append(arr1[j])
                tmp.append(arr2[k])
                j+=1
                k+=1
            tmp.extend(arr1[j:])
            res.append(tmp)
        i += 2
    return res



if __name__ == '__main__':
    stream = [[1,3,7],[2,4],[3,4],[9,5],[21,36],[90,81],[7,8],[6,45]]
    type = [0,0,1,0,0,1,1]
    
    while len(stream)>1:
        p_count = len(stream)//2
        type_level = type[p_count-1:2*(p_count-1)+1]
        stream = (parentStream(stream,type_level))
    print(stream[0])
