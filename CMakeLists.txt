cmake_minimum_required(VERSION 3.20)
project(LearnOpenGL CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

option(COMPILE_EXAMPLE "overwise compiler example" OFF)

add_subdirectory(src)

if (COMPILE_EXAMPLE)
    add_subdirectory(example)
endif()