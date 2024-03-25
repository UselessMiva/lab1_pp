from check import check_results, read_json, read_matrix, write_to_file, draw_graph


if __name__ == "__main__":
    arr = [100, 200, 300, 400, 500,600,700,800,900,1000]
    times = []
    for i in arr:
        i, time = read_json(f'matrix_{i}.json')
        times.append(time)
        m1 = read_matrix('data', f'matrix_1_{i}.txt')
        m2 = read_matrix('data', f'matrix_2_{i}.txt')
        res = read_matrix(f'results/result_matrix', f'result_matrix_{i}.txt')
        write_to_file(i, check_results(m1, m2, res))
    draw_graph(arr, times)