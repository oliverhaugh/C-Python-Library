# Made by OliverH
# date started 4/19/2023
import sys

print("for printf, for the last parameter, specify if the value is a variable, if it is, specify true, if not, specify false")
print("for scanf do the same thing with the var type but in the first parameter")


class c_input_and_output:
    # printf (print())
    def printf(var_type, value, if_variable):
        if if_variable == True:
            if var_type == "%d":
                int_value = int(value)
                print(int_value)
            if var_type == "%c":
                char_value = chr(value)
                print(char_value)
            if var_type == "%f":
                float_value = float(value)
                print(float_value)
            if var_type == "%lf":
                double_value = float(value)
                print(double_value)
            if var_type == "%s":
                string_value = str(value)
                print(string_value)
        else:
            print(value)


    # scanf (input())
    def scanf(var_type, input_value, variable_to_store_information):
        value_inputted = input(input_value)
        if var_type == "%d":
            int_value = int(input_value)
            return int_value
        if var_type == "%c":
            char_value = chr(input_value)
            return char_value
        if var_type == "%f":
            float_value = float(input_value)
            return float_value
        if var_type == "%lf":
            double_value = float(input_value)
            return double_value
        if var_type == "%s":
            string_value = str(input_value)
            return string_value
        
    # getchar() (ord())
    def getchar():
        char = sys.stdin.read(1)
        return char
