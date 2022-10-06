
def non_recursive_levenshtein(source: str, target: str) -> int:
    source_len = len(source)
    target_len = len(target)

    matrix_dist = [[0 for i in range(target_len + 1)] for j in range(source_len + 1)]

    for i in range(source_len + 1):
        for j in range(target_len + 1):
            if i == 0 and j == 0:
                matrix_dist[i][j] = 0
            elif i == 0 and j > 0:
                matrix_dist[i][j] = j
            elif i > 0 and j == 0:
                matrix_dist[i][j] = i
            else:
                matrix_dist[i][j] = min(matrix_dist[i][j - 1] + 1,
                                        matrix_dist[i - 1][j] + 1,
                                        matrix_dist[i - 1][j - 1] + (source[i - 1] != target[j - 1]))
    return matrix_dist[source_len][target_len]


def non_recursive_damerau_levenshtein(source: str, target: str) -> int:
    source_len = len(source)
    target_len = len(target)

    matrix_dist = [[0 for i in range(target_len + 1)] for j in range(source_len + 1)]

    for i in range(source_len + 1):
        for j in range(target_len + 1):
            if i == 0 and j == 0:
                matrix_dist[i][j] = 0
            elif i == 0 and j > 0:
                matrix_dist[i][j] = j
            elif i > 0 and j == 0:
                matrix_dist[i][j] = i
            else:
                matrix_dist[i][j] = min(matrix_dist[i][j - 1] + 1,
                                        matrix_dist[i - 1][j] + 1,
                                        matrix_dist[i - 1][j - 1] + (source[i - 1] != target[j - 1]))

                if i > 1 and j > 1 and source[i - 1] == target[j - 2] and source[i - 2] == target[j - 1]:
                    exchange_dist = matrix_dist[i - 2][j - 2] + 1
                    matrix_dist[i][j] = min(matrix_dist[i][j], exchange_dist)

    return matrix_dist[source_len][target_len]


def _rdl_wrap(source: str, target: str, i: int, j: int) -> int:
    answer = -1

    if i == 0 and j == 0:
        answer = 0
    elif i == 0:
        answer = j
    elif j == 0:
        answer = i
    else:

        left = _rdl_wrap(source, target, i - 1, j) + 1
        up = _rdl_wrap(source, target, i, j - 1) + 1
        left_up = _rdl_wrap(source, target, i - 1, j - 1) + (source[i - 1] != target[j - 1])

        answer = min(left, up, left_up)

        if i > 1 and j > 1 and source[i - 1] == target[j - 2] and source[i - 2] == target[j - 1]:
            exchange_dist = _rdl_wrap(source, target, i - 2, j - 2) + 1
            answer = min(answer, exchange_dist)

    return answer


def recursive_damerau_levenshtein(source: str, target: str) -> int:
    source_len = len(source)
    target_len = len(target)

    return _rdl_wrap(source, target, source_len, target_len)


def _rdl_cache_wrap(source: str, target: str, i: int, j: int, cache: list[list[int]]) -> int:
    if cache[j][i] != -1:
        return cache[j][i]

    if i == 0 and j == 0:
        cache[j][i] = 0
        return cache[j][i]
    elif i == 0 and j > 0:
        cache[j][i] = j
        return cache[j][i]
    elif j == 0 and i > 0:
        cache[j][i] = i
        return cache[j][i]
    else:
        left = _rdl_cache_wrap(source, target, i - 1, j, cache) + 1
        up = _rdl_cache_wrap(source, target, i, j - 1, cache) + 1
        left_up = _rdl_cache_wrap(source, target, i - 1, j - 1, cache) + (source[i - 1] != target[j - 1])

        cache[j][i] = min(left, up, left_up)

        if i > 1 and j > 1 and source[i - 1] == target[j - 2] and source[i - 2] == target[j - 1]:
            exchange = _rdl_cache_wrap(source, target, i - 2, j - 2, cache) + 1
            cache[j][i] = min(cache[j][i], exchange)

    return cache[j][i]


def recursive_damerau_levenshtein_with_cache(source: str, target: str) -> int:
    source_len = len(source)
    target_len = len(target)

    cache = [[-1 for i in range(source_len + 1)] for j in range(target_len + 1)]
    return _rdl_cache_wrap(source, target, source_len, target_len, cache)



