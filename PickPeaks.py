def pick_peaks(arr):
    peaks = []
    positions = []
    result = {}
    plateu = False

    if not arr:
        return {'pos': [], 'peaks': []}
    print(len(arr)-1)
    print(arr)
    for i in range(1, len(arr)-1):
        if i == len(arr)-1:
            continue
        if arr[(i+1)] < arr[i] > arr[(i-1)]:
            peaks.append(arr[i])
            positions.append(i)

        elif arr[i] == arr[i+1] and not plateu:
            plateu = True
            peaks.append(arr[i])
            positions.append(i)

        elif plateu and arr[i] > arr[i+1] and i != (len(arr)-2):
            plateu = False

        elif plateu and arr[i] < arr[i+1] and i != (len(arr)-2):
            peaks.pop()
            positions.pop()
            plateu = False

        elif plateu and i == (len(arr)-2):
            plateu = False
            peaks.pop()
            positions.pop()

    result["pos"] = positions
    result["peaks"] = peaks
    return result


print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))
