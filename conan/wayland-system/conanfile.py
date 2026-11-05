import os

from conan import ConanFile
from conan.tools.gnu import PkgConfig


class WaylandSystem(ConanFile):
    name = "wayland"
    version = "system"
    settings = "os", "arch"
    options = {"shared": [True]}
    default_options = {"shared": True}

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
        self.cpp_info.set_property("pkg_config_name", "wayland_all_do_not_use")

        for name in ("wayland-client", "wayland-server", "wayland-cursor",
                     "wayland-egl", "wayland-egl-backend", "wayland-scanner"):
            pkg = PkgConfig(self, name)
            component = self.cpp_info.components[name]
            pkg.fill_cpp_info(component)
            component.bindirs = []
            component.set_property("pkg_config_name", name)
            component.set_property("component_version", pkg.version)

        scanner = self.cpp_info.components["wayland-scanner"]
        scanner_path = PkgConfig(self, "wayland-scanner").variables["wayland_scanner"]
        scanner.bindirs = [os.path.dirname(scanner_path)]
        scanner.set_property("pkg_config_custom_content", f"wayland_scanner={scanner_path}")
