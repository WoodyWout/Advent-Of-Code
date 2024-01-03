def trebuchet(file_path):
    total_sum = 0

    with open(file_path) as text:
        for line in text:
            # Extract numeric values from the line
            numeric_values = ''.join(c for c in line if c.isdigit())

            if len(numeric_values) >= 2:
                # Calculate the sum of the first and last digits
                result_sum = int(numeric_values[0] + numeric_values[-1])
                total_sum += result_sum
            else:
                # Duplicate the numeric values and convert to an integer
                numeric_values *= 2
                numeric_values = int(numeric_values)
                total_sum += numeric_values

    return total_sum

# Example usage:
file_path = 'input_d1.txt'
result = trebuchet(file_path)
print(result)
