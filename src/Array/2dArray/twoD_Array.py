# challenge Link : https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D
# =interview-preparation-kit&playlist_slugs%5B%5D=arrays
if __name__ == '__main__':
    print('Started 2D array python Program')


def hourglass_sum(arr):
    current_hourglass = 0
    highest_hourglass = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i + 2 < len(arr) and j + 2 < len(arr[i]):
                current_hourglass = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + \
                                    arr[i + 2][j + 1] + arr[i + 2][j + 2]
                highest_hourglass = max(current_hourglass, highest_hourglass)
    #print(highest_hourglass)
    return highest_hourglass
