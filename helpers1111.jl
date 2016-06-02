module helpers

export x, y

x() = "x"
y() = "y"
p() = "p"

end

# module helpers
#
# export unionPartition1,test
#
#
# function unionPartition1(S1::Array{Int64}, c_s::Int64)
#   tempSet = push!(Set(S1),c_s);
#   sort(collect(tempSet));
# end
#
# #Require: D is the sorted array tuples, is a set of n ordered pairs
# #Require: y is the number of rows, which is an integer greater than 1
# function test1(xxx)
#   print(xxx)
#   xxx
# end
#
# # function equipartitionYAxis(D::sortedArrayByY{Tuple}, y)
# #   n = size(D,1)
# #   i = 1;
# #   currRow = 1;
# #   desiredRowSize = n/y;
# #
# #   currRowNum = 0
# #   while i > n
# #     j = i + 1;
# #     while D[j][2] == D[i][2]
# #       j = j + 1;
# #     end
# #     S = j - i;
# #     if currRowNum == 0 && abs(currRow + S - desiredRowSize) >= abs(currRow - desiredRowSize)
# #       currRow = currRow + 1;
# #       desiredRowSize = (n - i + 1)/(y - currRow + 1);
# #     end
# #     Q[currRow] = D[i][2];
# #     currRowNum = currRowNum + S;
# #     i = i + S;
# #   end
# #
# #   return Q
# # end
#
# end
