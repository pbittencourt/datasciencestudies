import numpy as np

def calculate(numbers: list):
    """
    Receives a list of numbers and convert the list
    into a 3 x 3 Numpy array. Then, return a dictionary
    containing the mean, variance, standard deviation,
    max, min, and sum along both axes and for the
    flattened matrix.
    """

    if len(numbers) == 9:
        # convert list into numpy array
        matrix = np.array([
            numbers[:3],
            numbers[3:6],
            numbers[6:]
        ])

        # initialize dictionary
        calculations = dict()

        calculations['mean'] = [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix)
        ]

        calculations['variance'] = [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix)
        ]

        calculations['standard deviation'] = [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix)
        ]

        calculations['max'] = [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix)
        ]

        calculations['min'] = [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix)
        ]

        calculations['sum'] = [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix)
        ]

        return calculations
    else:
        raise ValueError('List must contain nine numbers.')

if __name__ == '__main__':
    listinha = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(calculate(listinha))
