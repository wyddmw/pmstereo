import sys
import os

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <lower_bound> <upper_bound>")
    print("Generates a fast exponential c file for values between the lower and upper bounds inclusive by precomputing at compile time and caching values in an array")

with open("fast_exp_array_declaration.cpp", "w") as fast_exp_file:
    lower_bound = int(sys.argv[1])
    upper_bound = int(sys.argv[2])
    num_vals = upper_bound-lower_bound+1
    fast_exp_file.write("#include <cmath>"+os.linesep)
    fast_exp_file.write("#include \"parameters.hpp\""+os.linesep)

    fast_exp_file.write("namespace pm {"+os.linesep)
    fast_exp_file.write("namespace fastexp_array_declaration {"+os.linesep)
    fast_exp_file.write(os.linesep)
    fast_exp_file.write("float precomputed_vals["+str(num_vals)+"] = {"+os.linesep)
    for val in range(upper_bound, -lower_bound+1):
        fast_exp_file.write("std::exp("+str(-val)+"/GAMMA), ")
    fast_exp_file.write("};"+os.linesep)

    fast_exp_file.write("float fast_exp(int val) {"+os.linesep)
    fast_exp_file.write("  // Assume value is in [-n,0]"+os.linesep)
    fast_exp_file.write("  if (val<=0 || val>="+str(lower_bound)+") {"+os.linesep)
    fast_exp_file.write("      return precomputed_vals[-val];"+os.linesep)
    fast_exp_file.write("  }"+os.linesep)
    fast_exp_file.write("  return std::exp(val/GAMMA);"+os.linesep)
    fast_exp_file.write("}"+os.linesep)
    fast_exp_file.write("} // namespace fastexp_array_declaration"+os.linesep)
    fast_exp_file.write("} // namespace pm"+os.linesep)

