import os

# Define the cache sizes and policies to test
test_cases = [
    ("-N 3 -F", "in_files/input1.txt", "out_files/output1.txt"),
    ("-N 3 -L", "in_files/input2.txt", "out_files/output2.txt"),
    ("-N 3 -C", "in_files/input3.txt", "out_files/output3.txt"),
    ("-N 6 -F", "in_files/input4.txt", "out_files/output4.txt"),
    ("-N 6 -L", "in_files/input5.txt", "out_files/output5.txt"),
    ("-N 6 -C", "in_files/input6.txt", "out_files/output6.txt"),
]

for case in test_cases:
    command = "./cacher " + case[0] + " < " + case[1]
    output = os.popen(command).read().strip()
    expected_output = open(case[2]).read().strip()

    if output == expected_output:
        print(case[1], "OK")
    else:
        print(case[1], "FAILED")
        print("Expected Output:", expected_output)
        print("Output:", output)