{
    "targets": [
        {
            "target_name": "mpvjs",
            "win_delay_load_hook": "false",
            "sources": ["index.cc"],
            "libraries": ["-lppapi_cpp", "-lppapi_gles2"],
            "conditions": [
                ["OS=='win'", {
                    "include_dirs": ["libraries/pepper_49/win/include", "libraries/libmpv/include"],
                    "libraries": ["-llibmpv.dll.a"],
                    "conditions": [
                        ["target_arch=='ia32'", {
                            "library_dirs": [
                                "libraries/pepper_49/win/lib/win_x86_32_host/Release",
                                "libraries/libmpv/win",
                            ],
                        }, "target_arch=='x64'", {
                            "library_dirs": [
                                "libraries/pepper_49/win/lib/win_x86_64_host/Release",
                                "libraries/libmpv/win",
                            ],
                        }],
                    ],
                }, {
                    "include_dirs": ["libraries/pepper_49/win/linux/include"],
                    "libraries": ["-lmpv"],
                    "conditions": [
                        ["OS=='linux'", {
                            "defines": ["_GLIBCXX_USE_CXX11_ABI=0"],
                            "library_dirs": ["libraries/pepper_49/win/linux/lib/linux_host/Release"],
                            "ldflags": ["-static-libstdc++"],
                        }, "OS=='mac'", {
                            "xcode_settings": {"MACOSX_DEPLOYMENT_TARGET": "10.9"},
                            "library_dirs": ["libraries/pepper_49/win/linux/lib/mac_host/Release"],
                        }],
                    ],
                }],
            ],
        },
    ],
}
