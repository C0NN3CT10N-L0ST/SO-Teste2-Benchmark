# SO-Teste2-Benchmark

## Usage
___
```
$ ./benchmark.py -h
usage: Benchmark [-h] [-o OUTPUT] program_name magic_number iterations_file elapsed_time_string

Benchmarks C calculation program

positional arguments:
  program_name          Name of the C program
  magic_number          Magic number to be used in calculation
  iterations_file       Name of the file with iterations to benchmark
  elapsed_time_string   String used to grep for elapsed time value

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of the file which will be used to store the results
```

## C Program Example
___
```
$ ./main
Quantas iteracoes?
50000
Qual o numero magico?
123
Valor calculado: 4828857
Calculation elapsed time: 0.065 seconds
```

## Benchmark Script Example Usage (based on C program above)
___
### Program Execution
```
$ ./benchmark.py main 123 iterations.txt "Calculation elapsed time"
Valor calculado: 49692
Calculation elapsed time: 0.001 seconds

Valor calculado: 99384
Calculation elapsed time: 0.002 seconds

Valor calculado: 969117
Calculation elapsed time: 0.016 seconds

Valor calculado: 4828857
Calculation elapsed time: 0.059 seconds
```
___
### ***'iterations.txt'*** file
```
$ cat iterations.txt
500
1000
10000
50000
```
___
### Output file: ***'benchmark_results.txt'*** (default name)
```
$ cat benchmark_results.txt

Iterations: 500
MagicNumber: 123
Calculated Value: 49692
Elapsed Time: 0.001 seconds

----------------------------------------

Iterations: 1000
MagicNumber: 123
Calculated Value: 99384
Elapsed Time: 0.001 seconds

----------------------------------------

Iterations: 10000
MagicNumber: 123
Calculated Value: 969117
Elapsed Time: 0.012 seconds

----------------------------------------

Iterations: 50000
MagicNumber: 123
Calculated Value: 4828857
Elapsed Time: 0.056 seconds

----------------------------------------
```