find_package(glfw3 REQUIRED)
find_package(glad REQUIRED)
find_package(imgui REQUIRED)

set(SRC_LIST
    ${CMAKE_CURRENT_SOURCE_DIR}/main.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ShaderLoader/ShaderLoader.cc

    ${CMAKE_SOURCE_DIR}/bindings/imgui_impl_glfw.cpp
    ${CMAKE_SOURCE_DIR}/bindings/imgui_impl_opengl3.cpp
)

add_executable(LearnOpenGL
    ${SRC_LIST}
)

target_include_directories(LearnOpenGL PUBLIC
    ${CMAKE_SOURCE_DIR}/bindings
    ${CMAKE_CURRENT_SOURCE_DIR}/ShaderLoader
)

target_link_libraries(LearnOpenGL PUBLIC
    glfw
    glad::glad
    imgui::imgui
)