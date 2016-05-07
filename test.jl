push!(LOAD_PATH, "./")

import MyModule
MyModule.mycoolfunction()
#
# import helpers: x, p
# using Base.Test
#
# x()
#
# # Unit test function unionPartion
# # Testcase 1
# # x = [1,3]
# # @test unionPartition(x,0) == [0,1,3]
# #
# # #Testcase 12
# # x = [1,3];
# # @test unionPartition(x,1) == [1,3]
# #
# # #Testcase 12
# # x = [1,3];
# # @test unionPartition(x,4) == [1,3,4]
#
#
# #Unit test fuction equipartitionYAxis
# # #Testcase 1
# # D = [(1,2),(2,3),(3,4)]
# # equipartitionYAxis(D,2)
