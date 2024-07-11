import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402

class RealState:
    """Representes a real state property.
    """

    highest_id = 0
    fine_value_per_month = 50.0

    def __init__(
            self,
            id: int,
            IPTU_value: float,
            months_delayed: int
    ):
        """Builds a RealState instance. Should only be called internally;
        use the .build_from_stdin() class method to create an instance
        outside this class.

        Args:
            id (int): The highest_id class attribute should be used here, and
            must always be increased by one before calling the constructor.
            IPTU_value (float): The IPTU value for this property.
            months_delayed (int): How many months payment has been delayed
            for.
        """

        self._id = id
        self._IPTU_value = IPTU_value
        self._months_delayed = months_delayed
        self._fine_value = months_delayed * self.fine_value_per_month
    
    def __str__(self) -> str:
        """Returns a string representation of the object's state for debugging
        purposes.

        Returns:
            str: A string representing the internal state of the object.
        """

        return f"id: {self._id}; IPTU: {self._IPTU_value}; Fine: {self._fine_value}"
    
    @classmethod
    def build_from_stdin(cls) -> 'RealState':
        """Uses the default system input stream to ask user for information
        and builds a new RealState.

        Returns:
            RealState: The instance built from the data gathered.
        """

        IPTU_value = get_valid_input("Insira o valor do IPTU: ", float)
        months_delayed = get_valid_input("Quantos meses está atrasado? ", int)

        cls.highest_id += 1
        
        new_real_state = cls(
            cls.highest_id,
            IPTU_value,
            months_delayed
        )

        return new_real_state

if __name__ == "__main__":
    arr_length = get_valid_input("Quantos imóveis pretende cadastrar? ", int)
    real_state_arr = list()

    for i in range(arr_length):
        print(f"\nImóvel {i+1}:\n")

        new_real_state = RealState.build_from_stdin()
        real_state_arr.append(new_real_state)

    for real_state in real_state_arr:
        print(real_state)