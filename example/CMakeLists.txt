find_package(glfw3 REQUIRED)
find_package(glad REQUIRED)
find_package(imgui REQUIRED)

set(SRC_LIST
    ${CMAKE_CURRENT_SOURCE_DIR}/glfw_opengl3_imgui.cc


    ${CMAKE_SOURCE_DIR}/bindings/imgui_impl_glfw.cpp
    ${CMAKE_SOURCE_DIR}/bindings/imgui_impl_opengl3.cpp
)


add_executable(ImGUIExp
    ${SRC_LIST}
)


target_include_directories(ImGUIExp PUBLIC
    ${CMAKE_SOURCE_DIR}/bindings
)


target_link_libraries(ImGUIExp PUBLIC
    glfw
    glad::glad
    imgui::imgui
)