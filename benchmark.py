#!/bin/python3
import argparse
import subprocess
import sys


# Iterations to test
testing_iterations = []


def benchmark(program_name: str, magic_number: int, filename: str, time_str: str):
    for number in testing_iterations:
        # Sets C program input
        input = f"{number}\n{magic_number}\n".encode('utf-8')
        
        # Executes program with desired values
        result = subprocess.run([f"./{program_name}"], stdout=subprocess.PIPE, input=input)

        # Greps for wanted results
        grepped_result = subprocess.run(["grep", "-E", f"Valor calculado|{time_str}"], input=result.stdout, stdout=subprocess.PIPE) 

        # Decodes stdout
        grepped_result = grepped_result.stdout.decode('utf-8')

        # Saves results to a file
        results_lines = grepped_result.splitlines()
        calculated_value = int(results_lines[0].split(" ")[2])
        elapsed_time_str = results_lines[1].split(" ")[3]
        saveResult(number, magic_number, calculated_value, elapsed_time_str, filename)

        print(grepped_result)


# Saves each result to a file
def saveResult(iterations: int, magic_number: int, calculated_value: int, elapsed_time: str, filename: str):
    with open(filename, 'a') as fd:
        result = f"\nIterations: {iterations}\nMagicNumber: {magic_number}\nCalculated Value: {calculated_value}\nElapsed Time: {elapsed_time} seconds\n\n{'-' * 40}\n"
        fd.write(result)


# Gets the iteration values from the given file
def getIterationValues(filename: str):
    with open(filename, "r") as fd:
        data = fd.readlines()

        lineIndex = 1
        for line in data:
            try:
                iteration_value = int(line)
                testing_iterations.append(iteration_value)
            except ValueError:
                sys.exit(f"Invalid iteration value in line {lineIndex}!")

            lineIndex += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Benchmark', description='Benchmarks C calculation program')
    parser.add_argument('program_name', type=str, help='Name of the C program')
    parser.add_argument('magic_number', type=int, help='Magic number to be used in calculation')
    parser.add_argument('iterations_file', type=str, help='Name of the file with iterations to benchmark')
    parser.add_argument('elapsed_time_string', type=str, help='String used to grep for elapsed time value')
    parser.add_argument('-o', '--output', type=str, default='benchmark_results.txt', help='Name of the file which will be used to store the results')
    args = parser.parse_args()


    getIterationValues(args.iterations_file)
    benchmark(args.program_name, args.magic_number, args.output, args.elapsed_time_string)
