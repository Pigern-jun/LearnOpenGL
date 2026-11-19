import os

from conan import ConanFile
from conan.tools.build import cross_building
from conan.tools.cmake import cmake_layout
from conan.tools.files import copy

class LearnOpenGL(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("glfw/3.4")
        self.requires("glad/2.0.8")
        self.requires("imgui/1.92.8-docking")
        self.requires("glm/1.0.3")
        self.requires("stb/cci.20261021")
        if self.settings.os == "Linux" and not cross_building(self):
            # EGL and GLFW must load the same system Wayland client library.
            self.requires("wayland/system", override=True)

    def generate(self):
        copy(self, "*glfw*", os.path.join(self.dependencies["imgui"].package_folder, "res", "bindings"), os.path.join(self.source_folder, "bindings"))
        copy(self, "*opengl3*", os.path.join(self.dependencies["imgui"].package_folder, "res", "bindings"), os.path.join(self.source_folder, "bindings"))

    def layout(self):
        cmake_layout(self)
