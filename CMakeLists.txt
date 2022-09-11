cmake_minimum_required(VERSION 3.10) 

# set the project name 
project(main)

set(CMAKE_CXX_COMPILER "/usr/bin/g++")

# specify the C++ standard 
set(CMAKE_CXX_STANDARD 11) 
set(CMAKE_CXX_STANDARD_REQUIRED True) 

# add_compile_options(-Wall -Werror -Wstrict-prototypes -Wmissing-prototypes -g -O0)
# debug 版本
add_compile_options(-g -O0)
# release 版本
# add_compile_options(-O0)

# 头文件路径
include_directories(
    "./src/tools/elog/",
    "./src/base/",
    "./src/leetcode/"
    "./src/main/")

# 源文件
# 
file(GLOB LeetCode "./src/leetcode/*.cpp" "./src/main/main.cpp")
# 日志工具
file(GLOB EasyLog "./src/tools/elog/*.c" )

# add the executable 
add_executable(main ${LeetCode} ${EasyLog})

# 链接所需要的库
target_link_libraries( main pthread)

