import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402

class Matrix:
    """Represents a 2-dimension array with an equal number of rows and
    columns.
    """

    def __init__(self, rows_num: int) -> 'Matrix':
        """Builds a Matrix object. Should only be called internally; when
        building a Matrix outside of the class, call the class method
        .build_from_stdin().

        Args:
            rows_num (int): The number of rows, which shall also be applied to
            the number of columns.

        Returns:
            Matrix: The matrix object.
        """

        self.rows_num = rows_num

        lists_range = range(rows_num)
        self.representation = list(map(lambda x: list(), lists_range))
    
    def __str__(self) -> str:
        return self.representation.__str__()
    
    def __getitem__(self, index: int | slice) -> list:
        if isinstance(index, slice):
            return self.representation[index]
        
        elif isinstance(index, int):
            if index < 0 or index >= len(self.representation):
                raise IndexError("Index out of range.")
            
            return self.representation[index]
        
        else:
            raise TypeError("Invalid argument type")
    
    def __len__(self) -> int:
        return self.rows_num
    
    @classmethod
    def build_from_stdin(cls) -> 'Matrix':
        """Makes calls to the system stdin, asking for user input, and creates
        a new Matrix instance.

        Returns:
            Matrix: The new Matrix instance.
        """

        rows_num = get_valid_input("Insira o número de linhas e colunas: ", int)
        new_matrix = Matrix(rows_num)
        new_matrix.fill_from_stdin()

        return new_matrix
    
    def fill_from_stdin(self) -> None:
        """Fills all of the matrixes' positions by prompting the user and
        getting inputs from the system's stdin.
        """

        for i in range(self.rows_num):
            for j in range (self.rows_num):
                num = get_valid_input(
                    f"Insira um número para a linha {i+1}, coluna {j+1}: ",
                    int
                )
                self.representation[i].append(num)

    @staticmethod
    def matrix_sum(matrix1: 'Matrix', matrix2: 'Matrix') -> 'Matrix':
        """Returns the matrix that is the result of the sum of two matrixes.
        In case both matrixes have the same dimensions, the return will be the
        exact sum. In case these have different dimensions, the sum shall be
        executed to the bounds of the smallest, and then fill the rest with
        values from the largest.

        Args:
            matrix1 (Matrix): The first matrix.
            matrix2 (Matrix): The second matrix.

        Returns:
            Matrix: The sum result.
        """

        if len(matrix1) > len(matrix2):
            largest = matrix1
            smallest = matrix2
        else:
            largest = matrix2
            smallest = matrix1
        
        sum_matrix = Matrix(len(largest))

        first_range = range(len(smallest))
        for i in first_range:
            for j in first_range:
                sum_matrix[i].append(matrix1[i][j] + matrix2[i][j])

        if (len(matrix1) == len(matrix2)):
            return sum_matrix
        
        second_range = range(len(smallest), len(largest))
        for i in second_range:
            for j in second_range:
                sum_matrix[i].append(largest[i][j])
        
        return sum_matrix

if __name__ == "__main__":
    first_matrix = Matrix.build_from_stdin()
    second_matrix = Matrix.build_from_stdin()

    third_matrix = Matrix.matrix_sum(first_matrix, second_matrix)

    print(third_matrix)