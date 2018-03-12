cmake_minimum_required(VERSION 3.9)

project(flx-deps CXX)

set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# Set global include directories, libraries directories, definitions, etc.
conan_basic_setup()

add_executable(${PROJECT_NAME}
	main.cpp
)

